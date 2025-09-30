# 10 years *raspiBackup* (Retrospective by framp)

Today (August 07, 2023) 10 years ago the first version of *raspiBackup*
was stored in my local cvs.

```
revision 1.1
date: 2013-08-07 21:28:14 0200; author: framp; state: Exp; commitid: 10052029FC71A98602F;
Initial version
=============================================================================
```

Unfortunately, this cvs no longer exists, because it would be interesting to see
how the script has changed over the last 10 years. Initially t had about 50
lines of code. Now there are 8000 lines of code.

In the [wayback machine](https://web.archive.org/) I found an initial version of *raspiBackup* on this website 6/2013.
initial version of *raspiBackup*. I put it on my website as [raspiBackup_201306.sh](https://www.linux-tips-and-tricks.de/raspiBackup/raspiBackup_201306.sh).
It was not 50 but 314 lines of code.

My son gave me a Raspberry for Christmas 2013. I enthusiastically started
working with it and quickly added a second Raspberry, which was then
used in production. As SD cards unfortunately only have a limited
ilife time, *raspiBackup* was created. At first it was only used privately - but
but after it did its job very well, it was made available to the community.

I had underestimated the amount of work involved: there is a difference
between writing and using a small script yourself and having it used by other users.
A lot of tests for incorrect input and system
and system environments had to be added. Corresponding error messages also had to be
written. As the error messages are only short,
various websites were created in parallel, on which the functionality of
*raspiBackup*, as well as more detailed descriptions of the error messages and
how the errors can be corrected. 

The installer was then created to simplify the initial installation. Soon
friends of *raspiBackup* were also found who helped to add language support for
Finnish, Chinese and French in addition to German and English.

There was a lot of feedback and suggestions from *raspiBackup* users on what else would be
useful features in *raspiBackup*. Without these suggestions from
*raspiBackup* users, *raspiBackup* would still have the initial functionality
that I need @home. There were and are many helpers. Initially
I once maintained a website on which all helpers were listed.
At some point it just became too much and I took the website off the net.

Thanks to this help, *raspiBackup* has continued to develop over the last 10 years.
in its range of functions. At first, all feedback came via the
comment function on [my website](https://www.linux-tips-and-tricks.de). However, this proved to be very
cumbersome and eventually the cvs code was moved to *GitHub*. This
simplified the creation of feature requests considerably. In addition
reporting bugs and questions about *raspiBackup* usage
is much easier.

Relatively quickly, I then registered in the [German Raspberry Forum](https://forum-raspberrypi.de/forum/).
The members there helped me a lot to get to know my Raspberry
and how to use it. At some point I then asked whether it wouldn't make sense to create a backup
subforum, which was then done. Since then I have been helping in the subforum
for questions about *raspiBackup*.

I don't really think much of videos, but prefer textual descriptions
descriptions, because you can search in them. But in the boring Corona period
I did create various videos about *raspiBackup* and published them on
[Youtube](https://www.youtube.com/channel/UCnFHtfMXVpWy6mzMazqyINg).
I didn't put much effort into it - in contrast to
other people who publish very fancy videos on Youtube: A few slides
and then I explained them in presentation mode. Later I
added videos with practical use of *raspiBackup* on the command line.
But the number of people watching the videos
is growing. So the effort was not useless.

Franjo from Raspberryforum wrote a small tool called [raspiBackupDialog](https://github.com/framps/raspiBackup/blob/master/helper/raspiBackupDialog.sh), with which the backup and restore with
*raspiBackup* can be done dialog guided.

At some point I also created a [Facebook group for *raspiBackup*](https://www.facebook.com/raspiBackup). Initially
users could contact me directly. But that became
too much for me at some point, as it eventually led to an unpaid 7/24
hotline support for *raspiBackup*.

Finally I set up a Paypal account to which everyone can pay if he 
likes *raspiBackup* [can donate](introduction.md#donation). Furthermore
anyone can donate as a [sponsor](https://github.com/sponsors/framps) via *GitHub*.

Of course, this won't make me rich, but it is a recognizable acknowledgement of the work,
that I put into *raspiBackup* development and support.

I can also use it to buy test hardware, because
I cannot and will not shut down my productive systems to test and maintain *raspiBackup*.
In addition, I am no longer prepared to invest a cent
in required HW for *raspiBackup*. *raspiBackup* is available for free
and users should show their appreciation and finance the required HW through donations.

For example, a user donated a CM4 so that I iwas able to add and test NVMe support in *raspiBackup*.

From the general small donations I was able to purchase an RPi4 with 8GB memory and add Ubuntu support in *raspiBackup*.

Finally, someone donated so that I could buy an RPi5. The donation was made because there was a
problem with [rpi-clone](https://github.com/geerlingguy/rpi-clone) that could not be reproduced on an RPi4.
So then I was finally able to reproduce and fix the intermittent problem on the RPi5.
(*rpi-clone* is a useful clone tool - not a backup tool like *raspiBackup*, but often requested,
which I also keep an eye on).

In May 2025, [simonz](https://github.com/rpi-simonz/) put a lot of effort and energy into a new git repository [raspiBackupDoc](https://github.com/framps/raspiBackupDoc),
to bring the previous documentation of *raspiBackup* on my website into this repository
and to improve the documentation significantly. All tooling as well as the transfer and
customization from my web pages into this repository is due to him. This repository and the generated
[raspiBackup documentation](https://framps.github.io/raspiBackupDoc) will replace the documentation on my website in the future.

In addition, many [small scripts](https://github.com/framps/raspiBackup/tree/master/scripts) were created to support the use of *raspiBackup*.

Herewith I give out a virtual round of free beer to celebrate the day.

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/649-10-jahre-raspibackup
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/657-10-years-raspibackup


