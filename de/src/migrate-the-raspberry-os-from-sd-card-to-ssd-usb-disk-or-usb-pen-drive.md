# Umziehen des Raspberry Betriebssystems von SD Karte auf SSD, USB Platte oder USB Stick

*raspiBackup* ist dafür gedacht, ein Backup wieder auf die originale
Gerätekonfiguration zurückzuspielen. Es gibt 3 mögliche Szenarien:

1. `/boot` und `/` auf SD Karte
2. `/boot` auf SD Karte und `/` extern auf einer SSD, USB Platte oder USB Stick
   (Ältere Rasperry, welche keinen USB Boot Mode kann)
3. `/boot` und `/` auf einer SSD, USB Platte oder USB Stick
   (USB Boot Mode auf neueren Raspberries)

*raspiBackup* kann aber auch dafür benutzt werden, sehr einfach von (1) nach (2) oder (3) zu migrieren.

Dazu wird ein Backup mit *raspiBackup* erstellt und anschließend auf die neue Gerätekonfiguration zurückgespielt.

Für (2) als Migrationsziel ist folgender Befehl zum Restore notwendig:

```
sudo raspiBackup.sh -d <SD-Karte> -R <USB Gerät> <Backup>
```

Für (3) ist folgender Befehl zum Restore notwendig:

```
sudo raspiBackup.sh -d <USB Gerät> <Backup>
```

Dabei kann <USB Gerät> eine SSD, eine USB Platte oder ein USB Stick sein


Wenn auf ein grosses USB Gerät umgezogen werden soll, ist die Option
`--resizeRootFS-` sinnvoll, die die Rootpartition nicht expandiert, denn dann kann
der Rest des USB Gerätes für weitere Partitionen genutzt werden.

Details zum Restore können bei "[Wiederherstellen/Restore](restore.md)" nachgelesen werden.


[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/592-umziehen-des-raspberry-betriebssystems-von-sd-karte-auf-ssd-usb-platte-oder-usb-stick
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/593-migrate-the-raspberry-os-from-sd-card-to-ssd-usb-disk-or-usb-pen-drive

