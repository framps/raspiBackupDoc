# Erstellung eines Clones am Ende des Backups

> [!NOTE]
> Diese Funktionalität steht erst mit *raspiBackup* Release 0.7.3 zur Verfügung und ist momentan im Beta Stadium

*raspiBackup* kann nach der Erstellung eines Backups dieses Backup sofort auf ein lokal angeschlossenes Gerät zurückspielen.
Damit existiert ein Backup, welches sofort genutzt werden kann, um ein ausgefallenes Gerät oder ein nicht mehr startbares OS
durch Wechsel des Bootmediums sofort wieder zu starten. Ohne diese Funktion muss erst ein existierendes Backup zurückgespielt werden.
Dieses dauert seine Zeit. Wird der Backuptyp rsync genutzt ist das Zurückspielen des aktuellen Backups auf das Clonegerät nur eine Synchonisation mit dem aktuellen Backup und
sehr schnell beendet. Der Backuptyp tar ist immer ein vollständiges Zurückspielen des Backups auf das Clonegerät und dauert dementsprechend länger.

Es werden nur der Backuptyp rsync und tar sowie beide Backupmodes unterstützt.

> [!NOTE]
> Im Folgenden wird als Clonegerät `/dev/sda` angenommen. Andere Beispiele wären `/dev/mmcblk1` oder `/dev/nvme1n1`.
> Ausserdem wird eine PARTUUID `2a6bd249-01` angenommen.

Vorgehensweise um das Cloning einzuschalten:

1) Erstellen eines Backups

2) Zurückspielen des Backups auf das Clonedevice `/dev/sda`

3) Auflistung der PARTUUIDs des Clonegerätes mit `blkid | grep "/dev/sda"` und Auswahl einer PARTUUID. Z.B. `2a6bd249-01`.

4) Cloning einschalten

   1) Manuelle Anpassung der Kopnfigurationsdatei /usr/local/etc/raspiBackup.conf

      In der Option `DEFAULT_CLONE_DEVICE` muss das Clonedevice `/dev/sda` sowie die PARTUUID in der Option
      `DEFAULT_CLONE_PARTUUID` eine PARTUUID konfiguriert werden.

   2) Installer

      Im Installer ist das `<Clonegerät>` wie auch die PARTUUID bei `M3->C10` zu konfigurieren. Die PARTUUID
      muss von dem Clonegerät durch Leerzeichen getrennt sein.

      **Hinweis**: Das Clonegerät muss dazu angeschlossen sein.


5) Erstellen eines Backups sowie eines Clones

   1) Befehlzeile

      Auf der Befehlszeile ist beim Starten des Backups die Option `--clone <Clonegerät>` anzugegeben. `<Clonegerät>`
      ist dabei das lokal angeschlossene Gerät auf welchem der aktuelle Backup synchronisiert bzw zurückgespielt werden soll. Im Beispiel wäre es `--clone /dev/sda`

      **Hinweis**: Eine PARTUUID muss vorher konfiguriert worden sein.

   2) Regelmäßiger automatischer Aufruf

      Ist im Installer der regelmäßige Aufruf konfiguriert wird automatisch regelmäßig ein Backup und ein Clone erstellt.

> [!IMPORTANT]
> Es werden folgende Tests vorgenommen, um ein versehentliches Überschreiben von anderen angeschlossenen Geräten zu verhindern:
> 1) Die Konfigurationsvariable `DEFAULT_CLONE_PARTUUID` muss mit der PARTUUID einer Partition des Clonedevices übereinstimmen.
> 2) Die Partitionierung des Clonegerätes muss mit der Partitionierung des laufenden Systems übereinstimmen. Die letzte Partionsgröße darf unterschiedlich sein.

> [!CAUTION]
> Bei bestimmten Konfigurationen kann es sein, dass nach einem Neustart der Raspberry von dem Clonegerät gebootet wird.
> Das kann besonders dann auftreten, wenn per USB Boot von einer USB Platte oder USB SSD gebootet wird und das Clonegerät ebenfalls per USB angeschlossen ist. Ein sorgfältiger Test ist dann unumgänglich.

Soll die Erstellung eines Clones wieder ausgeschaltet werden muss mit dem Installer bei `M3->C10` das Clonegerät und die PARTUUID bzw manuell in der Konfigurationsdatei gelõscht werden.

[.status]: translated
