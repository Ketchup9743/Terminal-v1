### Header for Terminal ###
admin = False
admin_logged_in = False
print("")
print("                Welcome to your Computer Terminal Program!")
print("")
print("=============================================================================")
print("")
print("» Type [STOP] to end the process.")
print("» Type [START] to start the process.")
print("» Type [HELP] for a list of executable commands.")
def command_logic():
    global admin
    global admin_logged_in
    global command
    while True:
        command = input("» COMMAND : ")
        if command == "STOP":
            print("» Stopping current process...")
            print("")
            print("» Process Ended!")
        elif command == "START":
            print("» Starting current process...")
            print("")
            print("» Process Started!")
        elif command == "HELP":
            print("» Showing list of available commands...")
            print("» [STOP] - Stops the current running process.")
            print("» [START] - Starts the process.")
            print("» [HELP] - Shows this window.")
            print("» [VERIFY] - Verify to use ADMIN panel.")
            print("» [ADMIN] - Enters administrator mode.")
            print("» [ADMIN-HELP] - Shows a list of all available ADMIN commands.")
            print("» [QUIT] - ENDS all processes.")
        elif command == "VERIFY":
            admin_login = input("» Please enter your ADMIN password...")
            if admin_login == "admin100":
                print("» Successfully logged in!")
                admin_logged_in = True
            else:
                    print("» Incorrect Password! Please try again!")
        elif command == "ADMIN":
            if admin_logged_in == True:
                admin = True
                print("                  ----- ADMININISTRATOR MODE ENABLED ----")
            else:
                print("» User not verified! Please verify with [VERIFY]")
        elif command == "ADMIN-HELP":
            if admin == True:
                print("» Showing list of available ADMIN commands")
                print("» [FILE] - Displays System File Directories")
                print("» [SETTINGS] - Access Terminal Settings")
                print("» [ROOT] - Access the ROOT file of the Terminal")
                print("» [COMP-SPECS] - Displays Computer Specs")
            else:
                print("» ADMIN Mode not enabled!")
        elif command == "QUIT":
            print("» Ending all processes...")
            print("» Processes stopped!")
            print("» Clearing terminal...")
            print("» Terminal Cleared!")
            print("» Please Restart the Terminal!")
            admin = False
            admin_logged_in = False
            break
        elif command == "FILE":
            if admin == True:
                print("System Folders:")
                print("/boot/")
                print("/sbin/")
                print("/lib/")
                print("/etc/")
                print("/bin/")
                print("c:/Windows/")
                folder_selector = input("Please select a folder to browse its files!")
                if folder_selector == "/boot/":
                        print("System Files in /boot/ Directory")
                        print("/vmlinuz")
                        print("Select a File to browse its contents")
                if folder_selector == "/sbin/":
                        print("System Files in /sbin/ Directory")
                        print("/init")
                        print("/fsck")
                        print("Select a File to browse its contents")
                if folder_selector == "/lib/":
                        print("System Files in /lib/ Directory")
                        print("/ld-linux.so")
                        print("/libc.so")
                        print("Select a File to browse its contents")
                if folder_selector == "/etc/":
                        print("System Files in /etc/ Directory")
                        print("/fstab")
                        print("/passwd")
                        print("/shadow")
                        print("/resolv.conf")
                        print("/hosts")
                        print("Select a File to browse its contents")
                if folder_selector == "/bin/":
                        print("System Files in /bin/ Directory")
                        print("/bash")
                        print("/mount")
                        print("Select a File to browse its contents")
                if folder_selector == "c:/Windows/":
                        print("System Files in c:/Windows/ Directory")
                        print("...")
                        print("Select a File to browse its contents")
        elif command == "ROOT":
            if admin == True:
                print("...")
        elif command == "SETTINGS":
            if admin == True:
                print("...")
        elif command == "COMP-SPECS":
            if admin == True:
                print("...")
        else:
            print("» Please re-run the program and input a valid command!")
command_logic()