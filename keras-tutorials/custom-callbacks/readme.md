# Callbacks in Keras
The Neural Network parts of this short tutorial are based on the tutorial found [here](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/). Their code is a lot better documented with regards to neural networks. If you are new to the topic and do not understand the basics of how they work, have a look at it, since this Tutorial focuses more on `Callbacks` and prior knowledge of neural networks is required.

Keras Callbacks can be used for a variety of purposes. For example to either save a model during the training process rather than at the end or to stop the training process prematurely should it not converge anymore.

This short tutorial gives an explanation on how to implement a custom Callback class that allows to either save the model after every epoch or only if the model showed improvement with regards to certain conditions that can be specified by the user.
