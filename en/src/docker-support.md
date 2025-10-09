# Docker support

A *raspiBackup* user has written a *raspiBackup* extension
which ensures that all Docker containers are stopped before the backup
are stopped and restarted at the end.

The code is available on [github](https://github.com/framps/raspiBackup/tree/master/extensions_userprovided)

To use the extension, execute following steps:

1) Download the extension
   ```
   cd /usr/local/bin
   sudo wget https://raw.githubusercontent.com/framps/raspiBackup/refs/heads/master/extensions_userprovided/raspiBackup_docker_pre.sh
   sudo wget https://raw.githubusercontent.com/framps/raspiBackup/refs/heads/master/extensions_userprovided/raspiBackup_docker_post.sh
   sudo chmod x raspiBackup_docker*.sh
   ```

2) The extension must then be defined in *raspiBackup*.
   To do this, the configuration file `/usr/local/etc/raspiBackup.conf` must be updated as follows.

   If no extension is active yet, the following definition is sufficient:
   ```
   DEFAULT_EXTENSIONS="docker"
   ```

      Otherwise, `docker` must be added to the existing extensions.

**Note**:
There should be no commands in the `DEFAULT_STOPSERVICES` and `DEFAULT_STARTSERVICES` definitions,
that start or stop Docker.

[.status]: translated
