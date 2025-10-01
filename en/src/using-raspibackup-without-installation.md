<a name="adhoc"></a>
# Use *raspiBackup* without installation

1st download of *raspiBackup*: `curl -sSLO https://www.linux-tips-and-tricks.de/raspiBackup.sh`

1. Mount the backup partition under `/backup` or specify the backup partition as the last parameter
   parameter in the call, e.g. `sudo bash ./raspiBackup.sh /media/pi`

1. Configure *raspiBackup*. See [Call and options](invocation-options.md) and
   the configuration in the *raspiBackup* configuration file or use the corresponding invocation options.

1. Start the backup: `sudo bash ./raspiBackup.sh`

If no `rsync` backup is desired, the backup type `tar` or `dd` with option `-t` must be specified, 
i.e. `sudo bash ./raspiBackup.sh -t tar` or `sudo bash ./raspiBackup.sh -t dd`.

Brief information on all invocation options of *raspiBackup* can be obtained with `bash ./raspiBackup.sh -h`.

[.status]: translated


