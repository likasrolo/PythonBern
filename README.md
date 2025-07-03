https://replit.com/@lucasrolo2205/PromptCraftAI?s=app


Je veux faire une app web pour pouvoir aider les utilisateur à copier des prompt en fonction des requis des infos qu'ils renseignent.

Le but du programme est de à partir d'un grosse extraction de portefeuilles client, et d'une newsletter en format excel, on puisse faire une newsletter personnaliser alleger avec les infos qui concerne les clients uniquement.
le code python ci-joint est un programme avec une petite interface qui sert à faire le programme et pouvoir copier coller les prompts.

l'architecture est la suivante : 

traitement de le newsletter : client donne (via drag and drop) la newsletter en format html. 
(Via IA)on extrait les titres de la newsletter (présent dans le sommaire) et on les stocke dans une liste. 
en paralelle on peux crée(Via IA) une vertion de la newsletter résumé. pour alleger les futures prompts. 

on traite le fichier excel des crm(actifs des clients) on extrait les données des clients dans le fichier exel(sinon beaucoup trop lourd) on le faire adns le script python.
on stocke ces infos clients. 

puis via IA, on identifie les les numéro de clients correspondant à chaque titres avec des commentaires. chaque 100 position client pour ne pas etre trop lourd. 

puis on extrait la liste des des clients associées et la liste des commentaires.

dans la newsletter on ajoute la liste des numéro clients en dessous de chaque titre associées.

(via IA) on donne cette newsletter avec les numéro client et la liste des commentaires - pour avoir une newsletter personnalisé.

(via IA) signifie qu'un prompt texte est générer, puis que l'utilisateur le copie l'envoie à l'ia et colle le résultat pour l'enregistrer dans le programme.


peux tu me faire l'app en fonction de l'app python pour avoir une belle interface. 
