# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:37:22 2023

@author: mordj
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("D:\Efrei_cours\Semestre_6\Mastercamp\Atelier_Data_Science\Solution_factory\BDD_Amazon.csv", delimiter=";", on_bad_lines= "skip")
df.drop(df.columns[list(range(10,17))], axis = 1, inplace = True)

print(df.columns)

df.drop(["Id", "ProductId", "UserId", "ProfileName"], axis=1, inplace = True)
df.dropna(inplace=True)
df.drop_duplicates(inplace = True)

new_bdd = df.to_csv("D:\Efrei_cours\Semestre_6\Mastercamp\Atelier_Data_Science\Solution_factory\BDD_New.csv", index = False,sep=";", header = True)


#%%
print(df)
print(df.describe())
df.info()

print("Pourcentage du nombre de valeurs manquantes par colonne dans l'ordre décroissant")
print((df.isnull().sum() / df.shape[0]).sort_values(ascending=False))
plt.figure(figsize=(20,13))
sns.heatmap(df.isna(), cbar=False) # affichage sous forme d'image de ces valeurs manquantes
plt.show()


#%%Création du dictionnaire et de la liste avec les mots les plus fréquents

from collections import Counter

sentences_text = "".join(df["Text"].str.lower())
mots = sentences_text.split()
mots_frequents = Counter(mots).most_common(10000)

dictionnaire = {indice : mot for indice, (mot, _) in enumerate(mots_frequents)}
liste = [mot for mot,_ in mots_frequents]
print(liste)

def contain(mot):
    for i in liste :
        if i == mot :
            return True
    return False

def encoding(sentence):
    lst = []
    for i in sentence.split() :
        if (contain(i)):
            lst.append(1)
        else :
            lst.append(0)
    return lst

            
df["Encoding"] = df["Text"].apply(lambda x: encoding(x))

print(len(df.loc[0, "Encoding"]))



#%%

from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = df.Text
y = df.Score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy_score(y_test, y_pred)









