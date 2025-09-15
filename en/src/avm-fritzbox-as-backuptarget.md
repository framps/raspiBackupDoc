# AVM FRITZ!Box as backup target

If you don't have a NAS, but would like to back up your Raspberries with *raspiBackup*,
can of course also use the NAS storage of a Fritzbox. However, you must
backup type tar must be used for this, as the SMB protocol used does not support
hardlinks and therefore no rsync backup type can be used,
which provides incremental backups.

An [article from andwil.de](https://www.andwil.de/weblog/linux-fritznas-mounten-cifs) was very helpful for using a Fritzbox for this purpose.
It explains very nicely what needs to be configured on the Fritzbox side and the Raspberry side.

Here is an example line in the /etc/fstab:

```
//192.168.0.1/FRITZ.NAS/USB-Sandisk3-2Gen1-01 /backup cifs noauto,user,vers=3.0,credentials=/home/pi/.smbcredentials,noserverino,uid=1000,gid=1000 0 0
```

In addition, with
```
chmod 600 ~/.smbcredentials
```

to ensure that the Fritzbox access data can only be read by the user.
user. This is not absolutely necessary with the Raspberry, where normally only one user
works on it, this is not absolutely necessary. But it is good practice to always make access data
can only be read and changed by the respective user.

Then a backup with
```
sudo raspiBackup -t tar
```
can be created.

After the restoretest was successful, the backup type must be configured to tar in the installer
to tar in the installer and specify the time of the regular backup.

[.status]: translated

