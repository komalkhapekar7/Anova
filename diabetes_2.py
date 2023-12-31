# -*- coding: utf-8 -*-
"""diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dSxagZ7ILA5YgzZQfeiuaNz8ZqaEv0jv
"""

import pandas as pd
df = pd.read_csv("diabetes.csv")

df.info

p1 = df['Pregnancies'].to_list()

p2 = df['Glucose'].to_list()

p3 = df['BloodPressure'].to_list()

p4 = df['SkinThickness'].to_list()

p5 = df['Insulin'].to_list()

p6 = df['BMI'].to_list()

p7 = df['DiabetesPedigreeFunction'].to_list()

p8 = df['Age'].to_list()

p9 = df['Outcome'].to_list()

# Importing library
from scipy.stats import f_oneway

# Conduct the one-way ANOVA
f_oneway(p1, p2, p3, p4, p5, p6, p7, p8, p9)

