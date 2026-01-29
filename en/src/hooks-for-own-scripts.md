# Extensionpoints

It is possible to integrate your own code extensions before and after the
back-up process of the script. This is useful if
changes are actually necessary in the backup script, but which then have to be
would have to be updated again after each update of *raspiBackup* to a new version.
version. The extensions are independent of the
version of *raspiBackup* and are therefore recommended in this case.

[Example extensions](https://github.com/framps/raspiBackup/tree/master/extensions)
are available and can be used as a template for your own extensions.
The CPU temperature as well as the main memory and backup partition
memory and backup partition allocation as well as the partition allocation before
and after the backup.
The last extension is only called up at the end of the backup and can be used if the backup is successful
and can trigger different actions if the backup is successful or unsuccessful.

Anyone who has created useful extensions for the community is welcome to post them in the
German [Raspberry Pi Forum](https://forum-raspberrypi.de/forum/board/164-raspibackup/) and name the download location.
If extension features are missing, please create an [Issue at *GitHub*](https://github.com/framps/raspiBackup/issues).

In addition, there are interesting extensions provided by
[*raspiBackup* users written extensions](https://github.com/framps/raspiBackup/tree/master/extensions_userprovided).


### Extension invocation locations during backup

The extensions are called at the following points in the backup process
are called:

  - eMail extension (mem)
  - Notification extension (notify), if activated (DEFAULT_NOTIFY_START)
  - Slack*, *Pushover* and *Telegram* notifications, if configured and if
    switched on (DEFAULT_NOTIFY_START)
  - BEFORE_STOPSERVICES (defined commands are executed)
  - STOP_SERVICES (defined commands are executed)
  - PRE_BACKUP_EXTENSION
  - READY_BACKUP_EXTENSION

... Creating the backup ...

  - POST_BACKUP_EXTENSION
  - START_SERVICES (defined commands are executed)
  - AFTER_STARTSERVICES (Defined commands are executed)

... Cleanup tasks, such as deleting obsolete backups (may take longer) ...

  - FINAL_COMMANDS (from release 0.6.8) (defined commands are executed)
  - eMail (mail) plugin
  - Notification (notify) plugin
  - *Slack*, *Pushover* and *Telegram* notifications if configured

... Final housekeeping ...

  - Exit



### Extension invocation positions during restore

The various extensions are called at the following points in the restore process
are called:

  - PRE_RESTORE_EXTENSION

... restore the backup ...

  - POST_RESTORE_EXTENSION
 

### Example extensions

1. The easiest way is to install and activate the sample extensions with the [Installer](https://www.linux-tips-and-tricks.de/de/installation).
    and activate them. Either via the menu sequence
    **Install components-\>Install sample extensions** or
    directly via the command line with the `-e` option.

    ```
    raspiBackupInstallUI.sh
    ```

    or
    ```
    raspiBackupInstallUI.sh -e
    ```

2. If you want to install the sample extensions manually, you can download the `tgz` file with
    [this link](https://www.linux-tips-and-tricks.de/raspiBackupSampleExtensions.tgz) with a browser
    or download it directly to the Raspberry as follows and copy it to
    `/usr/local/bin`:

    ```
    wget http://www.linux-tips-and-tricks.de/raspiBackupSampleExtensions.tgz -O raspiBackupSampleExtensions.tgz
    tar -xzf raspiBackupSampleExtensions.tgz -C /usr/local/bin
    ```

This will copy the following scripts to `/usr/local/bin`:

1. `raspiBackup_mem_pre.sh` and `raspiBackup_mem_post.sh` -
   Reports memory usage of the Raspberry before and after the backup

2. `raspiBackup_temp_pre.sh` and `raspiBackup_temp_post.sh` - Reports the CPU temperature of the Raspberry.
   Reports the CPU temperature of the Raspberry before and after the backup

3. `raspiBackup_disk_pre.sh` and `raspiBackup_disk_post.sh` - reports the disk usage before and after the backup.
   Reports the disk usage before and after the backup

4. `raspiBackup_execute_post.sh` - Is called at the end of the backup.
   Helpful if you want to use your own success/error notification function
   is to be used.


To activate the extension, the following additional
invocation parameter for *raspiBackup* is necessary:

```
-N "temp mem disk execute"
```

or add the following line to the configuration file

```
DEFAULT_EXTENSIONS="temp mem disk execute"
```

### Notification extension

For notifications via *Slack*, *Pushover* and *Telegram* no extensions need to be
written. It is sufficient to configure the notifications in *raspiBackup*.
If you want to supply other notification targets, you can do this in a script
with the name `raspiBackup_notify.sh`.

### Example extensions

The following extensions can have a *pre* and/or *post* script and
must be called `raspiBackup_<extension>_pre.sh` and/or
`raspiBackup_<extension>_post.sh`.

  1. temp
  2. mem
  3. disk

All other extensions must not have `_pre` and `_post` at the end.

The extensions generate the following messages:

```
--- RBK1001I: Memory usage - Pre backup - Used: 97 MB Free: 130 MB - Post backup - Used: 98 MB Free: 121 MB
--- RBK1000I: CPU temperature pre and post backup: 53.2'C - 55.8'C
--- RBK1002I: Disk usage pre backup: Used: 1.30 TiB Free: 2.18 TiB
--- RBK1003I: Disk usage post backup: Used: 1.30 TiB Free: 2.18 TiB
--- RBK1004I: Free change: -256.00 KiB (0.00 %)
```

### Messages

The example extensions use messages that start from the number range 1000
such as RBK1000I. If you create your own extensions, you should
write messages, they should start at 2000 and not use the range below
1999.

### Interface

An extension receives current status code of *raspiBackup*
in as parameter. A status code of 0 in the poster extensions means: the backup
was successful. Any other status code means that the backup
was unsuccessfull.

### eMailExtension

If you want to program the sending of emails yourself, you can use the email extension.
This is particularly helpful if the email programs supported by the script do not support your own email client.
In addition, the appearance of the email can be changed as desired.
An extension that uses `mailx` can be found in the example extensions.

The following parameters are passed to the e-mail extension:

```
email="$1" # target email address
subject="$2" # email subject
content="$3" # email contents
parms="$4" # addtl email parms passed with -E
append="$5" # file to append
```

### Hints

- **Attention:** The extensions run with **root** rights and can therefore
  damage or even destroy the running system in case of errors!

- Both scripts (`pre` and `post`) are not necessary.
  One is sufficient.

- The parameter `-F` is very helpful for testing extensions.
  This means that the actual backup process is skipped and the
  script run very quickly.

- The extensions are called in the scope of *raspiBackup*. Therefore there is access
  to its internal script variables. However, this is strongly discouraged,
  as the internals can change at any time. For this reason, it is also
  advisable to provide your own variables with an extension-specific prefix,
  to avoid possible conflicts with variable names used by *raspiBackup*.

- If you would like to share your extension code, you are welcome to create a pull request on [*GitHub*](https://github.com/framps/raspiBackup).
  There, all extensions are available in source code to extend them and
  add new ones.

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/442-raspibackup-erweiterungen
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/443-raspibackup-extensions


