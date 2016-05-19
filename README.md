Machine Learning Project Based on KDD Cup 2010
-----------------------------------------------


## Synopsis

Machine learning methods are applied to the KDD Cup 2010's Educational 
Data Mining competition's datasets, found [here.](https://pslcdatashop.web.cmu.edu/KDDCup/downloads.jsp)

Python 3 libraries used:

* numpy/scipy
* pandas
* scikit-learn

All of these can be installed with [Anaconda for Python 3.](https://www.continuum.io/downloads)

## Motivation

This project was completed for Professor Ding's Spring 2016 Applied 
Machine Learning course at **UMass Boston**. Our main motivation is 
to understand the basic fundamentals of important machine learning 
concepts.

## Installation

Clone the project with the following:

    git clone https://github.com/imanmk/MLKDD.git

After installing [Anaconda](https://www.continuum.io/downloads), it is 
recommended to put the python executable in your $PATH environment 
variable:

    export PATH="/directory/to/anaconda3/bin:$PATH"

Note: Our CSV files can be found here:
https://github.com/imanmk/MLKDD/tree/master/CSV

## API Reference

API Documentation for pandas DataFrames can be found here:
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html

Importing a CSV file to a pandas DataFrame is as simple as a function call:

    import pandas as pd
    df = pd.read_csv("train.csv", header=0)


API Documentation for scikit-learn can be found here:
http://scikit-learn.org/stable/modules/classes.html

Some examples of packages used are:
* sklearn.preprocessing.LabelEncoder() - converting Nominal features to Numeric features.
* sklearn.neighbors.KNeighborsClassifier() - K-Nearest-Neighbors implementation
* sklearn.metrics.mean_squared_error() - RMSE calculator

## Questions? Comments?

Our contact information can be found on our gh-pages website here:
http://imanmk.github.io/MLKDD/#about

