### Dual Boot
1. Partition from Windows (Leave free partition)
1. Disable Secure Boot
1. Change from RAID to AHCI (apply to Windows )
    1. To set the default boot mode to Safe Mode, use `msconfig.exe` or open an admin cmd/PowerShell window and run:

    ```bat
    bcdedit /set '{current}' safeboot minimal
    ```

    2. Reboot and hit F2 to enter the BIOS.

    3. Change the SATA mode to AHCI.

    4. Save and reboot.

    5. After Windows successfully boots into Safe Mode, disable Safe Mode with `msconfig.exe` or open an admin cmd/PowerShell window and run:

        ```bat
        bcdedit /deletevalue '{current}' safeboot
        ```

    6. Reboot one last time. If you open the Device Manager, there should now be a `Standard NVM Express Controller` device under Storage Controllers.

1. Boot Debian from USB


### Support for Dell XPS15
1. Wifi Driver [update Linux firmware](https://www.dell.com/support/article/us/en/19/sln306440/killer-n1535-wireless-firmware-manual-update-guide-for-ubuntu-systems?lang=en)
    * Choose the newest FW
1. Update Linux image is usually a good choice [guide](https://wiki.debian.org/HowToUpgradeKernel). This might fix the sound and lighting problem


### Install GPU
1. For ***Optimus*** GPU (e.g: Intel as main GPU and say NVIDIA as 3D Controller) => bumblebee

### Misc
1. Adding backports, contrib, non-free to sources list
    ```
    sudo vim /etc/apt/sources.list
    ```
    ```
    deb http://ftp.fi.debian.org/debian/ stretch main contrib non-free
    deb-src http://ftp.fi.debian.org/debian/ stretch main contrib non-free

    deb http://security.debian.org/debian-security stretch/updates main contrib non-free
    deb-src http://security.debian.org/debian-security stretch/updates main contrib non-free

    # stretch-updates, previously known as 'volatile'
    deb http://ftp.fi.debian.org/debian/ stretch-updates main contrib non-free
    deb-src http://ftp.fi.debian.org/debian/ stretch-updates main contrib non-free

    deb http://ftp.fi.debian.org/debian/ stretch-backports main  
    ```

1. Restart a service
    ```bash
    systemctl restart <service_name>
    ```
