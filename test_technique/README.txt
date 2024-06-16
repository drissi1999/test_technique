# Ayomi Data Engineer Test

Ce projet est une API RESTful qui permet de réaliser des calculs en notation polonaise inverse (NPI) en utilisant FastAPI. 
L'API permet d'envoyer des opérations à réaliser et retourne les résultats. 
Les opérations et les résultats sont enregistrés dans une base de données SQLite, et il est possible de récupérer les données dans un fichier CSV.

## Prérequis

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

1. Clonez le dépôt du projet :

```sh
git clone repo
cd repo


## éxecute l'app:

docker-compose up --build


## l'API
Une documentation interactive de l'API est disponible via Swagger UI à l'adresse http://localhost:8000/docs.

Utilisation de l'API
Calculer une expression en NPI
Endpoint : /calculate
Méthode : POST

Corps de la requête :

{
  "expression": "3 4 +" #il faut changer string par l'equation que vous voulez
}

answer :

{
  "expression": "3 4 +",
  "result": 7.0
}