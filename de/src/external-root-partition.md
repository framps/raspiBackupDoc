# Wird eine externe Rootpartition unterstützt?

Ältere Raspberries, die noch keinen USB Boot Modus unterstützen,
können so konfiguriert werden, dass nur die Bootpartition
auf der SD Karte abgelegt wird
und das Rootfilesystem auf einer externen USB Platte.

*raspiBackup* unterstützt externe Rootpartitionen und
eine ausgelagerte Rootpartition wird mitgesichert.

Im normalen Backupmodus werden normalerwesie die beiden RaspbianOS-Partitionen
`/boot` und `/root` vom Systemgerät gesichert. Wenn die Rootpartition aber
auf eine externe
Partition (USB Stick, USB Platte, ...) ausgelagert wurde, wird diese externe
Partition gesichert sowie die Bootpartition von der SD Karte. Wird
dieser Backup zurückgespielt, muss die [Option `-R`](restore-options.md#parm_R) genutzt werden,
um das Zielgerät für die externe Rootpartition anzugeben.

[.status]: rst
