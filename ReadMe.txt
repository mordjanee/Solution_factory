Notre projet est une application et un site internet qui permettent de réaliser une analyse fine de sentiments à partir de données textuelles.
Il permet de faire ressortir le pourcentage de 5 sentiments : la joie, la déception, la tristesse, la colère et la surprise. 
De plus, ce dernier permet de générer pour chaque sentiment, un nuage de mots représentatifs afin d'aider l’utilisateur à mieux comprendre l'avis global de ses clients.

L'utilisateur a le choix entre analyser un texte qu'il peut tapper directement dans la zone de texte dédiée et analyser une colonne d'une base de données.

Afin d'utiliser notre programme, il faut télécharger le fichier Efreimotion.py qui contient l'application réalisée à l'aide de tkinter 
ainsi que le fichier Listes qui contient les listes de mot utilisé pour le traitement des données en one hot encoding
et enfin le fichier Modèles qu'il faudra décompresser et qui contient les modèles de Machine Learning entraînés.

Il faudra donc placer ses dossiers et le fichier python dans un même dossier avec l'image ml.png et la base de données BDD_Amazon.csv pour réaliser des tests (où n'importe quelle autre base de données).

Le site internet se trouve dans le fichier site-mastercamp

Les fichiers Main.py et modele_sentiments.py sont les fichiers python où nous avons réalisé, entraîné et sauvegardé les modèles. Ces derniers étant enregistrés dans un fichier, il n'est pas nécessaire de les lancer.
Les fichiers Application.py et Application_test.py sont des fichiers python qui comportent nos deux premiers prototypes et test d'application et ne sont donc pas utiles au lancement du programme.
