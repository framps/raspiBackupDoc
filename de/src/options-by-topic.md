# Thematisch sortierte Aufruf-Optionen

<a name="backup"></a>
## Backup-Optionen

  - [-a: Befehle die Services nach dem Backup starten](backup-options.md#-a)
  - [-A: Das Laufzeitlog wird in der eMail mitgeschickt](general-options.md#-A)
  - [-b: Definition der Blocksize die beim dd Backup genutzt wird](backup-options.md#parm_b)
  - [-B: Bootpartition wird als tar gesichert statt per dd](backup-options.md#parm_B)
  - [-c: Erlaube lokale Backupsicherung](backup-options.md#-c)
  - [-D: Weitere Optionen für den dd Backup](backup-options.md#parm_D)
  - [--dynamicMount: Dynamisches Mounten der Backuppartition](backup-options.md#parm_dynamicMount)
  - [--ignoreAdditionalPartitions: Es werden mehr als zwei Partitionen toleriert wobei aber nur die ersten beiden Partitionen gesichert werden.](backup-options.md#parm_ignoreAdditionalPartitions)
  - [--ignoreMissingPartitions: Test ob alle Partitionen gesichert werden](backup-options.md#--ignoremissingPartitions)
  - [-k : Anzahl der Backups die vorgehalten werden sollen](backup-options.md#parm_k)
  - [--keep_{type}: Anzahl der jeweiligen Backuptypen, die vorgehalten werden sollen](backup-options.md#parm_keepType)
  - [-M: Erstellen eines *raspiBackup* Snapshots](backup-options.md#parm_M)
  - [-o: Befehle, die Services vor dem Backup stoppen](backup-options.md#parm_o)
  - [-p: Backupverzeichnis](backup-options.md#parm_p)
  - [-P : Partitionsorientierter Backupmodus](backup-options.md#parm_P)
  - [--rebootSystem: Reboot des Systems nach dem Backup](backup-options.md#parm_rebootSystem)
  - [--smartRecycle: Nutzung von SmartReccyle](backup-options.md#parm_smartRecycle)
  - [--smartRecycleDryrun: Testmodus von SmartRecycle](backup-options.md#parm_smartRecycleDryrun)
  - [--smartRecycleOptions: SmartRecycle Optionen](backup-options.md#parm_smartRecycleOptions)
  - [--systemStatus: Aktive Services beim Backupstart anzeigen](backup-options.md#parm_systemstatus)
  - [-t : Typ des Backups (dd, tar, rsync)](backup-options.md#parm_t)
  - [-T: Zu sichernde Partitionen](backup-options.md#parm_T)
  - [-u: Ermöglicht weitere Verzeichnisse aus dem Backuprozess auszuschließen](backup-options.md#parm_u)
  - [-z: Kompression des Backups bei dd oder tar](backup-options.md#parm_z)

<a name="restore"></a>
## Restore-Optionen

  - [-C: Auf Badblocks prüfen](restore-options.md#parm_C)
  - [-d: Restoredevice](restore-options.md#parm_d)
  - [-R: Externe Rootpartition](restore-options.md#parm_R)
  - [--resizeRootFS: Rootfilesystem Anpassung](restore-options.md#parm_resizeRootFS)
  - [-T: Zu restorende Partitionen](restore-options.md#parm_T)
  - [--updateUUIDs: UUID Generierung](restore-options.md#parm_resizeRootFS)
  - [-Y: Automatisierter Restore](restore-options.md#parm_Y)
  - [-0: Keine Partitionierung](restore-options.md#parm_0)
  - [-00: Keine Partitionierung und Formatierung](restore-options.md#parm_00)
  - [-1: Partitionierungsfehler ignorieren](restore-options.md#parm_1)
 
<a name="messages-and-log"></a>
## Optionen, die die Meldungen und das Log betreffen

  - [-A: Das Laufzeitlog wird bei der eMail Benachrichtigung mitgeschickt](general-options.md#parm_A)
  - [--coloring: Kolorierungseinstellungen bei eMails und Konsolmeldungen](general-options.md#parm_coloring)
  - [-G: Sprache der Meldungen (Deutsch oder Englisch)](general-options.md#parm_G)
  - [-l: Einschalten des detaillierten Loglevels](general-options.md#parm_l)
  - [-L: Verzeichnis wo das Debuglog sowie die Laufzeitmeldungen gespeichert werden](general-options.md#parm_L)
  - [-m: Meldungsdetails](general-options.md#parm_m)
  - [--timestamps: Alle Meldungen werden mit einem führenden Zeitstempel ausgegeben](general-options.md#parm_timestamps)
  - [-v: Alle Meldungen des verwendeten Backuptools werden protokolliert](backup-options.md#parm_v)

<a name="notifications"></a>
## Optionen, die Benachrichtigungen steuern

  - [-e: eMailAdresse an die die Benachrichtigung geschickt wird](general-options.md#parm_e)
  - [-E: Optionale Parameter für die eMailClientProgramme](general-options.md#parm_E)
  - [--eMailColoring: Steuerung, wo der genutzte eMailClient Colorierungnsinformationen akzeptiert](general-options.md#parm_eMailColoring)
  - [-F: Simuliert den Backuplauf und hilft die eMailBenachrichtgung schnell zu testen](backup-options.md#parm_F)
  - [-s: eMailClientProgramm zum Verschicken der eMail](general-options.md#parm_s)

<a name="maintenance"></a>
## Optionen, die Update, Restore und lokale Verteilung von *raspiBackup* steuern

  - [-S: Unbedingtes Update](general-options.md#parm_S)
  - [-U: Update von *raspiBackup* mit der aktuellsten Version und Sicherung der alten Version](general-options.md#parm_U)
  - [-V: Reaktivierung einer vorhergehenden *raspiBackup* Version](general-options.md#parm_V)
  - [-y: Kopie der aktuellen *raspiBackup* Version auf vordefinierte lokale Hosts per scp](general-options.md#parm_y)

<a name="start-stop-extensions"></a>
## Optionen, die Services vor dem Backup starten und stoppen sowie Erweiterungen

  - [-o: Befehle, die Services vor dem Backup stoppen](backup-options.md#parm_o)
  - [-a: Befehle, die Services nach dem Backup starten](backup-options.md#parm_a)
  - [-N: Erweiterungen, die vor und nach dem Backup aufgerufen werden sollen](backup-options.md#parm_N)

<a name="miscellaneous"></a>
## Weitere Optionen

  - [-f: Angabe einer Konfigurationsdatei](general-options.md#parm_f)
  - [-g: Fortschrittsanzeige](general-options.md#parm_g)
  - [--unsupportedEnvironment: Nicht unterstützte HW und SW wird akzeptiert](general-options.md#parm_unsupportedEnvironment)
  - [--updateConfig: Update der *raspiBackup* Konfigurationsdatei](general-options.md#parm_updateConfig)

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/aufruf-und-optionen
[.source]: https://www.linux-tips-and-tricks.de/en/invocation-and-options
