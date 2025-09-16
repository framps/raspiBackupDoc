<center>     <!-- The blank line before the image definition is required! -->

![Icon](images/icons/Icon_rot_blau_final_64.png)
</center>


# Backup targets

*raspiBackup* mounts a backup partition in order to store the backups on it.
This means that any device from which a partition can be mounted under Linux can be used as a backup target,
can be used as a backup target.

This includes locally connected SD cards,
disks connected via USB, SSDs,
USB sticks and SD-USB adapters as well as NVMe SSDs.
Furthermore, [SMB](smb-as-backuptarget.md) and [NFS](nfs-as-backuptarget.md) can be used,
to connect non-locally connected backup partitions.
SSHFS, CurlFtpFS and [WebDAV](webdav-as-backuptarget.md) also work for storing backups on remote backups.
storage of backups on remote servers.
The [*AVM FRITZ!Box*](avm-fritzbox-as-backuptarget.md) also supports SMB and can therefore also be used as a backup target.
also be used as a backup target.

```admonish info title="Note"
The respective backup targets must have a formatted partition in which the backups are stored. See [Advantages and disadvantages of the respective
Filesystems](which-filesystem-can-be-used-on-the-backup-partition.md).
```

In addition to the following chapters, see also [How to access external data from the Raspberry Pi](https://linux-tips-and-tricks.de/de/13-raspberry/423-wie-kann-man-von-der-pi-unter-linux-auf-externe-daten-zugreifen).

[.status]: translated
