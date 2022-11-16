# werkplaats2_starter
Starter repository voor Werkplaats 2. Deze repository bevat een Flask applicatie met een aantal van de componenten die we ook nodig hebben om de werkplaats opdracht uit te voeren: 
- Een database
- Templates
- De Flask server
- HTML & Style sheets


# Installatie
Om Flask te kunnen starten zul je eerst de Flask packages moeten installeren. Wil je latere problemen met versies voorkomen, dan raden we je aan een virtual environment te maken en daar de modules in te installeren:  
```
pip install virtualenv
virtualenv venv
.\venv\scripts\activate
pip install -r requirements.txt
```

Als PowerShell de scripts niet will runnen: 

1. Open PowerShell als administrator.
2. Typ het volgende command in PowerShell:

``` 
Set-ExecutionPolicy RemoteSigned
```


Om de demo applicatie te starten: 
``` 
.\venv\scripts\activate
python app.py
```
