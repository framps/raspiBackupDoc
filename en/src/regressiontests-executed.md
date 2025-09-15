# Regression tests executed before a new release

Each new version of *raspiBackup* is subjected to a regression test before release.
regression test before release. Due to the many options and possible hardware and
hardware and software environments, a complete regression test is not possible.
possible. However, this ensures that the primary functionality
of *raspiBackup* to create a backup for the various backup types and modes
backup for the various backup types and modes is definitely successful. Also, all
new features, although they were of course already tested during development, are also
tested again.

The regression test is carried out in a virtualized environment on a Linux
desktop, in which a [Raspi per Qemu](https://linux-tips-and-tricks.de/de/raspberryd/22-wie-kann-man-raspberry-pi-unter-kvm-emulieren) is simulated.
(See [development-environment](development-environment.md).)

A *RaspbianOS Lite* is taken as the basis.
This is installed with the standard options of *raspiBackup* via
`dd`, `tar` and `rsync` in normal mode, both for a pure SD
card system as well as for a pure USB boot system. In addition, a `tar` and
`rsync` backup is created in partition-oriented mode.

Afterwards, all the respective backups are restored with *raspiBackup*, these
images are started via Qemu and the following tests are carried out:

  - `/boot/firmware/cmdline.txt` is downloaded from the VM via `scp` to the host and checked
  - `/etc/fstab` is downloaded from the VM to the host via `scp` and checked
  - IP address 8.8.8.8 is pinged in the VM and tested to see if the ping was successful
  - The number of active services of the original image is verified with `service --status-all`.

Every user of *raspiBackup* who uses additional options is strongly advised to
is strongly advised to carefully test backup and restore after a version upgrade of *raspiBackup*.
Restore again carefully. In this context, please refer to the
[disclaimer](introduction.md#disclaimer).


[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/509-raspibackup-ausgefuehrte-regressiontests
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/510-raspibackup-regressiontests-executed


