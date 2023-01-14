# Werkplaats2_starter
Starter repository voor Werkplaats 2. Deze repository bevat een Flask applicatie met een aantal van de componenten die we ook nodig hebben om de werkplaats opdracht uit te voeren: 
- Een database
- Templates
- De Flask server
- HTML & Style sheets


# Installatie
Om de virtual environment te activeren moet je het uitvoeringsbeleid van PowerShell wijzigen: 

1. Open PowerShell als administrator.
2. Type het volgende commando in PowerShell:
``` 
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```


Om Flask te kunnen starten zul je eerst de Flask packages moeten installeren. Wil je latere problemen met versies voorkomen, dan raden we je aan een virtual environment te maken en daar de modules in te installeren:
Mocht je Python versie 3 of hoger gebruiken in Pycharm, dan krijg je al de optie om een VENV aan te maken. Regel 1 en 2 van onderstaande code zijn in dat geval niet nodig.
```
pip install virtualenv
virtualenv venv
.\venv\scripts\activate
pip install -r requirements.txt
```

Om de demo applicatie te starten: 
``` 
.\venv\scripts\activate
python app.py
```


# Inloggen
Als je de demo applicatie start, kom je vervolgens in onze inlogscherm terecht.
Dit zorgt ervoor dat alleen redacteuren op deze website kunnen komen. 
Voor het gemak hebben we 4 testaccounts gemaakt die jullie kunnen gebruiken.

gebruiker 1
``` 
Gebruikersnaam : Kangyou 
Wachtwoord : beast
```
gebruiker 2
``` 
Gebruikersnaam : Sharelle 
Wachtwoord : beast
```
gebruiker 3
``` 
Gebruikersnaam : Erik 
Wachtwoord : beast
```
gebruiker 4
``` 
Gebruikersnaam : Dennis
Wachtwoord : beast
```



# Navigatiebar
Na het inloggen word je doorverwezen naar onze navigatiebar. We maken gebruik van een dropdownsysteem. 

Home
``` 
> je wordt terug gebracht naar onze Home-scherm
```
Auteurs 
``` 
> Alle Auteurs (Alle rijen in de tabel auteurs:)
> Ongeldige Medewerkers (Alle rijen in de tabel auteurs waarbij de kolom medewerkers tekst bevat terwijl er alleen getallen mogen zijn.)
> Ongeldige Auteurs (Alle rijen in de tabel vragen met ongeldige auteurs.)
> Ontbrekende Auteurs (Alle rijen in de tabel vragen met ontbrekende auteurs.)
``` 

Leerdoelen 
``` 
> Alle leerdoelen (Alle rijen in de tabel leerdoelen:)
> Ongeldige leerdoelen (Alle rijen in de tabel vragen met ongeldige leerdoelen.)
> Ontbrekende leerdoelen (Alle rijen in de tabel vragen met ontbrekende leerdoelen.)
``` 
Vragen 
``` 
> Alle vragen (Alle rijen in de tabel vragen:)
> HTML-fouten (Alle rijen in de tabel vragen met HTML-codes.)
```
Logout 
``` 
 > Je wordt uitgelogt
           
```
