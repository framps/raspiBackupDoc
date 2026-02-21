# Introduction

A regular backup of Raspberry Pis is important in case of a
failure of the system storage device (SD card, USB disk, SSD, NVMe ...) or an
unintentional change that causes the system to no longer boot or to boot incorrectly,
to be able to recover and reset the system to a previous state.

*raspiBackup* creates a system backup of a Raspberry Pi **while the system is running**.
See also [Is a backup of a running system reliable? Shouldn't the entire system be stopped before the backup?](faq.md#faq1)
This can be done manually or automatically at regular intervals.
A backup always contains the entire system, i.e. system data and user data.
The system therefore reboots immediately once it has been restored.
A restore can always be performed completely. The [partition-oriented backup](normal-or-partition-backup.md#parititionBackup) also supports a complete partition wise restore. In addition, it supports a delta restore for the rsync backup type, i.e., only the changes since the last backup are reversed. This significantly reduces the restore time.

*dd*, *tar*, and *rsync* can be selected as Linux backup tools. In addition, *dd* and *tar* offer the option of reducing the size of backups. See [here for a description](backup-types.md) of the advantages and disadvantages of each tool, as well as a decision tree to help you choose the right backup type.

raspiBackup creates a new backup each time, providing a backup history that can be accessed at any time. This differs from existing clone backup tools, which only update the latest changes in the existing clone with rsync, meaning that only a backup of the latest status is available.
This means that the clone is created very fast. However, the rsync backup type also only backs up the latest changes and is therefore the fastest backup method of *raspiBackup*. This backup type should be used if backup speed is an important criterion.

If you want to take advantage of a backup history and an up-to-date clone, you can use one of the two extension scripts: raspiBackupRestore2Image or raspiBackupAndClone, which are described [here](https://framps.github.io/raspiBackupDoc/de/extension-scripts.html).

For **installation and configuration** of *raspiBackup* there is an
[installer](installation-in-5-minutes.md), with which the most important options of *raspiBackup* can be easily and quickly configured similar to `raspi-config`. More specific settings can be configured in a configuration file.

All functions and applications of *raspiBackup* are described in the first chapter
[Function overview](function-overview.md).


Further topics on this page:

<!-- toc -->


## Introductory video and Youtube channel

There is an [introductory video for raspiBackup](https://youtu.be/PuK_FNK674s) on Youtube.

Topics covered are

  * Introduction of *raspiBackup* with its most important features
  * Visit to the most important websites for *raspiBackup*
  * Introduction of *GitHub* as a question and problem interaction tool
  * Live installation of *raspiBackup* with the menu-driven installer

The slides used there can be downloaded for reading [here](https://raspibackup.linux-tips-and-tricks.de/wp-content/uploads/simple-file-list/raspiBackup_de.pdf).

Many more videos on all kinds of *raspiBackup* topics can be found in the [raspiBackup-Channel](https://www.youtube.com/@raspiBackup).

<a name="contact_options"></a>
## Contact options

* Click [![GitHub](images/icons/GitHub-Mark-32px.png)](https://github.com/framps/raspiBackup/issues),
  to create questions or problems about *raspiBackup* as "Issues" on *GitHub*.
  The issues can also be created in German.
  This way you can track questions and problem reports and receive a notification about answers.
  That's the preferred contact method.

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
Any other communication channels such as e-mails, which are unfortunately often used, will be ignored!
```

<a name="donation"></a>
## Donations

Acknowledgment of the development and maintenance effort as well as support for
*raspiBackup* is welcome and possible as follows:

1. Become a [*GitHub* sponsor](https://github.com/sponsors/framps) for *raspiBackup*
2. Paypal: The email `framp att linux-tips-and-tricks dott de` is known to PayPal
   and anyone with a PayPal account can tip this email.
3. Bitcoins: Address is `32MErztPzuKhN3YFEpmFtVLZTyxZ7zKPPt`
4. Neither: Just ask at the above eMail. There is
   certainly an alternative. For example, donations have been sent several times in the
   the good old way by letter :-)

The donation is primarily used to buy consumables such as SD cards, adapters, cables etc.,
needed for development and testing. If the donations are sufficient,
new hardware is also purchased in order to add the necessary hardware support into *raspiBackup*
and to verify the correct functionality on the new hardware.

## Acknowledgements

Over the years, many people from the community have contributed to *raspiBackup* through comments,
suggestions and beta and fixed tests to *raspiBackup*.
Due to the large number of contributors, it is unfortunately not possible to list every single one.

Therefore simply: Many thanks to all supporters!

**Special thanks** go to [simonz](https://github.com/rpi-simonz) for setting up
this *raspiBackup* documentation repository in *GitHub*, the transfer of all
*raspiBackup* pages from [framps Homepage](https://www.linux-tips-and-tricks.de)
to this repository and the intensive support during the revision of the pages
of the pages with help and advice as well as very helpful tools.

## License and *GitHub* link

The code of *raspiBackup* is available under the GPL on [*GitHub*](https://github.com/framps/raspiBackup).

<a name="disclaimer"></a>
## Disclaimer

*raspiBackup* was created for personal use and, as it proved to be very useful,
made available to the general public.

Correct functionality is tested as far as possible, but it cannot be ruled out that errors in 
**raspiBackup** may prevent the expected functionality from being guaranteed. 
Anyone who uses **raspiBackup** does so at their own risk.
The creator of *raspiBackup* is in no way liable for
any malfunction of the script.

[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup
[.source]: https://www.linux-tips-and-tricks.de/en/backup
[.source]: https://linux-tips-and-tricks.de/de/trinkgeld
[.status]: translated
