# Funktionsübersicht

Auf dieser Seite findet sich eine high Level übersicht zu raspiBackup. Detailiertere Informationen zu raspiBackup finden sich auf der [Github-Seite](https://github.com/framps/raspiBackup).

**Sichere Deine Raspberries**

**Mit raspiBackup erhältst Du schnell und sicher regelmäßig einen vollständigen Systembackup Deiner Raspberries und eine konfigurierbare Backuphistorie**

![Icon](images/icons/Icon_rot_blau_final_128.png)


Eigenschaften
Open source

raspiBackup ist unter der GNU Lizenz als OpenSource und somit kostenlos verfügbar. Trinkgelder sind aber trotzdem gern gesehen 😉

Fragen zu raspiBackup werden auf github im Diskussionsbereich beantwortet. Mögliche Fehler können als Issues im github berichtet werden.

Die Anmeldung zu github ist kostenlos. Möglichst in Englisch aber auch Deutsch wird akzeptiert.
Einfache Installation mit menügeführtem Installer

Die wichtigsten Optionen von raspiBackup können so wie bei raspi-config – allerdings in Deutsch, Englisch, Finnisch, Chinesisch und Französisch konfiguriert werden so dass die erste Sicherung in 5 Minuten erstellt werden kann.

Alle weiteren z.T. sehr mächtigen Optionen sind im Nutzerhandbuch beschrieben und können in einer Konfigurationsdatei definiert werden.
Vollständige und inkrementelle Sicherungen

Die Backuptypen dd und tar erstellen vollständige Sicherungen. Der Backuptyp rsync erstellt inkrementelle Sicherungen.
Zwei Sicherungsstrategien

1) Eine definierte Anzahl von Sicherungen wird vorgehalten
2) Sicherungen werden nach der Grossvater, Vater und Sohn Sicherungsstrategie (GVS) vorgehalten.
Benachrichtigungen

Die Sicherungslaufmeldungen können von raspiBackup per eMail oder Telegram, Slack oder PushOver verschickt werden. Smilies weisen auf Erfolg oder Misserfolg des Sicherungslaufes hin. Andere Smilies informieren über andere wichtige Ereignisse wie die Verfügbarkeit einer Beta oder eines neuen Releases oder die Erinnerung daran mal wieder einen Restoretest durchzuführen um die Sicherungsintegrität zu testen.
Alle Bootmodes sind unterstützt

1) Boot von der SD Karte: Beide Partitionen liegen auf der SD Karte (jedes Modell)
2) Gemischter Modus: Boot von der SD Karte und Nutzung der Rootpartition von einem USB Gerät. Das ist notwendig bei älteren Raspberries die noch keinen USB Boot unterstützen (2A und 2B)
3) Boot von einem USB Gerät oder SSD (USB boot Modus): Beide Partitionen liegen auf einem USB Gerät. Wird von den neueren Raspberries unterstützt, (3B, 4, 400 und 5)
Snapshots

Zu wichtigen Update- oder Installationszeitpunkten können Snapshots mit einer Beschreibung erstellt werden. Im Falle eines größeren Fehlers oder eines nicht mehr startenden Systems erlauben sie dort wieder aufzusetzen ohne mit dem Update- oder der Neuinstallation wieder ganz von vorne anzufangen.
Aktive Social Media Kanäle

Fragen können auf github oder Facebook gestellt werden. Um Probleme zu berichten gehe auf github. Videos gibt es auf dem raspiBackup Channel.

Neuigkeiten werden auf Facebook und Twitter publiziert.
Eine beliebige Anzahl von Backups aus der Vergangenheit können vorgehalten werden

Es wird nicht nur ein Backup erstellt sondern eine Backupversionshistorie. Entweder definiert man eine Anzahl von Backups die vorgehalten werden sollen oder man nutzt das GVS Prinzip (Intelligente Rotationsstrategie in raspiBackup genannt)
Wiederherstellung einer Sicherung unter Windows

Eine Sicherung des Backuptyps dd kann auf einem Windows System wiederhergestellt werden. win32diskimger oder ähnliche Tools können genutzt werden.
tar und rsync benötigen ein Linuxsystem. Es wird empfohlen dazu eine vorkonfigurierte SD Karte mit RaspbianOS zu nutzen und auf einer Raspberry zu starten.
Benachrichtigungen bei neuen Releases

Sobald ein Beta oder eine neue Release verfügbar ist schreibt raspiBackup eine Meldung die darauf hinweist. Ein Upgrade ist einfach vorzunehmen wie auch ein Downgrade wieder auf eine vorhergehende Release einfach möglich ist.
Regressionstestsuite

Die Basisfunktionalität von raspiBackup (Sicherung und Wiederherstellung) wird für alle Backuptypen und Modi automatisch getestet um sicherzustellen dass die neue raspiBackup Release genauso zuverlässig funktioniert wie vorher.
Dokumentation

Benutzerhandbuch, FAQs, Konfigurationsbeispiele, NFS Konfiguration auf einer Synology, Liste von Fehlermeldungen und wie man die Fehlermeldungen beseitigen kann und vieles mehr. Es gibt schon raspiBackup Nutzer die beschweren sich dass es zu viel Doku gibt. Es existiert auch ein raspiBackup Channel auf Youtube.
Hilfs- und Beispielscripte

Verschiedene Hilfs- und Beispielscripts stehen zur Verfügung auf github.

Z.B. wie pishrink genutzt werden kann um eine dd Sicherung noch zu verkleinern oder wie parallel ein clone erstellt werden kann um einen aktuellen jederzeit einsetzbares geclontes Bootmeidum zu haben. Und vieles, vieles mehr.
Sicherung von NVMe Speicher

Wird für Raspberry 5 und compute model 4 (CM4) unterstützt
Unterstütze Betriebssysteme

– RaspbianOS
– Ubuntu
Einfacher Systemumzug auf andere Speichermedien

Jede Sicherung kann auf eine SD Karte, USB Platte oder SSD sowie NVMe SSD zurückgespielt werden. Schon ist das System auf ein anderes Gerät umgezogen.
Erweiterungspunkte

Vor und nach der Sicherung kann eigener Code ausgeführt werden um Vor- und Nachbereitungen bei der Sicherung wie auch dem Zurücksichern auszuführen


