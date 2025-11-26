# Move the Raspberry operating system from SD card to SSD, USB disk or USB stick

*raspiBackup* is designed to restore a backup to the original device configuration.
device configuration. There are 3 possible scenarios:

1. `/boot` and `/` to SD card
2. `/boot` on SD card and `/` externally on an SSD, USB disk or USB stick
   (Older Rasperry, which cannot use USB boot mode) and is called hybrid boot mode
3. `/boot` and `/` on an SSD, USB disk or USB stick
   (USB boot mode on newer Raspberries)

*raspiBackup* can also be used to easily migrate from (1) to (2) or (3).

To do this, a backup is created with *raspiBackup* and then restored to the new device configuration.

The following restore command is required for (2) as the migration target:

```
sudo raspiBackup.sh -d <SD card> -R <USB device> <Backup>
```

For (3) the following command is required to restore:

```
sudo raspiBackup.sh -d <USB device> <Backup>
```

Where <USB device> can be an SSD, a USB disk or a USB stick


If you want to move to a large USB device, the option
`--resizeRootFS-` is useful, which does not expand the root partition, because then the rest of the
the rest of the USB device can be used for further partitions.

Details on the restore can be found in "[Restore/Restore](restore.md)".


[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/592-umziehen-des-raspberry-betriebssystems-von-sd-karte-auf-ssd-usb-platte-oder-usb-stick
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/593-migrate-the-raspberry-os-from-sd-card-to-ssd-usb-disk-or-usb-pen-drive

