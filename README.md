# Notre projet 

Notre projet est quiz dont le thème porte sur le retrogaming !
Nous y avons ajouté de nombreuses fonctionnalités, dont:
- Animations et UI stylisée
- Système d'avatar
- Système de grades en fonction du score
- Classements
- Stastistiques
- Scène d'intro au quiz
- Scène de résultats animée
Etant donné que l'on a beaucoup de données stastiques et de classement, une page dédiée à été créée plutot que de les mettre à l'accueil.

# Guide pour lancer le projet

## Lancer le backend :

1. Accédez au répertoire `/quiz-api`.

2. Lancez l'application :
    ```bash
    flask --app src/app run
    ```

## Lancez le front :

1. Accédez au répertoire `/quiz-ui`.

2. Installez les dépendances en exécutant la commande suivante :
    ```bash
    npm install
    ```

3. Lancez le serveur de développement en exécutant la commande suivante :
    ```bash
    npm run dev
    ```

## Accéder à la base de données :

1. Accédez au répertoire `/db`.

2. Ouvrez la base de données en exécutant la commande suivante :
    ```bash
    sqlite3 database.db
    ```
