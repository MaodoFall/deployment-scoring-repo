# Implémenter et déployer un modèle de scoring


L'objectif du projet est de construire et déployer sur le cloud un modèle de machine learning permettant de vérifier la solvabilité des clients d'une société financière. 
J'ai déployé le modèle de scoring sous forme d'API sur AWS ECS(Elastic Container Service) à l'aide de Docker. 
Ceci permet au modèle d'être accessible via des réquêtes HTTP, facilitant ainsi son utilisation dans différentes applications ou services.

J'ai éffectué les étapes suivantes :
1. Déploiement du modèle sur AWS ECS
2. Automatisation du déploiement avec CI/CD (Github Actions)
3. Tests unitaires pour vérifier le bon fonctionnement de l'API

Tout ce processus permet de déployer le modèle de machine learning de manière fiable et évolutive tout en assurant la qualité du code à chaque modification. Le tout est automatisé pour réduire les risques d'érreur et les interventions manuelles, ce qui est essentiel dans un environnement de production.
