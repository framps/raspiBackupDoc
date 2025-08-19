<a name="adhoc"></a>
## *raspiBackup* ohne Installation nutzen

1. Download von *raspiBackup*: `curl -sSLO  https://www.linux-tips-and-tricks.de/raspiBackup.sh`

2. Mount der Backuppartition unter `/backup` oder Angabe der Backuppartition als letzten
   Parameter im Aufruf, also z.B. `sudo bash ./raspiBackup.sh /media/pi`

3. Start des Backups:  `sudo bash ./raspiBackup.sh`

Falls kein `rsync` Backup gewünscht wird, muss der Backuptyp `tar` oder `dd` mit Option `-t`
 mitgegeben werden, also `sudo bash ./raspiBackup.sh -t tar` oder `sudo bash ./raspiBackup.sh -t dd`

Kurzinfos zu allen Aufrufoptionen von *raspiBackup* erhält man mit `bash ./raspiBackup.sh -`

