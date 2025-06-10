Le projet est séparer un plusieur parties,

**demo.py** est le code permetant de faire tourner tout le projet. Celui-ci fait appel au different module disponible dans scr/projet_a afin de permettre à l'utilisateur d'utiliser l'application depuis le terminal.


Dans le dossier **données** :

    - **Aliments.csv** : Le  fichier csv contenant la liste des aliments de base et leurs valeurs nutritionelles


Dans le dossier **scr/projet_a** :

    - **base.py** : Le code servant à repondre simplement à l'énoncé de base 

    - **data.py** : Code permetant la lecture de la base de données et son utilisation futur
    - **optimisation.py** : Fonction d'optimisation des aliments en focntion des besoins et du coût
    
    - **ilfautunnom.py** : Dans ce fichier les classes *besoins*, *aliment* & *resultat* sont définies
    - **aliment.py** : Ici se trouve la fonction permetant de rajouter des aliments de maniére éphémere à la base de données pour l'optimisation
    - **besoins.py** : On trouve dans ce fichier la fonction permetant de changer les besoins journalier de l'utilisateur afin d'avoir une optimisation personalisée
    - **diagramme.py** : Diagramme de Kiviat  des besoins nutritionnels et des apports obtenus
    - **diagramme2.py** : Même utilité que précedement mais modifié pour être utilisé dans **app.py**

    - **app.py** : Ce fichier permet la création de l'interface terminal, elle utilise les modules précedement cités

    - **test_besoins** : Fonction de test verifiant que la fonction *ajout_besoins* créer bien un object de classe *besoins*
    - **test_aliment** : Fonction de test verifiant que la fonction *ajout_aliment* créer bien un object de classe *aliment*







Mes remerciments à Ilayda et Marc pour leur aide apportée
