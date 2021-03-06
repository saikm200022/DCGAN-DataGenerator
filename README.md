# Training Data Generator - GAN Implementation

## Motivation

In deep learning and machine learning models, data is essential to train models. However, there are certain scenarios where there is not enough training data to build robust models. The goal of this project is to take some initial training data and generate more training data.

## Dataset

With this being my first Generative Adversarial Network (GAN) project, I chose to use the CIFAR-10 dataset. I was able to generate more images for this particular dataset. However, I do believe that this project can be extended for more complex datasets.

<p align="center"> <img src="images_progress/source_data.png" height="200"/> </p>


## Model Architectures

For the discriminator architecture, it follows a relatively deep Convolutional Neural Network (CNN) that outputs a binary label for a given input determining if it is real or fake. The code for this model can be found in ``./architecture/Discriminator.py``.

The generator network follows the architecture suggested by a DCGAN, which takes a latent vector of random noise as input and outputs an image that is evaluated by the discriminator ``./architecture/Generator.py``.

<p align="center"> <img src="images_progress/architecture.pbm" height="200"/> </p>

## Training

I was surprised to find that the GAN required many epochs of training. I had needed to train for 200 epochs before I saw anything other than random noise. I was also forced to use a smaller learning rate = ``1e-5`` so that the discriminator does not get overconfident and learning goes to a halt. In this project, I also included the functionality to include pretrained versions of the generator and discriminator, example checkpoints after the 500 epoch mark are included in ``./model_checkpoints``. The ``ADAM`` optimizer was used along with ``BCEWithLogitsLoss``. 

## Running the Code

**Training the Models:**

Run the following command: ``python3 train.py``

**Using the utility functions to display and create the data from the trained model:**

Run the following command: ``python3 main.py``

## Findings

### **Some Challenges**
* I was unfamiliar with the need to train for more epochs to see results, so I was concerned with the lack of progress even after 50 or so epochs. I tried with larger lr but they led to the discriminator learning to be too overconfident.

* I found it initially difficult to interpret the loss values of the Generator vs the Discriminator loss. However, I later understood that these losses should in practice be opposite each other and change based on each other's loss values.

### **Some Fixes**
* I utilized upper-tailed label smoothing which caused the discriminator to stop being too overconfident and led to the generator actually being able to train without arriving at a single solution that is able to trick the discriminator.

* Using smaller learning rates were key in helping my models train. I found that too large learning rates like ``1e-1, 1e-2, 1e-3`` led to the generator only producing random white noise such as shown below:

<p align="center"> <img src="images_progress/noise_initial.bmp" height="200"/> </p>

## Results

As mentioned earlier, the results were random noise at the beginning of training but improved across epochs using the training configuration discussed above:

**After 100 Epochs:**

The images were resembling something other than random noise:

<p align="center"> <img src="images_progress/intermediate_100.png" height="100"/> </p>

**After 200 Epochs:**

The images were slightly better and began to take shape as there were more detailed features that were being generated:

<p align="center"> <img src="images_progress/intermediate_200.png" height="100"/> </p>

**After 360 Epochs:**

More improvement and certain images like the left most image becoming very clear as to what they could be:

<p align="center"> <img src="images_progress/intermediate_360.png" height="100"/> </p>

**500 and 600 Epochs:**

Images are very clear when viewed from a distance and resemble real world objects. The improvement from 500 to 600 epochs appears to be negligible:

<p float="middle">
  <img src="images_progress/intermediate_500.png" width="49%"/>
  <img src="images_progress/intermediate_600.png" width="49%" /> 
</p>

## Final Results

<p align="center"> <img src="images_progress/Final Results.png" height="400"/> </p>

Using the DCGAN architecture, I created additional training data shown above that can be used to train models for image classification of CIFAR-10. I believe that this approach can be used for other datasets as well. I have also created a template class in ``./utils/MyDataLoader.py`` where one can create a torch dataloader with local images. In ``./main.py``, there are also utility functions that visualize generated data and create repositories with the generated training data. Examples of the generated data can be found in the ``./generated_data`` directory. 

## Conclusion

With this project, I explored the possibility of creating additional for a given dataset. I implemented this specifically for the CIFAR-10 dataset, with this being my first experience with an image generation model. I used a DCGAN architecture and trained it from scratch for many epochs to produce realistic images that could be suitable additional images for the dataset I have chosen.

## Future Steps

1. Implement the code to be generalizable for any dataset
1. Use a different architecture such as SRGAN to produce more high resolution images that are less blurry
1. Train for even longer epochs with fewer computational constraints
1. Make the model architectures generic to handle the image types of all kinds of datasets

