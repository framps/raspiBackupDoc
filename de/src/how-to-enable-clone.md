# Erstellung eines Clones am Ende des Backups

> [!NOTE]
> Diese Funktionalität steht erst mit *raspiBackup* Release 0.7.3 zur Verfügung

*raspiBackup* kann nach der Erstellung eines Backups dieses Backup sofort auf ein lokal angeschlossenes Gerät zurückspielen.
Damit existiert ein Backup, welches sofort genutzt werden kann, um ein ausgefallenes Gerät oder ein nicht mehr startbares OS
durch Wechsel des Bootmediums sofort wieder zu starten. Ohne diese Funktion muss erst ein existierendes Backup zurückgespielt werden.
Dieses dauert etwas länger. Wird der Backuptyp rsync genutzt ist das Zurückspielen nur eine Synchonisation mit dem Backup und
sehr schnell beendet. Die Backuptypen dd und tar sind immer ein vollständiges Zurückspielen des Backups und dauern dementsprechend länger.

Vorgehensweise um das Cloning einzuschalten:

1) Erstellen eines Backups wobei das Cloning ausgeschaltet sein muss

2) Zurückspielen des Backups auf das Clonedevices

3) Cloning einschalten

   1) Befehlszeile

      Auf der Befehlszeile muss beim Starten des Backups noch die Option `--clone <Clonegerät>` angegeben werden. `<Clonegerät>`
      ist dabei das lokal angeschlossene Gerät auf welchem der aktuelle Backup synchronisiert bzw zurückgespielt werden soll.

   2) Installer

      Im Installer ist das `<Clonegerät>` bei `M3->C10` zu konfigurieren.
      Danach ist es auf der Befehlszeile nicht mehr notwendig die Option `--clone` anzugeben. Der regelmäßige Backup erstellt dann auch immer einen Clone.

   3) Anpassung der Kopnfigurationsdatei /usr/local/etc/raspiBackup.conf

      In der Option DEFAULT_CLONE_DEVICE muss das Clonedevice konfiguriert werden.

> [!CAUTION]
> Das Clonegerät wird mit dem Backup überschrieben. Es ist also unbedingt darauf zu achten, dass das Clonegerät das richtige Gerät ist.
> Ansonsten droht Datenverlust. Deshalb muss `/dev/disk/by-partuuid/<PARTUUID>` genutzt werden und nicht einfach `/dev/sda` oder ähnlich. Die PARTUUIDs der verfügbaren Partitionen werden mit folgendem Befehl angezeigt: `lsblk -o NAME,FSTYPE,LABEL,PARTUUID`

> [!WARNING]
> Bei bestimmten Konfigurationen kann es sein, dass nach einem Neustart der Raspberry von dem Clonegerät gebootet wird.
> Das kann besonders dann auftreten, wenn per USB Boot von einer USB Platte oder USB SSD gebootet wird und das Clonegerät ebenfalls per USB angeschlossen ist.

> [!NOTE]
> Wird der Backuptyp rsync genutzt muss einmalig ein Backup auf das Clonegerät zurückgespielt und damit der Clone initialisiert werden, damit spätere Backups nur noch synchronisiert werden können. Details siehe dazu [hier](restore-intro.md)

Soll die Erstellung eines Clones wieder ausgeschaltet werden muss mit dem Installer bei `M3->C10` das Clonegerät wieder gelöscht werden. Soll wieder manuell ein Backup zurückgespielt werden muss vorher das Cloning ausgeschaltet werden.

[.status]: translated
