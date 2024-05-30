# Guide pour lancer le projet

## Lancer le backend :

1. Accédez au répertoire `/backend`.

2. Activez l'environnement virtuel en exécutant la commande suivante :
    ```bash
    source .venv/bin/activate
    ```

3. Run l'application :
    ```bash
    flask --app src/app run
    ```

## Lancer le front :

1. Accédez au répertoire `/frontend`.

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