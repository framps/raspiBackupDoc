# Which file system can be used on the backup partition?

Depending on which backup method you use with *raspiBackup*, the correct
correct file system must be present on the backup device. In the following
table below shows the different file systems for each backup method
and their restrictions.

## Locally connected backup partitions

| filesystem | dd | tar | rsync |
|------------|-----------|-----------|-------|
| fat16 | 4GB limit | 4G limit | no |
| fat32 | yes | yes | no |
| exFat | yes | yes | no |
| ntfs | yes | yes | no |
| ext2/3/4 | **recommended** | **recommended** | **recommended** |

## Remotely connected backup partitions

| filesystem | dd | tar | rsync |
|------------|------------|----------|------------|
| SMB | yes | yes | restricted <br> Goes via the detour with the use of a loop device. See also [FAQ24](faq.md#faq24). |
NFS | yes | yes | yes | **recommended** <br> Backing up ACLs is also possible, but only via the detour of using a loop device. Or you can switch off the backup of ACLs. See also [FAQ24](faq.md#faq24). |

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/578-welches-dateisystem-kann-auf-dem-backupgeraet-benutzt-werden
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/580-which-filesystem-can-be-used-on-the-backup-partition


