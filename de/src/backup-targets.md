# Backupziele

*raspiBackup* mounted die Backup-Partition, um auf sie zu schreiben. D.h.
eine jede Partition, die unter Linux gemountet
werden kann, kann als Backup-Partition genutzt werden.

Dazu gehören lokal angeschlossene SD Karten,
per USB angeschlossene Platten, SSDs,
USB Sticks und SD USB Adapter sowie NVMe SSDs.
Des weiteren kann [SMB](smb-as-backupspace.md) und [NFS](nfs-as-backupspace.md) genutzt werden,
um nicht lokal angeschlossene Backuppartitionen zu nutzen.
SSHFS, CurlFtpFS und [WebDAV](webdav-as-backupspace.md) funktionieren ebenso mit *raspiBackup*,
um die Backups auf remoten Servern abzulegen.
Die [AVM Frit!zbox](avm-fritzbox-as-backupspace.md) unterstützt auch SMB und kann somit
auch als Backupziel genutzt werden.

```admonish info title="Filesysteme"
Die jeweiligen Backup-Partitionen müssen partitioniert sein. Siehe [Vor-und Nachteile der jeweiligen
Filesysteme](which-filesystem-can-be-used-on-the-backup-partition.md).
```

Neben den folgenden Kapiteln siehe dazu auch [Wie kann man von der Raspberry Pi auf externe Daten zugreifen](https://linux-tips-and-tricks.de/de/13-raspberry/423-wie-kann-man-von-der-pi-unter-linux-auf-externe-daten-zugreifen).

[.status]: rst
