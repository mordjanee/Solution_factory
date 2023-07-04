# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:37:16 2023

@author: mordj
"""


#%%Récupérer les fonctions, les listes et les modèles du main

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


def traitement_donnee(texte, liste_sentiment) : #Fonction qui encode un texte en fonction de la liste de sentiment sélectionnée
    texte.replace("[^\w\s]", "")
    texte.lower()
    enc = encoding(texte, liste_sentiment)
    return enc

def pourcentage_final(joy, disappointment, sadness, anger, surprise) :  #Fonction qui calcul le pourcentage de chaque émotion en fonction du total de pourcentage
    total = joy + disappointment + sadness + anger + surprise
    joy = float(joy[0]) / total * 100
    disappointment = float(disappointment[0]) / total * 100
    sadness = float(sadness[0]) / total * 100
    anger = float(anger[0]) / total * 100
    surprise = float(surprise[0]) / total * 100
    
    joy = abs(round(joy[0], 2))
    disappointment = abs(round(disappointment[0], 2))
    sadness = abs(round(sadness[0], 2))
    anger = abs(round(anger[0], 2))
    surprise = abs(round(surprise[0], 2))
    
    print("Pourcentage de joie : ", joy, "\nPourcentage de déception : ", disappointment,
          "\nPourcentage de tristesse : ", sadness, "\nPourcentage de colère : ", anger, 
          "\nPourcentage de surprise : ", surprise)
    

import pickle
import os

dossier = os.path.join(os.path.dirname(__file__), "Listes") #Récupérer le chemin du dossier actuel

with open(os.path.join(dossier, "Joy_list.pkl"), "rb") as fichier:
    joy_list = pickle.load(fichier)
    
with open(os.path.join(dossier, "Disappointment_list.pkl"), "rb") as fichier:
    disappointment_list = pickle.load(fichier)
    
with open(os.path.join(dossier, "Sadness_list.pkl"), "rb") as fichier:
    sadness_list = pickle.load(fichier)

with open(os.path.join(dossier, "Anger_list.pkl"), "rb") as fichier:
    anger_list = pickle.load(fichier)
    
with open(os.path.join(dossier, "Surprise_list.pkl"), "rb") as fichier:
    surprise_list = pickle.load(fichier)
    
with open(os.path.join(dossier, "liste_5000.pkl"), "rb") as fichier:
    liste_5000 = pickle.load(fichier)
    
    
dossier = os.path.join(os.path.dirname(__file__), "Modeles") #Récupérer le chemin du dossier actuel

with open(os.path.join(dossier, "lr_joy_sauvegarde.pkl"), "rb") as fichier:
    lr_joy = pickle.load(fichier)
    
with open(os.path.join(dossier, "lr_disappointment_sauvegarde.pkl"), "rb") as fichier:
    lr_disappointment = pickle.load(fichier)
    
with open(os.path.join(dossier, "lr_sadness_sauvegarde.pkl"), "rb") as fichier:
    lr_sadness = pickle.load(fichier)

with open(os.path.join(dossier, "lr_anger_sauvegarde.pkl"), "rb") as fichier:
    lr_anger = pickle.load(fichier)
    
with open(os.path.join(dossier, "lr_surprise_sauvegarde.pkl"), "rb") as fichier:
    lr_surprise = pickle.load(fichier)
    
with open(os.path.join(dossier, "SVC_sauvegarde.pkl"), "rb") as fichier:
    svc = pickle.load(fichier)
    
#%% Création de l'application de test

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd

fenetre = tk.Tk()
fenetre.title("EFREIMOTION")
fenetre.geometry("500x400")

bdd = tk.Entry(fenetre)
bdd.insert(0, "Database name's")
bdd.pack()

zone_analyse = tk.Entry(fenetre)
zone_analyse.insert(0, "Comment place's")
zone_analyse.pack()

    
def recuperer_texte():  #Fonction qui se lance quand le bouton est cliqué

    file = bdd.get()
    dossier = os.path.dirname(__file__) #Récupérer le chemin du dossier actuel
    file = os.path.join(dossier, file)
    
    df = pd.read_csv(file, delimiter=";", on_bad_lines= "skip")
    df = df[:100]
    zone_commentaire = zone_analyse.get()
    print(df.columns)
    
    for i in range(len(df)) :
        
        df.loc[i, "prediction_joy"] = lr_joy.predict([traitement_donnee(df.loc[i, zone_commentaire], joy_list)])
        df.loc[i, "prediction_disappointment"] = lr_disappointment.predict([traitement_donnee(df.loc[i, zone_commentaire], disappointment_list)])
        df.loc[i, "prediction_sadness"] = lr_sadness.predict([traitement_donnee(df.loc[i, zone_commentaire], sadness_list)])
        df.loc[i, "prediction_anger"] = lr_anger.predict([traitement_donnee(df.loc[i, zone_commentaire], anger_list)])
        df.loc[i, "prediction_surprise"] = lr_surprise.predict([traitement_donnee(df.loc[i, zone_commentaire], surprise_list)])
        
        total = df.loc[i, "prediction_joy"] + df.loc[i, "prediction_disappointment"] + df.loc[i, "prediction_sadness"] + df.loc[i, "prediction_anger"] + df.loc[i, "prediction_surprise"]
        df.loc[i, "prediction_joy"] = float(df.loc[i, "prediction_joy"]) / total * 100
        df.loc[i, "prediction_disappointment"] = float(df.loc[i, "prediction_disappointment"]) / total * 100
        df.loc[i, "prediction_sadness"] = float(df.loc[i, "prediction_sadness"]) / total * 100
        df.loc[i, "prediction_anger"] = float(df.loc[i, "prediction_anger"]) / total * 100
        df.loc[i, "prediction_surprise"] = float(df.loc[i, "prediction_surprise"]) / total * 100
        
        df.loc[i, "prediction_joy"] = abs(round(df.loc[i, "prediction_joy"], 2))
        df.loc[i, "prediction_disappointment"] = abs(round(df.loc[i, "prediction_disappointment"], 2))
        df.loc[i, "prediction_sadness"] = abs(round(df.loc[i, "prediction_sadness"], 2))
        df.loc[i, "prediction_anger"] = abs(round(df.loc[i, "prediction_anger"], 2))
        df.loc[i, "prediction_surprise"] = abs(round(df.loc[i, "prediction_surprise"], 2))
    
    df.to_csv(os.path.join(dossier, "test1.csv"), index = False,sep=";", header = True)
    
    average_joy = sum(df["prediction_joy"]) / len(df)
    average_disappointment = sum(df["prediction_disappointment"]) / len(df)
    average_sadness = sum(df["prediction_sadness"]) / len(df)
    average_anger = sum(df["prediction_anger"]) / len(df)
    average_surprise = sum(df["prediction_surprise"]) / len(df)
    
    print("Average joy detected in comments : ", average_joy)
    print("Average disappointed detected in comments : ", average_disappointment)
    print("Average sadness detected in comments : ", average_sadness)
    print("Average anger detected in comments : ", average_anger)
    print("Average surprise detected in comments : ", average_surprise)
    
    categories = ['Joy', 'Disappointment', 'Sadness', 'Anger', 'Surprise']
    pourcentages = [average_joy, average_disappointment, average_sadness, average_anger, average_surprise]
    
    #Création de la figure
    figure = plt.figure(figsize=(4, 4))
    graphique = figure.add_subplot(111)
    graphique.pie(pourcentages, labels=categories, autopct='%1.1f%%')

    # Création du canevas Tkinter pour afficher le graphique
    canvas = FigureCanvasTkAgg(figure, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().pack()
        
    
bouton = tk.Button(fenetre, text="Select this file", command=recuperer_texte)
bouton.pack()

fenetre.mainloop()


