# Configuration update when upgrading to a new version

Whenever a *raspiBackup* version is upgraded,
immediately checks are executed whether the new version requires a new
configuration version. If so, the local configuration is automatically
merged with the new configuration in a new
configuration file of *raspiBackup*.
The following section describes in detail how this merging
is carried out.

**Note**:
If for some reason no configuration file update
has taken place during an upgrade, the update can be triggered manually with the following command:

```
sudo raspiBackup.sh --updateConfig
```

When merging the two configurations, *raspiBackup* writes
various information messages. The following messages are written
for example, when upgrading from *raspiBackup* 0.6.4.3 to *raspiBackup*
0.6.5 is upgraded.

```
--- RBK0241I: Current configuration v0.1.3 is merged with the new configuration v0.1.4 in /usr/local/etc/raspiBackup.conf.merged.
--- RBK0248I: Option DEFAULT_SMART_RECYCLE=0 was added.
--- RBK0248I: Option DEFAULT_SMART_RECYCLE_DRYRUN=1 was added.
--- RBK0248I: Option DEFAULT_SMART_RECYCLE_OPTIONS="7 4 12 1" has been added.
--- RBK0248I: Option DEFAULT_TELEGRAM_TOKEN="" has been added.
--- RBK0248I: Option DEFAULT_TELEGRAM_CHATID="" has been added.
--- RBK0248I: Option DEFAULT_TELEGRAM_NOTIFICATIONS="F" has been added.
--- RBK0248I: Option DEFAULT_NOTIFY_START=0 was added.
--- RBK0248I: Option DEFAULT_COLORING="CM" has been added.
--- RBK0243I: Configuration merge was successfully completed but not activated.
!!! RBK0245W: Should the current configuration in /usr/local/etc/raspiBackup.conf.bak be saved and the updated configuration activated? y/N
```

You can see that a new configuration file
`/usr/local/etc/raspiBackup.conf.merged` is created and in this file the
merge of the current configuration file
`/usr/local/etc/raspiBackup.conf` with the new configuration file
is carried out.

Which changes are made can be seen in the
messages `RBK0248I`. Finally, you will be asked whether the
merged configuration file should be activated. Of course
a backup of the existing configuration file in
`/usr/local/etc/raspiBackup.conf.bak ` beforehand. If you answer with "yes",
the configuration merge is completed and the following
messages:

```
--- RBK0240I: Current configuration /usr/local/etc/raspiBackup.conf is saved in /usr/local/etc/raspiBackup.conf.bak.
--- RBK0244I: Merged configuration /usr/local/etc/raspiBackup.conf.merged is copied to /usr/local/etc/raspiBackup.conf and activated.
```

This is the simplest method for updating the configuration file
and is done quickly.

However, you can also answer "no" and not activate the merged configuration file
immediately. You will then receive the following
message:
```
--- RBK0247I: Now check the merged configuration file /usr/local/etc/raspiBackup.conf.merged and copy it to /usr/local/etc/raspiBackup.conf to finish the configuration update.
```

Within the merged configuration file, the new options are
marked as follows and are therefore easy to recognize:

```
# Smart recycle
# >>>>> NEW OPTION added in config version "0.1.4" <<<<<
DEFAULT_SMART_RECYCLE=0
# Smart recycle dryrun
# >>>>> NEW OPTION added in config version "0.1.4" <<<<<
DEFAULT_SMART_RECYCLE_DRYRUN=1
# Smart recycle parameters (daily, weekly, monthly and yearly)
# >>>>> NEW OPTION added in config version "0.1.4" <<<<<
DEFAULT_SMART_RECYCLE_OPTIONS="7 4 12 1"`
```

You can now use an editor to manually view the merged
configuration file `/usr/local/etc/raspiBackup.conf.merged` manually with an editor,
and change it if necessary. Finally, the file for
activation file is copied to `/usr/local/etc/raspiBackup.conf`.

Finally, as always after an upgrade, it makes sense to perform a backup/restore
cycle to test whether everything still works as before.

*raspiBackup* also supports the use of [different
configuration files](invocation-options.md#configFiles). However, the automatic configuration upgrade is only
done for the standard configuration `/usr/local/etc/raspiBackup.conf`.
All other configuration files have to  be updated manually by
taking the configuration lines marked as new and
and copying them to the other configuration files.

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/567-raspibackup-konfigurationsupdate-nach-einem-upgrade-auf-eine-neue-version
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/570-raspibackup-configuration-update-when-upgrading-to-a-new-version



