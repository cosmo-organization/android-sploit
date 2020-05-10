from com.cosmo.sploit.tools import ADB,DeviceConnection,AndroidOperation,ConsoleWindow
import os
import random
import time as t
from colorama import Fore, init
#API initialization
cw=ConsoleWindow()
adb=ADB()
dc=DeviceConnection()
ao=AndroidOperation()
#End api initialization
#Git PhoneSploit github
CurrentDir = os.path.dirname(os.path.abspath(__file__))
load_count = 0
arrow = Fore.RED + " âââ>" + Fore.WHITE
connect = Fore.RED + "â" + Fore.WHITE
page2 = False
page_1 = '''\n
{0}[{1}1{0}] {2}Show Connected Devices      {0}[{1}6{0}] {2}Screen record a phone               {0}[{1}11{0}] {2}Uninstall an app                   
{0}[{1}2{0}] {2}Disconect all devices       {0}[{1}7{0}] {2}Screen Shot a picture on a phone    {0}[{1}12{0}] {2}Show real time log of device       
{0}[{1}3{0}] {2}Connect a new phone         {0}[{1}8{0}] {2}Restart Server                      {0}[{1}13{0}] {2}Dump System Info                   
{0}[{1}4{0}] {2}Access Shell on a phone     {0}[{1}9{0}] {2}Pull folders from phone to pc       {0}[{1}14{0}] {2}List all apps on a phone           
{0}[{1}5{0}] {2}Install an apk on a phone   {0}[{1}10{0}] {2}Turn The Device off                {0}[{1}15{0}] {2}Run an app                         


{0}[{1}99{0}] {2}Exit   {0}[{1}0{0}] {2}Clear   {0}[{1}p{0}] Next Page                           v1.2
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN)

page_2 = '''\n
{0}[{1}16{0}]{2} Port Forwarding                {0}[{1}21{0}]{2} NetStat                {0}[{1}26{0}]{2} Stop Server
{0}[{1}17{0}]{2} Grab wpa_supplicant            {0}[{1}22{0}]{2} Turn WiFi On/Off       {0}[{1}27{0}]{2} Start Server
{0}[{1}18{0}]{2} Show Mac/Inet                  {0}[{1}23{0}]{2} Remove Password        {0}[{1}28{0}]{2} List all files and folder
{0}[{1}19{0}]{2} Extract apk from app           {0}[{1}24{0}]{2} Use Keycode            
{0}[{1}20{0}]{2} Get Battery Status             {0}[{1}25{0}]{2} Get Current Activity                  


{0}[{1}99{0}] {2}Exit   {0}[{1}0{0}] {2}Clear   {0}[{1}b{0}] Back to page one
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN)


# =============================
# Main
def main():
    page_num = 1
    option = input(Fore.WHITE + "phonesploit" + Fore.RED + "(main_menu) " + Fore.WHITE + "> ")
    if option == '1':
        dc.show_all_connected_device()
    elif option == '2':
        dc.disconnect_all_device()
    elif option == '3':
        print(("\n[{0}+{1}] Enter a phones ip address.").format(Fore.RED, Fore.WHITE))
        _ip = input(arrow + " phonesploit" + Fore.RED + "(connect_phone) IP" + Fore.WHITE + "> ")
        _port = input(arrow + " phonesploit" + Fore.RED + "(connect_phone) PORT" + Fore.WHITE + "> ")
        dc.connect_new_device(_ip,_port)
    elif option == '4':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(shell_on_phone) " + Fore.WHITE + "> ")
        ao.open_device_console(device_name)
    elif option == 'clear':
        cw.clear_src()
    elif option == '5':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(apk_install) " + Fore.WHITE + "> ")
        print(("     " + connect))
        print(("    [{0}+{1}]Enter the apk location.").format(Fore.RED, Fore.WHITE))
        apk_location = input("    " + arrow + "phonesploit" + Fore.RED + "(apk_install) " + Fore.WHITE + "> ")
        ao.install_apk(_connected_device_name=device_name,_installable_apk_location=apk_location)
        print(Fore.GREEN + "Apk has been installed.")
    elif option == '6':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(screen_record) " + Fore.WHITE + "> ")
        print(("     " + connect))
        print(("    [{0}+{1}] Please wait 3m its recording").format(Fore.RED, Fore.WHITE))
        print(("     " + connect))
        print(("    [{0}+{1}]Enter where you would like the video to be saved.").format(Fore.RED, Fore.WHITE))
        place_location = input("    " + arrow + "phonesploit" + Fore.RED + "(screen_record) " + Fore.WHITE + "> ")
        ao.screen_recording(device_name,place_location)
    elif option == '7':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(screenshot) " + Fore.WHITE + "> ")
        print(("     " + connect))
        print(("    [{0}+{1}]Enter where you would like the screenshot to be saved.").format(Fore.RED, Fore.WHITE))
        place_location = input("    " + arrow + "phonesploit" + Fore.RED + "(screenshot) " + Fore.WHITE + "> ")
        ao.screen_short(device_name,place_location)

    elif option == '8':
        adb.restart_server()

    elif option == '9':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(file_pull) " + Fore.WHITE + "> ")
        print(("     " + connect))
        print(("    [{0}+{1}]Enter a file location on a device").format(Fore.RED, Fore.WHITE))
        file_location = input("    " + arrow + "phonesploit" + Fore.RED + "(file_pull) " + Fore.WHITE + "> ")
        print(("        " + connect))
        print(("       [{0}+{1}]Enter where you would like the file to be saved.").format(Fore.RED, Fore.WHITE))
        place_location = input("       " + arrow + "phonesploit" + Fore.RED + "(file_pull) " + Fore.WHITE + "> ")
        ao.import_file(device_name,file_location,place_location)
    elif option == '10':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(device_reboot) " + Fore.WHITE + "> ")
        ao.reboot_device(device_name)
    elif option == '11':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(app_delete) " + Fore.WHITE + "> ")
        print(("     " + connect))
        print(("    [{0}+{1}]Enter a package name.").format(Fore.RED, Fore.WHITE))
        package_name = input("    " + arrow + "phonesploit" + Fore.RED + "(app_delete) " + Fore.WHITE + "> ")
        ao.uninstall_app(device_name,package_name)
    elif option == '12':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(log) " + Fore.WHITE + "> ")
        ao.show_all_log_cat(device_name)
    elif option == '13':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(sys_info) " + Fore.WHITE + "> ")
        ao.show_system_info(device_name)

    elif option == '14':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(package_manager) " + Fore.WHITE + "> ")
        ao.package_manager(device_name)
        main()

    elif option == '15':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(app_run) " + Fore.WHITE + "> ")
        print(("     " + connect))
        print(("    [{0}+{1}]Enter a package name. They look like this --> com.snapchat.android").format(Fore.RED,
                                                                                                         Fore.WHITE))
        package_name = input("    " + arrow + "phonesploit" + Fore.RED + "(app_run) " + Fore.WHITE + "> ")
        ao.launch_app(device_name,package_name)
        main()
    elif option == '16':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(port_forward) " + Fore.WHITE + "> ")
        print(("     " + connect))
        print(("    [{0}+{1}]Enter a port on the device.").format(Fore.RED, Fore.WHITE))
        port_device = input("    " + arrow + "phonesploit" + Fore.RED + "(port_forward) " + Fore.WHITE + "> ")
        print(("         " + connect))
        print(("        [{0}+{1}]Enter a port to forward it too.").format(Fore.RED, Fore.WHITE))
        forward_port = input("        " + arrow + "phonesploit" + Fore.RED + "(port_forward) " + Fore.WHITE + "> ")
        os.system("adb -s " + device_name + " forward tcp:" + port_device + " tcp:" + forward_port)
        dc.forward_tcp(device_name,port_device,forward_port)

    elif option == '17':
        try:
            print(("[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
            device_name = input(arrow + "phonesploit" + Fore.RED + "(wpa_grab) " + Fore.WHITE + "> ")
            print((Fore.WHITE + "    [{0}+{1}]{1}THE DEVICE NEEDS TO BE ROOTED TO CONTINUE TO EXIT USE CTRL +C").format(
                Fore.RED, Fore.WHITE))
            print(("     " + connect))
            print(("    [{0}+{1}]Enter where you want the file to be saved.").format(Fore.RED, Fore.WHITE))
            location = input("    " + arrow + "phonesploit" + Fore.RED + "(wpa_grab) " + Fore.WHITE + "> ")
            ao.grab_wpa(device_name,location)
        except KeyboardInterrupt:
            main()

    elif option == '18':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(mac_inet) " + Fore.WHITE + "> ")
        ao.show_wlan0_ip(device_name)
        main()

    elif option == '19':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(pull_apk) " + Fore.WHITE + "> ")
        print(("     " + connect))
        print(("    [{0}+{1}]Enter a package name. They look like this --> com.snapchat.android").format(Fore.RED,
                                                                                                         Fore.WHITE))
        package_name = input("    " + arrow + "phonesploit" + Fore.RED + "(pull_apk) " + Fore.WHITE + "> ")
        print(("         " + connect))
        print((
                  "        [{0}+{1}]Enter The path.looks like this /data/app/com.snapchat.android-qWgDcBiCEvANq6op_NPqeA==/base.apk").format(
            Fore.RED, Fore.WHITE))
        path = input("        " + arrow + "phonesploit" + Fore.RED + "(pull_apk) " + Fore.WHITE + "> ")
        print(("             " + connect))
        print(("            [{0}+{1}]Enter The location to store the apk: ").format(Fore.RED, Fore.WHITE))
        location = input("            " + arrow + "phonesploit" + Fore.RED + "(pull_apk) " + Fore.WHITE + "> ")
        ao.pull_apk(device_name,package_name,location,path)
        main()

    elif option == '20':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(battery) " + Fore.WHITE + "> ")
        ao.battery_info(device_name)
        main()

    elif option == '21':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(net_stat) " + Fore.WHITE + "> ")
        ao.net_status(device_name)
        main()

    elif option == '22':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(wifi) " + Fore.WHITE + "> ")
        print(("     " + connect))
        print(("    [{0}+{1}] To turn wifi back on you need the device to be pluged in.").format(Fore.RED, Fore.WHITE))
        print(("     " + connect))
        on_off = input(
            Fore.WHITE + "    [" + Fore.RED + "+" + Fore.WHITE + "]Would you like the wifi " + Fore.GREEN + "on" + Fore.WHITE + "/" + Fore.RED + "off " + Fore.WHITE)
        if on_off == 'off':
            ao.wifi_activation(device_name,"disable")
        else:
            ao.wifi_activation(device_name,"enable")


    elif option == '23':
        print(("[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(pass_remove) " + Fore.WHITE + "> ")
        print((
                          Fore.WHITE + "    [{0}+{1}]{1}THE DEVICE NEEDS TO BE ROOTED TO CONTINUE TO EXIT USE CTRL +C THIS IS ALSO UNTESTED").format(
            Fore.RED, Fore.WHITE))
        print(("     " + connect))
        print(Fore.RED + "******************TRYING TO REMOVE PASS******************")
        ao.remove_screen_lock(device_name)
        print(Fore.RED + "******************TRYING TO REMOVE PASS******************")

    elif option == '24':
        print(("[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(keycode) " + Fore.WHITE + "> ")
        print('''
0 -->  "KEYCODE_UNKNOWN" 
1 -->  "KEYCODE_MENU" 
2 -->  "KEYCODE_SOFT_RIGHT" 
3 -->  "KEYCODE_HOME" 
4 -->  "KEYCODE_BACK" 
5 -->  "KEYCODE_CALL" 
6 -->  "KEYCODE_ENDCALL" 
7 -->  "KEYCODE_0" 
8 -->  "KEYCODE_1" 
9 -->  "KEYCODE_2" 
10 -->  "KEYCODE_3" 
11 -->  "KEYCODE_4" 
12 -->  "KEYCODE_5" 
13 -->  "KEYCODE_6" 
14 -->  "KEYCODE_7" 
15 -->  "KEYCODE_8" 
16 -->  "KEYCODE_9" 
17 -->  "KEYCODE_STAR" 
18 -->  "KEYCODE_POUND" 
19 -->  "KEYCODE_DPAD_UP" 
20 -->  "KEYCODE_DPAD_DOWN" 
21 -->  "KEYCODE_DPAD_LEFT" 
22 -->  "KEYCODE_DPAD_RIGHT" 
23 -->  "KEYCODE_DPAD_CENTER" 
24 -->  "KEYCODE_VOLUME_UP" 
25 -->  "KEYCODE_VOLUME_DOWN" 
26 -->  "KEYCODE_POWER" 
27 -->  "KEYCODE_CAMERA" 
28 -->  "KEYCODE_CLEAR" 
29 -->  "KEYCODE_A" 
30 -->  "KEYCODE_B" 
31 -->  "KEYCODE_C" 
32 -->  "KEYCODE_D" 
33 -->  "KEYCODE_E" 
34 -->  "KEYCODE_F" 
35 -->  "KEYCODE_G" 
36 -->  "KEYCODE_H" 
37 -->  "KEYCODE_I" 
38 -->  "KEYCODE_J" 
39 -->  "KEYCODE_K" 
40 -->  "KEYCODE_L" 
41 -->  "KEYCODE_M" 
42 -->  "KEYCODE_N" 
43 -->  "KEYCODE_O" 
44 -->  "KEYCODE_P" 
45 -->  "KEYCODE_Q" 
46 -->  "KEYCODE_R" 
47 -->  "KEYCODE_S" 
48 -->  "KEYCODE_T" 
49 -->  "KEYCODE_U" 
50 -->  "KEYCODE_V" 
51 -->  "KEYCODE_W" 
52 -->  "KEYCODE_X" 
53 -->  "KEYCODE_Y" 
54 -->  "KEYCODE_Z" 
55 -->  "KEYCODE_COMMA" 
56 -->  "KEYCODE_PERIOD" 
57 -->  "KEYCODE_ALT_LEFT" 
58 -->  "KEYCODE_ALT_RIGHT" 
59 -->  "KEYCODE_SHIFT_LEFT" 
60 -->  "KEYCODE_SHIFT_RIGHT" 
61 -->  "KEYCODE_TAB" 
62 -->  "KEYCODE_SPACE" 
63 -->  "KEYCODE_SYM" 
64 -->  "KEYCODE_EXPLORER" 
65 -->  "KEYCODE_ENVELOPE" 
66 -->  "KEYCODE_ENTER" 
67 -->  "KEYCODE_DEL" 
68 -->  "KEYCODE_GRAVE" 
69 -->  "KEYCODE_MINUS" 
70 -->  "KEYCODE_EQUALS" 
71 -->  "KEYCODE_LEFT_BRACKET" 
72 -->  "KEYCODE_RIGHT_BRACKET" 
73 -->  "KEYCODE_BACKSLASH" 
74 -->  "KEYCODE_SEMICOLON" 
75 -->  "KEYCODE_APOSTROPHE" 
76 -->  "KEYCODE_SLASH" 
77 -->  "KEYCODE_AT" 
78 -->  "KEYCODE_NUM" 
79 -->  "KEYCODE_HEADSETHOOK" 
80 -->  "KEYCODE_FOCUS" 
81 -->  "KEYCODE_PLUS" 
82 -->  "KEYCODE_MENU" 
83 -->  "KEYCODE_NOTIFICATION" 
84 -->  "KEYCODE_SEARCH" 
85 -->  "TAG_LAST_KEYCODE"        
        ''')
        print(("[{0}+{1}]Enter a number.").format(Fore.RED, Fore.WHITE))
        num = input(arrow + "phonesploit" + Fore.RED + "(keycode) " + Fore.WHITE + "> ")
        ao.press_key(device_name,num)

    elif option == '25':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(current_activity) " + Fore.WHITE + "> ")
        ao.show_current_activity(device_name)
        main()
    elif option == '26':
        adb.kill_server()
        main()
    elif option == '27':
        adb.start_server()
        main()
    elif option == '28':
        print(("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit" + Fore.RED + "(files_and_folder_list/device_name) " + Fore.WHITE + "> ")
        parent = input(arrow + "phonesploit" + Fore.RED + "(files_and_folder_list/parent_folder) " + Fore.WHITE + "> ")
        ao.show_list_files_and_directories(device_name,parent)
        main()
    elif option == '0':
        global page2
        if page2 == True:
            clear(page_2)
        else:
            clear(page_1)

    elif option == 'p':
        os.system('cls')
        page2 = True
        print(Fore.RED + banner_title)
        print(page_2)

    elif option == 'b':
        os.system('cls')
        page2 = False
        print(page_1)

    elif option == '99':
        exit()
    elif option == 'exit':
        exit(0)

    main()


# =============================
def verify_platform():
    adb.configure()
def clear(page):
    global page2
    os.system('cls')
    print(page)
# =============================
# Run
try:
    init(convert=True)
    verify_platform()
    print(Fore.RED + "Starting  adb server..")
    adb.start_server()
    t.sleep(4)
    cw.clear_src()
    print(page_1)
    main()
except KeyboardInterrupt:
    adb.kill_server()
    exit(0)

