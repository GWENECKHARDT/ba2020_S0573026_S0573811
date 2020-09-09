# Django To-Do Liste 

Django To-Do Liste ist eine To-Do Listen Web-Anwendung, in der die Grundfunktionen von
To-Do Listen und eines oder mehrerer dazugehöriger To-Do's erstellt wurden.
Jedem Nutzer ist es möglich ein Benutzerprofil mit einem Passwort zu erstellen. 
Außerdem sind die allgemeinen Nutzungsbedingungen einsehbar. 
Man kann To-Do Listen erstellen, diesen einen Titel und einen Zuständigen zuordnen. 
Wenn man eine Liste auswählt kann man sie bearbeiten und löschen.
Außerdem kann man in jeder To-Do Liste weitere To-Do's mit einem Text erstellen. 
Diese kann man im Menüpunkt "To-Do's" bearbeiten, löschen und erledigen. 
Sobald man eines erledigt hat, ist es auch in "Erledigte To-Do's" zu finden, wo man es löschen kann.
Sollte der Nutzer nicht zurechtkommen, gibt es den Menüpnkt "Hilfe". 
Dort findet er eine Beschreibung der Anweudung, sowie Erklärungen zu einzelnen Optionen.

## Herunterladen

Mit Hilfe dieser Anweisungen erhalten Sie eine Kopie des Projekts, die auf Ihrem lokalen Rechner zu Entwicklungs- und Testzwecken läuft. 

### Anfang

Bevor es losgehen kann, muss folgender Befehl im Zielverzeichnis des Projektes im Terminal ausgeführt werden:
```
git clone https://github.com/GWENECKHARDT/ba2020_S0573026_S0573811.git
```

### Installieren mit PyCharm

Als erstes muss der Ordner mit dem Projektnamen in PyCharm geöffnet werden. 

Danach müssen diese Schritte ausgeführt werden:

Installieren der requirements.txt Datei:

```
pip install -r requirements.txt
```

Migrate:

```
python manage.py migrate
```

Zum Starten des Servers:

```
python manage.py runserver
```

## Deployte-Version 

http://projektbetriebliche.pythonanywhere.com/

Benutzername: Test

Passwort: Test

## Ersteller

* **Gwendolin Eckhardt** - (https://github.com/GWENECKHARDT)
* **Vivien Bentzen** -(https://github.com/vivienbentzen)
