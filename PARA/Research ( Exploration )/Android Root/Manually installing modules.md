
To manually install a Magisk module using a root shell, follow these steps:

1. **Download and Extract Module:**
   - Download the module `.zip` file and extract its contents on your computer.

2. **Connect Your Device:**
   - Connect your device to your computer via USB.

3. **Open ADB Shell:**
   - Open a terminal or command prompt on your computer.
   - Enter the following command to start an ADB shell:
     ```bash
     adb shell
     ```

4. **Gain Root Access:**
   - In the ADB shell, gain root access:
     ```bash
     su
     ```

5. **Create Module Directory:**
   - Create a directory for the module:
     ```bash
     mkdir -p /data/adb/modules/<module_name>
     ```

6. **Transfer Module Files:**
   - Use ADB to push the extracted module files to the device:
     ```bash
     adb push <local_module_path> /data/adb/modules/<module_name>
     ```

7. **Set Permissions:**
   - Set the correct permissions for the module files:
     ```bash
     chmod -R 755 /data/adb/modules/<module_name>
     ```

8. **Reboot Your Device:**
   - Reboot your device to activate the module:
     ```bash
     reboot
     ```

Replace `<module_name>` with the name of your module and `<local_module_path>` with the path to the extracted module files on your computer.
