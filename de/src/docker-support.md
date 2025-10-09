# Docker Support

Ein raspiBackup Nutzer hat eine *raspiBackup* Extension geschrieben
die dafür sorgt dass vor dem Backup sämtliche Dockercontainer
gestoppt werden und zum Schluss wieder gestartet werden.

Der Code steht auf [github](https://github.com/framps/raspiBackup/tree/master/extensions_userprovided) zur Verfügung.

Um die Extension zu nutzen ist wie folgt vorzugehen:

1) Download der Extension
   ```
   cd /usr/local/bin
   sudo wget https://raw.githubusercontent.com/framps/raspiBackup/refs/heads/master/extensions_userprovided/raspiBackup_docker_pre.sh
   sudo wget https://raw.githubusercontent.com/framps/raspiBackup/refs/heads/master/extensions_userprovided/raspiBackup_docker_post.sh
   sudo chmod +x raspiBackup_docker*.sh
   ```

2) Anschließend muss die Extension noch in *raspiBackup* bekanntgemacht werden.
   Dazu ist die Konfigurationsdatei `/usr/local/etc/raspiBackup.conf` anzupassen.

   Sollte noch keine Extension aktiv sein reicht folgende Definition:
   ```
   DEFAULT_EXTENSIONS="docker"
   ```

   Ansonsten muss `docker` noch zu den schon existierenden Extensions zugefügt werden.

**Hinweis**:
In den `DEFAULT_STOPSERVICES` und `DEFAULT_STARTSERVICES` Definitionen sollten keine Befehle stehen,
die Docker starten oder stoppen.

[.status]: translated
