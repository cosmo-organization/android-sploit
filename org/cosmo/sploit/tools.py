'''
@author Sonu Aryan(cosmo-developer)
BSD 3-Clause License

Copyright (c) 2020, Cosmo Org
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
import os
class ADB:
    def __init__(self):
        self.adb="adb "
    def configure(self):
        pass
    def adb_c(self,sub_command):
        os.system(self.adb+sub_command)
    def kill_server(self):
        self.adb_c('kill-server')
    def start_server(self):
        self.adb_c("start-server")
    def restart_server(self):
        self.adb_c("kill-server")
        self.adb_c("start-server")
#This class used for handling device connections
class DeviceConnection(ADB):
    def __init__(self):
        self.adb="adb "
        self._shell_mode="shell"
        return
    def set_shell_mode(self,_mode="su"):
        self._shell_mode="shell "+_mode
    def get_shell_mode(self):
        return self._shell_mode
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
    def disconnect_device(self,_connected_device_name):
        self.adb_c(f"disconnect {_connected_device_name}")
#This class used for performing various types of android operation
class AndroidOperation(DeviceConnection):
    def __init__(self):
        self.adb="adb "
        self._su=''
        self._shell_mode="shell"
    def set_super_user_mode(self,_su):
        self._su=_su
    #Open shell of device parameter->_current_device_name="IP:port"
    def open_device_console(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} shell")
    #Install apk on _connected_device_name=IP:port ,_installable_apk_location="C:\User Name\Your computer directory"
    def install_apk(self,_connected_device_name,_installable_apk_location):
        self.adb_c(f'-s {_connected_device_name} install "{_installable_apk_location}"')

    #Uninstall application from device
    def uninstall_app(self,_connected_device_name,_installed_apk_package):
        self.adb_c(f'-s {connected_device_name} uninstall "{_installed_apk_package}"')
    #Record screen for sometimes and store in _where_to_store="C:\Your Name\Your Directory"
    def screen_recording(self,_connected_device_name,_where_in_device,_where_to_store,_time_limit):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} screenrecord --time-limit {_time_limit} "{_where_in_device}"')
        self.adb_c(f'-s {_connected_device_name} pull "{_where_in_device}" "{_where_to_store}"')
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()}  rm "{_where_in_device}"')
    #Take Screen Short of device and store in your computer
    def screen_short(self,_connected_device_name,_where_in_device,_where_to_store):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} screencap "{_where_in_device}"')
        self.adb_c(f'-s {_connected_device_name} pull "{_where_in_device}" "{_where_to_store}"')
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} rm "{_where_in_device}"')
    #Show all list of files and folder in connected device specify _parent_folder="/storage/" or"your choice how much you know"
    def show_list_files_and_directories(self,_connected_device_name,_parent_folder):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} ls "{_parent_folder}"')
    #Import file of android device in your computer
    def import_file(self,_connected_device_name,_remote_file_or_folder="storage/",_where_to_store="C:\\"):
        self.adb_c(f'-s {_connected_device_name} pull "{_remote_file_or_folder}" "{_where_to_store}"')
    #export file from computer to android device
    def export_file(self,_connected_device_name,_remote_folder="storage/",_computer_file="adb"):
        self.adb_c(f'-s {_connected_device_name} push "{_computer_file}" "{_remote_folder}"')
    #Reboot device
    def reboot_device(self,_connected_device_name):
        self.adb_c(f'-s {_connected_device_name} reboot')
    #Show all log cat
    def show_all_log_cat(self,_connected_device_name):
        self.adb_c(f'-s {_connected_device_name} logcat')
    #Shhow System info
    def show_system_info(self,_connected_device_name):
        self.adb_c(f'-s {_connected_device_name} dumpsys')
    #show all packages installed on android device
    def package_manager(self,_connected_device_name):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} pm list packages -f')
    #Launch an app  using package_name
    def launch_app(self,_connected_device_name,_app_package):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} monkey -p {_app_package} -v 500')
    #Grab wpa
    def grab_wpa(self,_connected_device_name,_location,_where_in_device,_callable):
        try:
            self.adb_c(f'-s { _connected_device_name } {self.get_shell_mode()} -c "cp /data/misc/wifi/wpa_supplicant.conf" "{_where_in_device}"')
            self.adb_c(f'-s { _connected_device_name } pull "{_where_in_device}/wpa_supplicant.conf"" "{_location}"')
            self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} rm "{_where_in_device}/wpa_supplicant.conf"')
        except KeyboardInterrupt:
            _callable()
    #Show WLAN IP ADDRESS
    def show_wlan0_ip(self,_connected_device_name):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} ip address show wlan0')
    #Import an apk of pre-installed application of android device _installed_app_package="com.cosmo.sploit.metasploit.MetaTool" _location="Where to store in your computer pkg_with_name="where is apk stored in android device""
    def pull_apk(self,_connected_device_name,_installed_app_package,_location,_pkg_with_name):
        self.adb_c(f'-s{_connected_device_name} {self.get_shell_mode()} pm path "{_installed_app_package}"')
        self.adb_c(f'-s {_connected_device_name} pull "{_pkg_with_name}" "{_location}"')
    #Show Battery Information
    def battery_info(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} dumpsys battery")
    #Show Network Status
    def net_status(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} netstat")
    #Activiate wifi using _wifi_status="disable" or "enable"
    def wifi_activation(self,_connected_device_name,_wifi_status):
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} svc wifi {_wifi_status}")
    @staticmethod
    def unlock_oem(_connected_device_name):
        os.system("fastboot")
        os.system("fastboot unlock oem")
    #Remove screen lock safely
    def remove_screen_lock(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} rm /data/system/gesture.key")
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} rm /data/system/password.key")
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} rm /data/system/locksettings.db")
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} rm /data/system/locksettings.db-wal")
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} rm /data/system/locksettings.db-shm")
    #Press key by key code
    def press_key(self,_connected_device_name,_key_code):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} input keyevent {_key_code}')
    #show current activity on android device
    def show_current_activity(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} dumpsys activity")
    #Hide or unhide application app_pkg="com.app.example" visibility ="hide" or "unhide"
    def app_visibility(self,_connected_device_name,_app_pkg,_visibility="hide"):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} pm {_visibility} "{_app_pkg}"')
    #Enable or disable bluetooth _operation="true" or "false"
    def blue_tooth_activation(self,_connected_device_name,_operation):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} am broadcast -a android.intent.action.BLUETOOTH_ENABLE --ez state {_operation}')
    def make_a_call(self,_connected_device_name,_contact_number):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} am start -a android.intent.action.CALL -d tel:{_contact_number}')
    def send_sms(self,_connected_device_name,_sms_body,_contact_number):
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} am start -a android.intent.action.SENDTO -d sms:{_contact_number} --es sms_body '{_sms_body}' --ez exit_on_sent true")
        self.press_key(_connected_device_name,"22")
        self.press_key(_connected_device_name,"66")
    def send_email(self,_connected_device_name,_to,_subject,_body):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} am start -n com.google.android.gm/com.google.android.gm.ComposeActivityGmail -d email:"{_to}" --es subject "{_subject}" --es body "{_body}"')
    def get_prop(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} getprop")
    def reboot_recovery(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} reboot-recovery")
    def reboot_fastboot(self,_connected_device_name):
        self.adb_c(f"-s {_connected_device_name} reboot fastboot")
    #_file_name="/storage/emulated/abc.t
    def delete_file(self,_connected_device_name,_file_name):
        self.adb_c(f'-s {_connected_device_name} {self.get_shell_mode()} rm "{_file_name}"')

class ConsoleWindow:
    def __init__(self):
        pass
    @staticmethod
    def clear_src():
        os.system('cls')

class Session(AndroidOperation):
    def __init__(self,_host,_port,_unique_session_id=None):
        self._host=_host
        self._port=_port
        self.closed=True
        self._unique_session_id=_unique_session_id
        self.adb="adb "
        self._time_limit=None
    def start_session(self):
        self.connect_new_device(self._host,self._port)
        self.closed=False
        return self
    def get_device(self):
        return self._host+":"+self._port
    def stop_session(self):
        self.disconnect_device(self.get_device())
        self.closed=True
    def is_closed(self):
        return self.closed
    def get_session_id(self):
        return self._unique_session_id
    def set_time_limit(self,_time_limit):
        self._time_limit=_time_limit
        return self
    def get_time_limit(self):
        return self._time_limit
class SessionManager:
    def __init__(self):
        self._sessions=[]
    def add_session(self,_open_session):
        self.sync_session()
        if self.validate_session_id(_open_session):
           self._sessions.append(_open_session)
    def sync_session(self):
        for _session in self._sessions:
            if _session.is_closed():
                self._sessions.remove(_session)
    def validate_session_id(self,_open_session):
        for _session in self._sessions:
            if _open_session.get_session_id() is None:
                return True
            elif _session.get_session_id() is _open_session.get_session_id():
                print(f"Session ID:{_open_session.get_session_id()} is duplicate")
                return False
        return True
    def remove_session(self,_unique_session_id):
        for _session in self._sessions:
            if _session.get_session_id() is _unique_session_id:
                self._sessions.remove(_session)
    def remove_session(self,_open_session):
        if _open_session.is_closed():
          self._sessions.remove(_open_session)
        else:
            print("Session is opened can't remove session from SessionManager")
    def get_session_unique(self,_unique_session_id):
        for _session in self._sessions:
            if _session.get_session_id() is _unique_session_id:
                return _session
    def get_session_index(self,_index):
        return self._sessions[_index]
    def close_all_session(self):
        for _session in self._sessions:
            _session.stop_session()
    def remove_all_closed_session(self):
        for _session in self._sessions:
            if _session.is_closed():
                self._sessions.remove(_session)