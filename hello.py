import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
        
if is_admin():
  # Do stuff
  print()
  
else:
    # Re-run the program with admin rights
    sys.stdout.write('Not running as admin, relaunching...?\n')
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


print("Admin!")
x=input("Admin")