# DataStructure---BattleShip-Game
**(Data Structure -- QuadTree ) represent a variation battleship game with quadtree datastructure.**


Dans le jeu battleship (bataille
navale) chacun de deux
adversaires dispose ses
bateaux sur une grille qu’il
garde secrète. Tour à tour les
joueurs lancent une bombe en
spécifiant la coordonnée
visée. Le joueur qui reçoit la
bombe doit repérer cette
coordonnée sur sa grille et
déclarer si la bombe touche un bateau (en s’écriant : touché) ou non (en
s’écriant : raté). Chaque bateau occupe un certain nombre de coordonnées
contigües (parallèles à l’un des axes) et lorsque
chaque coordonnée d’un bateau a été touchée,
le bateau est alors déclaré coulé (en s’écriant :
coulé). La grille dessous montre l’état du jeu
d’un des joueurs après quelques bombes
larguées par son adversaire. Ici, un vaisseau est
coulé et trois vaisseaux au total ont reçu des
coups. Le joueur a donc dû dire 5 fois :raté, 7
fois : touché et 1 fois : coulé.  
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/1.PNG?raw=true)
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/2.PNG?raw=true)


## Battleship inversé  
Modifions maintenant le jeu :  
1. chaque bateau est représenté par un point
2. les bombes larguées détruisent tout bateau dans une zone rectangulaire de
taille variable (selon la puissance de la bombe)
3. le nombre de bateaux n’est pas borné et peut être assez grand (1 million par
exemple)
4. la taille de la grille est de 10315 km par 10315 km (soit environ l’équivalent
de la surface de l’océan Atlantique)
5. le but du jeu n’est pas de gagner mais de perdre le plus rapidement et en
utilisant le moins de mémoire possible!

## Quadtree - définition  
Encodez la position des bateaux dans un quadtree. Considérons l’arbre binaire
de la figure 4. Chaque noeud est soit une feuille ou un noeud interne avec deux
enfants (nommés ici G et D). Un quadtree est très similaire mais chacun de ses
noeuds compte jusqu’à 4 enfants. Chaque noeud est soit 1) null, 2) une feuille
ou 3) un noeud interne. De plus, chaque noeud
interne ne peut avoir plus de trois enfants nulls.

![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/3.PNG?raw=true)
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/4.PNG?raw=true)
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/5.PNG?raw=true)
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/6.PNG?raw=true)

On peut étiqueter un arbre binaire (fig ci-haut) et utiliser cette étiquette pour
séparer les points sur une ligne (fig ci-bas).  
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/7.PNG?raw=true)  
De même, on peut utliser
un quadtree pour
découper le plan en quatre
quadrants : nord-ouest,
nord-est, sud-est et sudouest.  
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/8.PNG?raw=true)

Le plan qu’un noeud découpe peut-être associé à une variable que l’on nomme
ici frontière  
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/9.PNG?raw=true)

Les subdivisions successives de l’espace par notre quadtree sont montrées cidessous.
Constatez en particulier qu’il n’est pas nécessaire d’expliciter les
sous-arbres pour les quadrants dans lesquels on ne retrouve aucun point. Les
quadtrees sont donc naturellement performants pour représenter des
ensembles de points clairsemés (« sparse »).  
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/10.PNG?raw=true)

Sur la figure dessous de gauche, l’image du haut
montre des points sur un plan cartésien.
L’image du centre montre le même espace, sur
lequel on a dessiné une grille et l’image du bas
montre l’organisation d’un quadtree
représentant les mêmes points.  
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/11.PNG?raw=true)
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/12.PNG?raw=true)
![](https://github.com/michelleminchangma/DataStructure---BattelShip-Game/blob/master/readme-img/13.PNG?raw=true)

## Les trois phases du jeu :  
1. chargement de la position des bateaux dans l’arbre  
a. La liste de coordonnées de bateaux est fournie dans un fichier nommé
bateaux.txt  
b. Chaque ligne donne les coordonnées d’un bateau dans le format ‘x y’ où
x et y sont des entiers entre 0 et 10315 séparés par une espace.  

2. destruction des bateaux par une suite de bombes :  
a. les coordonnées des bombes sont données dans un fichier nommé
bombes.txt  
b. Chaque ligne donne les coordonnées d’une bombe dans le format ‘x1 y1
x2 y2’ des entiers (entre 0 et 10315 inclus) séparés par des points tels
que x2>=x1 et y2>=y1  
c. Lorsque une bombe est lue, tous les bateaux dont les coordonnées sont
dans la portée de la bombe (à l’intérieur de la zone, incluant le
périmètre de la zone) sont détruits. C’est à dire qu’ils sont retirés de
l’arbre. Après cette opération, il ne doit pas y avoir de noeud dont tous
les enfants sont nulls.

3. affichage de l’arbre résiduel  
a. Lorsque toutes les bombes ont été larguées, l’arbre est affiché à l’écran.
Celui-ci doit donc contenir tous les noeuds nécessaires, toutes les
feuilles nécessaires et aucun noeud dont tous les enfants sont nulls.

## Jouer  
Ce programme comprend un fichier `battleship.py` qui
sera exécuté dans un dossier comprenant les fichiers `bateaux.txt` et `bombes.txt`.

