# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:37:22 2023

@author: mordj
"""

import pandas as pd

df = pd.read_csv("D:\Efrei_cours\Semestre_6\Mastercamp\Atelier_Data_Science\Solution_factory\BDD_Amazon.csv", delimiter=";", on_bad_lines= "skip")
df.drop(df.columns[list(range(10,17))], axis = 1, inplace = True)

print(df.columns)

df.drop(["Id", "ProductId", "UserId", "ProfileName"], axis=1, inplace = True)
df.dropna(inplace=True)