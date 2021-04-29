# analysis.py
# Analysis of iris flower data set for Programming and Scripting module 2021
# Author: Anja Antolkovic

# 1. Importing relevant libraries
import pandas as pd # used to read the data into Pandas data frame and efficient work with data 
import numpy as np # used for descriptive statistics calculations  
import matplotlib.pyplot as plt # used for plotting  

# 2. Working out the summary of each variable within the data set
iris = pd.read_csv("01_iris.data") # loading data set into a DataFrame
df = pd.DataFrame(iris) # defining data frame
iris_setosa = iris[iris["iris_type"] == "Iris-setosa"] # isolating rows only for iris Setosa's from a DataFrame 
iris_versicolor = iris[iris["iris_type"] == "Iris-versicolor"] # isolating rows only for iris Versicolor's from a DataFrame
iris_virginica = iris[iris["iris_type"] == "Iris-virginica"] # isolating rows only for iris Virginica's from a DataFrame   
iris_types_summary = df.describe(include=[np.object]) # summary of descriptive statistics for character columns      
iris_setosa_summary = iris_setosa.describe() # summary of descriptive statistics for iris Setosa
iris_versicolor_summary = iris_versicolor.describe() # summary of descriptive statistics for iris Versicolor
iris_virginica_summary = iris_virginica.describe() # summary of descriptive statistics for iris Virginica

# 3. Copying the summary of descriptive statistics into txt file 
with open ("04_iris_data_summary", "w") as f: # opening txt file for writing in test mode
    f.write("varieties\n{}\n\n".format(str(iris_types_summary))) # overwriting the summary of descriptive statistics for character chategory into a txt file     
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
sepal_width_to_plot = [sepal_width_setosa, sepal_width_versicolor, sepal_width_virginica]
petal_length_to_plot = [petal_length_setosa, petal_length_versicolor, petal_length_virginica]
petal_width_to_plot = [petal_width_setosa, petal_width_versicolor, petal_width_virginica]

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
sepal_width_boxplot = ax2.boxplot(sepal_width_to_plot, patch_artist=True, labels=labels)
ax2.set_title("sepal_width_boxplot")

# 4.6. Boxplot 3
petal_length_boxplot = ax3.boxplot(petal_length_to_plot, patch_artist=True, labels=labels)
ax3.set_title("petal_length_boxplot")

# 4.7. Boxplot 4
petal_width_boxplot = ax4.boxplot(petal_width_to_plot, patch_artist=True, labels=labels)
ax4.set_title("petal_width_boxplot")

# 4.8. Fill the colors
colors =  ["pink", "lightblue", "lightgreen"] # colors for each boxplot
for boxplot in (sepal_length_boxplot, sepal_width_boxplot, petal_length_boxplot, petal_width_boxplot): # iterates over tuple of boxplot
    for patch,color in zip(boxplot['boxes'], colors): # boxplot is a dictinary object with 'boxes' as one of the keys
                                                      # zip method pairs together items from a 'colors' list and ['boxes'] values 
                                                      # Source: https://matplotlib.org/stable/gallery/statistics/boxplot_color.html
        patch.set_facecolor(color) # set the color to each boxplot 

# 4.9. Saving the plot
plt.savefig("05_boxplot.png") # save the boxplot
plt.show() # show the boxplot

# 5. Working out the histograms

# 5.1. Histogram 1
for sepal_length, color in zip(sepal_length_to_plot, colors): # iterates over a list of lengths and colors, zip method pairs each item from the length and color list together in sequential order
    sepal_length_histogram = plt.hist(sepal_length, # passing data to plot the histogram from
                                      alpha=0.75, # adjusting the transparency 
                                      bins=15, # defines the equal-width bins in the range.
                                      color=color) # setting the color

plt.legend(labels) # adding the legend
plt.xlabel("sepal_length") # labeling the plot
plt.ylabel("frequency") # labeling the plot
plt.title("sepal_length_histogram") # adding the title
plt.savefig('07_sepal_length_histogram.png') # saving the plot
plt.show() # showing the plot 

# 5.2. Histogram 2
for sepal_width, color in zip(sepal_width_to_plot, colors):
    sepal_width_histogram = plt.hist(sepal_width, alpha=0.75, bins=15, color=color)

plt.legend(labels)
plt.xlabel("sepal_width")
plt.ylabel("frequency")
plt.title("sepal_width_histogram")
plt.savefig('08_sepal_width_histogram.png')
plt.show()

# 5.3. Histogram 3
for petal_length, color in zip(petal_length_to_plot, colors):
    petal_length_histogram = plt.hist(petal_length, alpha=0.75, bins=15, color=color)

plt.legend(labels)
plt.xlabel("petal_length")
plt.ylabel("frequency")
plt.title("petal_length_histogram")
plt.savefig('09_petal_length_histogram.png')
plt.show()

# 5.4. Histogram 4
for petal_width, color in zip(petal_width_to_plot, colors):
    petal_width_histogram = plt.hist(petal_width, alpha=0.75, bins=15, color=color)

plt.legend(labels)
plt.xlabel("petal_width")
plt.ylabel("frequency")
plt.title("petal_width_histogram")
plt.savefig('10_petal_width_histogram.png')
plt.show()

# 6. Correlation
corrMatrix_setosa = iris_setosa.corr() # correlation matrix for iris setosa
corrMatrix_versicolor = iris_versicolor.corr() # correlation matrix for iris versicolor
corrMatrix_virginica = iris_virginica.corr() # correlation matrix for iris virginica 

with open ("04_iris_data_summary", "a") as f: # opening txt file for appending in test mode
    f.write("correlation matrix setosa\n{}\n\n".format(str(corrMatrix_setosa)))  # appending the correlation matrix for iris setosa into a txt file
    f.write("correlation matrix versicolor\n{}\n\n".format(str(corrMatrix_versicolor))) # appending the correlation matrix for iris versicolor into a txt file
    f.write("correlation matrix virginica\n{}\n\n".format(str(corrMatrix_virginica))) # appending the correlation matrix for iris virginica into a txt file

# 7. Working out the scatter plots

# 7.1. Scatter plot 1
fig, ax1 = plt.subplots() # this line of code defines a figure instance, axis insance and a set of subplots 
                          # fig-> figure instance
                          # ax -> axis instance
for x, y, color in zip(sepal_length_to_plot, sepal_width_to_plot, colors): # iterates over a list of lengths, widths and colors, zip method pairs each item from the length, widths color lists together in sequential order   
    scatter = ax1.scatter(x, y, color=color) # passing data to plot the histogram from
plt.legend(labels) # adding the legend
plt.xlabel("sepal_length") # labeling the plot
plt.ylabel("sepal_width") # labeling the plot
plt.savefig('11_petwid_sepwid_scatterplot.png') # saving the plot
plt.show() # showing the plot

# 7.2 Scatter plot 2
fig, ax2 = plt.subplots()
for x, y, color in zip(sepal_length_to_plot, petal_length_to_plot, colors):    
    ax2.scatter(x, y, color=color) 
plt.legend(labels)
plt.xlabel("sepal_length")
plt.ylabel("petal_length")
plt.savefig('12_seplen_petlen_scatterplot.png')
plt.show()

# 7.3. Scatter plot 3
fig, ax3 = plt.subplots()
for x, y, color in zip(sepal_length_to_plot, petal_width_to_plot, colors):    
    ax3.scatter(x, y, color=color)
plt.legend(labels)
plt.xlabel("sepal_length")
plt.ylabel("petal_width")
plt.savefig('13_seplen_petwid_scatterplot.png')
plt.show()

# 7.4. Scatter plot 4
fig, ax4 = plt.subplots()
for x, y, color in zip(sepal_width_to_plot, petal_length_to_plot, colors):    
    ax4.scatter(x, y, color=color)
plt.legend(labels)
plt.xlabel("sepal_width")
plt.ylabel("petal_length")
plt.savefig('14_sepwid_petlen_scatterplot.png')
plt.show()

# 7.5. Scatter plot 6
fig, ax6 = plt.subplots()
for x, y, color in zip(petal_length_to_plot, petal_width_to_plot, colors):    
    ax6.scatter(x, y, color=color)
plt.legend(labels)
plt.xlabel("petal_length")
plt.ylabel("petal_width")
plt.savefig('15_petlen_petwid_scatterplot.png')
plt.show()

# 7.6. Scatter plot 5
fig, ax5 = plt.subplots()
for x, y, color in zip(sepal_width_to_plot, petal_width_to_plot, colors):    
    ax5.scatter(x, y, color=color)
plt.legend(labels)
plt.xlabel("sepal_width")
plt.ylabel("petal_width")
plt.savefig('16_sepwid_petwid_scatterplot.png')
plt.show()

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
# Plot two histograms on single chart with matplotlib, Available at: https://stackoverflow.com/questions/6871201/plot-two-histograms-on-single-chart-with-matplotlib (Accessed: 23rd April 2021).
# MatPlotLib: Multiple datasets on the same scatter plot, Available at: https://stackoverflow.com/questions/4270301/matplotlib-multiple-datasets-on-the-same-scatter-plot (Accessed: 26th April 2021).
# DESCRIPTIVE OR SUMMARY STATISTICS IN PYTHON PANDAS – DESCRIBE(), Available at: https://www.datasciencemadesimple.com/descriptive-summary-statistics-python-pandas/ (Accessed: 27th April 2021).
# (2020) How to Create a Correlation Matrix using Pandas, Available at: https://datatofish.com/correlation-matrix-pandas/ (Accessed: 28th April 2021).
