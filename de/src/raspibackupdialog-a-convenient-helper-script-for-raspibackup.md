# *raspiBackupDialog* - ein komfortables Hilfsscript für *raspiBackup*

Ein agiler Nutzer von *raspiBackup* - [Franjo-G](https://github.com/franjo-G) - hat ein sehr nützliches kleines
Hilfsscript mit dem Namen [raspiBackupDialog](https://github.com/framps/raspiBackup/blob/master/helper/raspiBackupDialog.sh) geschrieben, welches in einem Dialog
die wichtigsten Aufrufoptionen für den Backup und den Restore abfragt und mit
denen dann *raspiBackup* anstößt. *raspiBackup* Snapshots werden unterstützt. Sehr
einfach ist besonders der Restore durchzuführen: Vor dem Restore wird die Liste
der vorhandenen Backups angezeigt und man kann auswählen, welches Backup
wieder hergestellt werden soll.

``` admonish info title="Hinweis"
Es ist empfehlenwert, *raspiBackupDialog* nach erfolgreicher Installation und Konfiguration
von *raspiBackup* einfach mal downzuloaden und auszuprobieren.
```

## Installation und Aufruf

*raspiBackupDialog* steht als Hilfsscript im *GitHub* Repository zur Verfügung.

Es kann wie folgt in das aktuelle Verzeichnis heruntergeladen werden:

```
curl -s https://raw.githubusercontent.com/framps/raspiBackup/master/scripts/raspiBackupDownloadFromGit.sh | bash -s -- master helper/raspiBackupDialog.sh
```

Nun lässt es sich aufrufen mit:

```
sudo ./raspiBackupDialog.sh
```

Möchte man es nicht jedes Mal herunterladen, kann man es auf seiner Raspberry wie folgt dauerhaft verfügbar machen:

```
sudo mv ./raspiBackupDialog.sh /usr/local/bin
sudo chown root:root /usr/local/bin/raspiBackupDialog.sh
```

Danach kann es jederzeit wie folgt aufgerufen werden:

```
sudo raspiBackupDialog.sh
```


## Aufrufoptionen

```
sudo raspiBackupDialog.sh --select            # Startet einen restore. Das Image kann aus einer Liste ausgefählt werden.
sudo raspiBackupDialog.sh --last              # Startet einen Restore vom letzten Backup.
sudo raspiBackupDialog.sh --backup            # Startet einen Backup.
sudo raspiBackupDialog.sh --delete            # Ein Backup kann zum Löschen ausgewählt werden.
sudo raspiBackupDialog.sh --mountfs "fstab"   # Das Backupverzeichnis wird gemäß fstab Eintrag gemountet.
sudo raspiBackupDialog.sh --mountfs "*.mount" # Das Backupverzeichnis wird per systemctl start *.mount gemountet.
```

Falls das Verzeichnis schon gemounted war, wird es nicht unmounted. Ansonsten wird es wieder umounted.

Dynamic mount funktioniert auch mit cron.

```
* * * /usr/local/bin/raspiBackupDialog.sh --mountfs "backup.unit" oder "fstab" --cron
```

## Beispielaufrufdialog bei einem Backup

```
sudo raspiBackupDialog.sh

Please choose your preferred language
Bitte waehle deine bevorzugte Sprache
German = 1
English = 2
1
Soll ein Backup erstellt oder ein bestehendes Backup restored werden?
backup 1
restore 2
1
Befinden sich auf dem Systemlaufwerk mehr als die 2 Standard-Partitionen /boot und /root ? j/N
n
Soll ein Kommentar am Ende des Backup-Verzeichnisses eingefügt werden?
Dieses Backup wird dann nicht in die backup-Strategie übernommen und nicht automatisch recycled.
j/N
n
raspiBackup wird jetzt gestartet
```

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/637-raspibackupdialog-ein-komfortables-hilfsscript-fuer-raspibackup
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/642-raspibackupdialog-a-convenient-helper-script-for-raspibackup
