### Header for Terminal ###
print("                Welcome to your Computer Terminal Program!")
print("")
print("=============================================================================")
print("")
print("Type [STOP] to end the process.")
print("Type [START] to start the process.")
print("Type [HELP] for a list of executable commands.")
command = input("COMMAND : ")
if command == "STOP":
    print("Stopping current process...")
    print("")
    print("Process Ended!")
elif command == "START":
    print("Starting current process...")
    print("")
    print("Process Started!")
elif command == "HELP":
    print("Showing list of available commands...")
    print("[STOP] - Stops the current running process")
    print("[START] - Starts the process")
    print("[HELP] - Shows this window")
    print("[ADMIN] - Enters administrator mode")
    print("[ADMIN-HELP] - Shows a list of all available ADMIN commands")
    print("[QUIT] - ENDS all processes, and cleans the terminal")
elif command == "ADMIN":
    print("                  ----- ADMININISTRATOR MODE ENABLED ----")
elif command == "ADMIN-HELP":
    print("Showing list of available ADMIN commands")
elif command == "QUIT":
    print("Ending all processes...")
    print("Processes stopped!")
    print("Clearing terminal...")
    print("Terminal Cleared!")
    print("Please scroll down!")
    print("\n" * 100)
else:
    print("Please re-run the program and input a valid command")
    