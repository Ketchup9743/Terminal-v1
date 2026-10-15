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
            else:
                print("» ADMIN Mode not enabled!")
        elif command == "QUIT":
            print("» Ending all processes...")
            print("» Processes stopped!")
            print("» Clearing terminal...")
            print("» Terminal Cleared!")
            print("» Please Restart the Terminal!")
            break
        else:
            print("» Please re-run the program and input a valid command!")
command_logic()