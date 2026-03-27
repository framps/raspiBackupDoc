# Backupverzeichnisstruktur

## Normaler Backup

Jeder Backuplauf erstellt im Backupverzeichnis ein Unterverzeichnis,
welches folgendes Format hat:
`<hostname>`.

Jeweils darunter wird ein weiteres Verzeichnis erstellt:
`<hostname>@<osversion>-<backuptyp>-<backupdatum>`.

Bei Verwendung der Option `-M` (*raspiBackup* Snapshot) wird der Optionswert noch angehängt:
`<hostname>@<osversion>-<backuptyp>-<backupdatum><-M parameter>`.

**Beispiele:**

Die Raspberry hat den Hostnamen "raspberrypi" und es wird ein
`rsync` Backup von einem *Bookworm* OS am 15.04.2016 um 22:29:00 erstellt.
Dann entstehen folgende Verzeichnisse:

```
 ├── raspberrypi
 │   └── raspberrypi@debian12-rsync-backup-20160415-222900
```

Gibt man als Parameter für die Option `-M "Hello world"` mit,

```
 ├── raspberrypi
 │   └── raspberrypi@debian12-rsync-backup-20160415-222900_Hello_world
```

Anbei die Verzeichnisstruktur meines Backupservers, der in diesem Falle auch
eine Raspberry Pi ist. Verschiedene Backuptypen können pro Pi kombiniert
werden. Jedes Backup wird in einem neuen Unterverzeichnis abgelegt.

Pro Raspberry System werden immer drei bzw. fünf weitere Dateien zusätzlich zum
eigentlichen Backup erstellt und sind notwendig für den Restore, wenn es kein `dd`
Backup ist. Damit ist es Linuxkundigen möglich, ein Backup auch manuell zu restoren.
Dies ist im Kapitel [Manueller Restore](manual-restore.md) beschrieben.

  - `.img` - Bootpartition
  - `.mbr` - *Master Boot Record* des Systems
  - `.sfdisk` - Partitionslayout des Systems - Ausgabe des `sfdisk` Befehls
  - `.blkid` - (Partitionsorientierter Modus) - Ausgabe des `blkid` Befehls
  - `.parted` - (Partitionsorientierter Modus) - Ausgabe des `parted` Befehls


```
root@raspiBackup:/mnt/backup/raspberrypi# tree -L 2

 .
 ├── raspberrypi@debian12-dd-backup-20160415-222900
 │   └── raspberrypi@debian12-dd-backup-20160415-222900.img
 ├── raspberrypi@debian12-rsync-backup-20160416-094106
 │   ├── backup
 │   ├── bin
 │   ├── boot
 │   ├── boot.bak
 │   ├── dev
 │   ├── etc
 │   ├── home
 │   ├── lib
 │   ├── lost+found
 │   ├── media
 │   ├── mnt
 │   ├── opt
 │   ├── proc
 │   ├── raspberrypi-backup.img
 │   ├── raspberrypi-backup.mbr
 │   ├── raspberrypi-backup.sfdisk
 │   ├── raspiBackup.log
 │   ├── raspiBackup.msg
 │   ├── remote
 │   ├── root
 │   ├── run
 │   ├── sbin
 │   ├── selinux
 │   ├── srv
 │   ├── sys
 │   ├── tmp
 │   ├── usr
 │   └── var
 └── raspberrypi@debian12-tar-backup-20160415-204305
     ├── raspberrypi-backup.img
     ├── raspberrypi-backup.mbr
     ├── raspberrypi-backup.sfdisk
     ├── raspberrypi-tar-backup-20160415-204305.tar
     ├── raspiBackup.log
     └── raspiBackup.msg
```

## Partitionsorientierter Backup

```
root@boockworm:/mnt/backup/raspberrypi# tree -L 2
.

├── raspberrypi-backup.blkid
├── raspberrypi-backup.fdisk
├── raspberrypi-backup.mbr
├── raspberrypi-backup.parted
├── raspberrypi-backup.sfdisk
├── mmcblk0p1
│   ├── bcm2708-rpi-b.dtb
│   ├── bcm2708-rpi-b-plus.dtb
│   ├── bcm2708-rpi-b-rev1.dtb
│   ├── bcm2708-rpi-cm.dtb
│   ├── bcm2708-rpi-zero.dtb
│   ├── bcm2708-rpi-zero-w.dtb
│   ├── bcm2709-rpi-2-b.dtb
│   ├── bcm2710-rpi-2-b.dtb
│   ├── bcm2710-rpi-3-b.dtb
│   ├── bcm2710-rpi-3-b-plus.dtb
│   ├── bcm2710-rpi-cm3.dtb
│   ├── bcm2711-rpi-400.dtb
│   ├── bcm2711-rpi-4-b.dtb
│   ├── bcm2711-rpi-cm4.dtb
│   ├── bootcode.bin
│   ├── cmdline.txt
│   ├── config.txt
│   ├── COPYING.linux
│   ├── fixup4cd.dat
│   ├── fixup4.dat
│   ├── fixup4db.dat
│   ├── fixup4x.dat
│   ├── fixup_cd.dat
│   ├── fixup.dat
│   ├── fixup_db.dat
│   ├── fixup_x.dat
│   ├── issue.txt
│   ├── kernel7.img
│   ├── kernel7l.img
│   ├── kernel8.img
│   ├── kernel.img
│   ├── LICENCE.broadcom
│   ├── overlays
│   ├── start4cd.elf
│   ├── start4db.elf
│   ├── start4.elf
│   ├── start4x.elf
│   ├── start_cd.elf
│   ├── start_db.elf
│   ├── start.elf
│   └── start_x.elf
├── mmcblk0p2
│   ├── backup
│   ├── bin
│   ├── boot
│   ├── dev
│   ├── etc
│   ├── home
│   ├── lib
│   ├── lost+found
│   ├── media
│   ├── mnt
│   ├── opt
│   ├── proc
│   ├── remote
│   ├── root
│   ├── run
│   ├── sbin
│   ├── srv
│   ├── sys
│   ├── tmp
│   ├── usr
│   └── var
├── raspiBackup.log
└── raspiBackup.msg
```

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup#Vergleichtodo
[.source]: https://www.linux-tips-and-tricks.de/en/backup
