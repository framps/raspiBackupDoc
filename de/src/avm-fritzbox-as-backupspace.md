# AVM FRITZ!Box als Backupziel

Wer kein NAS besitzt, aber seine Raspberries mit *raspiBackup* sichern möchte,
kann natürlich auch den NAS Speicher einer Fritzbox nutzen. Allerdings muss
dazu der Backuptyp tar genommen werden, da das genutzte SMB-Protokoll keine
Hardlinks unterstützt und somit auch kein rsync Backuptyp genutzt werden kann,
bei dem man inkrementelle Backups erhält.

Sehr hilfreich, um eine Fritzbox dazu zu nutzen, war ein [Artikel von andwil.de](https://www.andwil.de/weblog/linux-fritznas-mounten-cifs).
Dort wird sehr schön erklärt, was auf der Fritzboxseite und der Raspberryseite zu konfigurieren ist.

Anbei eine Beispielzeile in der /etc/fstab:

```
//192.168.0.1/FRITZ.NAS/USB-Sandisk3-2Gen1-01 /backup cifs noauto,user,vers=3.0,credentials=/home/pi/.smbcredentials,noserverino,uid=1000,gid=1000 0 0
```

Außerdem sollte mit
```
chmod 600 ~/.smbcredentials
```

dafür gesorgt werden, dass die Fritzbox-Zugangsdaten nur vom Nutzer gelesen werden
können. Das ist zwar bei der Raspberry, wo normalerweise nur ein Nutzer drauf
arbeitet, nicht unbedingt nötig. Aber es ist gute Praxis, Zugangsdaten immer
nur für den jeweiligen Nutzer les- und änderbar zu machen.

Dann kann ein Backup mit
```
sudo raspiBackup -t tar
```
erstellt werden.

Nachdem der Restoretest erfolgreich war, ist dann noch im Installer der Backuptyp
auf tar zu konfigurieren sowie der Zeitpunkt des regelmäßigen Backups festzulegen.

[.status]: rst
