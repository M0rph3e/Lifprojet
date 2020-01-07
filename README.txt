Prerequis avant de pouvoir lancer le jeu :
Avoir installé python (version 3 ou +) ainsi que la bibliothèque Pygame.

Lancez le fichier start.bat ou compilez le fichier lahonda.py situé dans le dossier game
Les classes utilisés sont dans le dossier classes.

Les règles du jeu sont les suivantes :
•	Vous contrôlez trois joueurs (en bleu), votre but est d’éliminer les adversaires (en rouge) qui seront contrôlés par IA (réalisant des raisonnements stratégiques).
•	Vous pouvez attaquer un ennemi que s’il est adjacent. Cet ennemi répliquera.
•	Chaque unité possède un type d’armes caractérisé par une couleur (ROUGE pour Epée, VERT pour Hache et BLEU pour Lance). Un triangle des armes est mis en place donnant un bonus/malus de 20% de dégâts en fonctions des armes utilisées.
•	Les dégâts sont calculés en fonctions des statistiques d’attaques et de défenses et d’un avantage/désavantage tactique en fonction des types d’armes des unités.

Comment jouer :

•	Vous déplacez les unités et attaquez avec le curseur. Pour finir votre tour, appuyez sur le bouton « P » de votre clavier.
•	Vous pouvez vous déplacer de 7 cases et attaquez une seule fois par tour et par joueur.
