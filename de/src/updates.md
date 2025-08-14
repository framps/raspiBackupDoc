# Updates

Von Zeit zu Zeit wird eine neue Version von *raspiBackup* zum Download
bereitgestellt, die neue Funktionen, Erweiterungen und kleine Fixes enthält.

Auf dieses wird von *raspiBackup* beim Aufruf und in der gesendeten eMail
hingewiesen und man kann dann mit dem Parameter `-U` die neueste Version
herunterladen und aktivieren. Die aktuelle Version wird dabei gesichert und mit
dem Parameter `-V` kann jederzeit wieder die vorherige Version aktiviert werden.

Bei kleinen Änderungen wird kein neues Release zur Verfügung gestellt und man wird auch
nicht auf die Änderung hingewiesen. Mit den Optionen `-U -S` wird immer der aktuelle Code
heruntergeladen und aktiviert. So ein Update ist i.d.R. nicht notwendig und sollte nur vorgenommen werden,
wenn dazu explizit aufgefordert wird.

**Hinweis**:
Dabei wird kein Backup vom aktuell aktiven *raspiBackup* erstellt.

Vor dem Update sollte man nachlesen, welche Änderungen und Neuerungen in der
neuen Version enthalten sind. Diese Information dazu findet sich in der
[Versionshistorie](https://github.com/framps/raspiBackup/releases).
Sollte einmal ein gravierender Fehler entdeckt werden, wird
eine neue Version sofort bereitgestellt.

Jede neue Version wird [vor der Veröffentlichung auf Regressions getestet](regressiontests-executed.md).

## Konfigurationsupdate

Sofern in einem neuen Release neue Optionen eingeführt wurden, wird die
Konfigurationsdatei `/usr/local/etc/raspiBackup.conf` automatisch mit den neuen Optionen
versehen. Die Details dazu sind [hier](configuration-update-when-upgrading-to-a-new-version.md)
beschrieben.

[.status]: rst
[.source]: https://linux-tips-and-tricks.de/de/raspibackup#updatestrategie
[.source]: https://linux-tips-and-tricks.de/de/raspibackupcategoried/432-raspibackup-versionshistorie
