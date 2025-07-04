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




Portfolio	DATE DE COTATION	CODE ISIN	CODE TLK	INSTRUMENT	EMMETEUR	EMMETEUR CODE	EMMETEUR-TYPE	DEV.	QUANTITE	PRIX ACTUEL	ACTIFS	TYPE	TYPE	TYPE	RATING S&P	DATE RATING S&P	COUT DAQUISITION	INTERET COURUS	APPL DEFE	CONSEILLER	DEFE DISTRIB	DEFE VNI	RENSEIGNEMENTS	CONTROLE : XXXXX	DATE DE DEBUT	DATE DE FIN/ 1 er coupon	COURS D ACHAT	INSTRUMENT	TAUX	ROUND LOT	INTERET COURUS DEVISE	DATE DE COUPON	%/ V.I. TOT	Portfolio	MOYENNE ISF	CONTROLE : XXXXX	FREQUENCE	EMMETEUR/PAYS DE RESIDENCE	EMETEUR/RISQUE PAYS	type fonds	sous type fonds	niveau risque.	COUT DAQUISITION BRUT	COUT DAQUISITION NET	cap garanti	cap garanti %	ESSAI CODE DEPOT	titre QI	type	type	INSTRUMENT	INSTRUMENT	Zone geographique	Zone geographique	APA1	APA2	open nature	Gerant	PAYS DE RESIDENCE GEOGRAPHIQUE	PAYS DE RESIDENCE FISCAL 2	%/ V.I. TOT	TX FACIAL	RENDEMENT	MATURITE	Duration	SENSIBILITE	CONVEX.	Especes et depots + FX TARGET	Fonds et sicav monetaires	Fixed incomes echeance < 31 12 2011	Fixed incomes echeance >= 31 12 2011	AUTRES TITRES	SECTEUR	SECTEUR II	INSTRUMENT	DATE PROCHAIN COUPON	EMMETEUR-TYPE	% de la ligne dans le Portefeuille	DATE D OUVERTURE DU COMPTE	DATE MANDAT	TAUX CHGE	GA/GZ	GRILLE
MC72001152	30/04/2025		MCM-TELO-EUR-5	TERM LOAN				EUR	-301742.410000000	1.000000000	-301872.61	0.00	M-402	MM-05			-301742.41	-130.20		ROLLAND JEAN-MARC			AUTRES		23/04/2025	25/07/2033	1.000000000		2.250000000		-130.20		-0.01	720			Aucune			CO_ACL_CSH	CO_SAC_CSH_DELO		0.00	-301742.41	No		MC04745560051-25L	No	Non géré	Autre					AUTRES	AUTRES	Open	ROLLAND JEAN-MARC	France	France		2.25000		25/07/2033	6.84	6.70	0.00								Without frequency	23/04/2025		50.604394300			2.250000000	<None>	 
MC72001152	30/04/2025		MCM-TELO-EUR-5	TERM LOAN				EUR	-301742.410000000	1.000000000	-301872.61	0.00	M-402	MM-05			-301742.41	-130.20		ROLLAND JEAN-MARC			AUTRES		23/04/2025	25/07/2033	1.000000000		2.250000000		-130.20		-0.01	720			Aucune			CO_ACL_CSH	CO_SAC_CSH_DELO		0.00	-301742.41	No		MC04749930051-25L	No	Non géré	Autre					AUTRES	AUTRES	Open	ROLLAND JEAN-MARC	France	France		2.25000		25/07/2033	6.84	6.70	0.00								Without frequency	23/04/2025		50.604394300			2.250000000	<None>	 
MC72001152	30/04/2025		MC72001152-0012600-EUR	CAV-2600-EUR				EUR	7210.840000000	1.000000000	7210.84	0.00	C-001	CSH-04			2457.44	0.00		ROLLAND JEAN-MARC			APA_CASH		11/07/2018	31/12/9999	0.340798021				0.00		0.00	720			Année			CO_ACL_CSH	CO_SAC_CSH_CACC		0.00	2457.44	No		MC04749930051-25L	No	Non géré	Autre					APA_CASH	AUTRES	<None>	ROLLAND JEAN-MARC	France	France				31/12/9999	0.00	0.00	0.00								Without frequency	11/07/2018		-1.208788700			1.000000000	<None>	 
MC72002131	30/04/2025		MCM-TELO-EUR-8	TERM LOAN				EUR	-6570000.000000000	1.000000000	-6599181.75	0.00	M-402	MM-05			-6570000.00	-29181.75		ROLLAND JEAN-MARC			AUTRES		07/02/2025	07/02/2029	1.000000000		1.950000000		-29181.75		-0.19	720			Aucune			CO_ACL_CSH	CO_SAC_CSH_DELO		0.00	-6570000.00	No		MC03332630007-25L	No	Non géré	Autre					AUTRES	AUTRES	Open	ROLLAND JEAN-MARC	France	France		1.95000		07/02/2029	1.84	1.81	0.00								Without frequency	07/02/2025		111.276405100			1.950000000	<None>	 
MC72002131	30/04/2025		MC72002131-0012600-EUR	CAV-2600-EUR				EUR	999.750000000	1.000000000	999.75	0.00	C-001	CSH-04			999.75	0.00		ROLLAND JEAN-MARC			APA_CASH		06/02/2019	31/12/9999	1.000000000				0.00		0.00	720			Année			CO_ACL_CSH	CO_SAC_CSH_CACC		0.00	999.75	No		MC96590380032-25L	No	Non géré	Autre					APA_CASH	AUTRES	<None>	ROLLAND JEAN-MARC	France	France				31/12/9999	0.00	0.00	0.00								Without frequency	06/02/2019		-0.016857900			1.000000000	<None>	 
MC72002131	30/04/2025		MCM-CADP-EUR-8	CALL DEPOSIT				EUR	633267.260000000	1.000000000	667740.82	0.00	M-401	MM-05			633267.26	34473.56		ROLLAND JEAN-MARC			APA_CASH		23/04/2025	31/12/9999	1.000000000		2.100000000		34473.56		0.02	720			Aucune			CO_ACL_CSH	CO_SAC_CSH_FIDU		0.00	633267.26	No		MC96590380032-25L	No	Non géré	Autre					APA_CASH	AUTRES	Open	ROLLAND JEAN-MARC	France	France		2.10000		31/12/9999	0.01	0.01	0.00								Without frequency	23/04/2025		-11.259547100			2.100000000	<None>	 
MC72002164	30/04/2025		MCM-TELO-EUR-8	TERM LOAN				EUR	-455300.020000000	1.000000000	-457088.84	0.00	M-402	MM-05			-455300.02	-1788.82		ROLLAND JEAN-MARC			AUTRES		21/02/2025	21/02/2029	1.000000000		2.080000000		-1788.82		-0.01	720			Aucune			CO_ACL_CSH	CO_SAC_CSH_DELO		0.00	-455300.02	No		MC03359280013-25L	No	Non géré	Autre					AUTRES	AUTRES	Open	ROLLAND JEAN-MARC	Monaco	Monaco		2.08000		21/02/2029	1.84	1.81	0.00								Without frequency	21/02/2025		101.446962900			2.080000000	<None>	 
MC72002164	30/04/2025		MC72002164-0012600-EUR	CAV-2600-EUR				EUR	6519.570000000	1.000000000	6519.57	0.00	C-001	CSH-04			6519.57	0.00		ROLLAND JEAN-MARC			APA_CASH		15/02/2019	31/12/9999	1.000000000				0.00		0.00	720			Année			CO_ACL_CSH	CO_SAC_CSH_CACC		0.00	6519.57	No		MC13098936-4-202503P	No	Non géré	Autre					APA_CASH	AUTRES	<None>	ROLLAND JEAN-MARC	Monaco	Monaco				31/12/9999	0.00	0.00	0.00								Without frequency	15/02/2019		-1.446962900			1.000000000	<None>	 
MC72002662	30/04/2025		MC72002662-0013200-EUR	CAV-3200-EUR				EUR	135755.280000000	1.000000000	135755.28	0.00	C-001	CSH-04			135755.28	0.00		ROLLAND JEAN-MARC			APA_CASH		29/05/2019	31/12/9999	1.000000000				0.00		0.00	720			Année			CO_ACL_CSH	CO_SAC_CSH_CACC		0.00	135755.28	No		MC98872810028-25L	No	Non géré	Autre					APA_CASH	AUTRES	<None>	ROLLAND JEAN-MARC	Monaco	Monaco				31/12/9999	0.00	0.00	0.00								Without frequency	29/05/2019		7.613149400			1.000000000	<None>	 


