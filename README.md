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
