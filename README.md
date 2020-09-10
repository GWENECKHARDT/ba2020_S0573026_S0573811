# Django To-Do Liste 

Django To-Do Liste ist eine To-Do Listen Web-Anwendung, in der die Grundfunktionen von To-Do Listen und der dazugehörigen To-Do's erstellt wurden.
Jedem Nutzer ist es möglich, sich nach Angabe eines Nutzernamens und Passworts zu registrieren.
Dabei wird der Nutzer auf die ANB's hingewiesen.
Zu den Funktionen gehören das Erstellen, Bearbeiten sowie Löschen einer To-Do Liste, die dem Nutzer und einer weiteren Person/Gruppe zugeordnet werden kann.
Jeder vorhandenen To-Do Liste können beliebig viele To-Do's hinzugefügt werden.
Diese können im Menüpunkt "To-Do's" bearbeitet, gelöscht oder als erledigt gekennzeichnet werden.
Sobald eine solche Kennzeichnung erfolgt, sind diese To-Do's in "Erledigte To-Do's" zu finden und können wahlweise gelöscht werden.
Bei Problemen findet der Nutzer Ratschläge unter dem Menüpunkt "Hilfe".
Dort steht ihm eine kurze Beschreibung der Anwendung sowie Erklärungen zu einzelnen Optionen zur Verfügung.

## Benutzte Frameworks
Django, Bootstrap

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

http://projekttodoliste.pythonanywhere.com/

Benutzername: Test

Passwort: Test

## Ersteller

* **Gwendolin Eckhardt** - (https://github.com/GWENECKHARDT)
* **Vivien Bentzen** -(https://github.com/vivienbentzen)
