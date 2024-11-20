import os 
import winreg as reg
import json
import time
import stat
import ctypes
import sys

def sys_vars(settings):
    for config_struct_system in settings['Variables']['sys_vars']:
       


            try:
                print('Launching system variables configuration')
                time.sleep(2)
                KeyConfig = reg.OpenKey(reg.HKEY_LOCAL_MACHINE,
                            r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
                            0, reg.KEY_SET_VALUE)
                reg.SetValueEx(KeyConfig, config_struct_system['name'], 0, reg.REG_SZ, config_struct_system['value'])


                print(f"Successfully configured system environment variables: {config_struct_system['name']} with value: {config_struct_system['value']}")
                time.sleep(2)
                reg.CloseKey(KeyConfig)

            except Exception as e:
                print(f"Error configuring system environment variables: {config_struct_system['name']} - {str(e)}")