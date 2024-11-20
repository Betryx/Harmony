import os 
import winreg as reg
import json
import time
import stat
import ctypes
import sys


def user_vars(settings):
    if sys.platform == 'win32':
         
        for config_struct_user in settings['Variables']['user_vars']:
            
                try:
                    print('Launching user variables configuration')
                    time.sleep(2)
                    KeyConfig = reg.OpenKey(reg.HKEY_CURRENT_USER,r"Environment",0, reg.KEY_SET_VALUE)
                    reg.SetValueEx(KeyConfig, config_struct_user['name'], 0, reg.REG_SZ, config_struct_user['value'])
                    print(f"Successfully configured user environment variables: {config_struct_user['name']} with value: {config_struct_user['value']}")
                    time.sleep(2)
                    reg.CloseKey(KeyConfig)
                except Exception as e:
                    print(f"Error configuring user environment variables: {config_struct_user['name']} - {str(e)}")
                    time.sleep(2)
    elif sys.platform == "linux":
         for config_struct_user in settings['Variables']['user_vars']:
             try:
                 print('Launching user variables configuration')
                 time.sleep(2)
                 with open(f"/home/{os.getenv('USER')}/.bashrc", "a") as file:
                     file.write(f'\nexport {config_struct_user["name"]}="{config_struct_user["value"]}"')
                 print(f"Successfully configured user environment variables: {config_struct_user['name']} with value: {config_struct_user['value']}")
                 time.sleep(2)
             except Exception as e:
                 print(f"Error configuring user environment variables: {config_struct_user['name']} - {str(e)}")
                 time.sleep(2)  
    elif sys.platform == "Darwin":
         for config_struct_user in settings['Variables']['user_vars']:
             try:
                 print('Launching user variables configuration')
                 time.sleep(2)
                 with open(f"/Users/{os.getenv('USER')}/.bash_profile", "a") as file:
                     file.write(f'\nexport {config_struct_user["name"]}="{config_struct_user["value"]}"')
                 print(f"Successfully configured user environment variables: {config_struct_user['name']} with value: {config_struct_user['value']}")
                 time.sleep(2)
             except Exception as e:
                 print(f"Error configuring user environment variables: {config_struct_user['name']} - {str(e)}")
                 time.sleep(2)