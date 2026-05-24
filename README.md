# NHANES Data Analysis

## About project
This project demonstrates data cleaning, visualization, and statistical analysis using a sample NHANES dataset. 
Dataset
Source: NHANES — National Health and Nutrition Examination Survey
Publisher: Centers for Disease Control and Prevention (CDC), USA
Description: Official U.S. population data on health, nutrition, and body measurements
License: Public Domain

## Project structure
* analysis.py
* project.ipynb
* project_clean.ipynb
* project.csv
* project_clean.csv

## Project Goals
* Data cleaning
* Creating categorical variables
* Calculating BMI
* Detecting outliers
* Building visualizations (histograms, boxplots, heatmaps)
* Correlation analysis

## Conclusion 
The analysis reveals several patterns: BMI is highest in the 41-60 age group (aout 25, at the upper boundary of normal) and lowest in children (about 18). According to the heatmap, BMI is most strongly driven by weight (r = 0.95). The unexpectedly high correlation between BMI and height (r = 0.82) is likely explained by the fact that taller participants in this sample also tend to weigh more - meaning weight overrides the effect of height in the BMI formula. Males show slightly higher BMI than females, with greater spread in values. However, drawing global conclusions about the causes of these differences is difficult - the sample size is too small for confident generalizations.

## Limitations:
* The dataset contains only 25 records, which is insufficient for statistically significant conclusions
* BMI does not account for muscle mass or body composition
* No data on diet, physical activity, or lifestyle factors
* The 81+ age group has too few observations for reliable conclusions

## Next Steps:
* Use the full NHANES dataset (thousands of records) for more reliable analysis
* Add statistical testing (t-test) to verify differences between groups
* Build a regression model to predict BMI

## How to Run
1. Clone the repository
2. Install dependencies:
   pip install pandas seaborn matplotlib
3. Open project.ipynb in Jupyter Notebook and run all cells

## Technologies
![Python](https://img.shields.io/badge/Python-3.10-blue)
![pandas](https://img.shields.io/badge/pandas-2.3.2-pink)
![seaborn](https://img.shields.io/badge/seaborn-0.13.2-red)
![matplotlib](https://img.shields.io/badge/matplotlib-3.10.7-purple)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)

## Author
[vaslinx] · [GitHub]( https://github.com/vaslinx)
