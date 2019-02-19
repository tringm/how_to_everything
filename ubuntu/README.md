## How to deal with ubuntu

#### Drivers
1. Auto install Drivers

  ```
  sudo ubuntu-drivers autoinstall  
  sudo reboot
  ```

#### Enable GPU(NVIDIA OPTIMUS)
Check for update [guide](https://askubuntu.com/questions/1046263/dell-xps-15-9570-2018-disable-nvidia-gpu)
1. Installation:
  * Either autoinstall drivers or follow the step bellows
  * If already install nvidia driver => purge
  ```
  sudo apt-get purge nvidia*
  ```
  * Install and configure power management
  ```
  sudo apt-get install tlp tlp-rdw powertop
  sudo tlp start
  ```
  * Install nvidia driver (Remeber to check version)
  ```
  sudo add-apt-repository ppa:graphics-drivers/ppa
  sudo apt update
  sudo apt install nvidia-384 nvidia-settings
  ```
  * Test that nvidia works. It should show some GPU stats if NVIDIA GPU is chosen or complaining about missing driver
  ```
  nvidia-smi
  ```
  * Install nvidia-prime to switch between NVIDIA and Intel GPU
  ```
  sudo apt-get install nvidia-prime
  ```
2. Switching between GPUs:
  * Switch to intel (Doesn't disable rightway, need reboot)
  ```
  sudo prime-select intel
  ```
  * Swith to nvidia (switch rightway)
  ```
  sudo prime-select nvidia
  ```
  * Remember to check for power consumption
  ```
  sudo powertop
  ```
