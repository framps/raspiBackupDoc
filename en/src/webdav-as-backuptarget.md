# WebDAV as backup destination

For *raspiBackup*, **davfs** must be used because it mounts the *WebDAV* drive in the same way
as it is done for all other drives in Linux.
It can then be accessed both via the command line and with a file manager.
Other tools for accessing WebDAV cannot be used.

## Installation of davfs2

```
sudo apt install davfs2
```

## Create the mountpoint

```
sudo mkdir -p /remote/webdav
```

## Define the access data

   - `/etc/davfs2/secrets`

     ```
     /remote/webdav <userid> <password>
     ```

## Make access data readable only for the user pi

```
sudo chmod 600 /etc/davfs2/secrets
sudo chown root:root /etc/davfs2/secrets
```


## Create entries in /etc/fstab

```
# t-online
https://webdav.mediencenter.t-online.de        /remote/webdav   davfs   rw,noauto,user  0       0 
# 1&1
https://sd2dav.1und1.de          /remote/webdav   davfs   rw,noauto,user  0       0
# ownCloud
https://cloud/owncloud/remote.php/webdav          /remote/webdav   davfs   rw,noauto,user  0       0
# seafile
https://seafile/seafdav       /remote/webdav  davfs   rw,noauto,user  0       0
```

Since *davfs* stores the program for mounting in `/usr/sbin/mount.davfs`,
mount` expects it in `/sbin`, you have to set up the following link:

```
sudo ln -s /usr/sbin/mount.davfs /sbin/mount.davfs
```

Due to an error in the WebDAV implementation at *t-online* no files can be created.
The message always appears that the file
exists - although it does not. Therefore, the
`/etc/davfs2/davfs2.conf` the following line must be inserted,
to switch off the locks.

```
use_locks 0
```

If you want to mount the disk space automatically when booting the system
the `noauto` in the `/etc/fstab` must be removed. This is for
**raspiBackup** if the `dynamicmount` option is used.

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/12-networking/190-wie-kann-man-medienspeicher-oder-smartdrive-unter-linux-einbinden>
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/644-nutzung-von-webdav-als-backupziel-fuer-raspibackup>1
