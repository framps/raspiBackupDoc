# Backupziele

*raspiBackup* mounted die Backup-Partition, um auf sie zu schreiben.
Also kann jede Partition, die unter Linux gemountet werden kann,
als Backup-Partition genutzt werden.

Dazu gehören lokal angeschlossene SD-Karten,
per USB angeschlossene Platten, SSDs,
USB-Sticks und SD-USB-Adapter sowie NVMe-SSDs.
Des weiteren kann [SMB](smb-as-backuptarget.md) und [NFS](nfs-as-backuptarget.md) genutzt werden,
um nicht lokal angeschlossene Backuppartitionen anzubinden.
SSHFS, CurlFtpFS und [WebDAV](webdav-as-backuptarget.md) funktionieren ebenso zur
Ablage der Backups auf entfernten Servern.
Die [*AVM Frit!zbox*](avm-fritzbox-as-backuptarget.md) unterstützt ebenfalls SMB und kann somit
auch als Backupziel genutzt werden.

```admonish info title="Filesysteme"
Die jeweiligen Backup-Partitionen müssen partitioniert sein. Siehe [Vor-und Nachteile der jeweiligen
Filesysteme](which-filesystem-can-be-used-on-the-backup-partition.md).
```

Neben den folgenden Kapiteln siehe dazu auch [Wie kann man von der Raspberry Pi auf externe Daten zugreifen](https://linux-tips-and-tricks.de/de/13-raspberry/423-wie-kann-man-von-der-pi-unter-linux-auf-externe-daten-zugreifen).

[.status]: rst
[.status]: review-comment "Benennungskonsistenz prüfen:
Es heisst hier und anderswo 'Backup-Target bzw. -Ziel. Aber die untergeordneten Dateien haben 'backupspace' im Dateinamen."
