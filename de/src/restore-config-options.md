# Restore Konfigurationsoptionen

Die meisten Aufrufoptionen können ebenso in der Konfigurationsdatei
definiert werden. Siehe dazu [Restoreoptionen](restore-options.md).

<div class="table-wrapper-for-options">

------------------

<!-- toc -->

------------------

### DEFAULT_RESTORE_EXTENSIONS

*raspiBackup* bietet für den Restore wie beim Backup die Möglichkeit,
auch pre und post Exits zu konfigurieren, um vor und nach dem Restore noch
Aktionen vorzunehmen. Die Syntax ist genauso wie für die Backup Extensions.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_RESTORE_EXTENSIONS | keiner   |


### DEFAULT_RESTORE_REMINDER_INTERVAL

Backup Restore Test Reminder Intervall (Einheit: Monate)

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_RESTORE_REMINDER_INTERVAL | 6 |

### DEFAULT_RESTORE_REMINDER_REPEAT

Anzahl der Erinnerungen, einen Backup Restore Test durchzuführen.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_RESTORE_REMINDER_REPEAT | 3   |

### DEFAULT_YES_NO_DEVICES

Mit der Aufrufoption `-Y` können die Ja/Nein
Abfragen beim Restore unterdrückt werden.

Da dieses aber unbeabsichtigtes Löschen von
Devices bewirken kann muss mit dieser Option
vermitteles eines regulären Ausdruckes
definiert werden, welche Restoredevices
ohne Abfrage überschrieben werden dürfen.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_YES_NO_DEVICES     | loop   |

</div>

[.status]: translated

