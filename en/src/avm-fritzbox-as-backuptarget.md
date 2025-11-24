# AVM FRITZ!Box as backup target

If you don't have a NAS, but would like to back up your Raspberries with *raspiBackup*,
you can of course also use the NAS storage of a Fritzbox. However, you have to
use backup type tar for this, as the SMB protocol does not support
hardlinks and therefore no rsync backup
which provides incremental backups can be used.

An [article from andwil.de](https://www.andwil.de/weblog/linux-fritznas-mounten-cifs) was very helpful for using a Fritzbox for this purpose.
It explains very nicely what needs to be configured on the Fritzbox side and the Raspberry side.

Here is an example line in the /etc/fstab:

```
//192.168.0.1/FRITZ.NAS/USB-Sandisk3-2Gen1-01 /backup cifs noauto,user,vers=3.0,credentials=/home/pi/.smbcredentials,noserverino,uid=1000,gid=1000 0 0
```

In addition
```
chmod 600 ~/.smbcredentials
```

ensures that the Fritzbox access data can only be read by the user.
This is not absolutely necessary with the Raspberry, where normally only one user
works on it. But it is good practice to always make sure data
can only be read and changed by the respective user.

Then a backup with
```
sudo raspiBackup -t tar
```
can be created.

After the restoretest was successful, the backup type should be configured to tar in the installer
and the time of the regular backup configured.

[.status]: translated

