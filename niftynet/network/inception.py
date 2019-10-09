# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import tensorflow as tf

from niftynet.layer.base_layer import TrainableLayer, Layer
from niftynet.layer.convolution import ConvolutionalLayer as Conv
from niftynet.layer.crop import CropLayer as Crop
from niftynet.layer.deconvolution import DeconvolutionalLayer as DeConv
from niftynet.layer.downsample import DownSampleLayer as Pooling
from niftynet.layer.elementwise import ElementwiseLayer as ElementWise
from niftynet.layer.linear_resize import LinearResizeLayer as Resize
from niftynet.layer.activation import ActiLayer
from niftynet.network.base_net import BaseNet
from niftynet.layer.fully_connected import FCLayer, FullyConnectedLayer


class Inception(BaseNet):
    """

    """

    def __init__(self,
                 num_classes,
                 w_initializer=None,
                 w_regularizer=None,
                 b_initializer=None,
                 b_regularizer=None,
                 acti_func='relu',
                 name='inception'):
        BaseNet.__init__(self,
                         num_classes=num_classes,
                         name=name)
        self.n_fea = [32, 64, 80, 192, 256, 288, 768, 1280, 2048, 2]
        # self.fc_features = [64, 2]

        net_params = {'padding': 'SAME',
                      'with_bias': True,
                      'with_bn': False,
                      'group_size': -1,
                      'acti_func': acti_func,
                      'w_initializer': w_initializer,
                      'b_initializer': b_initializer,
                      'w_regularizer': w_regularizer,
                      'b_regularizer': b_regularizer}

        self.conv_params11 = {'kernel_size': 1, 'stride': 1}
        self.conv_params31 = {'kernel_size': 3, 'stride': 1}
        self.conv_params32 = {'kernel_size': 3, 'stride': 2}
        self.conv_params51 = {'kernel_size': 5, 'stride': 1}
        self.conv_params131 = {'kernel_size': [1, 3], 'stride': 1}
        self.conv_params311 = {'kernel_size': [3, 1], 'stride': 1}
        self.conv_params711 = {'kernel_size': [7,1], 'stride': 1}
        self.conv_params171 = {'kernel_size': [1,7], 'stride': 1}

        self.pooling_params11 = {'kernel_size': 1, 'stride': 1}
        self.pooling_params31 = {'kernel_size': 3, 'stride': 1}
        self.pooling_params32 = {'kernel_size': 3, 'stride': 2}
        self.pooling_params51 = {'kernel_size': 5, 'stride': 1}
        self.pooling_params131 = {'kernel_size': [1, 3], 'stride': 1}
        self.pooling_params311 = {'kernel_size': [3, 1], 'stride': 1}
        self.pooling_params711 = {'kernel_size': [7, 1], 'stride': 1}
        self.pooling_params171 = {'kernel_size': [1, 7], 'stride': 1}

        self.conv_params11.update(net_params)
        self.conv_params31.update(net_params)
        self.conv_params32.update(net_params)
        self.conv_params51.update(net_params)
        self.conv_params131.update(net_params)
        self.conv_params311.update(net_params)
        self.conv_params711.update(net_params)
        self.conv_params171.update(net_params)

        self.net_params = net_params

    def layer_op(self, images, is_training=True, **unused_kwargs):
        # contracting path

        output_1 = Conv(self.n_fea[0],**self.conv_params32)(images)

        output_2 = Conv(self.n_fea[0],**self.conv_params31)(output_1)

        output_3 = Conv(self.n_fea[1],**self.conv_params31)(output_2)

        down_3 = Pooling(func='MAX', **self.pooling_params32)(output_3)
        output_4 = Conv(self.n_fea[2],**self.conv_params11)(down_3)

        output_5 = Conv(self.n_fea[3],**self.conv_params31)(output_4)

        down_5 = Pooling(func='MAX', **self.pooling_params32)(output_5)

        output_61_1 = mixedInception0([32, 48, 64, 96], [self.conv_params11, self.conv_params31, self.conv_params51, self.pooling_params31])(
            down_5)

        output_61_2 = mixedInception1([48, 64, 96],[self.conv_params11,self.conv_params31,self.conv_params51, self.pooling_params31])(output_61_1)
        output_61_3 = mixedInception1([48, 64, 96], [self.conv_params11, self.conv_params31, self.conv_params51, self.pooling_params31])(output_61_2)

        output_62 = mixedInception3([64, 96, 384],[self.conv_params11,self.conv_params31,self.conv_params32, self.pooling_params32])(output_61_3)

        output_62 = mixedInception4([128, 192],[self.conv_params11, self.conv_params171,self.conv_params711, self.pooling_params31])(output_62) # KERNELS -> [1, 7] and [7, 1]

        output_62 = mixedInception4([160, 192],[self.conv_params11, self.conv_params171,self.conv_params711, self.pooling_params31])(output_62)
        output_62 = mixedInception4([160, 192],[self.conv_params11, self.conv_params171,self.conv_params711, self.pooling_params31])(output_62)

        output_7 = mixedInception7([192],[self.conv_params11, self.conv_params31, self.conv_params171,self.conv_params711, self.pooling_params31])(output_62) # KERNELS -> [1, 7] and [7, 1]

        output8 = mixedInception8([192,320],[self.conv_params11, self.conv_params32, self.conv_params171, self.conv_params711, self.pooling_params32])(output_7)

        output9 = mixedInception9([320, 384, 448, 192],
                                  [self.conv_params11, self.conv_params131, self.conv_params311, self.conv_params31, self.pooling_params31])(output8)
        output10 = mixedInception9([320, 384, 448, 192],
                                  [self.conv_params11, self.conv_params131, self.conv_params311, self.conv_params31, self.pooling_params31])(
            output9)

        shape_t = output10.shape #check if this shape works

        self.pooling_params_shape = {'kernel_size': shape_t, 'stride': 1}
        # self.conv_params_shape.update(self.net_params)
        output_tensor_class = Pooling(func='AVG', **self.pooling_params_shape)(output10)

        output_tensor_class = FCLayer(n_output_chns=self.n_fea[8],
                                          with_bias=True,
                                          w_initializer=self.conv_params11.get('w_initializer'),
                                          w_regularizer=self.conv_params11.get('w_regularizer'),
                                          name='fc1'
                                          )(output_tensor_class)

        output_tensor_class = FCLayer(n_output_chns=self.n_fea[9],
                                      with_bias=True,
                                      w_initializer=self.conv_params11.get('w_initializer'),
                                      w_regularizer=self.conv_params11.get('w_regularizer'),
                                      name='fc2'
                                      )(output_tensor_class)

            # output_tensor_class = ActiLayer(func='sigmoid',name='sigmoid')(output_tensor_class)

        return output_tensor_class


class mixedInception0(TrainableLayer):
    """

    """

    def __init__(self, n_chns, conv_params):
        TrainableLayer.__init__(self, name='mixedInception0')
        self.n_chns = n_chns
        self.conv_params = conv_params

    def layer_op(self, input_tensor):
        branch1x1 = Conv(self.n_chns[2], **self.conv_params[0])(input_tensor)

        branch5x5 = Conv(self.n_chns[1], **self.conv_params[0])(input_tensor)
        branch5x5 = Conv(self.n_chns[2], **self.conv_params[2])(branch5x5)

        branch3x3_dbl = Conv(self.n_chns[2], **self.conv_params[0])(input_tensor)
        branch3x3_dbl = Conv(self.n_chns[3], **self.conv_params[1])(branch3x3_dbl)
        branch3x3_dbl = Conv(self.n_chns[3], **self.conv_params[1])(branch3x3_dbl)

        branchpool = Pooling(func='AVG', **self.conv_params[-1])(input_tensor)
        branchpool = Conv(self.n_chns[0], **self.conv_params[0])(branchpool)

        output_tensor = CropConcat()(branch1x1, branch5x5)
        output_tensor = CropConcat()(output_tensor, branch3x3_dbl)
        output_tensor = CropConcat()(output_tensor, branchpool)

        return output_tensor

class mixedInception1(TrainableLayer):
    """

    """

    def __init__(self, n_chns, conv_params):
        TrainableLayer.__init__(self, name='mixedInception1')
        self.n_chns = n_chns
        self.conv_params = conv_params

    def layer_op(self, input_tensor):
        branch1x1 = Conv(self.n_chns[1],**self.conv_params[0])(input_tensor)

        branch5x5 = Conv(self.n_chns[0],**self.conv_params[0])(input_tensor)
        branch5x5 = Conv(self.n_chns[1], **self.conv_params[2])(branch5x5)

        branch3x3_dbl = Conv(self.n_chns[1],**self.conv_params[0])(input_tensor)
        branch3x3_dbl = Conv(self.n_chns[2], **self.conv_params[1])(branch3x3_dbl)
        branch3x3_dbl = Conv(self.n_chns[2], **self.conv_params[1])(branch3x3_dbl)

        branchpool = Pooling(func='AVG', **self.conv_params[-1])(input_tensor)
        branchpool = Conv(self.n_chns[1], **self.conv_params[0])(branchpool)


        output_tensor = CropConcat()(branch1x1,branch5x5)
        output_tensor = CropConcat()(output_tensor,branch3x3_dbl)
        output_tensor = CropConcat()(output_tensor,branchpool)

        return output_tensor


class mixedInception3(TrainableLayer):
    """

    """

    def __init__(self, n_chns, conv_params):
        TrainableLayer.__init__(self, name='mixedInception3')
        self.n_chns = n_chns
        self.conv_params = conv_params

    def layer_op(self, input_tensor):
        branch3x3 = Conv(self.n_chns[2],**self.conv_params[2])(input_tensor)

        branch3x3_dbl = Conv(self.n_chns[0],**self.conv_params[0])(input_tensor)
        branch3x3_dbl = Conv(self.n_chns[1], **self.conv_params[1])(branch3x3_dbl)
        branch3x3_dbl = Conv(self.n_chns[1], **self.conv_params[2])(branch3x3_dbl)

        branchpool = Pooling(func='MAX', **self.conv_params[-1])(input_tensor)

        output_tensor = CropConcat()(branch3x3,branch3x3_dbl)
        output_tensor = CropConcat()(output_tensor,branchpool)

        return output_tensor


class mixedInception4(TrainableLayer):
    """

    """

    def __init__(self, n_chns, conv_params):
        TrainableLayer.__init__(self, name='mixedInception4')
        self.n_chns = n_chns
        self.conv_params = conv_params

    def layer_op(self, input_tensor):
        branch1x1 = Conv(self.n_chns[1],**self.conv_params[0])(input_tensor)

        branch7x7 = Conv(self.n_chns[0],**self.conv_params[0])(input_tensor)
        branch7x7 = Conv(self.n_chns[0], **self.conv_params[1])(branch7x7)   #[1,7]
        branch7x7 = Conv(self.n_chns[1], **self.conv_params[2])(branch7x7)   #[7,1]

        branch7x7_dbl = Conv(self.n_chns[0], **self.conv_params[0])(input_tensor)
        branch7x7_dbl = Conv(self.n_chns[0], **self.conv_params[2])(branch7x7_dbl)  # [7,1]
        branch7x7_dbl = Conv(self.n_chns[0], **self.conv_params[1])(branch7x7_dbl)  # [1,7]
        branch7x7_dbl = Conv(self.n_chns[0], **self.conv_params[2])(branch7x7_dbl)  # [7,1]
        branch7x7_dbl = Conv(self.n_chns[1], **self.conv_params[1])(branch7x7_dbl)  # [1,7]

        branchpool = Pooling(func='AVG', **self.conv_params[-1])(input_tensor)
        branchpool = Conv(self.n_chns[1], **self.conv_params[0])(branchpool)

        output_tensor = CropConcat()(branch1x1,branch7x7)
        output_tensor = CropConcat()(output_tensor,branch7x7_dbl)
        output_tensor = CropConcat()(output_tensor, branchpool)

        return output_tensor


class mixedInception7(TrainableLayer):
    """

    """

    def __init__(self, n_chns, conv_params):
        TrainableLayer.__init__(self, name='mixedInception4')
        self.n_chns = n_chns
        self.conv_params = conv_params

    def layer_op(self, input_tensor):
        branch1x1 = Conv(self.n_chns[0], **self.conv_params[0])(input_tensor)

        branch7x7 = Conv(self.n_chns[0], **self.conv_params[0])(input_tensor)
        branch7x7 = Conv(self.n_chns[0], **self.conv_params[2])(branch7x7)  # [1,7]
        branch7x7 = Conv(self.n_chns[0], **self.conv_params[3])(branch7x7)  # [7,1]

        branch7x7_dbl = Conv(self.n_chns[0], **self.conv_params[0])(input_tensor)
        branch7x7_dbl = Conv(self.n_chns[0], **self.conv_params[3])(branch7x7_dbl)  # [7,1]
        branch7x7_dbl = Conv(self.n_chns[0], **self.conv_params[2])(branch7x7_dbl)  # [1,7]
        branch7x7_dbl = Conv(self.n_chns[0], **self.conv_params[3])(branch7x7_dbl)  # [7,1]
        branch7x7_dbl = Conv(self.n_chns[0], **self.conv_params[2])(branch7x7_dbl)  # [1,7]

        branchpool = Pooling(func='AVG', **self.conv_params[-1])(input_tensor)
        branchpool = Conv(self.n_chns[0], **self.conv_params[0])(branchpool)

        output_tensor = CropConcat()(branch1x1, branch7x7)
        output_tensor = CropConcat()(output_tensor, branch7x7_dbl)
        output_tensor = CropConcat()(output_tensor, branchpool)

        return output_tensor

class mixedInception8(TrainableLayer):
    """

    """

    def __init__(self, n_chns, conv_params):
        TrainableLayer.__init__(self, name='mixedInception4')
        self.n_chns = n_chns
        self.conv_params = conv_params

    def layer_op(self, input_tensor):
        branch3x3 = Conv(self.n_chns[0], **self.conv_params[0])(input_tensor)
        branch3x3 = Conv(self.n_chns[1], **self.conv_params[1])(branch3x3)

        branch7x7x3 = Conv(self.n_chns[0], **self.conv_params[0])(input_tensor)
        branch7x7x3 = Conv(self.n_chns[0], **self.conv_params[2])(branch7x7x3)  # [1,7]
        branch7x7x3 = Conv(self.n_chns[0], **self.conv_params[3])(branch7x7x3)  # [7,1]
        branch7x7x3 = Conv(self.n_chns[0], **self.conv_params[1])(branch7x7x3)  # [7,1]

        branchpool = Pooling(func='MAX', **self.conv_params[-1])(input_tensor)

        output_tensor = CropConcat()(branch3x3, branch7x7x3)
        output_tensor = CropConcat()(output_tensor, branchpool)

        return output_tensor

class mixedInception9(TrainableLayer):
    """

    """

    def __init__(self, n_chns, conv_params):
        TrainableLayer.__init__(self, name='mixedInception4')
        self.n_chns = n_chns
        self.conv_params = conv_params

    def layer_op(self, input_tensor):
        branch1x1 = Conv(self.n_chns[0], **self.conv_params[0])(input_tensor)

        branch3x3 = Conv(self.n_chns[1], **self.conv_params[0])(input_tensor)
        branch3x3_1 = Conv(self.n_chns[1], **self.conv_params[1])(branch3x3)
        branch3x3_2 = Conv(self.n_chns[1], **self.conv_params[2])(branch3x3)
        branch3x3 = CropConcat()(branch3x3_1,branch3x3_2)

        branch3x3_dbl = Conv(self.n_chns[2], **self.conv_params[0])(input_tensor)
        branch3x3_dbl = Conv(self.n_chns[1], **self.conv_params[3])(branch3x3_dbl)  # [1,7]
        branch3x3_dbl_1 = Conv(self.n_chns[1], **self.conv_params[1])(branch3x3_dbl)
        branch3x3_dbl_2 = Conv(self.n_chns[1], **self.conv_params[2])(branch3x3_dbl)
        branch3x3_dbl = CropConcat()(branch3x3_dbl_1, branch3x3_dbl_2)

        branchpool = Pooling(func='AVG', **self.conv_params[-1])(input_tensor)
        branchpool = Conv(self.n_chns[3], **self.conv_params[0])(branchpool)

        output_tensor = CropConcat()(branch1x1, branch3x3)
        output_tensor = CropConcat()(output_tensor, branch3x3_dbl)
        output_tensor = CropConcat()(output_tensor, branchpool)

        return output_tensor



class ConvBlock(TrainableLayer):

    def __init__(self, n_chns, conv_params):
        TrainableLayer.__init__(self, name='ConvBlock')
        self.n_chns = n_chns

        net_params1 = {'acti_func': 'leakyrelu'}

        self.conv_params1 = conv_params
        self.conv_params1.update(net_params1)

        net_params = {'acti_func': None}

        self.conv_params = conv_params
        self.conv_params.update(net_params)


    def layer_op(self, input_tensor):
        h = Conv(self.n_chns,**self.conv_params1)(input_tensor)
        h = Conv(self.n_chns,**self.conv_params)(input_tensor)

        output_tensor = input_tensor + h

        output_tensor = ActiLayer(func='relu')(output_tensor)

        return output_tensor

class CropConcat(Layer):
    """
    This layer concatenates two input tensors,
    the first one is cropped and resized to match the second one.

    This layer assumes the same amount of differences
    in every spatial dimension in between the two tensors.
    """

    def __init__(self, name='crop_concat'):
        Layer.__init__(self, name=name)

    def layer_op(self, tensor_a, tensor_b):
        """
        match the spatial shape and concatenate the tensors
        tensor_a will be cropped and resized to match tensor_b.

        :param tensor_a:
        :param tensor_b:
        :return: concatenated tensor
        """
        crop_border = (tensor_b.shape[1] - tensor_a.shape[1]) // 2
        tensor_b = Crop(border=crop_border)(tensor_b)
        output_spatial_shape = tensor_a.shape[1:-1]
        tensor_b = Resize(new_size=output_spatial_shape)(tensor_b)
        return ElementWise('CONCAT')(tensor_a, tensor_b)
