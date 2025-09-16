<center>

![raspiBackup icon](images/icons/Icon_rot_blau_final_64.png)
</center>

# Supported hardware and software

*raspiBackup* is only supported on Raspberry Pi hardware with the *Raspberry Pi OS* and *Ubuntu*
is supported. However, it also runs successfully on other Raspberry Pi compatible hardware and
other Linux distributions successfully. It should be noted that *raspiBackup* uses the
requires the two partitions `/boot` and `/root` as they exist for *Raspberry Pi OS*.

This means that you can try out *raspiBackup* on the respective environment and if
it runs successfully, you can be happy and use it. But if it does not
runs or gives error messages, **no** support is given. You can create an
issue in *GitHub* and attach the debug log. This way *framp* can check whether the problem can be solved with
the problem can be solved with a few small changes. If larger changes are necessary,
these are not made and therefore *raspiBackup* cannot be used in the environment.
But even if a fix eliminates the problem, the environment remains unsupported.

In particular, any Linux OS can usually be used on any hardware,
to restore a backup. Here, too, the option `--unsupportedEnvironment` is necessary.
If there are problems, a Raspberry must be used for the restore.

Given the fact that *raspiBackup* **is for free**, it is too expensive/too complex for *framp*,

 1) Purchase all possible hardware for the tests
 1) Set up all possible hardware and software test combinations
 1) Test everything for each new release

So *framp* can only support *raspiBackup* under the above conditions.

There is the possibility of [Donation](introduction.md#donation)
and depending on the effort involved, there is a chance that further
environments will be supported by *raspiBackup* in the future.

When called, *raspiBackup* checks whether supported hardware and software is available
and terminates itself if not. With the option `--unsupportedEnvironment` this check is
not carried out and may lead to errors and program aborts.

## Raspberry Pi OS (RaspbianOS) Lite and Desktop

Both *Raspberry Pi OS* (formerly *RaspbianOS*) *Lite* and *Desktop* are
are supported by *raspiBackup*.
The desktop version should be used at least on a RPi4/RPi5 with 4GB memory.

## Ubuntu

If the official Ubuntu version for Raspberries is used, this is
is supported by *raspiBackup*. However, at least a Raspberry Pi 4 with 4GB, better still
with 8GB memory, should be used. The same applies to a Raspberry Pi 5. Presumably
the requirements for an Ubuntu server system are lower.

## Raspberry Pi Compute Module (CM)

*raspiBackup* supports Raspberry Pi compute modules
with an SD card, eMMC memory and NVMe.

How to make CM4 NVMe devices available on Linux to restore an NVMe backup from *raspiBackup*,
is described on the [English page](https://www.linux-tips-and-tricks.de/en/raspberrye/614-raspberry-compute-module-4-setup-guide).

## Supported devices

*raspiBackup* supports the following devices and storages

  - SD cards
  - Disks/HDDs
  - SSDs
  - USB sticks
  - USB SD adapters
  - eMMC memory
  - NVMe storage

In principle, anything can be used as a backup target for the backups,
that can be mounted under Linux. This includes

  - SMB network drives
  - NFS network drives
  - SSHFS network drives
  - WebDAV network drives
  - FtpFS network drives

Examples for SMB, NFS and WebDAV configuration can be found on [backup-targets](backup-targets.md).

[.source]: https://linux-tips-and-tricks.de/de/raspibackupcategoried/608-unterstuetzte-hard-und-software/
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/609-supported-hard-and-software/
[.status]: translated


