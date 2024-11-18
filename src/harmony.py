import os as sys
import winreg as reg
import json
import time
import stat
import ctypes
import sys
def main():
    
    
    print("<----------------------Harmony Enviroment variable configuration------------------------>")
    path_to_config_file=str(input("enter config.hm.json path: "))
    if sys.path.exists(path_to_config_file):

        config_file = open(path_to_config_file, 'r')
        settings = json.load(config_file)
        for config_struct_system in settings['Variables']['sys_vars']:
       


            try:
                print('Launching system variables configuration')
                time.sleep(4)
                KeyConfig = reg.OpenKey(reg.HKEY_LOCAL_MACHINE,
                            r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
                            0, reg.KEY_SET_VALUE)
                reg.SetValueEx(KeyConfig, config_struct_system['name'], 0, reg.REG_SZ, config_struct_system['value'])


                print(f"Successfully configured system environment variables: {config_struct_system['name']} with value: {config_struct_system['value']}")
                time.sleep(4)
                reg.CloseKey(KeyConfig)

            except Exception as e:
                print(f"Error configuring system environment variables: {config_struct_system['name']} - {str(e)}")
        for config_struct_user in settings['Variables']['user_vars']:
         
            try:
                print('Launching user variables configuration')
                time.sleep(4)
                KeyConfig = reg.OpenKey(reg.HKEY_CURRENT_USER,
                            r"Environment",
                            0, reg.KEY_SET_VALUE)
                reg.SetValueEx(KeyConfig, config_struct_user['name'], 0, reg.REG_SZ, config_struct_user['value'])
                print(f"Successfully configured user environment variables: {config_struct_user['name']} with value: {config_struct_user['value']}")
                time.sleep(4)
                reg.CloseKey(KeyConfig)
            except Exception as e:
                print(f"Error configuring user environment variables: {config_struct_user['name']} - {str(e)}")
                time.sleep(4)
    else:
        print("config.hm.json file not found!")
        time.sleep(4)
        print("Restart and enter a valid path")
        time.sleep(4)
    
            
            





                


                
                
            

            
 

        
if __name__ == "__main__":
    main()