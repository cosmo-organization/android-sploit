import os
import platform
#Written by Sonu Aryan
class ADB:
    def __init__(self):
        self.adb="adb "
    def configure(self):
        if platform.platform().startswith("Win"):
            os.chdir("adb")
        else:
            an=input("You have adb pre-installed(Y/n):")
            if an == 'n':
                os.system("sudo apt install adb")
    def adb_c(self,sub_command):
        os.system(self.adb+sub_command)
    def kill_server(self):
        self.adb_c('kill-server')
    def start_server(self):
        self.adb_c("start-server")
    def restart_server(self):
        self.adb_c('kill-server && start-server')
#This class used for handling device connections
class DeviceConnection(ADB):
    def __init__(self):
        self.adb="adb "
        return
    #Connect new device using IP:port of host
    def connect_new_device(self,_host_ip,_host_port):
        self.adb_c(f'tcpip {_host_port}')
        self.adb_c(f"connect {_host_ip}:{_host_port}")
    #Disconnect all devices connected with ADB Server
    def disconnect_all_device(self):
        self.adb_c('disconnect')
    #Show all the list of connected devices
    def show_all_connected_device(self):
        self.adb_c('devices -l')
    #Forward tcp
    def forward_tcp(self,_connected_device_name,_port_device,_forward_port):
        self.adb_c(f"-s {_connected_device_name} forward tcp:{_port_device} tcp:{_forward_port}")
#This class used for performing various types of android operation
class AndroidOperation(DeviceConnection):
    def __init__(self):
        self.adb="adb "
    #Open shell of device parameter->_current_device_name="IP:port"
    def open_device_console(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} shell")
    #Install apk on _connected_device_name=IP:port ,_installable_apk_location="C:\User Name\Your computer directory"
    def install_apk(self,_connected_device_name,_installable_apk_location):
        self.adb_c(f'-s {_connected_device_name} install {_installable_apk_location}')

    #Uninstall application from device
    def uninstall_app(self,_connected_device_name,_installed_apk_package):
        self.adb_c(f'-s {connected_device_name} uninstall {_installed_apk_package}')
    #Record screen for sometimes and store in _where_to_store="C:\Your Name\Your Directory"
    def screen_recording(self,_connected_device_name,_where_to_store,_time_limit):
        self.adb_c(f'-s {_connected_device_name} shell screenrecord --time-limit storage/emulated/legacy/rcX.mp4')
        self.adb_c(f"-s {_connected_device_name} pull storage/emulated/legacy/rcX.mp4 '{_where_to_store}'")
        self.adb_c(f"-s {_connected_device_name} shell rm storage/emulated/legacy/rcX.mp4")
    #Take Screen Short of device and store in your computer
    def screen_short(self,_connected_device_name,_where_to_store):
        self.adb_c(f"-s {_connected_device_name} shell screencap storage/emulated/legacy/rcxI.png")
        self.adb_c(f"-s {_connected_device_name} pull storage/emulated/legacy/rcxI.png {_where_to_store}")
        self.adb_c(f"-s {_connected_device_name} shell rm storage/emulated/legacy/rcxI.png")
    #Show all list of files and folder in connected device specify _parent_folder="/storage/" or"your choice how much you know"
    def show_list_files_and_directories(self,_connected_device_name,_parent_folder):
        self.adb_c(f"-s {_connected_device_name} shell {_parent_folder}/ ls")
    #Import file of android device in your computer
    def import_file(self,_connected_device_name,_remote_file_or_folder="storage/",_where_to_store="C:\\"):
        self.adb_c(f"-s {_connected_device_name} pull {_remote_file_or_folder} {_where_to_store}")
    #export file from computer to android device
    def export_file(self,_connected_device_name,_remote_folder="storage/",_computer_file="adb"):
        self.adb_c(f"-s {_connected_device_name} push {_computer_file} {_remote_folder}")
    #Reboot device
    def reboot_device(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} reboot")
    #Show all log cat
    def show_all_log_cat(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} logcat")
    #Shhow System info
    def show_system_info(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} dumpsys")
    #show all packages installed on android device
    def package_manager(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} shell pm list packages -f")
    #Launch an app  using package_name
    def launch_app(self,_connected_device_name,_app_package):
        self.adb_c(f"-s {_connected_device_name} shell monkey -p {_app_package} -v 500")
    #Grab wpa
    def grab_wpa(self,_connected_device_name,_location,_callable,_su):
        try:
            self.adb_c(f"-s { _connected_device_name } shell {_su} -c 'cp /data/misc/wifi/wpa_supplicant.conf /storage/emulated/legacy'")
            self.adb_c(f"-s { _connected_device_name } pull /storage/emulated/legacy/wpa_supplicant.conf {_location}")
        except KeyboardInterrupt:
            _callable()
    #Show WLAN IP ADDRESS
    def show_wlan0_ip(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} shell ip address show wlan0")
    #Import an apk of pre-installed application of android device _installed_app_package="com.cosmo.sploit.metasploit.MetaTool" _location="Where to store in your computer pkg_with_name="where is apk stored in android device""
    def pull_apk(self,_connected_device_name,_installed_app_package,_location,_pkg_with_name):
        self.adb_c(f"-s{_connected_device_name} shell pm path {_installed_app_package}")
        self.adb_c(f"-s {_connected_device_name} pull {_pkg_with_name} {_location}")
    #Show Battery Information
    def battery_info(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} shell dumpsys battery")
    #Show Network Status
    def net_status(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} shell netstat")
    #Activiate wifi using _wifi_status="disable" or "enable"
    def wifi_activation(self,_connected_device_name,_wifi_status):
        self.adb_c(f"-s {_connected_device_name} shell svc wifi {_wifi_status}")
    #Remote lockscreen safely
    def remove_screen_lock(self,_connected_device_name,_su):
        self.adb_c(f"-s {_connected_device_name} shell {_su} rm /data/system/gesture.key")
        self.adb_c(f"-s {_connected_device_name} shell {_su} rm /data/system/password.key")
        self.adb_c(f"-s {_connected_device_name} shell {_su} rm /data/system/locksettings.db")
        self.adb_c(f"-s {_connected_device_name} shell {_su} rm /data/system/locksettings.db-wal")
        self.adb_c(f"-s {_connected_device_name} shell {_su} rm /data/system/locksettings.db-shm")
    #Press key by key code
    def press_key(self,_connected_device_name,_key_code):
        self.adb_c(f"-s {_connected_device_name} shell input keyevent "+_key_code)
    #show current activity on android device
    def show_current_activity(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} shell dumpsys activity")
    #Hide or unhide application app_pkg="com.app.example" visibility ="hide" or "unhide"
    def app_visibility(self,_connected_device_name,_app_pkg,_visibility):
        self.adb_c(f"-s {_connected_device_name} shell pm "+_visibility+" "+_app_pkg)
    #Enable or disable bluetooth _operation="true" or "false"
    def blue_tooth_activation(self,_connected_device_name,_operation):
        self.adb_c(f"-s {_connected_device_name} shell am broadcast -a android.intent.action.BLUETOOTH_ENABLE --ez state "+_operation)
    def make_a_call(self,_connected_device_name,_contact_number):
        self.adb_c(f"-s {_connected_device_name} shell am start -a android.intent.action.CALL -d tel:"+_contact_number)
    def send_sms(self,_connected_device_name,_sms_body,_contact_number):
        self.adb_c(f"-s {_connected_device_name} shell am start -a android.intent.action.SENDTO -d sms:{_contact_number} --es sms_body '{_sms_body}' --ez exit_on_sent true")
        self.press_key(_connected_device_name,"22")
        self.press_key(_connected_device_name,"66")
    def send_email(self,_connected_device_name,_to,_subject,_body):
        self.adb_c(f"-s {_connected_device_name} shell am start -n com.google.android.gm/com.google.android.gm.ComposeActivityGmail -d email:{_to} --es subject '{_subject}' --es body '{_body}'")
    def get_prop(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} shell getprop")
    def reboot_recovery(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} reboot-recovery")
    def reboot_fastboot(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} reboot fastboot")

class ConsoleWindow:
    def __init__(self):
        pass
    def clear_src(self):
        os.system('cls')
