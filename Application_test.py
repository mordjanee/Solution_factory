# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 09:47:25 2023

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

fenetre = tk.Tk()
fenetre.title("EFREIMOTION")
fenetre.geometry("500x400")

zone_texte = tk.Text(fenetre, width=50, height=10)
zone_texte.pack()


def fonction_test(test) :
    prediction_joy = lr_joy.predict([traitement_donnee(test, joy_list)])
    prediction_disappointment = lr_disappointment.predict([traitement_donnee(test, disappointment_list)])
    prediction_sadness = lr_sadness.predict([traitement_donnee(test, sadness_list)])
    prediction_anger = lr_anger.predict([traitement_donnee(test, anger_list)])
    prediction_surprise = lr_surprise.predict([traitement_donnee(test, surprise_list)])
    
    pourcentage_final(prediction_joy, prediction_disappointment, prediction_sadness, prediction_anger, prediction_surprise)
    return abs(prediction_joy[0]), abs(prediction_disappointment[0]), abs(prediction_sadness[0]), abs(prediction_anger[0]), abs(prediction_surprise[0])
    
    
def recuperer_texte():  #Fonction qui se lance quand le bouton est cliqué
    texte = zone_texte.get("1.0", tk.END)
    print(texte)
    prediction_joy, prediction_disappointment, prediction_sadness, prediction_anger, prediction_surprise = fonction_test(texte)

    categories = ['Joy', 'Disappointment', 'Sadness', 'Anger', 'Surprise']
    pourcentages = [prediction_joy, prediction_disappointment, prediction_sadness, prediction_anger, prediction_surprise]
    
    #Création de la figure
    figure = plt.figure(figsize=(4, 4))
    graphique = figure.add_subplot(111)
    graphique.pie(pourcentages, labels=categories, autopct='%1.1f%%')

    # Création du canevas Tkinter pour afficher le graphique
    canvas = FigureCanvasTkAgg(figure, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    resultat_svc = svc.predict([encoding(texte, liste_5000)])[0]
    print(type(resultat_svc))
    etoiles = "Nombre d'étoiles prédit : " + str(resultat_svc)
    label = tk.Label(text = etoiles)
    label.pack()
    

    
bouton = tk.Button(fenetre, text="Analyser le texte", command=recuperer_texte)
bouton.pack()

fenetre.mainloop()

#%%

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Votre texte
texte = "Votre texte ici ici ici texte"

# Création d'un objet WordCloud avec la taille des mots basée sur leur fréquence
wordcloud = WordCloud(width=800, height=400, background_color="white", relative_scaling=0.5).generate(texte)

# Affichage du nuage de mots
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()






