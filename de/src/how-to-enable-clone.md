# Erstellung eines Clones am Ende des Backups

> [!NOTE]
> Diese Funktionalität steht erst mit *raspiBackup* Release 0.7.3 zur Verfügung und ist momentan im Beta Stadium

*raspiBackup* kann nach der Erstellung eines Backups dieses Backup sofort auf ein lokal angeschlossenes Gerät zurückspielen.
Damit existiert ein Backup, welches sofort genutzt werden kann, um ein ausgefallenes Gerät oder ein nicht mehr startbares OS
durch Wechsel des Bootmediums sofort wieder zu starten. Ohne diese Funktion muss erst ein existierendes Backup zurückgespielt werden.
Dieses dauert etwas länger. Wird der Backuptyp rsync genutzt ist das Zurückspielen nur eine Synchonisation mit dem Backup und
sehr schnell beendet. Der Backuptyp tar ist immer ein vollständiges Zurückspielen des Backups und dauert dementsprechend länger.
Der Backuptyp dd wird nicht unterstützt.

Vorgehensweise um das Cloning einzuschalten:

1) Erstellen eines Backups

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

> [!Note]
> Das Clonegerät wird mit dem Backup überschrieben. Deshalb werden verschiedenen Tests von *raspiBackup*
> vorgenommen, um ein versehentliches Überschreiben von anderen angeschlossenen Geräten zu verhindern
> und dann wird der Clone sofort abgebrochen.
> 1) Es darf vom Clonedevicetyp nur einer vorhanden sein. D.h. iz.B. zwei /dev/sd oder /dev/mmcblk sind nicht erlaubt
> 2) Sollen trotzdem mehrere Clonedevicetypen erlaubt sein, muss in der Konfigurationsvariable `DEFAULT_CLONE_ROOT_PARTUUID` die PARTUUID der Rootpartition des Clonedevices stehen und übereinstimmen.

> [!WARNING]
> Bei bestimmten Konfigurationen kann es sein, dass nach einem Neustart der Raspberry von dem Clonegerät gebootet wird.
> Das kann besonders dann auftreten, wenn per USB Boot von einer USB Platte oder USB SSD gebootet wird und das Clonegerät ebenfalls per USB angeschlossen ist.

Soll die Erstellung eines Clones wieder ausgeschaltet werden muss mit dem Installer bei `M3->C10` das Clonegerät wieder gelöscht werden. Soll wieder manuell ein Backup zurückgespielt werden muss vorher das Cloning ausgeschaltet werden.

[ästatus]: translated
