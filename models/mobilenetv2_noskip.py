from tensorflow.keras.layers import Conv2D, UpSampling2D, LeakyReLU, Concatenate,MaxPooling2D
from tensorflow.keras import Model
from tensorflow.keras.applications import MobileNetV2
import tensorflow as tf

class UpscaleBlock(Model):
    def __init__(self, filters, name):
        super(UpscaleBlock, self).__init__()
        self.up = UpSampling2D(size=(2, 2), interpolation='bilinear', name=name+'_upsampling2d')
        self.convA = Conv2D(filters=filters, kernel_size=3, strides=1, padding='same', name=name+'_convA')
        self.reluA = LeakyReLU(alpha=0.2)
        self.convB = Conv2D(filters=filters, kernel_size=3, strides=1, padding='same', name=name+'_convB')
        self.reluB = LeakyReLU(alpha=0.2)

    def call(self, x):
        return self.reluB( self.convB( self.reluA( self.convA(self.up(x) ) ) ))

class Encoder(Model):
    def __init__(self):
        super(Encoder, self).__init__()
        self.base_model = MobileNetV2(input_shape=(480,640, 3), include_top=False, weights='imagenet')
        print('Base model loaded')

        outputs = [self.base_model.outputs[-1]]
        for name in ['Conv1_relu'] : outputs.append( self.base_model.get_layer(name).output )
        self.encoder = Model(inputs=self.base_model.inputs, outputs=outputs)

    def call(self, x):
        return self.encoder(x)

class Decoder(Model):
    def __init__(self, decode_filters):
        super(Decoder, self).__init__()
        self.conv2 =  Conv2D(filters=decode_filters, kernel_size=1, padding='same', name='conv2')
        self.up1 = UpscaleBlock(filters=decode_filters//2,  name='fup1')
        self.up2 = UpscaleBlock(filters=decode_filters//4,  name='fup2')
        self.up3 = UpscaleBlock(filters=decode_filters//8,  name='fup3')
        self.fup = UpscaleBlock(filters=decode_filters//16, name='fup')
        self.conv3 = Conv2D(filters=1, kernel_size=3, strides=1, padding='same', name='conv3')

    def call(self, features):
        #print('d')
        #print(features)
        x,conv1 = features[0], features[1]
        upo0 = self.conv2(x)
        #print(upo0)
        upo1 = self.up1(upo0)
        #print(upo1)
        upo2 = self.up2(upo1)
        #print(upo2)
        upo3 = self.up3(upo2)
        #print(upo3)
        #print(conv1)
        upo4 = self.fup(upo3)
        #print(upo4)
        upo5=self.conv3( upo4)
        #print(upo5)
        return upo5

class DepthEstimate(Model):
    def __init__(self):
        super(DepthEstimate, self).__init__()
        self.encoder = Encoder()
        self.decoder = Decoder( decode_filters = int(self.encoder.layers[-1].output[0].shape[-1] // 2 ) )
        print('\nModel created.')

    def call(self, x):
        return self.decoder(self.encoder(x))
