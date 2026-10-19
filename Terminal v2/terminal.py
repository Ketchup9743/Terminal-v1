import time
admin = False
password = "admin100"
command = ""

print("=================================================================")
print("                      Welcome to Terminal v2")
print("=================================================================")
print("")
def base_input():
    command = input("» Type 'Help' for a list of available commands")
if command == "Help":
    time.sleep(0.6)
    print("» Showing list of available commands.")
    print("» Help - Shows list of available commands")
    print("» Quit - Ends all processes, (removes ADMIN from user)")
    print("» Login - Allows the user to login into the ADMIN terminal")
    print("» Verify - Allows the user to verify themselves as an admin")
    command = input("» Please input one of the above listed commands.")
elif command == "Quit":
    print("» Ending all processes...")
    time.sleep(3)
    print("» Processes Terminated!")
    print("» Removing ADMIN from user...")
    time.sleep(2)
    print("» ADMIN has successfully been removed from user")
elif command == "Verify":
    print("» Verifying user is admin...")
    time.sleep(1)
    if admin == False:
        print("» Error! User does not have ADMIN permissions.")
        base_input()
    elif admin == True:
        print("» User successfully verified with ADMIN permissions.")
        command = input("» Type 'Admin-Help' for a list of available ADMIN commands")
        if command == "Admin-Help":
            print("» Showing list of available ADMIN commands")
            time.sleep(0.5)
            print("» ADMIN-Logs - Displays system logs")
            print("» ADMIN-Reset - Resets the terminal, keeps user logged in as ADMIN")
            print("» ADMIN-Settings - Displays the configured settings")
            print("» ADMIN-Configure - Allows the user to configure current settings")
        elif command == "ADMIN-Logs":
            print()
        elif command == "ADMIN-Reset":
            print()
        elif command == "ADMIN-Settings":
            print()
        elif command == "ADMIN-Configure":
            print()
elif command == "Login":
    loginAttempt = input("» Please enter your ADMIN password")
    if loginAttempt == password:
        print("» User successfully logged in.")
        admin = True
        base_input()
    else:
        print("» Incorrect password")
        base_input()
else:
    print("» Please provide a valid command and re-run the terminal.")
    base_input()