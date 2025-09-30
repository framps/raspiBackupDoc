# *raspiBackupDialog* - a comfortable help script for *raspiBackup*

An agile user of *raspiBackup* - [Franjo-G](https://github.com/franjo-G) - has written a very useful little helper script called [raspiBackupDialog](https://github.com/franjo-G).
help script with the name [raspiBackupDialog](https://github.com/framps/raspiBackup/blob/master/helper/raspiBackupDialog.sh), which shows in a dialog
the most important invocation options for the backup and restore in a dialog and with
which then triggers *raspiBackup*. *raspiBackup* snapshots are supported. Very
especially easy to perform the restore: Before the restore, the list of existing
the list of existing backups is displayed and you can select which backup
should be restored.

``` admonish info title="Note"
It is recommended to download *raspiBackupDialog* after successful installation and configuration of *raspiBackup
of *raspiBackup* and try it out.
```

## Installation and call

*raspiBackupDialog* is available as a helper script in the *GitHub* repository.

It can be downloaded to the current directory as follows:

```
curl -s https://raw.githubusercontent.com/framps/raspiBackup/master/scripts/raspiBackupDownloadFromGit.sh | bash -s -- master helper/raspiBackupDialog.sh
```

Now it can be called with :

```
sudo ./raspiBackupDialog.sh
```

If you don't want to download it every time, you can make it permanently available on your Raspberry as follows:

```
sudo mv ./raspiBackupDialog.sh /usr/local/bin
sudo chown root:root /usr/local/bin/raspiBackupDialog.sh
```

It can then be called at any time as follows:

```
sudo raspiBackupDialog.sh
```


## Invocation options

```
sudo raspiBackupDialog.sh --select # Starts a restore. The image can be selected from a list.
sudo raspiBackupDialog.sh --last # Starts a restore from the last backup.
sudo raspiBackupDialog.sh --backup # Starts a backup.
sudo raspiBackupDialog.sh --delete # A backup can be selected for deletion.
sudo raspiBackupDialog.sh --mountfs "fstab" # The backup directory is mounted according to the fstab entry.
sudo raspiBackupDialog.sh --mountfs "*.mount" # The backup directory is mounted via systemctl start *.mount.
```

If the directory was already mounted, it will not be unmounted. Otherwise it will be remounted.

Dynamic mount also works with cron.

```
* * * * /usr/local/bin/raspiBackupDialog.sh --mountfs "backup.unit" or "fstab" --cron
```

## Example dialog for a backup

```
sudo raspiBackupDialog.sh

Please choose your preferred language
German = 1
English = 2
2
Should a backup be created or an existing backup restored?
backup 1
restore 2
1
Are there more than the 2 standard partitions /boot and /root on the system drive ? y/N
n
Should a comment be inserted at the end of the backup directory?
This backup is then not included in the backup strategy and is not automatically recycled.
y/N
n
raspiBackup is now started
```

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/637-raspibackupdialog-ein-komfortables-hilfsscript-fuer-raspibackup
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/642-raspibackupdialog-a-convenient-helper-script-for-raspibackup


