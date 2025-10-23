# Tipps für große SD Karten, HDDs und SSDs

Als *raspiBackupi* entstand gab es nur kleine SD Karten und Platten. SSDs waren noch Luxus und auch klein.
Mittlerweile sind die SD Karten zig GB gross und die Platten und SSDs haben zig TB.

In der *raspiBackup* Release 0.7 wurden deshalb Neuerungen eingeführt die helfen,
die Backup- und Restorezeit bei großen Devices zu minimieren.
Dazu ist dann der partitionsorientierte Modus zu nutzen und nicht der normale, da der nur
2 Partitionen unterstützt. Die Annahme ist, dass die ersten zwei Partitionen
das OS beherbergen und weitere große Partitionen für Daten genutzt werden.

Beim partitionsorientierten Modus kann ausgewählt werden, welche Partitionen zu sichern sind
wie auch welche Partitionen zu restoren sind (`Option -T`). Dadurch kann man regelmäßig
nur die ersten beiden Partitionen, auf denen sich das OS befindet, in sehr kurzer Zeit sichern.
Die weiteren großen Partitionen, die für Daten genutzt werden, können separat zu anderen
Zeitpunkten gesichert werden, bei denen es nicht auf schnelles Sichern ankommt.
Bootet das System dann nicht, restored man nur die zwei ersten Systempartitionen.

Noch viel schneller geht es, wenn die `Option -00` beim Restore eines rsync Backups genutzt wird.
Dann werden die Partitionen nicht neu formatiert und die vollständigen Partitionen nicht zurückgespielt,
sondern per rsync nur die Änderungen, die sich in der Zwischenzeit ergeben haben.
So kann man gezielt einzelne Partitionen schnell wieder in den Zustand bringen,
den sie zum Backupzeitpunkt hatten. Das funktioniert natürlich nur wenn das
Device des Originalsystems und auch das Filesystem nicht defekt sind.
Sonst muss doch ein vollständiger langer Restore durchgeführt werden.

Wer Devices > 2TB vollständig nutzen will wird empfohlen,
[mbr2gpt von RonR](https://forums.raspberrypi.com/viewtopic.php?t=196778) zu nutzen,
um das System von mbr auf gpt umzustellen.

[.status]: translated
