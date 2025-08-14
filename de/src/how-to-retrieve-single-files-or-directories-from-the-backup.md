# Restore einzelner Dateien/Verzeichnisse aus einem Backup

Manchmal ist nicht ein kompletter Restore des ganzen Systems, sondern nur
einzelner Datei(en) oder Verzeichnisse gewünscht.
Dies wird nicht direkt von *raspiBackup* unterstützt.
Da *raspiBackup* zum Restore des Gesamtsystem nur Standard-Linux-Tools
verwendet, ist das aber für alle Backuptypen manuell möglich.

Allerdings müssen diese Aktivitäten auf einem Linux-System durchgeführt
werden.

Am einfachsten geht das bei rsync-Backups. dd und tar Backups erfordern einige
zusätzliche Schritte auf der Kommandozeile.


## dd backup

Zuerst muss die dd Image-Datei verfügbar gemacht werden.

Im folgenden Beispiel ist die USB-Platten-Partition `/dev/sda1` und wird nach
`/mnt` gemounted mit:

```
sudo mount -o ro /dev/sda1 /mnt
```

Dort nach der gewünschten Backup-Generation und der Image-Datei suchen.

Als nächstes ist der Sektor-Offset in der Image-Datei mit fdisk zu ermitteln.

```
sudo fdisk -l raspberrypi-dd-backup-20160415-222900.img

Disk raspberrypi-dd-backup-20160415-222900.img: 7.5 GiB, 8011120640 bytes, 15646720 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x000798a3

Device                                     Boot Start  End      Sectors  Size Id Type
raspberrypi-dd-backup-20160415-222900.img1      8192   122879   114688   56M   c W95 FAT32 (LBA)
raspberrypi-dd-backup-20160415-222900.img2      122880 15646719 15523840 7.4G 83 Linux
```

Es sind also 8192 für die erste und 122880 für die zweite Partition.

Nun wird die Partition nach `/media` gemounted, in dem Beispiel die zweite, die root-Partition.
Hinweis: Der Offset ist mit der Sektorgröße, hier 512, zu multiplizieren.

```
sudo mount -o ro,norecovery,loop,offset=$((122880*512)) raspberrypi-dd-backup-20160415-222900.img /media
```

Nun ist im Verzeichnis `/media` der Zugriff auf alle Daten des Backups möglich.

```
ls /media/

backup boot dev home lost+found mnt proc root sbin srv tmp var
bin boot.bak etc lib media opt remote run selinux sys usr
```

Zum Beenden die Partition wieder unmounten:

```
sudo umount /media
sudo umount /mnt
```


## tar backup

Zuerst muss die tar-Datei verfügbar gemacht werden.

Im folgenden Beispiel ist die USB-Platten-Partition `/dev/sda1` und wird nach `/mnt` gemounted mit:

```
sudo mount -o ro /dev/sda1 /mnt
```

Angenommen, auf das gesamte Verzeichnis `/etc` in der tar-Datei soll zugegriffen werden.
Das geht mit folgendem Kommando.

```
tar -xf raspberrypi-tar-backup-20171028-205746.tar -C /tmp etc
```
Aber dabei muss man etwas geduldig sein, denn je nach Größe der tar-Datei kann das etwas dauern.

Schließlich wurde das `/etc`-Verzeichnis aus der tar-Datei nach `/tmp` extrahiert. Dort ist nun der Zugriff möglich.


## rsync backup

Zu Beginn muss Zugriff auf das rsync-Backup-Verzeichnis bestehen.

Im folgenden Beispiel ist die USB-Platten-Partition `/dev/sda1` und wird nach `/mnt` gemounted mit:

```
sudo mount -o ro /dev/sda1 /mnt
```

Nun ist direkt Zugriff auf die Inhalte möglich:

```
cd /mnt/backups/raspberrypi/raspberrypi-rsync-backup-20160705-212724-8G

ls -la

total 57592
drwxr-xr-x 26  pi   pi       4096 Jul 5 2016 .
drwxr-xr-x 14  root root     4096 Apr 18 2018 ..
drwxr-xr-x 2   root root     4096 Nov 15 2015 backup
drwxr-xr-x 2   root root     4096 May 29 2016 bin
drwxr-xr-x 2   root root     4096 Jan 1 1970 boot
drwxr-xr-x 3   root root     4096 Apr 20 2014 boot.bak
drwxr-xr-x 2   root root     4096 Jul 4 2016 dev
drwxr-xr-x 125 root root    12288 Jul 5 2016 etc
drwxr-xr-x 3   root root     4096 Feb 1 2015 home
drwxr-xr-x 16  root root     4096 May 29 2016 lib
drwx------ 2   root root     4096 Dec 15 2012 lost+found
drwxr-xr-x 2   root root     4096 Jul 3 2016 media
drwxr-xr-x 2   root root     4096 Jan 8 2014 mnt
drwxr-xr-x 3   root root     4096 Mar 1 2015 opt
-rwxr-xr-x 1   pi   pi     126799 Jul 5 2016 pi
dr-xr-xr-x 2   root root     4096 Jan 1 1970 proc
drwx------ 2   root root     4096 Jul 10 2013 .pulse
-rw------- 2   root root      256 Dec 16 2012 .pulse-cookie
-rw-r--r-- 1   root root 58720256 Jul 5 2016 raspberrypi-backup.img
-rw-r--r-- 1   root root      512 Jul 5 2016 raspberrypi-backup.mbr
-rw-r--r-- 1   root root      273 Jul 5 2016 raspberrypi-backup.sfdisk
drwxr-xr-x 4   root root     4096 Aug 15 2013 remote
drwx------ 13  root root     4096 Jul 3 2016 root
drwxr-xr-x 2   root root     4096 Jul 5 2016 run
drwxr-xr-x 2   root root     4096 May 29 2016 sbin
drwxr-xr-x 2   root root     4096 Jun 20 2012 selinux
drwxr-xr-x 3   root root     4096 Mar 7 2014 srv
dr-xr-xr-x 2   root root     4096 Jul 4 2016 sys
drwxrwxrwx 2   root root     4096 Jul 5 2016 tmp
drwxr-xr-x 10  root root     4096 Dec 15 2012 usr
drwxr-xr-x 12  root root     4096 Jul 8 2014 var
```

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/596-how-to-retrieve-single-files-or-directories-from-the-backup

