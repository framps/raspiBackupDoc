# Typical restore usecases 

Various application examples of
*raspiBackup* and their configuration are presented and explained hoe to use
a backup for restore.
overview of all options can be found in
in the [Restore](restore.md) chapter.

*Note*
In the following examples, /dev/sda is taken as the device to be restored.

<!-- toc -->

## A system no longer started because an SD card became unusable

In this case, the entire backup must be restored to a new SD card

```
sudo raspiBackup -d /dev/sda <backup>
```

## A system no longer started because changes were made to the system

In this case, the entire backup must be restored if a normal backup was created. If there is a partition-oriented backup, the restore to the system device is much faster as no new partitioning is performed.

```
sudo raspiBackup -d /dev/sda -00 <backup>
```

In this case, only the changes since the backup are rolled back, i.e. new files are deleted, changed files are replaced by the previous contents and deleted files are restored.

## A new system has been set up and a few configuration files are to be restored to the status of a backed up system

If a dd or tar backup is available, the files have to be extracted from the backups. If a rsync backup has been created, the files can simply be accessed and copied to the new system. Details on how single files can be copied are described [here](how-to-retrieve-single-files-or-directories-from-the-backup.md).

## A system is to be moved to another medium. E.g. from SD card to an SSD

To do this, a snapshot is created (option -M) and then the backup is restored to the new system device.

```
sudo raspiBackup -M "Systemumzug" <Backupverzeichnis>
sudo raspiBackup -d /dev/sda <Backupverzeichnis>_Systemumzug
```

## A system with a separate data partition no longer boots

A restore of the data partition is not necessary. Only the boot and system partition must be restored.

```
sudo raspiBackup -d /dev/sda -T "1 2"
```

If only a few changes have been made to the system partition, the `-00` option can also be used.


[.status]: translated
[.source]: https://linux-tips-and-tricks.de/de/konfigurationsbeispiele
[.source]: https://www.linux-tips-and-tricks.de/en/configuration-samples


