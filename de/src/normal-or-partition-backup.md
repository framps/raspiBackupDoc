# Vergleich partitionsorientierter Backup und normaler Backup

Es existieren zwei Backupmodi:

1. Normaler Backup

   In diesem Modus werden die ersten zwei Partitionen (die Bootpartition und die
   Rootpartition) der SD-Karte gesichert. Außerdem wird beim `tar` und `rsync` Backup
   auch eine externe Rootpartition, d.h. eine auf einen USB Stick oder USB Platte
   ausgelagerte Rootpartition, gesichert.
   Falls das Zielgerät beim Restore größer ist als das Quellgerät,
   wird automatisch die zweite Partition entsprechend erweitert.

   Mit dem `dd` Backup kann auch die gesamte SD-Karte gesichert werden.
   Es wird aber dringend davon abgeraten, ein `dd` Backup zu nutzen.
   Siehe: [Warum sollte man dd als Backuptyp besser nicht benutzen?](why-shouldn-t-you-use-dd-as-backup-type.md)

2. Partitionsorientierter Backup

   In diesem Modus wird jede auf dem System befindliche oder eine bestimmte ausgewählte
   Anzahl von Partitionen mit `tar` oder `rsync` gesichert. Dabei ist die Anzahl der
   Partitionen beliebig. Beim Restore kann ebenso ausgewählt werden, welche Partitionen
   zurückzuspielen sind.
   Wird auf das Originalsystem zurückgespielt, weil durch Änderungen
   am System es nicht mehr bootet, können bei einem rsync Backup nur die Änderungen zurückgespielt
   werden statt das ganze Backup und der Restore endet wesentlich schneller.
   Falls das Zielgerät beim Restore größer ist als das
   Quellgerät, wird die letzte Partition soweit erweitert, dass das gesamte Zielgerät genutzt wird.

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup#Vergleich
[.source]: https://www.linux-tips-and-tricks.de/en/backup
