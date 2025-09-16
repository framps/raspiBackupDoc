
<center>     <!-- The blank line before the image definition is required! -->

![Icon](images/icons/Icon_rot_blau_final_128.png)
</center>

``` admonish info title="Usage hints"
At the top of the pages there are two groups of icons for operating
the documentation:

![Menu-left](images/mdbook-icons-left.png)

  - Show/hide a table of contents
  - Selection of a theme
  - Search function

![Menü-right](images/mdbook-icons-right.png)

  - Language selection (German/English)
  - Print
  - *GitHub* page of the documentation project
  - Suggest changes to the current page in *GitHub

Typing a `?` displays a small keyboard navigation aid.
```

``` admonish info title="Note"
To reduce the translation effort given the amount of documentation pages all German pages were
translated with [DeepL](https://www.deepl.com) into English.
Thank you very much to DeepL who offer to use the translator for free.
```

---

Topics on this page:

<!-- toc -->

---

# Introduction

A regular backup of Raspberry Pis is important in the event of a system
failure of the system storage device (SD card, USB disk, SSD, NVMe ...) or also of
unintentional changes that cause the system to no longer boot or to boot incorrectly,
to be able to reset the system to a previous state.

*raspiBackup* creates a system backup of a Raspberry Pi **while the system is running**.
This can be done manually or automatically at regular intervals.
A backup always contains the entire system, i.e. system data and user data.
The system therefore reboots immediately once it has been restored.

Backups can be saved to all devices that can be mounted on Linux.
be backed up. This includes SD cards, USB sticks, USB disks, SSDs and NVMe SSDs.
Even network drives that are mounted via NFS, SMB, SSHFS, FtpFS and WebDAV,
can also be used as a target for backups.

A backup can be restored to devices other than the device from which the backup was created.
from which a backup was created. For example, a backup of an SD card can be restored to
be restored to an SSD.

The number of backups to be kept can be configured or the
[grandfather-father-son generation principle](https://www.framp.de/raspiBackupDoc/de/smart-recycle.md) be used.
In addition, so-called *raspiBackup* [snapshots](snapshots.md) can be created manually. These are backups that
are not deleted automatically and are used to save intermediate steps during system upgrades
to be able to go back to previous versions at any time in the event of errors during the upgrade.

There exist [Backupmodes](normal-or-partition-backup.md):
The **normal backup mode** only backs up the boot and root partition.
The **partition-oriented mode** backs up any number of partitions.

The following Linux backup tools can be used:
`dd`and `tar`, both also zipped, which always create a full backup
and `rsync` with [hardlink usage](how-do-hardlinks-work-with-rsync.md),
to create a delta backup relatively quickly.
The individual backup types are described in detail [here](backup-types.md).
There is also a [decision tree](backup-types.md#decisiontree),
to quickly find the right backup type.

For **installation and configuration** of *raspiBackup* there is an
[installer](installation-in-5-minutes.md), with which the most important options of *raspiBackup* can be
options of *raspiBackup*, comparable to `raspi-config`.
More specific settings can be made in a configuration file.

For developers, *raspiBackup* offers various [extension points](hooks-for-own-scripts.md),
to execute your own code.

There are also various [Scripts](https://github.com/framps/raspiBackup/tree/master/helper),
that extend the functionality of *raspiBackup* and can either be used unchanged
or can be adapted to your own requirements.

At the end of a backup run, *raspiBackup* can, if desired, send a notification by email,
*Telegram*, *Slack* or *Pushover*.

All functions and application areas of *raspiBackup* are listed in table form in the
[function overview](function-overview.md).

## Introductory video and YouTube channel

There is an [introductory video for raspiBackup](https://youtu.be/PuK_FNK674s) on Youtube.

Topics covered are

  * Introduction of *raspiBackup* with its most important features
  * Visit to the most important websites for *raspiBackup*
  * Introduction of *GitHub* as a question and problem interaction tool
  * Live installation of *raspiBackup* with the menu-driven installer

The slides used there can be read [here](https://raspibackup.linux-tips-and-tricks.de/wp-content/uploads/simple-file-list/raspiBackup_de.pdf).

Many more videos on all kinds of topics related to *raspiBackup* can be found in the [raspiBackup-Channel](https://www.youtube.com/@raspiBackup).

<a name="kontakt"></a>
## Contact options

* Click [![GitHub](images/icons/GitHub-Mark-32px.png)](https://github.com/framps/raspiBackup/issues),
  to create questions or problems about *raspiBackup* as "Issues" on *GitHub*.
  The issues can also be created in German.
  This allows you to track questions and problem reports and receive notifications of answers.

* Click [![Facebook](images/icons/FB-f-Logo__blue_29.png)](https://www.facebook.com/raspiBackup/),
  to find out about current activities and peripheral information about *raspiBackup* on Facebook.
  Questions about *raspiBackup* are also possible. Please only report problems in [*GitHub*](https://github.com/framps/raspiBackup/issues).

* Click [![Twitter](images/icons/Twitter-f-Logo__blue_29.png)](https://www.twitter.com/linuxframp),
  to follow *raspiBackup* on Twitter.

* Click [![RaspberryForum](images/icons/RaspberryForumSmall.png)](https://forum-raspberrypi.de/forum/board/153-backup/),
  to ask questions about Raspberry backups in general and *raspiBackup* in particular or to read existing threads about *raspiBackup* in the German RaspberryForum.

* Click [![Reddit](images/icons/reddit-icon.png)](https://www.reddit.com/r/raspiBackup/),
  to follow *raspiBackup* on Reddit.

``` admonish info title="Note"
All other communication channels such as e-mails, which are unfortunately often used, are ignored!
```

<a name="donation"></a>
## Donations

Acknowledgment of the development and maintenance effort as well as support for
*raspiBackup* is welcome and possible as follows:

1. Become a [*GitHub* sponsor](https://github.com/sponsors/framps) for *raspiBackup*
2. Paypal: The email `framp att linux-tips-and-tricks dott de` is known to PayPal
   and anyone with a PayPal account can tip to this email.
3. Neither: Just ask at the above eMail. There is
   certainly an alternative. For example, tips have been sent several times in the
   the good old way by letter :-)

The tip is primarily used to buy consumables such as SD cards, adapters, cables etc.,
needed for development and testing. If the tip is sufficient,
new hardware is also purchased in order to build the necessary hardware support into *raspiBackup
hardware support in *raspiBackup* and to verify the correct functionality
on the new hardware.

## Acknowledgements

Over the years, many people from the community have contributed to *raspiBackup* through comments,
suggestions and beta and fixed tests to *raspiBackup*.
In view of the large number, it is unfortunately not possible to list every single one.

Therefore simply: Many thanks to all supporters!

**Special thanks** go to [simonz](https://github.com/rpi-simonz) for setting up
this *raspiBackup* documentation repository in *GitHub*, the transfer of all
*raspiBackup* pages from [framps Homepage](https://www.linux-tips-and-tricks.de)
to this repository and the intensive support with the revision of the pages
of the pages with help and advice as well as very helpful tools.

## License and *GitHub* link

The code of *raspiBackup* is available under the GPL on [*GitHub*](https://github.com/framps/raspiBackup).

## Disclaimer

*raspiBackup* was created for personal use and, as it proved to be very useful,
made available to the general public.

The correct functionality is tested as far as possible
but it cannot be ruled out that errors in
*raspiBackup* the expected functionality is not guaranteed.
Anyone using *raspiBackup* does so at their own risk.

The creator of *raspiBackup* is in no way liable for
any malfunction of the script.

[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup
[.source]: https://www.linux-tips-and-tricks.de/en/backup
[.source]: https://linux-tips-and-tricks.de/de/trinkgeld
[.status]: translated
