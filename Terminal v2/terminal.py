import time
print("####################################################")
print("####            Welcome to Terminal v2          ####")    
print("####################################################")
logged_in = False
admin_enabled = False
admin_username = "admin"
admin_password = "admin100"
is_admin = False
username = "blank"
password = "blank"
def signup():
    global username, password, logged_in
    username = input("System - Please enter a username for the terminal.")
    password = input("System - Please enter a password for the terminal.")
    logged_in = True
signup()
def commands():
    global username, password, logged_in, admin_enabled, admin_username, admin_password, is_admin
    command = input("System - Please type in a command...")
    if command == "help":
        print("System - Showing list of available commands:")
        print("System - login | Allows the user to login to the terminal")
        print("System - sign_out | Allows the user to sign out of their account")
        print("System - enable_admin | Allows the user to enable administrator mode")
        print("System - panel | Allows the user to view their current panel")
        print("System - settings | Allows the user to see the current settings")
        commands()
        
    
    elif command == "login":
        if logged_in == True:
            print("Error | User already logged in!")
        else:
            username_input = input("System - Please enter your username")
            password_input = input("System - Please enter your password")
            if username_input == username and password_input == password:
                print("System - Logging in...")
                time.sleep(2)
                print("System - Logged in.")
                logged_in = True
                commands()
            else:
                print("ERROR  | Username and/or password is incorrect")
                commands()
    
    elif command == "sign_out":
        if logged_in != True:
            print("ERROR | Must be logged in to sign out")
            commands()
        else:
            print("System - Signing out....")
            time.sleep(1)
            print("System - Signed out!")
            logged_in = False
            is_admin = False
            commands()
    
    elif command == "enable_admin":
        adminuser_attempt = input("Input the admin username...")
        adminpass_attempt = input("Input the admin password...")
        if adminuser_attempt == admin_username and adminpass_attempt == admin_password:
            is_admin = True
            print("Admin enabled.")
            print("Run admin-help to see a list of admin commands.")
            admin_command = input("Please enter an admin command.")
            if admin_command == admin-help:
                print("Showing list of available admin commands")
                print("ADMIN - admin-help | Shows a list of availaable admin commands")
                print("ADMIN - admin-settings | Allows the admin to configure terminal settings")
                print("ADMIN - admin-logout | Logs the user out of the admin account")
            elif admin_command == admin-settings:
                pass
            elif admin_command == admin-logout:
                pass
        else:
            print("Incorrect username and/or password")
            commands()
    elif command == "panel":
        pass
    
    elif command == "settings":
        pass
    else:
        print("Invalid command.")
        commands()



































commands() 