# Thematically sorted invocation options

<a name="backup"></a>
## Backup options

  - [-a: Commands to start the services after the backup](backup-options.md#-a)
  - [-A: The runtime log is sent in the email](general-options.md#-A)
  - [-b: Definition of the block size to be used for the dd backup](backup-options.md#parm_b)
  - [-B: Boot partition is backed up as tar instead of dd](backup-options.md#parm_B)
  - [-c: Allow local backup](backup-options.md#-c)
  - [-D: More options for the dd backup](backup-options.md#parm_D)
  - [--dynamicMount: Dynamic mounting of the backup partition](backup-options.md#parm_dynamicMount)
  - [--ignoreAdditionalPartitions: More than two partitions are tolerated, but only the first two partitions are backed up](backup-options.md#parm_ignoreAdditionalPartitions)
  - [--ignoreMissingPartitions: Test whether all partitions are backed up](backup-options.md#--ignoremissingPartitions)
  - [-k : Number of backups to be kept](backup-options.md#parm_k)
  - [--keep_{type}: Number of backup types to be kept](backup-options.md#parm_keepType)
  - [-M: Create a *raspiBackup* snapshot](backup-options.md#parm_M)
  - [-o: Commands that stop services before the backup](backup-options.md#parm_o)
  - [-p: Backup directory](backup-options.md#parm_p)
  - [-P : Partition-oriented backup mode](backup-options.md#parm_P)
  - [--rebootSystem: Reboot the system after the backup](backup-options.md#parm_rebootSystem)
  - [--smartRecycle: Use of SmartReccyle](backup-options.md#parm_smartRecycle)
  - [--smartRecycleDryrun: Test mode of SmartRecycle](backup-options.md#parm_smartRecycleDryrun)
  - [--smartRecycleOptions: SmartRecycle options](backup-options.md#parm_smartRecycleOptions)
  - [--systemStatus: Show active services at backup start](backup-options.md#parm_systemstatus)
  - [-t : Type of backup (dd, tar, rsync)](backup-options.md#parm_t)
  - [-T: Partitions to be backed up](backup-options.md#parm_T)
  - [-u: Enables additional directories to be excluded from the backup process](backup-options.md#parm_u)
  - [-z: Compression of the backup with dd or tar](backup-options.md#parm_z)

<a name="restore"></a>
## Restore options

  - [-C: Check for bad blocks](restore-options.md#parm_C)
  - [-d: Restoredevice](restore-options.md#parm_d)
  - [-R: External root partition](restore-options.md#parm_R)
  - [--resizeRootFS: Root file system adjustment](restore-options.md#parm_resizeRootFS)
  - [-T: Partitions to be restored](restore-options.md#parm_T)
  - [--updateUUIDs: UUID generation](restore-options.md#parm_resizeRootFS)
  - [-Y: Automated restore](restore-options.md#parm_Y)
  - [-0: No partitioning](restore-options.md#parm_0)
  - [-00: No partitioning and formatting](restore-options.md#parm_00)
  - [-1: Ignore partitioning error](restore-options.md#parm_1)
 
<a name="messages-and-log"></a>
## Options that affect the messages and the log

  - [-A: The runtime log is sent with the email notification](general-options.md#parm_A)
  - [--coloring: Coloring settings for e-mails and console messages](general-options.md#parm_coloring)
  - [-G: Language of messages (German or English)](general-options.md#parm_G)
  - [-l: Switch on the detailed log level](general-options.md#parm_l)
  - [-L: Directory where the debug log and the runtime messages are saved](general-options.md#parm_L)
  - [-m: Message details](general-options.md#parm_m)
  - [--timestamps: All messages are output with a leading timestamp](general-options.md#parm_timestamps)
  - [-v: All messages from the backup tool used are logged](backup-options.md#parm_v)

<a name="notifications"></a>
## Options that control notifications

  - [-e: email address to which the notification is sent](general-options.md#parm_e)
  - [-E: Optional parameters for the eMailClient programs](general-options.md#parm_E)
  - [--eMailColoring: Control where the eMailClient used accepts coloring information](general-options.md#parm_eMailColoring)
  [ -F: Simulates the backup run and helps to quickly test the email notification](backup-options.md#parm_F)
  - [-s: eMailClientProgram for sending the eMail](general-options.md#parm_s)

<a name="maintenance"></a>
## Options that control update, restore and local distribution of *raspiBackup*

  - [ -S: Unconditional update](general-options.md#parm_S)
  - [-U: Update *raspiBackup* with the latest version and backup the old version](general-options.md#parm_U)
  - [-V: Reactivate a previous *raspiBackup* version](general-options.md#parm_V)
  - [-y: Copy the current *raspiBackup* version to predefined local hosts via scp](general-options.md#parm_y)

<a name="start-stop-extensions"></a>
## Options that start and stop services before the backup and extensions

  - [-o: Commands that stop services before the backup](backup-options.md#parm_o)
  - [-a: Commands that start services after the backup](backup-options.md#parm_a)
  - [-N: Extensions to be called before and after the backup](backup-options.md#parm_N)

<a name="miscellaneous"></a>
## Further options

  - [-f: Specification of a configuration file](general-options.md#parm_f)
  - [-g: Progress bar](general-options.md#parm_g)
  - [--unsupportedEnvironment: Unsupported HW and SW is accepted](general-options.md#parm_unsupportedEnvironment)
  - [--updateConfig: Update of the *raspiBackup* configuration file](general-options.md#parm_updateConfig)

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/aufruf-und-optionen
[.source]: https://www.linux-tips-and-tricks.de/en/invocation-and-options


