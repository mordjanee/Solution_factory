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
from matplotlib.figure import Figure

from wordcloud import WordCloud
import matplotlib.pyplot as plt


fenetre = tk.Tk()
fenetre.title("EFREIMOTION")
fenetre.geometry("500x400")

bdd = tk.Entry(fenetre)
bdd.insert(0, "Database name's")
bdd.grid(row=0, column=0)

zone_analyse = tk.Entry(fenetre)
zone_analyse.insert(0, "Comment place's")
zone_analyse.grid(row=1, column=0)

                                            
determiners = ['the', 'a', 'an', 'this', 'that', 'these', 'those', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'each', 'every', 'either', 'neither', 'both', 'another', 'any', 'some', 'several', 'few', 'many', 'much', 'most', 'all', 'enough', 'no', 'any', 'other', 'such', 'what', 'which', 'whichever', 'whose', 'rather', 'quite', 'somebody', 'nobody', 'everyone', 'anyone', 'somebody', 'nobody', 'everyone', 'anyone', 'something', 'nothing', 'everything', 'anything', 'someone', 'no one', 'everyone', 'anyone', 'somewhere', 'nowhere', 'everywhere', 'anywhere', 'either', 'neither', 'both', 'half', 'several', 'few', 'many', 'much', 'most', 'all', 'enough', 'no', 'any', 'other', 'another', 'such', 'what', 'rather', 'quite', 'that', 'those', 'these', 'this', 'the', 'a', 'an']

pronouns = ['i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'you', 'him', 'her', 'us', 'them', 'myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves', 'mine', 'yours', 'his', 'hers', 'its', 'ours', 'theirs', 'this', 'that', 'these', 'those', 'who', 'whom', 'whose', 'which', 'what', 'whatever', 'whoever', 'whichever', 'whomever', 'anyone', 'everyone', 'someone', 'no one', 'anybody', 'everybody', 'somebody', 'nobody', 'anywhere', 'everywhere', 'somewhere', 'nowhere', 'anything', 'everything', 'something', 'nothing', 'any', 'each', 'every', 'either', 'neither', 'both', 'one', 'another', 'such', 'other', 'anybody', 'everybody', 'somebody', 'nobody', 'anyone', 'everyone', 'someone', 'no one', 'anywhere', 'everywhere', 'somewhere', 'nowhere', 'anything', 'everything', 'something', 'nothing', 'any', 'each', 'every', 'either', 'neither', 'both', 'one', 'another', 'some', 'several', 'few', 'many', 'much', 'most', 'all', 'enough']

adjectives = ['good', 'new', 'first', 'last', 'long', 'great', 'little', 'own', 'other', 'old', 'right', 'big', 'high', 'different', 'small', 'large', 'next', 'early', 'young', 'important', 'few', 'public', 'bad', 'same', 'able', 'better', 'best', 'high', 'low', 'early', 'late', 'early', 'late', 'early', 'late', 'early', 'late', 'early', 'late', 'high', 'low', 'early', 'late', 'high', 'low', 'early', 'late', 'early', 'late', 'early', 'late', 'early', 'late', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new', 'young', 'old', 'new']

prepositions = ['about', 'above', 'across', 'after', 'not', 'so', 'too', 'or', 'and', 'against', 'along', 'among', 'around', 'as', 'at', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'beyond', 'by', 'concerning', 'considering', 'despite', 'down', 'during', 'except', 'for', 'from', 'in', 'inside', 'into', 'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'outside', 'over', 'past', 'regarding', 'round', 'since', 'through', 'throughout', 'to', 'toward', 'under', 'underneath', 'until', 'up', 'upon', 'with', 'within', 'without']

verbs = ['be', 'have', 'do', 'go', 'say', 'see', 'get', 'make', 'know', 'think', 'take', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'call', 'try', 'feel', 'become', 'leave', 'put', 'mean', 'keep', 'let', 'begin', 'seem', 'show', 'hear', 'follow', 'help', 'play', 'stop', 'talk', 'turn', 'start', 'bring', 'write', 'provide', 'sit', 'stand', 'lose', 'pay', 'meet', 'include']

def supprimer_mots(texte, dictionnaire):
    mots = texte.split()
    mots_filtres = [mot for mot in mots if mot not in dictionnaire]
    texte_filtre = ' '.join(mots_filtres)
    return texte_filtre

    
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
    graphique.set_title('Graphique des pourcentages de chaque sentiment')

    # Création du canevas Tkinter pour afficher le graphique
    canvas = FigureCanvasTkAgg(figure, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)
    
    
    # Création de la figure n°2
    figure2 = plt.figure(figsize=(4, 4))
    graphique2 = figure2.add_subplot(111)
    graphique2.bar(categories, pourcentages)
    
    # Personnalisation des axes et du titre si nécessaire
    graphique2.set_xlabel('Catégories')
    graphique2.set_ylabel('Pourcentages')
    graphique2.set_title('Graphique en bâton')
    
    canvas6 = FigureCanvasTkAgg(figure2, master=fenetre)
    canvas6.draw()
    canvas6.get_tk_widget().grid(row=0, column=1)
    
    conc_joy = "joy"
    conc_disappointment = "disappointment"
    conc_sadness = "sadness"
    conc_anger = "anger"
    conc_surprise = "surprise"
    
    for i in range(len(df)) : 
        if df.loc[i, "prediction_joy"] > df.loc[i, "prediction_disappointment"] and df.loc[i, "prediction_joy"] > df.loc[i, "prediction_sadness"] and df.loc[i, "prediction_joy"] > df.loc[i, "prediction_anger"] and df.loc[i, "prediction_joy"] > df.loc[i, "prediction_surprise"] :
            conc_joy =conc_joy + " " + str(df.loc[i, zone_commentaire])
            
        if df.loc[i, "prediction_disappointment"] > df.loc[i, "prediction_joy"] and df.loc[i, "prediction_disappointment"] > df.loc[i, "prediction_sadness"] and df.loc[i, "prediction_disappointment"] > df.loc[i, "prediction_anger"] and df.loc[i, "prediction_disappointment"] > df.loc[i, "prediction_surprise"] :
            conc_disappointment = conc_disappointment + " " + str(df.loc[i, zone_commentaire])
            
        if df.loc[i, "prediction_sadness"] > df.loc[i, "prediction_disappointment"] and df.loc[i, "prediction_sadness"] > df.loc[i, "prediction_joy"] and df.loc[i, "prediction_sadness"] > df.loc[i, "prediction_anger"] and df.loc[i, "prediction_sadness"] > df.loc[i, "prediction_surprise"] :
            conc_sadness = conc_sadness + " " + str(df.loc[i, zone_commentaire])
            
        if df.loc[i, "prediction_anger"] > df.loc[i, "prediction_disappointment"] and df.loc[i, "prediction_anger"] > df.loc[i, "prediction_sadness"] and df.loc[i, "prediction_anger"] > df.loc[i, "prediction_joy"] and df.loc[i, "prediction_anger"] > df.loc[i, "prediction_surprise"] :
            conc_anger = conc_anger + " " + str(df.loc[i, zone_commentaire])
            
        if df.loc[i, "prediction_surprise"] > df.loc[i, "prediction_disappointment"] and df.loc[i, "prediction_surprise"] > df.loc[i, "prediction_sadness"] and df.loc[i, "prediction_surprise"] > df.loc[i, "prediction_anger"] and df.loc[i, "prediction_surprise"] > df.loc[i, "prediction_joy"] :
            conc_surprise = conc_surprise + " " + str(df.loc[i, zone_commentaire])
    
    print(conc_surprise)
    print("\n")

    
    conc_joy.replace("[^\w\s]", "")
    conc_joy.lower()
    conc_joy = supprimer_mots(conc_joy, determiners)
    conc_joy = supprimer_mots(conc_joy, pronouns)
    conc_joy = supprimer_mots(conc_joy, adjectives)
    conc_joy = supprimer_mots(conc_joy, prepositions)
    conc_joy = supprimer_mots(conc_joy, verbs)
    
    conc_disappointment.replace("[^\w\s]", "")
    conc_disappointment.lower()
    conc_disappointment = supprimer_mots(conc_disappointment, determiners)
    conc_disappointment = supprimer_mots(conc_disappointment, pronouns)
    conc_disappointment = supprimer_mots(conc_disappointment, adjectives)
    conc_disappointment = supprimer_mots(conc_disappointment, prepositions)
    conc_disappointment = supprimer_mots(conc_disappointment, verbs)
    
    conc_sadness.replace("[^\w\s]", "")
    conc_sadness.lower()
    conc_sadness = supprimer_mots(conc_sadness, determiners)
    conc_sadness = supprimer_mots(conc_sadness, pronouns)
    conc_sadness = supprimer_mots(conc_sadness, adjectives)
    conc_sadness = supprimer_mots(conc_sadness, prepositions)
    conc_sadness = supprimer_mots(conc_sadness, verbs)
    
    conc_anger.replace("[^\w\s]", "")
    conc_anger.lower()
    conc_anger = supprimer_mots(conc_anger, determiners)
    conc_anger = supprimer_mots(conc_anger, pronouns)
    conc_anger = supprimer_mots(conc_anger, adjectives)
    conc_anger = supprimer_mots(conc_anger, prepositions)
    conc_anger = supprimer_mots(conc_anger, verbs)
    
    conc_surprise.replace("[^\w\s]", "")
    conc_surprise.lower()
    conc_surprise = supprimer_mots(conc_surprise, determiners)
    conc_surprise = supprimer_mots(conc_surprise, pronouns)
    conc_surprise = supprimer_mots(conc_surprise, adjectives)
    conc_surprise = supprimer_mots(conc_surprise, prepositions)
    conc_surprise = supprimer_mots(conc_surprise, verbs)
    
    
    wordcloud_joy = WordCloud(width=800, height=400, background_color="white", relative_scaling=0.5).generate(conc_joy)
    # Affichage du nuage de mots
    
    figure = Figure(figsize=(10, 5))
    ax = figure.add_subplot(111)
    ax.imshow(wordcloud_joy, interpolation='bilinear')
    ax.axis('off')
    canvas1 = FigureCanvasTkAgg(figure, master=fenetre)
    canvas1.draw()
    canvas1.get_tk_widget().grid(row=0, column=2)
    
    wordcloud_disappointment = WordCloud(width=800, height=400, background_color="white", relative_scaling=0.5).generate(conc_disappointment)
    # Affichage du nuage de mots
    figure = Figure(figsize=(10, 5))
    ax = figure.add_subplot(111)
    ax.imshow(wordcloud_disappointment, interpolation='bilinear')
    ax.axis('off')
    canvas2 = FigureCanvasTkAgg(figure, master=fenetre)
    canvas2.draw()
    canvas2.get_tk_widget().grid(row=0, column=3)
    
    wordcloud_sadness = WordCloud(width=800, height=400, background_color="white", relative_scaling=0.5).generate(conc_sadness)
    # Affichage du nuage de mots
    figure = Figure(figsize=(10, 5))
    ax = figure.add_subplot(111)
    ax.imshow(wordcloud_sadness, interpolation='bilinear')
    ax.axis('off')
    canvas3 = FigureCanvasTkAgg(figure, master=fenetre)
    canvas3.draw()
    canvas3.get_tk_widget().grid(row=1, column=0)
    
    wordcloud_anger = WordCloud(width=800, height=400, background_color="white", relative_scaling=0.5).generate(conc_anger)
    # Affichage du nuage de mots
    figure = Figure(figsize=(10, 5))
    ax = figure.add_subplot(111)
    ax.imshow(wordcloud_anger, interpolation='bilinear')
    ax.axis('off')
    canvas4 = FigureCanvasTkAgg(figure, master=fenetre)
    canvas4.draw()
    canvas4.get_tk_widget().grid(row=1, column=2)
    
    wordcloud_surprise = WordCloud(width=800, height=400, background_color="white", relative_scaling=0.5).generate(conc_surprise)
    # Affichage du nuage de mots
    figure = Figure(figsize=(10, 5))
    ax = figure.add_subplot(111)
    ax.imshow(wordcloud_surprise, interpolation='bilinear')
    ax.axis('off')
    canvas5 = FigureCanvasTkAgg(figure, master=fenetre)
    canvas5.draw()
    canvas5.get_tk_widget().grid(row=1, column=3)  
    
    
bouton = tk.Button(fenetre, text="Select this file", command=recuperer_texte)
bouton.grid(row=2, column=0)

fenetre.mainloop()


