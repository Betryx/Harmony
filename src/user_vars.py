import os 
import winreg as reg
import json
import time
import stat
import ctypes
import sys


def user_vars(settings):
    for config_struct_user in settings['Variables']['user_vars']:
         
            try:
                print('Launching user variables configuration')
                time.sleep(2)
                KeyConfig = reg.OpenKey(reg.HKEY_CURRENT_USER,
                            r"Environment",
                            0, reg.KEY_SET_VALUE)
                reg.SetValueEx(KeyConfig, config_struct_user['name'], 0, reg.REG_SZ, config_struct_user['value'])
                print(f"Successfully configured user environment variables: {config_struct_user['name']} with value: {config_struct_user['value']}")
                time.sleep(2)
                reg.CloseKey(KeyConfig)
            except Exception as e:
                print(f"Error configuring user environment variables: {config_struct_user['name']} - {str(e)}")
                time.sleep(2)
