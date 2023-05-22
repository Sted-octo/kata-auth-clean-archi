# kata-auth-clean-archi

## Why
Pour voir comment chacun interprète les contrainte de la clean archi et implémente ce qu'il en a compris.

Et aussi pour échanger sur ce choix et trouver s'aligner sur des convictions communes

## How
En crant une petit Api qui respecte les quelques contraintes, et en comparant avec les implémentations existantes.
Contrtaintes :
 - Dans le langage de votre choix
 - Clean archi
 - endpoint POST /api/auth
 - Retour un 401 (Status unauthorized) si l'accès n'est pas autorisé
 - La couche de database peu être un service qui réponds en dur ! 

## What
Dans le langage de votre choix, réaliser une (petite) api qui aura comme endpoint POST /api/auth
Ce endpoint récupérera dans le body un json comme celui là
```
{
"name":"dertex",
"password":"killer"
}
```
Et retournera
 - Un 401 (Status unauthorized) si l'accès n'est pas autorisé
   - Si le name reçu n'est pas dans la database.
   - Si le password ne correspond pas.
   - Si pas de name/password dans le json on entrée (pour faire simple)
 - Un token (on va dire pour faire simple => 32 chars aléatoires)
