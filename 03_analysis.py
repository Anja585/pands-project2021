# analysis.py
# Author: Anja Antolkovic

# 1. Importing relevant libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# 2. Working out the summary of each variable within the data set  

iris = pd.read_csv("iris.data") # loading data set into a DataFrame
iris_setosa = iris[iris["iris_type"] == "Iris-setosa"] # isolating rows only for iris Setosa's from a DataFrame 
iris_versicolor = iris[iris["iris_type"] == "Iris-versicolor"] # isolating rows only for iris Versicolor's from a DataFrame
iris_virginica = iris[iris["iris_type"] == "Iris-virginica"] # isolating rows only for iris Virginica's from a DataFrame         
iris_setosa_summary = iris_setosa.describe() # summary of descriptive statistics for iris Setosa
iris_versicolor_summary = iris_versicolor.describe() # summary of descriptive statistics for iris Versicolor
iris_virginica_summary = iris_virginica.describe() # summary of descriptive statistics for iris Virginica

# 3. Copying the summary of descriptive statistics into txt file 

with open ("iris_data_summary", "w") as f: # opening txt file for writing in test mode
    f.write("iris setosa\n{}\n\n".format(str(iris_setosa_summary))) # overwriting the summary of descriptive statistics for iris Setosa into a txt file  
    f.write("iris versicolor\n{}\n\n".format(str(iris_versicolor_summary))) # overwriting the summary of descriptive statistics for iris Versicolor into a txt file
    f.write("iris virginica\n{}\n\n".format(str(iris_virginica_summary))) # overwriting the summary of descriptive statistics for iris Virginica into a txt file

# 4. Working out the boxplots 

# 4.1. Creating the object variables for each attribute for each class
sepal_length_setosa = iris_setosa.sepal_length
sepal_length_versicolor = iris_versicolor.sepal_length
sepal_length_virginica = iris_virginica.sepal_length
sepal_width_setosa = iris_setosa.sepal_width
sepal_width_versicolor = iris_versicolor.sepal_width
sepal_width_virginica = iris_virginica.sepal_width
petal_length_setosa = iris_setosa.petal_length
petal_length_versicolor = iris_versicolor.petal_length
petal_length_virginica = iris_virginica.petal_length
petal_width_setosa = iris_setosa.petal_width
petal_width_versicolor = iris_versicolor.petal_width
petal_width_virginica = iris_virginica.petal_width

# 4.2. Combining variables into a list appropriately
sepal_length_to_plot = [sepal_length_setosa, sepal_length_versicolor, sepal_length_virginica]
sepal_width_to_plot = [iris_setosa.sepal_width, iris_versicolor.sepal_width, iris_virginica.sepal_width]
petal_length_to_plot = [iris_setosa.petal_length, iris_versicolor.petal_length, iris_virginica.petal_length]
petal_width_to_plot = [iris_setosa.petal_width, iris_versicolor.petal_width, iris_virginica.petal_width]

# 4.3. Labels and subplots
labels = ["setosa", "versicolor", "virginica"] # labels that will be on the x axis
# this line of code defines a figure instance, axis insances and a set of subplots 
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(12,8)) # fig-> figure instance
                                                               # ax1-ax4 -> axis instances, 1 for each subplot 
                                                               # 1,4 -> number of rows and columns      
                                                               # figsize -> figure size, width and height
                                                               # Source: https://matplotlib.org/stable/gallery/statistics/boxplot_color.html
# 4.4. Boxplot 1                  
sepal_length_boxplot = ax1.boxplot(sepal_length_to_plot, # using asix instance and boxplot method to plot the data
                                   patch_artist=True, # to be able to fill with color
                                   labels=labels) # setting up the labels 
ax1.set_title("sepal_length_boxplot") # setting up a title

# 4.5. Boxplot 2
sepal_width_boxplot = ax2.boxplot(sepal_width_to_plot,
                                  patch_artist=True,
                                  labels=labels)
ax2.set_title("sepal_width_boxplot")

# 4.6. Boxplot 3
petal_length_boxplot = ax3.boxplot(petal_length_to_plot,
                                  patch_artist=True,
                                  labels=labels)
ax3.set_title("petal_length_boxplot")

# 4.7. Boxplot 4
petal_width_boxplot = ax4.boxplot(petal_width_to_plot,
                                  patch_artist=True,
                                  labels=labels)
ax4.set_title("petal_width_boxplot")

# 4.8. Fill the colors
colors =  ["pink", "lightblue", "lightgreen"] # colors for each boxplot
for boxplot in (sepal_length_boxplot, sepal_width_boxplot, petal_length_boxplot, petal_width_boxplot): # iterates over tuple of boxplot
    for patch,color in zip(boxplot['boxes'], colors): # boxplot is a dictinary object with 'boxes' as one of the keys
                                                      # zip method pairs together items from a 'colors' list and ['boxes'] values 
                                                      # Source: https://matplotlib.org/stable/gallery/statistics/boxplot_color.html
        patch.set_facecolor(color) # set the color to each boxplot 

# 4.9. Saving the plot
plt.savefig("boxplot.png") # save the boxplot
plt.show() # show the boxplot

# References: 
# (2021) Python, Pandas : write content of DataFrame into text File, Available at: https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file (Accessed: 19th April 2021).
# (2021) TypeError: write() argument must be str, not list, Available at: https://stackoverflow.com/questions/41454921/typeerror-write-argument-must-be-str-not-list (Accessed: 19th April 2021).
# How do I select a subset of a DataFrame?, Available at: https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html?highlight=subset (Accessed: 19th April 2021).
# pandas.DataFrame.boxplot, Available at: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html (Accessed: 20th April 2021).
# (2020) Box Plot in Python using Matplotlib, Available at: https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/ (Accessed: 20th April 2021).
# (2013) Creating boxplots with Matplotlib, Available at: http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/ (Accessed: 21st April 2021).
# Advanced plotting, Available at: https://python4astronomers.github.io/plotting/advanced.html (Accessed: 21st April 2021).
# python matplotlib filled boxplots, Available at: https://stackoverflow.com/questions/20289091/python-matplotlib-filled-boxplots (Accessed: 21st April 2021).
# Box plots with custom fill colors, Available at: https://matplotlib.org/stable/gallery/statistics/boxplot_color.html (Accessed: 21st April 2021).
# matplotlib.pyplot.subplots, Available at: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots (Accessed: 21st April 2021).
# Python zip() Function, Available at: https://www.w3schools.com/python/ref_func_zip.asp (Accessed: 22nd April 2021).