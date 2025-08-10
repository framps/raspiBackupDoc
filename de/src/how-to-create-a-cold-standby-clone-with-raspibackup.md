# Wie kann man mit *raspiBackup* einen Clone erstellen?

*raspiBackup* erstellt regelmäßig beliebige Backupversionen, die man im
Bedarfsfall zurückspielen kann. Häufig möchte man aber einfach den letzten Backup
auf einem Medium fertig greifbar haben, um ihn im Fehlerfalle sofort einsetzen
zu können, also einen Clone.

*raspiBackup* bietet keine direkte Möglichkeit, einen Clone zu erzeugen.

Mit Hilfe eines kleinen Hilfstools ist dieses aber möglich: Mit diesem
wird ein Backup erstellt und anschließend dieser Backup auf ein Medium
zurückgespielt. Wird der Backup Typ `rsync` genutzt, ist der Restore nur eine
Synchronisation der Änderungen von dem letzten Backup zum aktuellen Backup und
ist i.d.R. schnell erledigt.

Das Hilfstool heißt [raspiBackupAndClone.sh](https://github.com/framps/raspiBackup/blob/master/helper/raspiBackupAndClone.sh) und steht auf *GitHub* zur Verfügung.

Folgende Schritte sind notwendig, um es einzusetzen:

Hinweis: <clonedevice> ist im Folgenden das Device, welches den Clone erhalten soll, also z.B. `/dev/mmcblk0` oder `/dev/sda`.

 1. `raspiBackupAndClone.sh` installieren

     1. Download von `raspiBackupAndClone.sh`
        ```
        curl -s -O https://raw.githubusercontent.com/framps/raspiBackup/refs/heads/master/helper/raspiBackupAndClone.sh
        ```
     2. Verschieben des Scripts nach `/usr/local/bin`
        ```
        sudo mv raspiBackupAndClone.sh /usr/local/bin
        ```
     3. `raspiBackupAndClone.sh` ausführbar machen
        ```
        sudo chmod +x /usr/local/bin/raspiBackupAndClone.sh
        ```

 2. Einmaliges Initialisierung des Clonedevices

     1. Erstellen eines partitionsorientierten Backups durch den Aufruf von
        ```
        sudo raspiBackup -P -t rsync <BackupVerzeichnis>
        ```
     2. Zurückspielen des gerade erstellten Backup auf das Clonedevice mit
        ```
        sudo raspiBackup -d <clonedevice> <Backupverzeichnis>
        ```

 3. Regelmäßigen Aufruf von `raspiBackupAndClone.sh` statt `raspiBackup.sh` einstellen

     1. In der Datei `/etc/systemd/system/raspiBackup.service`
        ```
        ExecStart=/usr/local/bin/raspiBackup.sh
        ```
        ändern in
        ```
        ExecStart=/usr/local/bin/raspiBackupAndClone.sh <clonedevice>
        ````

Falls manuell ein Backup erstellt werden soll,
muss `raspiBackupAndClone.sh` statt `raspiBackup.sh` aufgerufen werden.

Hinweis: Falls kein `rsync` Backup möglich ist, muss in `raspiBackupAndClone.sh` die
Zeile `USE_RSYNC=1` in `USE_RSYNC=0` geändert werden. Dann dauert der Restore
allerdings wesentlich länger, da keine Synchronisation sondern ein Vollrestore
vorgenommen wird.

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/684-wie-kann-man-mit-raspibackup-einen-clone-erstellen
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/685-how-to-create-a-cold-standby-clone-with-raspibackup
