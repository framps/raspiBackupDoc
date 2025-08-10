# SMB als Backupziel

Eigentlich wird empfohlen, NFS statt SMB zu nutzen, um die Backups
von *raspiBackup* abzulegen.
Dann lässt sich Backuptyp rsync nutzen und immer nur ein Deltabackup
erstellen statt eines Vollbackups, was bei SMB notwendig ist.
Aber trotzdem mag es Gründe geben, warum man ein *raspiBackup* auf einem
SMB Laufwerk ablegen möchte.

Im Folgenden wird beschrieben, wie das bei einer Synology zu
konfigurieren ist. Dabei wird auch autoFS konfiguriert.
Wird nicht bereits autoFS genutzt, erreicht man bei *raspiBackup* mit der
Option `DynamicMount` dasselbe Verhalten.

Um automatisch die SMB Backup-Partition zu mounten, wenn *raspiBackup* sie
nutzt, ist auf der NAS ein shared Folder zu definieren und zu konfigurieren.

In der folgenden Anleitung wird der shared Folder Name "raspiBackup"
angenommen.

## Installation von autoFS

```
sudo apt install autofs
```

### AutoFS konfiguration

  - `/etc/auto.cifs`

    ```
    synoRaspiBackup -fstype=cifs,rw,credentials=/home/pi/scratch.conf,cache=none,iocharset=utf8,file_mode=0664,dir_mode=0775,vers=3.1.1,soft,iocharset=utf8 ://<synologyIP>/raspiBackup
    ```

Damit wird ein SMB shared folder mit dem Namen `raspiBackup`
auf dem NAS definiert mit dem Mountpoint `synoRaspiBackup`.

  - `/etc/auto.master`

    ```
    /mnt /etc/auto.cifs --timeout=600 --ghost
    ```

sorgt dafür, dass in `/mnt/synoRaspiBackup` die SMB Partition des NAS
automatisch gemountet wird, sobald darauf zugegriffen wird.

## Definition der SMB Zugangsdaten

  - `/home/pi/raspiBackup.conf`
    ```
    user=<AdministratorName>
    password=<AdministratorKennwort>
    ```

### Zugangsdaten nur für den Nutzer pi lesbar machen

```
chmod 600 /home/pi/raspiBackup.conf
```

## Definition der SMB Partition als Backuppartition in raspiBackup

Aufruf des raspiBackupInstallers mit `sudo raspiBackupInstallUI`
und Definition von `/mnt/synoRaspiBackup` (`M3 -> C2`)

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/687-raspibackup-nutzung-einer-synology-als-backupspace-mit-cifs-samba-und-autofs
