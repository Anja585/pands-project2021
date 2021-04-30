# pands-project2021
## Project for Programming and Scripting module 2021
## Anja Antolkovic
# Introduction
This README file presents the research methodology and outcomes to the final project for the Programming and Scripting module as a part of the Higher Diploma in Computing (Data Analytics) at GMIT. 

The topic of the research project is the Iris flower data set introduced by the British statistician, eugenicist, and biologist Ronald Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems* as an example of linear discriminant analysis. Students were given deliberately vague instructions on how to tackle the project with the intention to come with their own ideas. We will be mainly focusing on descriptive statistics. 
# Iris flower data set
Iris flower data set (sometimes called Anderson's Iris data set by Edgar Anderson who collected the data) consists of 3 classes of 50 instances each, where each class refers to a type of iris plant - *iris setosa, iris versicolor, iris virginica*.
The attributes measured were: 
* sepal length
* sepal width
* petal length
* petal width. 

All measures were given in centimeters. The Iris flower data set is now widely used as a data set for testing purposes in computer science. Below is an image of each flower type and a summary of samples presented in a table. 

![alt text](https://github.com/Anja585/pands-project2021/blob/main/iris_versicolor_setosa_virginica.jpg)
(source: https://www.datacamp.com/community/tutorials/machine-learning-in-r)
```
     sepal-length  sepal_width  petal_length  petal_width    type_of_Iris
0             5.1          3.5           1.4          0.2     Iris-setosa
1             4.9          3.0           1.4          0.2     Iris-setosa
2             4.7          3.2           1.3          0.2     Iris-setosa
3             4.6          3.1           1.5          0.2     Iris-setosa
4             5.0          3.6           1.4          0.2     Iris-setosa
..            ...          ...           ...          ...             ...
145           6.7          3.0           5.2          2.3  Iris-virginica
146           6.3          2.5           5.0          1.9  Iris-virginica
147           6.5          3.0           5.2          2.0  Iris-virginica
148           6.2          3.4           5.4          2.3  Iris-virginica
149           5.9          3.0           5.1          1.8  Iris-virginica    
```
# Descriptive statistics
## Libraries
The first step is to import all necessary libraries of Python that will be used for data analysis. 
```
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
```
* Pandas is a software library written for the Python programming language for data manipulation and analysis. We will use Pandas to read the data into Pandas data frame and efficient work with data. 
* Numpy is a library for the Python programming language, used for working with arrays. NumPy is short for "Numerical Python". We will use Numpy for descriptive statistics calculations. 
* Mathplotlib is a low-level graph plotting library in Python that serves as a visualization utility. Pyplot is a submodule of Mathplotlib. We are using mathplotlib.pyplot for plotting.
## Summary of the data 
Iris data set is stored as a CSV file (comma-separated file) as '01_iris.data'. 
We are loading the file into a Pandas data frame.

```
iris = pd.read_csv("01_iris.data") 
```
Putting data frame into an object variable. 
```
df = pd.DataFrame(iris) 
```
Next, we are selecting a subset of a data frame by filtering rows for Setosa, Versicolor and Virginica iris types separately. 
```
iris_setosa = iris[iris["iris_type"] == "Iris-setosa"]  
iris_versicolor = iris[iris["iris_type"] == "Iris-versicolor"] 
iris_virginica = iris[iris["iris_type"] == "Iris-virginica"]
```
We are using describe() method to get the summary of descriptive statistics for each variable. 
```
iris_types_summary = df.describe(include=[np.object])       
iris_setosa_summary = iris_setosa.describe() 
iris_versicolor_summary = iris_versicolor.describe() 
iris_virginica_summary = iris_virginica.describe() 
```
Finally, data is overwritten into a txt file '04_iris_data_summary'. 
```
with open ("04_iris_data_summary", "w") as f: 
    f.write("varieties\n{}\n\n".format(str(iris_types_summary))) 
    f.write("iris setosa\n{}\n\n".format(str(iris_setosa_summary))) 
    f.write("iris versicolor\n{}\n\n".format(str(iris_versicolor_summary))) 
    f.write("iris virginica\n{}\n\n".format(str(iris_virginica_summary))) 
```
First table gives the summary of descriptive statistics of a character variable 'iris_type'. The table shows there are 150 instances in total, 50 for each iris type. There are 3 unique iris types where iris Setosa is on the top of the list.  
```
varieties
          iris_type
count           150
unique            3
top     Iris-setosa
freq             50
```
The output of the descriptive statistics information for quantitative variables are presented in the tables below. All measures are given in centimeters.  

Count marks the number of instances in the sample for each variable type. Mean is the average of each variable. Standard deviation express how much the members of a group differ from the mean value for the group. The table also gives values of minimun and maximum values, median (50%), first (25%) and third quartile (75%).
```
iris setosa
       sepal_length  sepal_width  petal_length  petal_width
count      50.00000    50.000000     50.000000     50.00000
mean        5.00600     3.418000      1.464000      0.24400
std         0.35249     0.381024      0.173511      0.10721
min         4.30000     2.300000      1.000000      0.10000
25%         4.80000     3.125000      1.400000      0.20000
50%         5.00000     3.400000      1.500000      0.20000
75%         5.20000     3.675000      1.575000      0.30000
max         5.80000     4.400000      1.900000      0.60000
```
```
iris versicolor
       sepal_length  sepal_width  petal_length  petal_width
count     50.000000    50.000000     50.000000    50.000000
mean       5.936000     2.770000      4.260000     1.326000
std        0.516171     0.313798      0.469911     0.197753
min        4.900000     2.000000      3.000000     1.000000
25%        5.600000     2.525000      4.000000     1.200000
50%        5.900000     2.800000      4.350000     1.300000
75%        6.300000     3.000000      4.600000     1.500000
max        7.000000     3.400000      5.100000     1.800000
```
```
iris virginica
       sepal_length  sepal_width  petal_length  petal_width
count      50.00000    50.000000     50.000000     50.00000
mean        6.58800     2.974000      5.552000      2.02600
std         0.63588     0.322497      0.551895      0.27465
min         4.90000     2.200000      4.500000      1.40000
25%         6.22500     2.800000      5.100000      1.80000
50%         6.50000     3.000000      5.550000      2.00000
75%         6.90000     3.175000      5.875000      2.30000
max         7.90000     3.800000      6.900000      2.50000
```
## Boxplots 
We are visualizing data summary output in box plots. Box plot (also called box and whiskers plot) displays the five-number summary of a set of data. The five-number summary is the minimum, first quartile, median, third quartile, and maximum. The five-number summary divides the data into sections that each contain approximately 25%, percent of the data in that set. Example of a boxplot is presented in a below image. 
![alt text](https://github.com/Anja585/pands-project2021/blob/main/06_boxplot_example.jpg)

We are creating the object variables for each attribute for each class.
```
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
```
Varibles are grouped together into a list. 
```
sepal_length_to_plot = [sepal_length_setosa, sepal_length_versicolor, sepal_length_virginica]
sepal_width_to_plot = [sepal_width_setosa, sepal_width_versicolor, sepal_width_virginica]
petal_length_to_plot = [petal_length_setosa, petal_length_versicolor, petal_length_virginica]
petal_width_to_plot = [petal_width_setosa, petal_width_versicolor, petal_width_virginica]
```
Grouping together labels for x axis into a list. 
```
labels = ["setosa", "versicolor", "virginica"]
```
Matplotlib.pyplot is used to create a figure instance and a set of subplots.
```
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(12,8))
```
Plotting the box plots using matplotlib.pyplot.
```
Boxplot 1 
sepal_length_boxplot = ax1.boxplot(sepal_length_to_plot, patch_artist=True, labels=labels) 
ax1.set_title("sepal_length_boxplot") 

Boxplot 2
sepal_width_boxplot = ax2.boxplot(sepal_width_to_plot, patch_artist=True, labels=labels)
ax2.set_title("sepal_width_boxplot")

Boxplot 3
petal_length_boxplot = ax3.boxplot(petal_length_to_plot, patch_artist=True, labels=labels)
ax3.set_title("petal_length_boxplot")

Boxplot 4
petal_width_boxplot = ax4.boxplot(petal_width_to_plot, patch_artist=True, labels=labels)
ax4.set_title("petal_width_boxplot")
```
Using 'for loop' and zip() method to pair each box plot with the color from the list. 
```
colors =  ["pink", "lightblue", "lightgreen"] 
for boxplot in (sepal_length_boxplot, sepal_width_boxplot, petal_length_boxplot, petal_width_boxplot): 
    for patch,color in zip(boxplot['boxes'], colors): 
        patch.set_facecolor(color) 
```
Isolated points (little cicles) in boxplots are outliners - piece of data that is an abnormal distance from other points. Looking at the boxplot we can see there are not many of them, so they wouldn't have a large impact on the statistics.

The below image of boxplots for each variable type shows petal length and petal width measures are the best indicators to use for determining the type of iris.  
![alt text](https://github.com/Anja585/pands-project2021/blob/main/05_boxplot.png)
## Histograms 
Plotting the histograms using matplotlib.pyplot.
```
Histogram 1
for sepal_length, color in zip(sepal_length_to_plot, colors):
    sepal_length_histogram = plt.hist(sepal_length, alpha=0.75, bins=15, color=color) 

plt.legend(labels) 
plt.xlabel("sepal_length") 
plt.ylabel("frequency") 
plt.title("sepal_length_histogram") 
plt.savefig('07_sepal_length_histogram.png') 
plt.show() 

Histogram 2
for sepal_width, color in zip(sepal_width_to_plot, colors):
    sepal_width_histogram = plt.hist(sepal_width, alpha=0.75, bins=15, color=color)

plt.legend(labels)
plt.xlabel("sepal_width")
plt.ylabel("frequency")
plt.title("sepal_width_histogram")
plt.savefig('08_sepal_width_histogram.png')
plt.show()

Histogram 3
for petal_length, color in zip(petal_length_to_plot, colors):
    petal_length_histogram = plt.hist(petal_length, alpha=0.75, bins=15, color=color)

plt.legend(labels)
plt.xlabel("petal_length")
plt.ylabel("frequency")
plt.title("petal_length_histogram")
plt.savefig('09_petal_length_histogram.png')
plt.show()

Histogram 4
for petal_width, color in zip(petal_width_to_plot, colors):
    petal_width_histogram = plt.hist(petal_width, alpha=0.75, bins=15, color=color)

plt.legend(labels)
plt.xlabel("petal_width")
plt.ylabel("frequency")
plt.title("petal_width_histogram")
plt.savefig('10_petal_width_histogram.png')
plt.show()
```
The below images of histograms for each variable type shows petal length and petal width measures are the best indicators to use for determining the type of iris because there is least amount of overlap between histograms. 
![alt text](https://github.com/Anja585/pands-project2021/blob/main/07_sepal_length_histogram.png)
![alt text](https://github.com/Anja585/pands-project2021/blob/main/08_sepal_width_histogram.png)
![alt text](https://github.com/Anja585/pands-project2021/blob/main/09_petal_length_histogram.png)
![alt text](https://github.com/Anja585/pands-project2021/blob/main/10_petal_width_histogram.png)
## Correlation 
Pandas dataframe and corr() method is used to find the pairwise correlation of all columns in the dataframe for each iris type separately.
```
corrMatrix_setosa = iris_setosa.corr() 
corrMatrix_versicolor = iris_versicolor.corr() 
corrMatrix_virginica = iris_virginica.corr() 
```
Data is appended into a txt file '04_iris_data_summary'. 
```
with open ("04_iris_data_summary", "a") as f: mode
    f.write("correlation matrix setosa\n{}\n\n".format(str(corrMatrix_setosa)))  
    f.write("correlation matrix versicolor\n{}\n\n".format(str(corrMatrix_versicolor))) 
    f.write("correlation matrix virginica\n{}\n\n".format(str(corrMatrix_virginica)))
```

A correlation between variables indicates that as one variable changes in value, the other variable tends to change in a specific direction. The correlation coefficient is a statistical measure that measures both the direction and the strength of this tendency. The correlation coefficient can take the value anywhere between -1 and 1 where:
* 1 indicates a strong positive relationship,
* -1 indicates a strong negative relationship,
* zero indicates no relationship at all.
```
correlation matrix setosa
              sepal_length  sepal_width  petal_length  petal_width
sepal_length      1.000000     0.746780      0.263874     0.279092
sepal_width       0.746780     1.000000      0.176695     0.279973
petal_length      0.263874     0.176695      1.000000     0.306308
petal_width       0.279092     0.279973      0.306308     1.000000

correlation matrix versicolor
              sepal_length  sepal_width  petal_length  petal_width
sepal_length      1.000000     0.525911      0.754049     0.546461
sepal_width       0.525911     1.000000      0.560522     0.663999
petal_length      0.754049     0.560522      1.000000     0.786668
petal_width       0.546461     0.663999      0.786668     1.000000

correlation matrix virginica
              sepal_length  sepal_width  petal_length  petal_width
sepal_length      1.000000     0.457228      0.864225     0.281108
sepal_width       0.457228     1.000000      0.401045     0.537728
petal_length      0.864225     0.401045      1.000000     0.322108
petal_width       0.281108     0.537728      0.322108     1.000000
```
## Scatter plots
Plotting the scatter plots using matplotlib.pyplot.
```
Scatter plot 1
fig, ax1 = plt.subplots() 
for x, y, color in zip(sepal_length_to_plot, sepal_width_to_plot, colors): 
    scatter = ax1.scatter(x, y, color=color) # passing data to plot the histogram from
plt.legend(labels) 
plt.xlabel("sepal_length") 
plt.ylabel("sepal_width") 
plt.savefig('11_petwid_sepwid_scatterplot.png') 
plt.show() 

Scatter plot 2
fig, ax2 = plt.subplots()
for x, y, color in zip(sepal_length_to_plot, petal_length_to_plot, colors):    
    ax2.scatter(x, y, color=color) 
plt.legend(labels)
plt.xlabel("sepal_length")
plt.ylabel("petal_length")
plt.savefig('12_seplen_petlen_scatterplot.png')
plt.show()

Scatter plot 3
fig, ax3 = plt.subplots()
for x, y, color in zip(sepal_length_to_plot, petal_width_to_plot, colors):    
    ax3.scatter(x, y, color=color)
plt.legend(labels)
plt.xlabel("sepal_length")
plt.ylabel("petal_width")
plt.savefig('13_seplen_petwid_scatterplot.png')
plt.show()

Scatter plot 4
fig, ax4 = plt.subplots()
for x, y, color in zip(sepal_width_to_plot, petal_length_to_plot, colors):    
    ax4.scatter(x, y, color=color)
plt.legend(labels)
plt.xlabel("sepal_width")
plt.ylabel("petal_length")
plt.savefig('14_sepwid_petlen_scatterplot.png')
plt.show()

Scatter plot 6
fig, ax6 = plt.subplots()
for x, y, color in zip(petal_length_to_plot, petal_width_to_plot, colors):    
    ax6.scatter(x, y, color=color)
plt.legend(labels)
plt.xlabel("petal_length")
plt.ylabel("petal_width")
plt.savefig('15_petlen_petwid_scatterplot.png')
plt.show()

Scatter plot 5
fig, ax5 = plt.subplots()
for x, y, color in zip(sepal_width_to_plot, petal_width_to_plot, colors):    
    ax5.scatter(x, y, color=color)
plt.legend(labels)
plt.xlabel("sepal_width")
plt.ylabel("petal_width")
plt.savefig('16_sepwid_petwid_scatterplot.png')
plt.show()
```

![alt text](https://github.com/Anja585/pands-project2021/blob/main/11_petwid_sepwid_scatterplot.png)
![alt text](https://github.com/Anja585/pands-project2021/blob/main/12_seplen_petlen_scatterplot.png)
![alt text](https://github.com/Anja585/pands-project2021/blob/main/13_seplen_petwid_scatterplot.png)
![alt text](https://github.com/Anja585/pands-project2021/blob/main/14_sepwid_petlen_scatterplot.png)
![alt text](https://github.com/Anja585/pands-project2021/blob/main/15_petlen_petwid_scatterplot.png)
![alt text](https://github.com/Anja585/pands-project2021/blob/main/16_sepwid_petwid_scatterplot.png)

# References
1. (25th February 2021) Iris flower data set, Available at: https://en.wikipedia.org/wiki/Iris_flower_data_set (Accessed: 15th April 2021).
2. Real Python (20th June 2019) PEP8 Tips: Python Naming Conventions, Available at: https://www.youtube.com/watch?v=Uw95Uc3xgWU (Accessed: 17th April 2021).
3. UCI Machine Learning Repository Iris Data Set, Available at: http://archive.ics.uci.edu/ml/datasets/Iris (Accessed: 17th April 2021).
4. Grepper () “how to import .data file in python pandas” Code Answer, Available at: https://www.codegrepper.com/code-examples/python/how+to+import+.data+file+in+python+pandas (Accessed: 17th April 2021).
5. R. A. Fisher (1936) The use of multiple measurements in taxonomic problems. Wiley Online Library [Online]. Available at: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x (Accessed: 14th April 2021).
6. Karlijn Willems (20th November 2018) Machine Learning in R for beginners, Available at: https://www.datacamp.com/community/tutorials/machine-learning-in-r (Accessed: 18th April 2021).
7. Pratik Nabriya (2019) Exploratory Data Analysis: Uni-variate analysis of Iris Data set, Available at: https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40 (Accessed: 19th April 2021).
8. (2021) Python, Pandas : write content of DataFrame into text File, Available at: https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file (Accessed: 19th April 2021).
9. (2021) TypeError: write() argument must be str, not list, Available at: https://stackoverflow.com/questions/41454921/typeerror-write-argument-must-be-str-not-list (Accessed: 19th April 2021).
10. How do I select a subset of a DataFrame?, Available at: https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html?highlight=subset (Accessed: 19th April 2021).
11. pandas.DataFrame.boxplot, Available at: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html (Accessed: 20th April 2021).
12. (2020) Box Plot in Python using Matplotlib, Available at: https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/ (Accessed: 20th April 2021).
13. (2013) Creating boxplots with Matplotlib, Available at: http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/ (Accessed: 21st April 2021).
14. Advanced plotting, Available at: https://python4astronomers.github.io/plotting/advanced.html (Accessed: 21st April 2021).
15. python matplotlib filled boxplots, Available at: https://stackoverflow.com/questions/20289091/python-matplotlib-filled-boxplots (Accessed: 21st April 2021).
16. Box plots with custom fill colors, Available at: https://matplotlib.org/stable/gallery/statistics/boxplot_color.html (Accessed: 21st April 2021).
17. matplotlib.pyplot.subplots, Available at: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots (Accessed: 21st April 2021).
18. Python zip() Function, Available at: https://www.w3schools.com/python/ref_func_zip.asp (Accessed: 22nd April 2021).
19. Box Plot (Box and Whiskers): How to Read One & How to Make One in Excel, TI-83, SPSS, Available at: https://www.statisticshowto.com/probability-and-statistics/descriptive-statistics/box-plot/ (Accessed: 22nd April 2021).
20. (2014) Probability Density Function/Probability Distribution Function: Definition, TI83 NormalPDF, Available at: https://www.statisticshowto.com/probability-density-function/ (Accessed: 23rd April 2021).
21. Plot two histograms on single chart with matplotlib, Available at: https://stackoverflow.com/questions/6871201/plot-two-histograms-on-single-chart-with-matplotlib (Accessed: 23rd April 2021).
22. MatPlotLib: Multiple datasets on the same scatter plot, Available at: https://stackoverflow.com/questions/4270301/matplotlib-multiple-datasets-on-the-same-scatter-plot (Accessed: 25th April 2021).
23.  MatPlotLib: Multiple datasets on the same scatter plot, Available at: https://stackoverflow.com/questions/4270301/matplotlib-multiple-datasets-on-the-same-scatter-plot (Accessed: 26th April 2021).
24. DESCRIPTIVE OR SUMMARY STATISTICS IN PYTHON PANDAS – DESCRIBE(), Available at: https://www.datasciencemadesimple.com/descriptive-summary-statistics-python-pandas/ (Accessed: 27th April 2021).
25. (2020) How to Create a Correlation Matrix using Pandas, Available at: https://datatofish.com/correlation-matrix-pandas/ (Accessed: 28th April 2021).
26. pandas (software), Available at: https://en.wikipedia.org/wiki/Pandas_(software) (Accessed: 29th April 2021).
27. NumPy, Available at: https://en.wikipedia.org/wiki/NumPy (Accessed: 29th April 2021).
28. NumPy Tutorial, Available at: https://www.w3schools.com/python/numpy/default.asp (Accessed: 29th April 2021).
29. Matplotlib Tutorial, Available at: https://www.w3schools.com/python/matplotlib_intro.asp (Accessed: 29th April 2021).
30. Box plot review, Available at: https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/a/box-plot-review (Accessed: 30th April 2021).
31. Outliers: Finding Them in Data, Formula, Examples. Easy Steps and Video, Available at: https://www.statisticshowto.com/statistics-basics/find-outliers/ (Accessed: 30th April 2021).
32. Correlation Coefficient: Simple Definition, Formula, Easy Steps, Available at: https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/ (Accessed: 30th April 2021).