# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:01:21 2023

@author: mordj
"""

#%%Création des listes de mots pour chaque sentiment

joy_list = ['joy', 'happiness', 'delight', 'elation', 'bliss', 'ecstasy', 'excitement',
            'jubilation', 'thrill', 'rejoice', 'exhilaration', 'glee', 'joviality',
            'contentment', 'cheerfulness', 'mirth', 'gladness', 'euphoria', 'gratitude',
            'lightheartedness', 'euphoric', 'elated', 'happy', 'cheerful', 'thrilled', 'excited',
            'radiant', 'enthusiastic', 'ecstatic', 'upbeat', 'vibrant', 'delighted', 'overjoyed',
            'exuberant', 'optimistic', 'satisfied', 'grateful', 'bubbly', 'buoyant', 'blissful',
            'lively', 'sunny', 'giddy', 'jolly', 'jubilant', 'whimsical', 'energized', 'merry',
            'zestful', 'thrilling', 'smiling', 'laughing', 'carefree', 'upjoyed', 'triumphant',
            'rapturous', 'playful', 'sparkling', 'radiating', 'savoring', 'high-spirited',
            'giggly', 'cherished', 'uplifted', 'singing', 'enraptured', 'beaming', 'bouncing',
            'elfin', 'heartwarming', 'glowing', 'brimming', 'rejuvenated', 'paradisiacal',
            'gustatory', 'breezy', 'dreamy', 'ecphrastic', 'ebullient', 'blithesome', 'jocund',
            'sprightly', 'festive', 'effervescent', 'hilarious', 'laudatory', 'victorious',
            'fantastic', 'triumph', 'exultant', 'enthralling', 'gleeful', 'enchanting',
            'amazing', 'awesome', 'wonderful', 'great', 'excellent', 'fabulous', 'superb',
            'incredible', 'pleased', 'joyful', 'blessed', 'enjoyable', 'exhilarating',
            'mind-blowing', 'unbelievable', 'captivating', 'magical', 'inspiring', 'celebratory',
            'delicious', 'beautiful', 'sensational', 'outstanding', 'glorious', 'wonder-filled',
            'radiating', 'brilliant', 'fantabulous', 'breathtaking', 'fulfilled', 'thankful',
            'cheering', 'rejoicing', 'enlivened', 'wondrous', 'inspirited', 'paradisiacal',
            'squealing', 'pride', 'delightful', 'favorite', 'good', 'pleasant', 'best','love',
            'loves']

              
disappointment_list = ['disappointment', 'frustration', 'letdown', 'despair', 'regret', 'dismay',
                       'displeasure', 'defeat', 'disillusionment', 'gloom', 'sorrow',
                       'heartbreak', 'bitterness', 'discontentment', 'misery', 'anguish',
                       'melancholy', 'woe', 'unfulfilled', 'hopelessness', 'discouragement',
                       'downhearted', 'sad', 'dejected', 'crestfallen', 'unhappy', 'miserable',
                       'forlorn', 'despondent', 'gloomy', 'regretful', 'disheartened',
                       'demoralized', 'deflated', 'upset', 'dispirited', 'dissatisfied',
                       'desolate', 'wretched', 'broken-hearted', 'troubled', 'lament',
                       'lamentable', 'pathetic', 'sorry', 'pessimistic', 'betrayed', 'abandoned',
                       'crushed', 'suffering', 'tearful', 'weeping', 'crying', 'grieving',
                       'distressed', 'morose', 'apathetic', 'grievous', 'desperate', 'lonely',
                       'underwhelmed', 'disgruntled', 'mortified', 'shattered', 'dashed',
                       'angry', 'enraged', 'resentful', 'furious', 'indignant', 'exasperated',
                       'irritated', 'annoyed', 'displeased', 'bitter', 'sour', 'downcast',
                       'weary', 'downtrodden', 'woeful', 'doubtful', 'dismal', 'vanquished',
                       'overwhelmed', 'rueful', 'shocked', 'repentant', 'disappointing',
                       'frustrating', 'underwhelming', 'unsatisfied', 'unsatisfactory',
                       'disillusioned', 'discouraged', 'heartbreaking', 'annoying',
                       'discontent', 'lousy', 'bad', 'poor', 'mediocre', 'subpar', 'inferior',
                       'disastrous', 'deflating', 'bummer', 'unfortunate', 'unimpressed',
                       'unpromising', 'unfavorable', 'disconcerting', 'horrific', 'disgusted',
                       'grieved', 'disenchanted', 'dissatisfying', 'unexciting', 'uninspiring',
                       'depressing', 'dispiriting', 'disillusioning', 'discouraging',
                       'aggravating', 'exasperating', 'maddening', 'vexing', 'challenging',
                       'saddening', 'error', 'mess','deceptive']


sadness_list = ['sadness', 'grief', 'sorrow', 'heartache', 'melancholy', 'despair', 'depression',
                'misery', 'anguish', 'pain', 'regret', 'desolation', 'disheartenment', 'tears',
                'unhappiness', 'mournful', 'blue', 'down', 'gloomy', 'mourn', 'weep', 'cry',
                'suffering', 'bereavement', 'woeful', 'despondency', 'forlorn', 'lament',
                'agonizing', 'unbearable', 'tragic', 'broken', 'disconsolate', 'distressed',
                'wretched', 'pensive', 'loneliness', 'heartbroken', 'grieving', 'sombre',
                'mourning', 'dismal', 'weary', 'gloom', 'sigh', 'troublesome', 'sullen',
                'downtrodden', 'regretful', 'dejected', 'defeated', 'sob', 'solitude', 'upset',
                'inconsolable', 'desperate', 'burdened', 'downcast', 'funereal', 'pathetic',
                'low', 'aching', 'lamentable', 'somber', 'oppressed', 'downhearted', 'dolorous',
                'morose', 'suffer', 'broken-hearted', 'miserable', 'morning', 'distraught',
                'grievous', 'hurting', 'weepy', 'affliction', 'angst', 'crushed', 'darkness',
                'disappointed', 'depressed', 'despairing', 'heavy-hearted', 'hurt', 'sorrowful',
                'lonesome', 'wistful', 'painful', 'troubled', 'unconsolable', 'bereft', 'angry',
                'isolated', 'lonely', 'dreary', 'bitter', 'deplorable', 'pessimistic',
                'lamenting', 'grief-stricken', 'heartrending', 'heart-rending']


anger_list = ['anger', 'rage', 'fury', 'outrage', 'resentment', 'irritation', 'wrath',
              'indignation', 'annoyance', 'frustration', 'exasperation', 'hostility',
              'bitterness', 'displeasure', 'temper', 'madness', 'fume', 'irritability',
              'fuming', 'irritated', 'enraged', 'incensed', 'livid', 'infuriated', 'furious',
              'agitated', 'outraged', 'angry', 'resentful', 'provoked', 'upset', 'pissed off',
              'hateful', 'indignant', 'wrathful', 'irate', 'vengeful', 'storming', 'raving',
              'cross', 'offended', 'incandescent', 'infuriate', 'frenzy', 'choleric',
              'temperamental', 'steamed up', 'vexed', 'seething', 'aggravated', 'boiling',
              'splenetic', 'mad', 'ballistic', 'belligerent', 'rabid', 'pissed', 'huffy',
              'acerbic', 'bellicose', 'snappish', 'sullen', 'ticked off', 'disgusted',
              'incandescence', 'hot under the collar', 'passionate', 'malice', 'ire', 'scornful',
              'peeved', 'acerbity', 'acerbate', 'infuriation', 'enflamed', 'sharpness', 'piqued',
              'animosity', 'aggression', 'snappy', 'provocative', 'sore', 'wrangle',
              'hot-headed', 'up in arms', 'bellowing', 'boiling point', 'outrageous',
              'irritating', 'aggravating', 'provoking', 'steaming', 'ballistic', 'malicious']



surprise_list = ['surprise', 'amazement', 'astonishment', 'wonder', 'awe', 'shock',
                 'bewilderment', 'stunned', 'startled', 'dazed', 'perplexity', 'disbelief',
                 'incredulity', 'astounded', 'flabbergasted', 'marvel', 'gape', 'unexpected',
                 'unbelievable', 'speechless', 'jaw-dropping', 'eye-opening', 'stupefaction',
                 'gobsmacked', 'mind-blowing', 'awe-inspiring', 'astonished', 'fascination',
                 'staggered', 'surprised', 'baffled', 'taken aback', 'wow', 'mind-boggled',
                 'shocked', 'captivating', 'gobstruck', 'astounding', 'wowed', 'mind-boggling',
                 'impressed', 'jolted', 'awe-struck', 'disoriented', 'flummoxed', 'stupefied',
                 'overwhelmed', 'mystified', 'struck', 'spellbound', 'bewildered', 'surprising',
                 'awe-filled', 'jaw-dropping', 'stun', 'bewilder', 'shaken', 'in awe',
                 'dumbfounded', 'mesmerized', 'awestruck', 'stupefy', 'astonishing', 'unreal',
                 'incredible', 'unusual', 'jolt', 'unpredictable', 'unexpectedly',
                 'mind-bending', 'shattering', 'wondrous', 'flabbergast', 'goggle',
                 'eye-popping', 'delight', 'bemusement', 'curiosity', 'incomprehension',
                 'mystify', 'fascinated', 'disoriented', 'nonplussed', 'wonderment',
                 'unbelievably', 'impressive', 'unforeseen', 'suspense', 'marvelous',
                 'extraordinary', 'intrigue', 'gobsmack', 'dumbstruck', 'amazing',
                 'wonderstruck', 'dazzling', 'enchant', 'boggle', 'delighted', 'curious',
                 'remarkable', 'astonish', 'stunning', 'awe-inspired', 'breathtaking',
                 'spectacular', 'wonderful', 'captivate', 'fascinate']



print("Taille de la liste des mots exprimant la joie : ", len(joy_list))
print("Taille de la liste des mots exprimant la déception : ", len(disappointment_list))
print("Taille de la liste des mots exprimant la tristesse : ", len(sadness_list))
print("Taille de la liste des mots exprimant la colère : ", len(anger_list))
print("Taille de la liste des mots exprimant l'étonnement : ", len(surprise_list))


#%%

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


#%%
print(df)
print(df.describe())
df.info()

#%%Supprimer la ponctuation du texte et minuscule

df["Text"] = df["Text"].str.replace(",", "")
df["Text"] = df["Text"].str.replace("!", "")
df["Text"] = df["Text"].str.replace(":", "")
df["Text"] = df["Text"].str.replace("?", "")
df["Text"] = df["Text"].str.replace(";", "")
df["Text"] = df["Text"].str.replace(".", "")
df["Text"] = df["Text"].str.replace("[^\w\s]", "")

df["Text"] = df["Text"].str.lower()
df["Summary"] = df["Summary"].str.replace("[^\w\s]", "")
df["Summary"] = df["Summary"].str.lower()

#Concaténation du Summary et du Text
df["Text"] = df["Text"] + " " + df["Summary"]

#Fonctions qui encodent le texte

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


def pourcent_sentiment(encoding) :   #Pourcentage du sentiment dans l'encodage en comptant les 1
    cpt = 0
    for i in encoding :
        if i == 1 :
            cpt += 1
    if len(encoding)!=0:
        return (cpt / len(encoding)) * 100
    

#Application de l'encodage et création de colonnes pour chaque sentiments
df["Encoding_joy"] = df["Text"].apply(lambda x: encoding(x, joy_list))
df["Encoding_disappointment"] = df["Text"].apply(lambda x: encoding(x, disappointment_list))
df["Encoding_sadness"] = df["Text"].apply(lambda x: encoding(x, sadness_list))
df["Encoding_anger"] = df["Text"].apply(lambda x: encoding(x, anger_list))
df["Encoding_surprise"] = df["Text"].apply(lambda x: encoding(x, surprise_list))


#Application du pourcentage et création de colonnes pour chaque sentiments
df["Joy_pourcentage"] = df["Encoding_joy"].apply(pourcent_sentiment)
df["Disappointment_pourcentage"] = df["Encoding_disappointment"].apply(pourcent_sentiment)
df["Sadness_pourcentage"] = df["Encoding_sadness"].apply(pourcent_sentiment)
df["Anger_pourcentage"] = df["Encoding_anger"].apply(pourcent_sentiment)
df["Surprise_pourcentage"] = df["Encoding_surprise"].apply(pourcent_sentiment)


print(df.loc[2, "Encoding_joy"])
print(df.loc[2, "Joy_pourcentage"])


#Compter le nombre de ligne où aucun sentiment n'a été identifié
count = len(df[(df["Joy_pourcentage"].fillna(0) == 0) & (df["Disappointment_pourcentage"].fillna(0) == 0) &
              (df["Sadness_pourcentage"].fillna(0) == 0) & (df["Anger_pourcentage"].fillna(0) == 0) &
              (df["Surprise_pourcentage"].fillna(0) == 0)])

print(count)
print(len(df))

#Créer une colonne avec la somme des pourcentages
df["sum_pourcentage"] = df["Joy_pourcentage"] + df["Disappointment_pourcentage"] + df["Sadness_pourcentage"] + df["Anger_pourcentage"] + df["Surprise_pourcentage"]

#Supprimer les lignes sans sentiment
df.drop(df[df["sum_pourcentage"] == 0].index, inplace = True)

#Vérifier qu'il n'y a plus de ligne sans sentiment
count = len(df[(df["Joy_pourcentage"].fillna(0) == 0) & (df["Disappointment_pourcentage"].fillna(0) == 0) &
              (df["Sadness_pourcentage"].fillna(0) == 0) & (df["Anger_pourcentage"].fillna(0) == 0) &
              (df["Surprise_pourcentage"].fillna(0) == 0)])

print(count)
print(len(df))

#Création de la nouvelle base de données
df.to_csv("D:\Efrei_cours\Semestre_6\Mastercamp\Atelier_Data_Science\Solution_factory\BDD_New.csv", index = False,sep=";", header = True)

#%%

type(df["Encoding_joy"])

#%% Création des modèle de machine learning (régression linéaire)


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


lr_joy = LinearRegression()
X = df["Encoding_joy"].tolist()
y = df["Joy_pourcentage"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
lr_joy.fit(X_train, y_train)
y_pred = lr_joy.predict(X_test)
r2 = r2_score(y_test, y_pred)
print("R2 Score modèle joie:", r2)


lr_disappointment = LinearRegression()
X = df["Encoding_disappointment"].tolist()
y = df["Disappointment_pourcentage"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
lr_disappointment.fit(X_train, y_train)
y_pred = lr_disappointment.predict(X_test)
r2 = r2_score(y_test, y_pred)
print("R2 Score modèle déception:", r2)


lr_sadness = LinearRegression()
X = df["Encoding_sadness"].tolist()
y = df["Sadness_pourcentage"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
lr_sadness.fit(X_train, y_train)
y_pred = lr_sadness.predict(X_test)
r2 = r2_score(y_test, y_pred)
print("R2 Score modèle tristesse:", r2)


lr_anger = LinearRegression()
X = df["Encoding_anger"].tolist()
y = df["Anger_pourcentage"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
lr_anger.fit(X_train, y_train)
y_pred = lr_anger.predict(X_test)
r2 = r2_score(y_test, y_pred)
print("R2 Score modèle colère:", r2)


lr_surprise = LinearRegression()
X = df["Encoding_surprise"].tolist()
y = df["Surprise_pourcentage"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
lr_surprise.fit(X_train, y_train)
y_pred = lr_surprise.predict(X_test)
r2 = r2_score(y_test, y_pred)
print("R2 Score modèle surprise:", r2)

#%%

def traitement_donnee(texte, liste_sentiment) : #Fonction qui encode un texte en fonction de la liste de sentiment sélectionnée
    texte.replace("[^\w\s]", "")
    texte.lower()
    enc = encoding(texte, liste_sentiment)
    return enc

def pourcentage_final(joy, disappointment, sadness, anger, surprise) :  #Fonction qui calcul le pourcentage de chaque émotion en fonction du total de pourcentage
    total = joy + disappointment + sadness + anger + surprise
    joy = joy / total * 100
    disappointment = disappointment / total * 100
    sadness = sadness / total * 100
    anger = anger / total * 100
    surprise = surprise / total * 100
    print("Pourcentage de joie : ", joy, "\nPourcentage de déception : ", disappointment,
          "\nPourcentage de tristesse : ", sadness, "\nPourcentage de colère : ", anger, 
          "\nPourcentage de surprise : ", surprise)


#Test
test = "good quality dog food i have bought several of the vitality canned dog food products and have found them all to be of good quality the product looks more like a stew than a processed meat and it smells better my labrador is finicky and she appreciates this product better than  most good quality dog food"
prediction_joy = lr_joy.predict([traitement_donnee(test, joy_list)])
prediction_disappointment = lr_disappointment.predict([traitement_donnee(test, disappointment_list)])
prediction_sadness = lr_sadness.predict([traitement_donnee(test, sadness_list)])
prediction_anger = lr_anger.predict([traitement_donnee(test, anger_list)])
prediction_surprise = lr_surprise.predict([traitement_donnee(test, surprise_list)])

print("Joie : ", prediction_joy)
print("Déception : ", prediction_disappointment)
print("Tristesse : ", prediction_sadness)
print("Colère : ", prediction_anger)
print("Surprise : ", prediction_surprise)

pourcentage_final(prediction_joy, prediction_disappointment, prediction_sadness, prediction_anger, prediction_surprise)

    
    

