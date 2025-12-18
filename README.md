# Montecarlo-Systeme-Pannes
Étudier la fiabilité et la disponibilité d’un système industriel composé de 3 machines en série, en utilisant une simulation Monte-Carlo événementielle pour estimer la probabilité de défaillance .
## Introduction 
Dans l’industrie, la disponibilité des systèmes de production est un facteur clé de performance.
Les approches déterministes classiques permettent de calculer des indicateurs moyens, mais elles ne prennent pas en compte l’incertitude liée aux pannes et aux durées de réparation.

Ce projet propose une approche basée sur la simulation Monte-Carlo événementielle afin d’estimer la probabilité de défaillance et la disponibilité d’une chaîne de production composée de plusieurs machines en série.

## Description du système
Le système étudié est une chaîne de production composée de trois machines fonctionnant en série. Une panne sur une machine entraîne l’arrêt complet de la chaîne.

## Modélisation probabiliste
Les occurrences de pannes sont modélisées par un processus de Poisson, ce choix étant justifié par le caractère aléatoire, indépendant et stationnaire des défaillances observées sur la période d’étude. Par conséquent, les temps inter-pannes suivent une loi exponentielle, caractérisée par une propriété d’absence de mémoire, hypothèse classique en fiabilité des systèmes industriels.

## Simulation Monte-Carlo événementielle du système
La simulation Monte-Carlo est une méthode numérique qui consiste à reproduire le comportement aléatoire d’un système réel à l’aide de tirages aléatoires.
Dans ce projet, elle est utilisée pour modéliser l’apparition des pannes et les temps de réparation des machines industrielles étudiées.

La simulation est dite événementielle, car le temps n’évolue pas de manière continue, mais d’un événement à un autre. Les événements considérés sont principalement :
   l’apparition d’une panne sur une machine,
   la fin de la réparation de cette panne
Pour une simulation :

1- Temps = 0
2- Tirer le temps jusqu’à la prochaine panne
3- Tirer la machine en panne
4- Tirer la durée de réparation
5- Arrêter la chaîne
6- Reprendre
7- Continuer jusqu’à 1935 h
Répéter N = 10 000 fois
