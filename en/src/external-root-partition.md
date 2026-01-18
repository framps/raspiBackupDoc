# Is an external root partition supported (hybrid boot mode)?

Older Raspberries that do not yet support USB boot mode,
can be configured in such a way that only the boot partition
is stored on the SD card
and the root file system on an external USB disk.

*raspiBackup* supports external root partitions and
an external root partition is also backed up.

In normal backup mode, the two Raspberry Pi OS partitions
`/boot` and `/root` of the system device are normally backed up. However, if the root partition
to an external
partition (USB stick, USB disk, ...), this external partition is backed up as well as the boot
partition and the boot partition from the SD card are backed up. If
this backup is restored, the [option `-R`](restore-options.md#parm_R) must be used,
to specify the target device for the external root partition required in hybrid boot mode.

[.status]: translated


