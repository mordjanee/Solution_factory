# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:37:22 2023

@author: mordj
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle
import os

dossier = os.path.dirname(__file__)

df = pd.read_csv(os.path.join(dossier, "BDD_Amazon.csv"), delimiter=";", on_bad_lines= "skip")
df.drop(df.columns[list(range(10,17))], axis = 1, inplace = True)

print(df.columns)

df.drop(["Id", "ProductId", "UserId", "ProfileName"], axis=1, inplace = True)
df.dropna(inplace=True)
df.drop_duplicates(inplace = True)

df["Text"] = df["Text"].str.replace("[^\w\s]", "")
df["Text"] = df["Text"].str.lower()
df["Text"] = df["Text"] + " " + df["Summary"]


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
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


sentences_text = "".join(df["Text"].str.lower())
mots = sentences_text.split()
mots_frequents = Counter(mots).most_common(5000)

dictionnaire = {indice : mot for indice, (mot, _) in enumerate(mots_frequents)}
liste = [mot for mot,_ in mots_frequents]
print(liste)

def contain(word, sentence):
    for i in sentence.split() :
        if i == word :
            return True
    return False

def encoding(sentence, liste):
    lst = []
    for i in liste :
        if (contain(i, sentence)):
            lst.append(1)
        else :
            lst.append(0)
    return lst

#%%
            
df["Encoding"] = df["Text"].apply(lambda x: encoding(x, liste))

print(len(df.loc[0, "Encoding"]))

X = df.Encoding.tolist()
y = df.Score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)


#%%

from sklearn import neighbors


knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("KNN accuracy:", accuracy)


#%%

from sklearn.svm import SVC

svc = SVC(kernel = "linear")
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("SVC accuracy:", accuracy)


#%% Sauvegarde du modèle

#Créer un dossier Modeles dans le fichier ou se trouve le python AVANT

dossier = os.path.join(os.path.dirname(__file__), "Modeles") #Récupérer le chemin du dossier actuel

with open(os.path.join(dossier, "knn_sauvegarde.pkl"), "wb") as fichier:
    pickle.dump(knn, fichier)
    
#%%Sauvegarde du modèle SVC

with open(os.path.join(dossier, "SVC_sauvegarde.pkl"), "wb") as fichier:
    pickle.dump(svc, fichier)
    
#%%

dossier = os.path.join(os.path.dirname(__file__), "Listes")

with open(os.path.join(dossier, "liste_5000.pkl"), "wb") as fichier:
    pickle.dump(liste, fichier)



