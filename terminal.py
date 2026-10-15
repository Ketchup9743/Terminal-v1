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
                        boot_select = input("Please select a file in /boot/ Directory")
                        if boot_select == "/vmlinuz":
                            print("Showing contents of /boot/vmlinuz Directory")
                            print("")
                            print("""00000000: 4d5a 0000 0000 0000 0000 0000 0000 0000  MZ..............
00000010: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000020: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000030: 0000 0000 0000 0000 0000 0000 4000 0000  ............@...
00000040: 0e1f ba0e 00b4 09cd 21b8 014c cd21 0000  ........!..L.!..
00000050: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000060: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000070: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000080: 0000 0000 2400 0000 0000 0000 0000 0000  ....$...........
00000090: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000000a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000000b0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000000c0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000000d0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000000e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000000f0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000100: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000110: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000120: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000130: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000140: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000150: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000160: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000170: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000180: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000190: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000001a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000001b0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000001c0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000001d0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000001e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000001f0: 0000 0000 0000 0000 0000 0000 55aa 0100  ............U...
00000200: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000210: 0000 0000 0000 4865 6164 322e 3030 0000  ......Head2.00..
00000220: 0000 0500 0000 0000 0000 0000 0000 0000  ................
00000230: 0000 0000 0000 0000 8000 0000 0000 0000  ................
00000240: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000250: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000260: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000270: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000280: 1f8b 0800 0000 0000 0203 a554 4d6f d330  ...........TM..0
00000290: 10bd e757 0c6d d24d a034 a423 2a83 a6a2  ...W.m.M.4.#*...
000002a0: 504b c2a8 5d41 e26a e1a2 ec84 d455 117c  PK..]A.j.....U.|
000002b0: 4a25 c5ea dede b39c c9ee c432 e3ec b391  J%.........2....
000002c0: a733 f3de bc79 ef3d e79c efcd dcb3 ceec  .3...y.=........
000002d0: f184 dbb3 ee61 1fc2 db8f de24 fbb7 af6f  .....a.....$...o
000002e0: cff0 fa27 de0a 6fbd ecdd cfed bebf dbb5  ...'..o.........
000002f0: bfe3 fd9b ffc1 e1df bef7 deef dbbe bb7e  ...............~
00000300: c4e3 8fde bdfe d34f dbbf fdde c7c7 afee  .......O........
00000310: bedf fdc2 bbbe be0f e3fb fff0 c5ff def7  ................
00000320: efdf ff4b 2f42 f493 02e1 3280 ed82 bda0  ...K/B....2.....
00000330: a40a 12cd b60a 28ca c98b d141 de92 da2a  ......(....A...*
00000340: d1e3 f58b 41ee a2f4 bdfe f4e2 12ca c97b  ....A..........{
00000350: ebdf fa6b 0ee1 acae e40a 12cb a183 dede  ...k............
00000360: edbf abce ebef b7af dbbf fff5 efbb bee3  ................
00000370: fbff dffe dec7 cf0f e3fb eff0 f0f4 debf  ................
00000380: b7df de14 ba92 fa13 14df fa5b ca42 b4f5  ...........[.B..
00000390: db83 fa0b bde3 a4aa decd ad8f de14 bfc7  ................
000003a0: a29a d623 0c6d b7d1 e32b aa4c dedd d333  ...#.m...+.L...3
000003b0: bdba abba a4a4 cec9 0314 cdb6 aa0a ca0e  ................
000003c0: cac2 a1d9 de3a d6cd bad1 dace aa28 df92  .....:.......(..
000003d0: a492 fa5a df8b a28c abae bece afbb f9d1  ...Z............
000003e0: cfa3 a554 bcb6 af7c ebb7 de03 a4b5 b60c  ...T...|........
000003f0: bdba aa82 aa92 facf f0ef fa4b c94a dbb7  ...........K.J..
00000400: deca ce9b cef1 de3a 14de dbbf de2b eecb  .......:.....+..
00000410: bb1a debf d3a4 aaaa bbd1 c2ae bca2 ae2a  ...............*
00000420: dfab cec9 ba4a 13b4 deb6 bad1 dec7 dece  .....J..........
00000430: a20a 34de dec7 face fa5b 2baa a28c ab33  ..4......[+....3
00000440: dede ba2a dfb6 face df8b 2bcd b6d1 de30  ...*.......+...0
00000450: bdba ceab bbbe aee3 4a12 bdb6 bbbe b7af  ........J.......""")

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
                        print("System Folders in c:/Windows/ Directory")
                        print("/System32/")
                        print("/Applications/")
                        window_selector = input("Please Select a Windows Folder!")
                        if window_selector == "/System32/":
                            print("System Files in /System32/")
                            print("")
                        elif window_selector == "/Applications/":
                            print("System Files in /System32/")
            else:
                print("ADMIN mode not enabled!")
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