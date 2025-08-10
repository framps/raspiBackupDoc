# Wie kann ich eine Betaversion von *raspiBackup* installieren und ausprobieren?

Von Zeit zu Zeit gibt es eine neue Version von *raspiBackup*, die neue
Funktionen, Erweiterungen und auch Fehlerkorrekturen enthält.

Jede neue Version durchläuft einen automatisierten [Regressiontest](regressiontests-executed.md), der die
eigentliche Backup- und Restorefunktionialität testet. Dann werden die neuen
Funktionen, Erweiterungen und Bug Fixes, die während der Entwicklung schon
getestet wurden, noch einmal manuell verifiziert.

Danach wird die neue Version als Beta allgemein zur Verfügung gestellt. Dieses
ist erkennbar daran, dass dem eMail Subject das Smiley `:-D` vorangestellt wird.
Nun hat jeder Benutzer von *raspiBackup* die Möglichkeit, die zukünftige neue
Version vorneweg mit den neuen Funktionen, Erweiterungen und Fehlerkorrekturen
zu testen, und im Fehlerfalle ein Problemrecord zu erstellen, so dass das
Problem gefixed werden kann.

Da es nicht möglich ist, alle möglichen Systemumgebungsbedingungen zu
testen, hilft das Testen der Betaversion auch, für die Community
sicherzustellen, dass sich möglichst keine Fehler in der neuen Version
eingeschlichen haben.

Nun folgend wird beschrieben, wie man eine Beta installieren kann,
sie wieder deinstallieren und Problemberichte erstellen kann.

Die Installation der Beta ist relativ einfach. Man benutzt

```
sudo raspiBackup -U
```

Dabei wird die aktuelle *raspiBackup* Version gesichert, so dass jederzeit
wieder auf die vorhergehende Version zurückgewechselt werden kann.
Dies geschieht mit

```
sudo raspiBackup.sh -V
```
wobei aus einer Liste der vorherigen Versionen diejenige auswählbar ist,
die dann wieder aktiviert wird.

Sollte wider Erwarten ein Problem entdeckt werden, sollte auf [*GitHub*](https://github.com/framps/raspiBackup/issues) ein
Problemrecord bzw. Issue erstellt werden. Sehr wichtig dabei ist es, die
Ausgabe von `sudo *raspiBackup*.sh --version` anzugeben, damit genau klar ist,
welcher Codestand benutzt wird.

Da auch von internationalen *raspiBackup* Nutzern
die Records gelesen werden, wäre es gut, sie in Englisch zu erstellen. Es ist
aber auch kein Problem, nur Deutsch zu schreiben. Die Records werden dann
bearbeitet und gefixed. Wenn eine neue Version bereitsteht, wird der Ersteller
über *GitHub* informiert werden und sie kann mit `sudo *raspiBackup*.sh -U -S`
erneut runtergeladen und der Fix verifiziert werden.

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/594-wie-kann-ich-die-betaversion-installieren-und-ausprobieren
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/595-how-can-i-install-and-test-the-beta-version

