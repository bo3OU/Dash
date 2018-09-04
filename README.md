# Dash

Ce projet vise a présenter une visualisation de l'état des autorisations faites au sein de la CFG ainsi que les fraudes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prérequis

Ceci concerne les exigences du projet.

```
dash  # The core dash backend
dash-html-components  # HTML components
dash-core-components  # Supercharged components
dash-table-experiments
dash_auth
pyplot
cassandra.cluster
timeago
base64
pandas
```

### Installation et deploiement

Un tutoriel étape par étape pour avoir un environnement de production opérationnel. 

Installation des packages necessaires pour le deploiement de l'application.

```
pip install -r requirements.txt
```

Lancement de l'application avec spark-submit.

```
spark-submit --packages com.datastax.spark:spark-cassandra-connector_2.11:2.3.0 Main.py
```

## Fichiers inclus

le projet 5 fichiers obligatoires et un dossier, voici une idée de ce que contient chaque fichier:

### Main

Fichier root de l'application, permet de créer l'app et la lier a un port d'ecoute.

### Assets

Contient les fichiers CSS du projet (le visuel)

### DashFunctions

Contient toutes les fonctions qui vont permettre l'accès a la base de données et recupérer ou envoyer des données

### FirstTab

Contient le squelette de la premiére bar du menu de l'application

### SecondTab

Contient le squelette de la deuxieme bar du menu de l'application

### Requirements

Contient la liste des packages requis pour le lancement de l'application


## Crée par

* [Dash](https://dash.plot.ly/) - The web framework used
* [PySpark](http://spark.apache.org/docs/2.2.0/api/python/pyspark.html) - Python API for Spark
* [Pandas](https://pandas.pydata.org/) - Python Data Analysis Library

## Authors

* **Ali BAGHO** - [bo3ou](https://github.com/bo3ou)

## Acknowledgments

* Hat tip to anyone whose code was used

