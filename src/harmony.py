import os 
import winreg as reg
import json
import time
import stat
import ctypes
import sys
import user_vars
import sys_vars
def main():
    
    
    print("<----------------------Harmony Enviroment variable configuration------------------------>")
    path_to_config_file=str(input("enter config.hm.json path: "))
    if os.path.exists(path_to_config_file):
        config_file = open(path_to_config_file, 'r')
        settings = json.load(config_file)
        sys_vars.sys_vars(settings)
        user_vars.user_vars(settings)

        
        
    else:
        print("config.hm.json file not found!")
        time.sleep(2)
        print("Restart and enter a valid path")
        time.sleep(2)
    
            
            





                


                
                
            

            
 

        
if __name__ == "__main__":
    main()