# Dash

Ce projet vise a présenter une visualisation de l'état des autorisations faites au sein de la CFG ainsi que les fraudes.

## Commencement

Ces Instructions vont vous permettre d'avoir une copie local du projet pour developpement ou deploiement. 
```
git clone https://github.com/bo3OU/Dash.git
```

### Prérequis

Ceci concerne les exigences du projet.

```
dash 
dash-html-components 
dash-core-components 
dash-table-experiments
dash_auth
pyplot
timeago
base64
pandas
cassandra-driver
```

### Installation et deploiement

Un tutoriel étape par étape pour avoir un environnement de production opérationnel.
Installation de python
```
yum -y update
yum install gcc
wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
tar xzf Python-2.7.10.tgz
cd Python-2.7.10
./configure
make altinstall
```


Installation de JRE
```
yum install -y wget

wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jre-7u79-linux-x64.rpm"

yum install jre-7u79-linux-x64.rpm

vi .bash_profile

  # ajouter ce texte : 
      export JAVA_HOME=/usr/java/jdk1.7.0_79
      export JRE_HOME=/usr/java/jdk.7.0_79/jre

      PATH=$HOME/bin:$JAVA_HOME/bin:$JRE_HOME:$PATH

source .bash_profile

java -version
```

Installation de jupyter notebook (optionnelle)
```
pip install jupyter
```

Installation de pip
```
yum -y install python-pip
```

Installation des packages necessaires pour le deploiement de l'application.
```
pip install -r requirements.txt
```

Lancement de l'application avec spark-submit.
```
spark-submit --packages com.datastax.spark:spark-cassandra-connector_2.11:2.3.0 Main.py
```

## Fichiers inclus

L'application est composé de deux pages web, 5 fichiers
le projet 5 fichiers obligatoires et un dossier, voici une idée de ce que contient chaque fichier:

### Main

Fichier root de l'application, permet de créer l'app et la lier a un port d'ecoute, importe les deux fichiers app2 et app1 et les lies a des routes differents

  app1 -> localhost:9999/fraud
  app2 -> localhost:9999/general

### Assets

Contient les fichiers CSS du projet (le visuel/decor).

### DashFunctions

ensemble de fonctions qui vont permettre l'accès a la base de données ainsi que la recupération ou l'envois des données.

### app1

Contient le squelette de la premiére page de l'application ainsi que les "callbacks" de cette page

### app2

Contient le squelette de la deuxième page de l'application ainsi que les "callbacks" de cette page

### Requirements

Contient la liste des packages requis pour le lancement de l'application.(voir installations pour voir comment les installer).


## Crée par

* [Dash](https://dash.plot.ly/) - The web framework used
* [PySpark](http://spark.apache.org/docs/2.2.0/api/python/pyspark.html) - Python API for Spark
* [Pandas](https://pandas.pydata.org/) - Python Data Analysis Library

## Auteurs

* **Ali BAGHO** - [Github Link](https://github.com/bo3ou)

## Remerciements

* Salutations à toute personne dont le code a été utilisé.
* Salutations à l'entreprise pour l'opportunité.
