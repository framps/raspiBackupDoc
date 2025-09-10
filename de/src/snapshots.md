# Snapshots

*raspiBackup* bietet mit der Option `-M` die Möglichkeit, eine Art *Snapshot* zu erzeugen.
Dieses sind normale Backups, die aber zwei Besonderheiten haben:

  - Snapshots werden **nicht automatisch gelöscht** durch die gewählte Backupstrategie
  - Snapshots muss man eine Beschreibung als Parameter zur Option `-M` mitgeben.
    Diese wird am Ende des Verzeichnisnamens angehängt.

Somit kann man sehr leicht einen Snapshot außer der Reihe erstellen
und durch die Beschreibung im Namen des Backupverzeichnisses kann der Grund
des Snapshots erkannt werden. Das ist zum Beispiel sehr hilfreich, bevor man ein
Softwareupdate vornimmt oder eine andere größere Änderung plant. Wenn das
Update schief geht, hat man schnell wieder den vorherigen Stand hergestellt.
Wenn er erfolgreich war, löscht man den Snapshot im Backupverzeichnis.

**Hinweis:**
*raspiBackup* Snapshots sind keine Snapshots im eigentlichen Sinne wie sie z.B. mit *btrfs* erstellt werden können.
Es sind normale `dd`, `tar` oder `rsync` Backups.
`rsync` Backups sind Deltabackups und dementsprechend auch bei Snapshots schneller fertig als `dd` oder `tar` Backups.

Es gibt ein [Youtube Video](https://www.youtube.com/watch?v=8BlF9B8EX6k),
in dem die *raspiBackup* Snapshots erklärt werden sowie eine Demo gegeben wird.

[.status]: rft
[.source]: https://linux-tips-and-tricks.de/de/snapshots

