# NFS als Backupziel

Es macht sehr viel Sinn, die Backups von [raspiBackup](https://linux-tips-and-tricks.de/de/raspibackup)
auf einem NAS abzulegen und das NFS Protokoll dazu zu nutzen. Im Folgenden wird beschrieben, wie
das bei einer Synology zu konfigurieren ist. Natürlich kann man auch jedes andere NAS nutzen, sofern es NFS unterstützt.
Auch eine Raspberry kann als NFS Server konfiguriert und genutzt werden.

## *raspiBackup* - Nutzung von NFS am Beispiel einer Synology

**Wichtig**: Die Partition auf dem NAS muss mit `no_root_squash` exportiert werden,
damit *rsync* genutzt werden kann. Im UI muss dann bei Squash No-mapping eingetragen
werden.

![Synology Konfiguration](images/synology-nfs-defs.png)

Es darf **NICHT** *NFS4* aktiviert werden wie im Screenshot zu sehen ist! Es muss
*NFS3* genutzt werden. Mit *NFS4* habe ich es nicht hinbekommen.

![Synology NFS Konfiguration](images/synologyNFSAddtlSettings.png)

## Konfiguration einer Synology und der Raspberry, um ein rsync Backup per NFS auf einer Synology zu sichern

Im Wesentlichen sind folgende Schritte durchzuführen:

1) Gemeinsamen NFS Ordner auf der Synology erstellen
2) mount des gemeinsamen NFS Ordners auf der Raspi in der `/etc/fstab`
3) Installation und Konfiguration von *raspiBackup* per [Installer](installer.md) (keinen automatischen Backup konfigurieren)
4) Test des Backups und Restores von der Commandline
5) Einrichten des regelmäßigen Backups in der Crontab per [Installer](installer.md)

Es empfiehlt sich, vor dem Beginn die [FAQ](faq.md) zu lesen, wo die wichtigsten
Fragen und Antworten zu *raspiBackup* zusammengestellt sind.

### Gemeinsamen NFS Ordner auf der Synology erstellen

Im DSM, Systemsteuerung -> Gemeinsamer Ordner -> Erstellen erstellt man einen
gemeinsamen Ordner z.B. mit dem Namen `raspiBackups`. Eine Papierkorb braucht man
nicht. Die NFS Berechtigungen müssen wie folgt eingestellt werden (Hinweis:
*raspiBackup* läuft als root). Hostname oder IP: Hostname oder IP des NFS
Clients, z.B. 192.168.0.10. Privileg: lesen/schreiben, Squash: keine Zuordnung,
Sicherheit: sys.

### Eintrag des gemeinsamen NFs Ordners auf der Raspi in der fstab

Folgender Eintrag in der `/etc/fstab` bewirkt das Mounten des Synology NFS Orders
unter dem Mountpoint `/backup` unter der Annahme, dass 192.168.0.11 die Synology
ist:

```
192.168.0.11:/volume1/raspiBackups /backup nfs rw,nfsvers=3 0 0
```

**Es ist dringend zu empfehlen, den Mountpoint `/backup` zu nutzen und nicht z.B.
`/home/pi/backup` oder andere Verzeichnisse.**


### Manueller mount des gemeinsamen NFS Ordners

Jetzt kann man prüfen, ob der Backupspace auf der Synology freigegeben ist mit
`showmount -e 192.168.0.11`. Danach kann man mit `sudo mount /backup` den NFS
Ordner manuell mounten. Durch den obigen Eintrag in der `/etc/fstab` wird der
Mount nach jedem Neustart automatisch vorgenommen, und es ist kein manueller
Mount mehr notwendig.

### Test des Schreibzugriffs

Den Schreibzugriff kann man nun testen mit `sudo bash -c 'echo "Raspberry war
hier" > /backup/killroy.txt'` und `sudo cat /backup/killroy.txt`.
Falls es Probleme gibt, Hinweise von erfahrenen Synologybenutzern zu Synology
und *raspiBackup* lesen.

### Installation und Konfiguration von *raspiBackup*

Installation von *raspiBackup* gemäß [dieser Anleitung](installation-in-5-minutes.md).
Dabei dann `rsync` als Backupmethode und `/backup` als Backuppfad angeben.
Den regelmäßigen Backup noch nicht konfigurieren.

### Test des Backups und Restores von der Commandline

### Einrichten des regelmässigen Backups im Installer

Aufruf des Installers und Konfiguration des regelmäßigen Backupzeitpunktes.

## Hinweis zu ACLs

Eigentlich kann man ACLs mit *NFS3* sichern. Das klappt z.B., wenn man eine
Raspberry als NFS Server aufsetzt (Siehe [https://linux-tips-and-tricks.de](https://linux-tips-and-tricks.de/en/servere/604-how-to-backup-acls-with-rsync-on-a-nfs-partition)).
Allerdings funktioniert das nicht mit einer *Synology* - auch wenn sie *NFS3* nutzt.

Eine Anfrage bei Synology am 13.5.2022 lieferte folgende Antwort:

> Unfortunately, I have to inform you that both Linux ACL and setfacl are not supported by DSM.
> I would be pass this on as feedback to our development department as a function request.

## Hinweise und Tipps von *raspiBackup* Benutzern, die eine Synology als Backupspace benutzen

### Hinweis von Udo

Udo hat im Kommentar beschrieben, was man tun muss, damit der Automount der
Synology beim Booten der Raspberry funktioniert.

Es wurde verschiedentlich berichtet, dass es mit Synologies Probleme mit
Hardlinks geben kann, die von rsync benutzt werden, wenn NFS4 benutzt wird. Mit

```
192.168.0.42:/backup /backup nfs rw,nfsvers=3 0 0
```

wird das NFS3 Protokoll benutzt, so dass das Backupskript dann erfolgreich durchläuft.
Weiterhin werden Softlinks mit SMB nicht unterstützt, wenn nicht wenigstens SMB Version 3 benutzt wird.

### Hinweis von Markus

Bei mir läuft das Backup mit *raspiBackup* in folgender Konfiguration:

* Raspberry mit Raspbian Wheezy
* *raspiBackup*.sh, Version 0.5.7.10e
* Synology NAS DS213, mit aktueller DSM Version

Synology NAS Share: /volume1/backup
Synology NAS Share NFS Regeln: Hostname oder IP: *, Privileg: Lesen/Schreiben, Squash: Keine Zuordnung
Synology NAS Share Berechtigungen (Konsole): d---------    5 root     root          4096 Dec 15 06:01 backup
Raspberry Pi Mountpoint: /media/nas-backup

Raspberry Pi fstab Einträge für NFS3 und NFS4

```
# Entry for the NAS backup, mount with NFS version 3
192.168.X.XXX:/volume1/backup /media/nas-backup nfs rw,nfsvers=3 0 0
# Entry for the NAS backup, mount with NFS version 4
#192.168.X.XXX:/volume1/backup /media/nas-backup nfs nfsvers=3,rw 0 0
```

Auszug aus der `raspiBackup.conf` abgelegt unter `/usr/local/etc/`

```
cat /usr/local/etc/raspiBackup.conf
# path to store the backupfile
DEFAULT_BACKUPPATH="/media/nas-backup"
# how many backups to keep
DEFAULT_KEEPBACKUPS=4
# type of backup: dd, tar, xbmc or rsync
DEFAULT_BACKUPTYPE="rsync"
```

### Hinweise von Alfred

Alfred bekam folgende Fehlermeldung von rsync

```
rsync: chown "/mnt/nas/arami nta/araminta-rs ync-backup-2016 1029-190948/mmc blk0p1/overlays /.w1-gpio-overl ay.dtb.ansSC4" failed: Operation not permitted (1)"
```

Dann benutze er den rsync Befehl, den er im *raspiBackup*.log fand, den
*raspiBackup* ausführt, um das Backup zu erstellen, um das Problem zu
reproduzieren und gezielt ohne *raspiBackup* zu debuggen. Da er den -P Modus
benutzt, musste er vorher noch folgende Befehle ausführen:

```
sudo mkdir /tmp/mmcblk0p1
sudo mount /dev/mmcblk0p1 /tmp/mmcblk0p1
```

Er machte dann zufällig einen Fehler, der zur Lösung führte: Das ist der rsync
Befehl, den er ausführte:

```
rsync --exclude="/mnt/nas" --exclude=/proc/* --exclude=/lost+found/* --exclude=/sys/* --exclude=/dev/* --exclude=/boot/* --exclude=/tmp/* --exclude=/run/* --exclude=mmcblk0p1/overlays/* --numeric-ids -aHAXx -v /tmp/mmcblk0p1 "/mnt/nas/test.backup"
```

Dieser Befehl funktionierte ohne Fehlermeldung. Es lag aber daran, dass
vergessen wurde 'sudo' zu benutzen. Als der Befehl dann nochmal mit sudo
ausführte kam die Fehlermeldung wieder. Das weist IMHO auf ein Zugriffsproblem
auf dem Synology NAS hin. Nachdem dann auf dem NAS die NFS permissions von
**'map all users to admin'** auf **'no mapping'** geändert wurde, bingo, funktionierte
es auch mit sudo.

### Hinweis von Chris

Wie folgt wurde erfolgreich ein TAR-Backup via NFS 4.1 auf einem QNAP-NAS erstellt.

Inhalt - `/etc/fstab`:

```
<NAS-IP/-Hostname>:/<Share name>  /backup   nfs4    defaults,_netdev,noatime    0    2
```


QNAP-NAS seitig (share):

```
Zugriffsrecht -> sync = "no wdelay"
Zugriffsrecht -> secure (Ja)
Host: IP vom Raspi
Sicherheit: sys,
Squash-Option: lesen/schreiben
Squash-Option: "Nur root-Benutzer zuordnen"
Anonymer GID: guest
Anonymer UID: guest
```

[.status]: translated
[.source]: https://linux-tips-and-tricks.de/de/synology
[.source]: https://www.linux-tips-and-tricks.de/en/synology
