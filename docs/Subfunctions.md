Image preprocessing is defined as a method or technique which modify the image before passing it to the neural network model. The aim of preprocessing methods is to extensively increase performance due to simplification of information.

In medical image segmentation, it is required to perform extensive preprocessing to the medical images. Common preprocessing methods range from intensity value normalization to image resizing.  
The preprocessing is not only required for performance increase, but also to reduce the image information content in order to be fit-able in the neural network model in terms of GPU RAM size.

In the current state-of-the-art mdeical image segmentation pipelines, several preprocessing methods are common: Resampling slice thickness, resizing images to fit into GPUs and intensity value normalization.

In order to provide a wide variety of preprocessing methods, MIScnn offers the Subfunction modularity. The user is able to create a list of desired preprocessing functions (in MIScnn called Subfunctions) and pass them to the Preprocessor class, which allows high configurability for all scenarios.

## Usage of MIScnn Subfunctions

A list of Subfunctions can be passed to the Preprocessor class initialization.  
The Preprocessor automatically uses the list of Subfunctions and **sequentially** runs the Subfunctions on the data set.

For predictions, the medical images will also be automatically postprocessed in order to restore the predicted segmentation for the original image features (e.g. resizing back to original size).

```python
# Import desired Subfunctions
from processing.subfunctions import Normalization
from processing.subfunctions import Resampling

# Initialize Subfunctions into a list
sf_normalization = Normalization(z_score=True)
sf_resampling = Resampling(new_spacing=(3.22, 1.62, 1.62))
sf = [sf_normalization, sf_resampling]

# Pass list of Subfunctions to Preprocessor class
pp = Preprocessor(data_io, batch_size=2, subfunctions=sf)
```

## Available Subfunctions provided by MIScnn

#### Intensity Value Normalization

A Normalization Subfunction class which normalizes the intensity pixel values of an image using the Z-Score technique (default setting) or through scaling to [0,1].

```python
from processing.subfunctions import Normalization
sf_norm = Normalization(z_score=True)

pp = Preprocessor(data_io, batch_size=2, subfunctions=[sf_norm])
```

------------------

#### Resizing

A Resize Subfunction class which resizes an images according to a desired shape.

```python
from processing.subfunctions import Resize
sf_resize = Resize(new_shape=(128,128,128))

pp = Preprocessor(data_io, batch_size=2, subfunctions=[sf_resize])
```

------------------

#### Resampling

A Resampling Subfunction class which resizes an images according to a desired voxel spacing.  
This function only works with already cached "spacing" matrix in the detailed information dictionary of the sample.

```python
from processing.subfunctions import Resampling
sf_resampling = Resampling(new_spacing=(3.22, 1.62, 1.62))

pp = Preprocessor(data_io, batch_size=2, subfunctions=[sf_resampling])
```

------------------

#### Clipping

A Clipping Subfunction class which can be used for clipping intensity pixel values on a certain range.

```python
from processing.subfunctions import Clipping
sf_clip = Clipping(min=25, max=75)

pp = Preprocessor(data_io, batch_size=2, subfunctions=[sf_clip])
```

------------------

## Creation of custom Subfunctions

todo

```python
todo
```

## Abstract Base Class for Subfunctions

MIScnn also offers a documented Abstract Base Class for easier creating of custom Subfunctions for your specific needs.

A Subfunction is a class which consists of an init, preprocessing and postprocessing function.

```python
#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# External libraries
from abc import ABC, abstractmethod

#-----------------------------------------------------#
#     Abstract Interface for the Subfunction class    #
#-----------------------------------------------------#
""" An abstract base class for a processing Subfcuntion class.

Methods:
    __init__                Object creation function
    preprocessing:          Transform the imaging data
    postprocessing:         Transform the predicted segmentation
"""
class Abstract_Subfunction(ABC):
    #---------------------------------------------#
    #                   __init__                  #
    #---------------------------------------------#
    """ Functions which will be called during the Subfunction object creation.
        This function can be used to pass variables and options in the Subfunction instance.
        The are no mandatory required parameters for the initialization.

        Parameter:
            None
        Return:
            None
    """
    @abstractmethod
    def __init__(self):
        pass
    #---------------------------------------------#
    #                preprocessing                #
    #---------------------------------------------#
    """ Transform the image according to the subfunction during preprocessing (training + prediction).
        This is an in-place transformation of the sample object, therefore nothing is returned.
        It is possible to pass configurations through the initialization function of this class.

        Parameter:
            sample (Sample class):      Sample class object containing the imaging data (sample.img_data)
                                        and optional segmentation data (sample.seg_data)
            training (boolean):         Boolean variable indicating, if segmentation data is present at the
                                        sample object.
                                        If training is true, segmentation data in the sample object is available,
                                        if training is false, sample.seg_data is None
        Return:
            None
    """
    @abstractmethod
    def preprocessing(self, sample, training=True):
        pass
    #---------------------------------------------#
    #                postprocessing               #
    #---------------------------------------------#
    """ Transform the prediction according to the subfunction during postprocessing (prediction).
        This is NOT an in-place transformation of the prediction, therefore it is REQUIRED to
        return the processed prediction array.
        It is possible to pass configurations through the initialization function of this class.

        Parameter:
            prediction (numpy array):   Numpy array of the predicted segmentation
        Return:
            prediction (numpy array):   Numpy array of processed predicted segmentation
    """
    @abstractmethod
    def postprocessing(self, prediction):
        return prediction

```
