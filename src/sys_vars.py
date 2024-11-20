import os 
import winreg as reg
import json
import time
import stat
import ctypes
import sys

def sys_vars(settings):
    if sys.platform =='win32':
        KeyPath=r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
        for config_struct_system in settings['Variables']['sys_vars']:
        


                try:
                    print('Launching system variables configuration')
                    time.sleep(2)
                    KeyConfig = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, KeyPath, 0, reg.KEY_SET_VALUE)
                    reg.SetValueEx(KeyConfig, config_struct_system['name'], 0, reg.REG_SZ, config_struct_system['value'])


                    print(f"Successfully configured system environment variables: {config_struct_system['name']} with value: {config_struct_system['value']}")
                    time.sleep(2)
                    reg.CloseKey(KeyConfig)

                except Exception as e:
                    print(f"Error configuring system environment variables: {config_struct_system['name']} - {str(e)}")
    elif sys.platform =='linux':
        for config_struct_system in settings['Variables']['sys_vars']:
            try:
                print('Launching system variables configuration')
                time.sleep(2)
                with open('/etc/environment', 'a') as file:
                    file.write(f'{config_struct_system["name"]}={config_struct_system["value"]}\n')
                print(f"Successfully configured system environment variables: {config_struct_system['name']} with value: {config_struct_system['value']}")
                time.sleep(2)
            except Exception as e:
                print(f"Error configuring system environment variables: {config_struct_system['name']} - {str(e)}")
    elif sys.platform == 'Darwin':
        for config_struct_system in settings['Variables']['sys_vars']:
            try:
                print('Launching system variables configuration')
                time.sleep(2)
                with open('/etc/launchd.conf', 'a') as file:
                    file.write(f'export {config_struct_system["name"]}={config_struct_system["value"]}\n')
                print(f"Successfully configured system environment variables: {config_struct_system['name']} with value: {config_struct_system['value']}")
                time.sleep(2)
            except Exception as e:
                print(f"Error configuring system environment variables: {config_struct_system['name']} - {str(e)}")