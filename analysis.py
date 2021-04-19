# analysis.py
# Author: Anja Antolkovic

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# Working out the summary of each variable within the data set  

iris = pd.read_csv("iris.data") # loading data set into a DataFrame
iris_setosa = iris[iris["iris_type"] == "Iris-setosa"] # isolating rows only for iris Setosa's from a DataFrame 
iris_versicolor = iris[iris["iris_type"] == "Iris-versicolor"] # isolating rows only for iris Versicolor's from a DataFrame
iris_virginica = iris[iris["iris_type"] == "Iris-virginica"] # isolating rows only for iris Virginica's from a DataFrame         
iris_setosa_summary = iris_setosa.describe()
iris_versicolor_summary = iris_versicolor.describe()
iris_virginica_summary = iris_virginica.describe()

with open ("iris_data_summary", "w") as f:
    f.write("iris setosa\n{}\n\n".format(str(iris_setosa_summary)))   
    f.write("iris versicolor\n{}\n\n".format(str(iris_versicolor_summary)))
    f.write("iris virginica\n{}\n\n".format(str(iris_virginica_summary)))


# References: 
# (2021) Python, Pandas : write content of DataFrame into text File, Available at: https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file (Accessed: 19th April 2021).
# (2021) TypeError: write() argument must be str, not list, Available at: https://stackoverflow.com/questions/41454921/typeerror-write-argument-must-be-str-not-list (Accessed: 19th April 2021).
# How do I select a subset of a DataFrame?, Available at: https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html?highlight=subset (Accessed: 19th April 2021).
