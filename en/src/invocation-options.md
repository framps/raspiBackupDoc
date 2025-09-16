<center>     <!-- The blank line before the image definition is required! -->

![Icon](images/icons/Icon_rot_blau_final_64.png)
</center>


# Invocation and options

*raspiBackup* must be invoked as user *root* or via `sudo`.

```
raspiBackup Option1 Option2 Option3 ... Backup directory
```

All options that switch something on or off can be activated or deactivated by
an appended ` ` or `-` when calling *raspiBackup*.

Example: The `-z` option and the `-z` option switch backup compression on.
The `-z-` option, on the other hand, switches backup compression off, regardless of
what is in the configuration file in the parameter `DEFAULT_ZIP_BACKUP`. This allows an
option can be switched off in the command line, although it is switched on in the
configuration file is switched on.

There are corresponding options in the configuration file for most call options
`/usr/local/etc/raspiBackup.conf`. In addition, other configuration files
can be used to selectively set or overwrite certain options.

<a name="configFiles"></a>
## Configuration files

<a name="configfiles"></a>
In addition to `/usr/local/etc/raspiBackup.conf`, there are other configuration files,
which are read if available. The options have the highest priority,
that are specified when the file is called.

The priority of the option sources can be seen in the following table:

| Priority | Source |
|-----------|--------|
| 1 | Invocation options |
| 2 | -f \<configFile\> |
| 3 | $(pwd)/.raspiBackup.conf |
| 4 | ~/.raspiBackup.conf |
| 5 | /usr/local/etc/raspiBackup.conf |

**Note:**
Options in the configuration file that require yes/on or no/off as parameters
must be 0 for no and 1 for yes.
No entry in the default column means the default is `""`

**Note:**
During a version upgrade, only the default configuration file
`/usr/local/etc/raspiBackup.conf` is updated with
updated with new configuration options. All other configuration files
may need to be updated manually.

There are various options for the backup and restore call:

1. Invocation options and their configuration option ([Backup](backup.md) / [Restore](restore.md)).
   The configuration options can be temporarily overwritten by the corresponding iinvocation options.
   overwritten by the corresponding call options
1. pure configuration options that cannot be overwritten by an invocation option
   ([Backup](backup-config-options.md) / [Restore](restore-config-options.md))
1. General invocation and configuration options for both the backup
   and restore ([call-options](general.md))

## Help text on the console

As long as you are on the console, a list of the available
available invocation options and their current status with the
options `-h` or `--help`.

## Thematic list of invocation options

A list of invocation options is also available [sorted by topic](options-by-topic.md).

[.status]: translated
