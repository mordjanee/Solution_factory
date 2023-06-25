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
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


sentences_text = "".join(df["Text"].str.lower())
mots = sentences_text.split()
mots_frequents = Counter(mots).most_common(2000)

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

import pickle

# Sauvegarde du modèle
with open('modele_knn_sauvegarde.pkl', 'wb') as fichier:
    pickle.dump(knn, fichier)

# Chargement du modèle
with open('modele_knn_sauvegarde.pkl', 'rb') as fichier:
    knn_sauvegarde = pickle.load(fichier)

#%%Création des listes de mots pour chaque sentiment

joy_list = ['joy', 'happiness', 'delight', 'elation', 'bliss', 'ecstasy', 'excitement',
              'jubilation', 'thrill', 'rejoice', 'exhilaration', 'glee', 'joviality',
              'contentment', 'cheerfulness', 'mirth', 'gladness', 'euphoria', 'gratitude',
              'lightheartedness', 'euphoric', 'elated', 'happy', 'cheerful', 'thrilled',
              'excited', 'radiant', 'enthusiastic', 'ecstatic', 'upbeat', 'vibrant',
              'delighted', 'overjoyed', 'exuberant', 'optimistic', 'satisfied', 'grateful',
              'bubbly', 'buoyant', 'blissful', 'lively', 'sunny', 'giddy', 'jolly', 'jubilant',
              'whimsical', 'energized', 'merry', 'zestful', 'thrilling', 'smiling', 'laughing',
              'carefree', 'upjoyed', 'triumphant', 'rapturous', 'playful', 'sparkling',
              'radiating', 'savoring', 'high-spirited', 'giggly', 'cherished', 'uplifted',
              'singing', 'enraptured', 'beaming', 'bouncing', 'elfin', 'heartwarming',
              'glowing', 'brimming', 'rejuvenated', 'paradisiacal', 'gustatory', 'breezy',
              'dreamy', 'ecphrastic', 'ebullient', 'blithesome', 'jocund', 'sprightly',
              'in high spirits', 'festive', 'effervescent', 'hilarious', 'laudatory']
              
disappointment_list = ['disappointment', 'frustration', 'letdown', 'despair', 'regret',
                       'dismay', 'displeasure', 'defeat', 'disillusionment', 'gloom',
                       'sorrow', 'heartbreak', 'bitterness', 'discontentment', 'misery',
                       'anguish', 'melancholy', 'woe', 'unfulfilled', 'hopelessness',
                       'discouragement', 'downhearted', 'sad', 'dejected', 'crestfallen',
                       'unhappy', 'miserable', 'forlorn', 'despondent', 'gloomy', 'regretful',
                       'disheartened', 'demoralized', 'deflated', 'upset', 'dispirited',
                       'dissatisfied', 'desolate', 'wretched', 'broken-hearted', 'troubled',
                       'lament', 'lamentable', 'pathetic', 'sorry', 'pessimistic', 'betrayed',
                       'abandoned', 'crushed', 'suffering', 'tearful', 'weeping', 'crying',
                       'grieving', 'distressed', 'morose', 'apathetic', 'grievous', 'desperate',
                       'lonely', 'disappointed', 'underwhelmed', 'disgruntled', 'mortified',
                       'shattered', 'dashed', 'angry', 'enraged', 'resentful', 'furious',
                       'indignant', 'exasperated', 'irritated', 'annoyed', 'displeased',
                       'bitter', 'sour', 'downcast', 'weary', 'downtrodden', 'woeful',
                       'doubtful', 'dismal', 'vanquished', 'overwhelmed', 'rueful', 'shocked',
                       'repentant']

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
                'morose', 'suffer', 'broken-hearted', 'miserable', 'mournful', 'mourn', 'woe',
                'weeping', 'distraught', 'aching', 'morning', 'grievous', 'hurting', 'weepy',
                'affliction', 'angst', 'crushed', 'darkness']

satisfaction_list = ['satisfaction', 'contentment', 'fulfillment', 'pleasure', 'gratification',
                     'happiness', 'joy', 'delight', 'pride', 'achievement', 'fulfilled',
                     'content', 'glad', 'grateful', 'pleased', 'accomplishment', 'enjoyment',
                     'approval', 'satisfied', 'excitement', 'cheerful', 'thrilled', 'humbled',
                     'rejoice', 'exhilaration', 'elation', 'thankful', 'gratitude', 'gratified',
                     'ecstatic', 'delighted', 'honor', 'complacency', 'bliss','sense', 'relish',
                     'elated', 'cheerfulness', 'jubilation', 'ecstasy', 'triumph', 'euphoria',
                     'positive', 'overjoyed', 'contented', 'gladness', 'exuberance', 'savor',
                     'savoring', 'sunniness', 'serenity', 'self-fulfillment', 'happily',
                     'satisfying', 'thrilling', 'fulfilling', 'satiated', 'beaming', 'radiant',
                     'blissful', 'upbeat', 'triumphant', 'enthusiasm', 'merry', 'blessed',
                     'serene', 'sufficed', 'sufficiency', 'elatedness', 'comfortable',
                     'self-content', 'jollity', 'smugness', 'gratulate', 'euphoric', 'gladsome',
                     'smiling', 'gleeful', 'sated', 'glee', 'pleasurable', 'triumphal',
                     'satisfactorily', 'glory', 'appreciation', 'accomplished', 'proud',
                     'contentedness', 'comfort', 'blissfulness', 'gratify', 'sufficient',
                     'gladly', 'gratifying', 'felicitous', 'exultant', 'swooning', 'rapture',
                     'thankfulness', 'fulfilment', 'ease', 'compliment']

anger_list = ['anger', 'rage', 'fury', 'outrage', 'resentment', 'irritation', 'wrath',
              'indignation', 'annoyance', 'frustration', 'exasperation', 'hostility',
              'bitterness', 'displeasure', 'temper', 'madness', 'fume', 'fury', 'irritability',
              'fury', 'fuming', 'irritated', 'enraged', 'incensed', 'livid', 'infuriated',
              'furious', 'agitated', 'outraged', 'angry', 'resentful', 'provoked', 'upset',
              'pissed off', 'hateful', 'indignant', 'wrathful', 'irate', 'vengeful', 'storming',
              'raving', 'cross', 'offended', 'incandescent', 'infuriate', 'frenzy', 'choleric',
              'temperamental', 'steamed up', 'vexed', 'seething', 'aggravated', 'boiling',
              'irate', 'irate', 'splenetic', 'mad', 'ballistic', 'belligerent', 'irate', 'rabid',
              'pissed', 'huffy', 'acerbic', 'bellicose', 'snappish', 'sullen', 'ticked off',
              'disgusted', 'incandescence', 'hot under the collar', 'passionate', 'malice',
              'ire', 'scornful', 'peeved', 'acerbity', 'acerbate', 'infuriation', 'enflamed',
              'sharpness', 'piqued', 'animosity', 'aggression', 'snappy', 'provocative', 'sore',
              'wrangle', 'hot-headed', 'up in arms', 'bellowing', 'boiling point']

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
                 'incredible', 'mind-blowing', 'unusual', 'jolt', 'unpredictable',
                 'unexpectedly', 'mind-bending', 'shattering', 'wondrous', 'flabbergast',
                 'goggle', 'eye-popping', 'gape', 'delight', 'bemusement', 'curiosity',
                 'incomprehension', 'mystify', 'fascinated', 'disoriented', 'nonplussed',
                 'wonderment', 'unbelievably', 'impressive', 'unforeseen', 'suspense',
                 'marvelous', 'extraordinary', 'intrigue', 'gobsmack', 'dumbstruck', 'amazing',
                 'wonderstruck', 'dazzling', 'enchant', 'unbelievably', 'boggle', 'delighted',
                 'curious', 'mind-boggling', 'remarkable', 'astonish', 'stunning',
                 'awe-inspired', 'breathtaking', 'spectacular', 'wonderful', 'captivate',
                 'fascinate', 'surprisingly']


print("Taille de la liste des mots exprimant la joie : ", len(joy_list))
print("Taille de la liste des mots exprimant la déception : ", len(disappointment_list))
print("Taille de la liste des mots exprimant la tristesse : ", len(sadness_list))
print("Taille de la liste des mots exprimant la satisfaction : ", len(satisfaction_list))
print("Taille de la liste des mots exprimant la colère : ", len(anger_list))
print("Taille de la liste des mots exprimant l'étonnement : ", len(surprise_list))

