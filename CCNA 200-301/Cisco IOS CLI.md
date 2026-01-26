**CLI** - Command-line interface
- The interface you use to configure Cisco
- GUI (Graphical User Interface

## **User EXEC Mode**
Router**>**
       |=user EXEC mode
|
hostname of the device
- User EXEC mode is very limited.
- Users can look at some things, but can't make any changes to the configuration.
- Also called 'user mode'

## Privileged EXEC mode
Router>enable 
Router**#**       =privileged EXEC mode
- Provides complete access to view the device's configuration, restart the device, etc.
- Cannot change the configuration, but can change the time on the device, save the configuration file, etc.

## **running-config / startup-config**

- There are two separate configuration files kept on the device at once.
- **Running-config** = the current, active configuration file on the device. As you enter commands in the CLI, you edit the active configuration.
- **Startup-config** = the configuration file that will be loaded upon restart of the device.

## **Service password-encryption**
If you **enable** **service password-encryption**...
- current passwords will be encrypted.
- future passwords will be encrypted.
- the enable secret will not be effected.

If you **disable** **service password-encryption**...
- current passwords will not be decrypted.
- future passwords will not be encrypted.
- the enable secret will not be effected.

## **Models Review**
**Router>** = user EXEC mode
**Router#** = privileged EXEC mode
**Router(config)#** = global configuration mode 

## Commands Review
Router>**enable**
##used to enter privileged EXEC mode

Router#**configure terminal**
##used to enter global configuration mode

Router (config)#**enable password password**
##configures a password to protect privileged exec mode


Router(config)#**service password-encryption**
##encrypts the enable password (and other passwords)

Router(config)#**enable secret password**
##configures a more secure, always-encrypted enable password

Router(config)#**run privileged-exec-level-command**
##executes a privileged-exec level command from global configuration mode

Router (config)#**no command**
##removes the command

Router(config)#**show running-config**
##displays the current, active configuration file

Router(config)#**show startup-config**
##displays the saved configuration file which will be loaded if the device is restarted

Router(config)#**write**
##saves the configuration

Router(config)#**write memory**
##saves the configuration

Router (config)#**copy running-config startup-config**
##saves the configuration

#sh01