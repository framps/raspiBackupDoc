
``` admonish info title="Work in progress"
This documentation is being built with new tools on a new platform...

Initially by copying the original text from framp's website.

Currently the structure isn't finalized and most pages are empty or "broken",
especially regarding links and formatting.
The German version is more complete yet.

That means: For now it's **work in progress**.

There are two language versions, *german* and *english*.
Dynamically selectable with the language selector on the top right.
```

# Introduction

> raspiBackup - Create backup versions of your Raspberry Pis regularly/automatically.

A regular backup of your Raspberry Pis is important. In case of a failure of the system device
(SD Card, USB disk, USB flash drive, SSD, NVMe ...) or unintended updates which cause the system either
not to boot any more or boot with errors this backup enables you to restore a previous functional backup.

*raspiBackup* creates a backup of Raspberry Pis **from a running system**.
You can either start the backup manually or have the backups be started automatically with systemd or crontab.
Optionally you can let you notified about the backup result with eMail, Pushover, Slack or Telegram.

Backups can be saved ony an partition which can be mounted on a Linux system
(USB flash drive, USB disk, SSD, NVMe, NFS, SMB, SSHFS, WebDAV etc).

There exist two backup modes: The **normal backup mode** just saves the boot and root parition. If additional partitions should be saved, for example a 3rd data only partition, the **partition oriented mode** has to be used.

If you own an Synology or another NAS device see [here](backup-targets.md) for configuration hints.

Linux backuptools `dd` backup, `tar` backup, (both backups can also be zipped) and a `rsync` backup
with hardlink usage to create a delta backup can be used.
For details about the different backup methods see [here](backup-types.md).
There you will find a decision tree to decide which backup methods is the right one to use.

To **install and configure** raspiBackup there exists an installer similar to raspi-config, which allows menuedriven, simple and fast to configure raspiBackup with it's most important options to use raspiBackup.
All more sophisticated options have to be configured in a configuration file.

raspiBackup also **restores** a backup [Restore](restore.md).

All functions and usage scenarios of *raspiBackup* are listed in
[Functionoverview](function-overview.md)..

---

For additional chapters see here:

<!-- toc -->

---

## Supported hard- and software

See [Supported hard- and software](supported-hardware-and-software.md)

## Stop and start of services

To get a consistent backup of a running system all services which keep important information in memory have to be stopped before a backup starts and should be started when the backup finishes,

The required commands can be specified in the configuration file. The raspiBackup installer allows to select systemd services to be stopped and started and no configuration file update is required.

## Extensionpoints

There exist [extensionpoints](hooks-for-own-scripts.md) for plugins in *raspiBackup*, to hock in any additonal custom logic at different points of the backup and restore processing.

## Optionally external root partition

If an old Raspberry should be seaved which doesn't support USB boot an external root partition referred by
the SD boot partition will be saved also.

There exists the normal backup mode which just saves
/boot and /root. Partition oriented mode saves any number of partitions starting with release 0.6.6.

## Introduction video on Youtube-Channel

There exists a [Introductional video for raspiBackup](https://youtu.be/PuK_FNK674s) on Youtube.

Topics are

  * Present *raspiBackup* with its features
  * Present the most important webpages about *raspiBackup*
  * Introduction of *GitHub* as a question and problemreporting tools
  * Liveinstallation of *raspiBackup* with the menuedriven installer

All slides used in the videos can be downloaded from [hier](https://www.linux-tips-and-tricks.de/de/downloads/raspibackup-de-pdf/download).

A lot of additional videos about various features of *raspiBackup* are available in the [raspiBackup-Channel](https://www.youtube.com/@raspiBackup).

<a name="kontakt"></a>
## Contact

* Click [![Github questions](images/icons/GitHub-Mark-32px.png)](https://github.com/framps/raspiBackup/discussions)
or [![Github issues](https://github.com/framps/raspiBackup/issues)
   to ask questions or report issues for *raspiBackup*.
   That's my preference to get in contact.

* Click [![Facebook](images/icons/FB-f-Logo__blue_29.png)](https://www.facebook.com/raspiBackup/),
  to follow *raspiBackup* on facebook

* Click [![Twitter](images/icons/Twitter-f-Logo__blue_29.png)](https://www.twitter.com/linuxframp),
  to follow *raspiBackup* on twitter

* Click [![Youtube](images/icons/Youtube.png)](https://www.youtube.com/channel/UCnFHtfMXVpWy6mzMazqyINg),
  to visit the *raspiBackup* channel on Youtube

* Click [![RaspberryForum](images/icons/RaspberryForumSmall.png)](https://forum-raspberrypi.de/forum/board/153-backup/),
  to ask questions in the German Raspberry forum. If you're not a native German speaker you can post your question in English if you like.

* Click [![Reddit](images/icons/reddit-icon.png)](https://www.reddit.com/r/raspiBackup/),
  to follow *raspiBackup* on Reddit.

``` admonish info title="Hinweis"
Any other communication channels like eMail which is quite prominent will be discarded silently.
```

## Donations

Any recognition of raspiBackup development- and maintenance effort and any support is greatly appreciated. There exist following donation alternatives:

1) Become a [*GitHub* sponsor](https://github.com/sponsors/framps)
2) Paypal: The eMail `framp att linux-tips-and-tricks dott de` is known by PayPal and everybody who owns a Paypal account can donate to this eMail.
3) Neither one: Just contact me via eMail mentioned above and we will find a solution. For example I already received multiple times donations in a good old postal letter :-)

## Credits

raspiBackup wouldn't have the features and quality without folks from the community who asked for features and helped to test new features
and created PRs to add new featutures. Ths list will be very long and I was very busy to update the list in the past. I finally stopped to publish and update the list.

Thank you very much to everybody who helped to improve raspiBackup !

## License and *GitHub* link

The code of *raspiBackup* is pure bash code and is available under the GPL license on [*GitHub*](https://github.com/framps/raspiBackup).

## Disclaimer

This backupscript *raspiBackup* was initally created for personal use only.
But it's very useful and therefore was published for general use.
It's seriously tested but it's not possible to guarantee the script works as expected in all possible environments.
Everybody uses this script on his own risk. The creator of this script is not liable in any case for any malfunction.

[.de]: ../../de/src/introduction.md
[.source]: https://www.linux-tips-and-tricks.de/en/backup
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup
[.source]: https://linux-tips-and-tricks.de/de/trinkgeld
[.status]: rst
