## State if the following statements about nearest neighbors algorithms are true or false:

In nearest neighbors algorithms, no training is executed with the examples until a new input vector is given and the respective output needs to be predicted.
> TRUE

In the K-nearest-neighbors algorithm, the output of a new input vector may be predicted as the majority of the outputs of the k-nearest vectors in memory.
> TRUE

When applying the weighted k-nearest-neighbors algorithm, the output of a new input vector is predicted depending on the output of the nearest k vectors in memory, with a weighted average giving more weight to the closest examples.
> TRUE

Nearest neighbors algorithms can only be applied to classification problems.
> FALSE

Consider how the predicted output of a vector is predicted in weighted k-nearest-neighbors; 
d0 is a constant used to avoid division by zero. However, according to its value, the predictions of the algorithm change: the smaller d0, the larger is the relative contribution of far away points to the estimated output
> FALSE



## State if the following statements about supervised learning are true or false:

Available data is composed by vectors of features →x associated to an output y, and such data is used to build a function which models the relationship between →x and y.
> TRUE

The internal parameters (weights) of models created using supervised learning techniques define the flexibility of the models.
> TRUE

A suitable error measure for regression models is the sum of squared errors between the given output and the outcome predicted by the models.
> TRUE

Supervised learning does not assume that if two input points x1 and x2 are close, then the corresponding outputs y1 and y2 tend to be close in general.
> FALSE

If the complexity of a model is too small, learning the examples with zero errors becomes trivial, but the model is not going to be able to generalize results on unseen data.
> FALSE



## State if the following statements about the bias-variance dilemma are true or false

Models with too few parameters tend to fail because of a large bias.
> TRUE

Having few parameters contribute to the creation of flexible models.
> FALSE

Models with too many parameters tend to produce very different results if runs of training and testing are repeated (with some randomization).
> TRUE

Many parameters increase the complexity of the models.
> TRUE

Identifying the best model requires a compromise between bias and variance.
> TRUE




## State if the following statements about errors are true or false:

Systematic errors happen by pure randomness.
> FALSE

An example of systematic error is the error obtained when taking multiple measurements and each measurement is consistently overestimated by the measuring device.
> TRUE

The impact of systematic errors can be reduced by using large sample sizes.
> FALSE

Errors related to bias can be reduced by using large sample sizes.
> FALSE

Bias measures how the expected output of a machine learning model differs from the true value of the function approximated by the model.
> TRUE

The objective of supervised learning is to find a model that reduces to zero the error between the model and the function approximated by the model.
> FALSE



## State if the following statements about training, validating and testing are true or false:

Ideally, the number of data instances used for testing should ensure statistically significant results.
> TRUE

Cross-validation is useful in particular when data instances are not limited.
> FALSE

In cross-validation, the idea is to repeat many train-and-test experiments, by using different partitions of the original set of examples into two sets, one for training one for testing, and then averaging the test results.
> TRUE

For every k>0, in leave-one-out cross-validation, one of the k partitions is left out as validation data and the other partitions are used as training data.
> FALSE

In stratified cross-validation, classes are balanced in both training and validation sets.
> TRUE



## State if the following statements about evaluation metrics are true or false:

The root mean square error can be used as a classification metric.
> FALSE

Accuracy is defined as the proportion of true positives over all the predictions made by a classifier
> FALSE

Precision is the proportion of true positives over the all the predictions predicted as positive by a classifier.
> TRUE

Recall is the proportion of true positives and true negatives over all the elements that actually belong to the positive class
> FALSE

A confusion matrix can not be computed for a binary classification problem.
> FALSE


## Given the points {[(1, 4, 0), (2, 2.5, 0), (2, 3, 0), (2.5, 3, 0), (3.5, 2, 1), (4, 3, 1), (5, 1, 1), (6, 2, 1)]}, where the last coordinate is the label of the class of the point, apply 3-nearest neighbors to all the points and consider the class which would be predicted. Consider class 1 as the positive class; help yourself using the following plot, and state if the following statements are true or false:

Precision is 1.
> TRUE

Accuracy is 0.9.
> FALSE

Recall is 0.5.
> TRUE
