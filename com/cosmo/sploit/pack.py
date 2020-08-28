import os
import platform
import socket
# Written by Sonu Aryan
class ADB:
    def __init__(self):
        self.adb = "adb "
    def configure(self):
        if platform.platform().startswith("Win"):
            os.chdir("adb")
        else:
            an = input("You have adb pre-installed(Y/n):")
            if an == 'n':
                os.system("sudo apt install adb")
    def adb_c(self, sub_command):
        os.system(self.adb+sub_command)
    def kill_server(self):
        self.adb_c('kill-server')
    def start_server(self):
        self.adb_c("start-server")
    def restart_server(self):
        self.adb_c('kill-server && start-server')
# This class used for handling device connections
class DeviceConnection(ADB):
    def __init__(self):
        self.adb = "adb "
        self._shell_mode = "shell"
        return
    def set_shell_mode(self, _mode="su"):
        self._shell_mode = "shell "+_mode
    def get_shell_mode(self):
        return self._shell_mode
    # Connect new device using IP:port of host
    def connect_new_device(self, _host_ip, _host_port):
        self.adb_c(f'tcpip {_host_port}')
        self.adb_c(f"connect {_host_ip}:{_host_port}")
    # Disconnect all devices connected with ADB Server
    def disconnect_all_device(self):
        self.adb_c('disconnect')
    # Show all the list of connected devices
    def show_all_connected_device(self):
        self.adb_c('devices -l')
    # Forward tcp
    def forward_tcp(self, _connected_device_name, _port_device, _forward_port):
        self.adb_c(
            f"-s {_connected_device_name} forward tcp:{_port_device} tcp:{_forward_port}")
    def disconnect_device(self, _connected_device_name):
        self.adb_c(f"disconnect {_connected_device_name}")
# This class used for performing various types of android operation
class AndroidOperation(DeviceConnection):
    def __init__(self):
        self.adb = "adb "
        self._su = ''
        self._shell_mode = "shell"
    def set_super_user_mode(self, _su):
        self._su = _su
    # Open shell of device parameter->_current_device_name="IP:port"
    def open_device_console(self, _connected_device_name):
        self.adb_c(f"-s {_connected_device_name} shell")
    # Install apk on _connected_device_name=IP:port ,_installable_apk_location="C:\User Name\Your computer directory"
    def install_apk(self, _connected_device_name, _installable_apk_location):
        self.adb_c(
            f'-s {_connected_device_name} install {_installable_apk_location}')
    # Uninstall application from device
    def uninstall_app(self, _connected_device_name, _installed_apk_package):
        self.adb_c(
            f'-s {connected_device_name} uninstall {_installed_apk_package}')
    # Record screen for sometimes and store in _where_to_store="C:\Your Name\Your Directory"
    def screen_recording(self, _connected_device_name, _where_in_device, _where_to_store, _time_limit):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} screenrecord --time-limit {_time_limit} '{_where_in_device}'")
        self.adb_c(
            f"-s {_connected_device_name} pull {_where_in_device} '{_where_to_store}'")
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()}  rm '{_where_in_device}'")
    # Take Screen Short of device and store in your computer
    def screen_short(self, _connected_device_name, _where_in_device, _where_to_store):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} screencap '{_where_in_device}'")
        self.adb_c(
            f"-s {_connected_device_name} pull '{_where_in_device}' '{_where_to_store}'")
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} rm '{_where_in_device}'")
    # Show all list of files and folder in connected device specify _parent_folder="/storage/" or"your choice how much you know"
    def show_list_files_and_directories(self, _connected_device_name, _parent_folder):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} ls '/{_parent_folder}'")
    # Import file of android device in your computer
    def import_file(self, _connected_device_name, _remote_file_or_folder="storage/", _where_to_store="C:\\"):
        self.adb_c(
            f"-s {_connected_device_name} pull {_remote_file_or_folder} {_where_to_store}")
    # export file from computer to android device
    def export_file(self, _connected_device_name, _remote_folder="storage/", _computer_file="adb"):
        self.adb_c(
            f"-s {_connected_device_name} push {_computer_file} {_remote_folder}")
    # Reboot device
    def reboot_device(self, _connected_device_name):
        self.adb_c(f"-s {_connected_device_name} reboot")
    # Show all log cat
    def show_all_log_cat(self, _connected_device_name):
        self.adb_c(f"-s {_connected_device_name} logcat")
    # Shhow System info
    def show_system_info(self, _connected_device_name):
        self.adb_c(f"-s {_connected_device_name} dumpsys")
    # show all packages installed on android device
    def package_manager(self, _connected_device_name):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} pm list packages -f")
    # Launch an app  using package_name
    def launch_app(self, _connected_device_name, _app_package):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} monkey -p {_app_package} -v 500")
    # Grab wpa
    def grab_wpa(self, _connected_device_name, _location, _where_in_device, _callable):
        try:
            self.adb_c(
                f"-s { _connected_device_name } {self.get_shell_mode()} -c 'cp /data/misc/wifi/wpa_supplicant.conf {_where_in_device}'")
            self.adb_c(
                f"-s { _connected_device_name } pull '{_where_in_device}/wpa_supplicant.conf' {_location}")
            self.adb_c(
                f"-s {_connected_device_name} {self.get_shell_mode()} rm {_where_in_device}/wpa_supplicant.conf")
        except KeyboardInterrupt:
            _callable()
    # Show WLAN IP ADDRESS
    def show_wlan0_ip(self, _connected_device_name):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} ip address show wlan0")
    # Import an apk of pre-installed application of android device _installed_app_package="com.cosmo.sploit.metasploit.MetaTool" _location="Where to store in your computer pkg_with_name="where is apk stored in android device""
    def pull_apk(self, _connected_device_name, _installed_app_package, _location, _pkg_with_name):
        self.adb_c(
            f"-s{_connected_device_name} {self.get_shell_mode()} pm path {_installed_app_package}")
        self.adb_c(
            f"-s {_connected_device_name} pull '{_pkg_with_name}' '{_location}'")
    # Show Battery Information
    def battery_info(self, _connected_device_name):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} dumpsys battery")
    # Show Network Status
    def net_status(self, _connected_device_name):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} netstat")
    # Activiate wifi using _wifi_status="disable" or "enable"
    def wifi_activation(self, _connected_device_name, _wifi_status):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} svc wifi {_wifi_status}")
    @staticmethod
    def unlock_oem(_connected_device_name):
        os.system("fastboot")
        os.system("fastboot unlock oem")
    # Remove screen lock safely
    def remove_screen_lock(self, _connected_device_name):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} rm /data/system/gesture.key")
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} rm /data/system/password.key")
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} rm /data/system/locksettings.db")
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} rm /data/system/locksettings.db-wal")
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} rm /data/system/locksettings.db-shm")
    # Press key by key code
    def press_key(self, _connected_device_name, _key_code):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} input keyevent "+_key_code)
    # show current activity on android device
    def show_current_activity(self, _connected_device_name):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} dumpsys activity")
    # Hide or unhide application app_pkg="com.app.example" visibility ="hide" or "unhide"
    def app_visibility(self, _connected_device_name, _app_pkg, _visibility):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} pm "+_visibility+" "+_app_pkg)
    # Enable or disable bluetooth _operation="true" or "false"
    def blue_tooth_activation(self, _connected_device_name, _operation):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} am broadcast -a android.intent.action.BLUETOOTH_ENABLE --ez state "+_operation)
    def make_a_call(self, _connected_device_name, _contact_number):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} am start -a android.intent.action.CALL -d tel:"+_contact_number)
    def send_sms(self, _connected_device_name, _sms_body, _contact_number):
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} am start -a android.intent.action.SENDTO -d sms:{_contact_number} --es sms_body '{_sms_body}' --ez exit_on_sent true")
        self.press_key(_connected_device_name, "22")
        self.press_key(_connected_device_name, "66")
    def send_email(self, _connected_device_name, _to, _subject, _body):
        self.adb_c(f"-s {_connected_device_name} {self.get_shell_mode()} am start -n com.google.android.gm/com.google.android.gm.ComposeActivityGmail -d email:{_to} --es subject '{_subject}' --es body '{_body}'")
    def get_prop(self, _connected_device_name):
        self.adb_c(
            f"-s {_connected_device_name} {self.get_shell_mode()} getprop")
    def reboot_recovery(self, _connected_device_name):
        self.adb_c(f"-s {_connected_device_name} reboot-recovery")
    def reboot_fastboot(self, _connected_device_name):
        self.adb_c(f"-s {_connected_device_name} reboot fastboot")
class ConsoleWindow:
    def __init__(self):
        pass
    @staticmethod
    def clear_src():
        os.system('cls')
class APKUnbindedException(Exception):
    def __init__(self, _msg="APK is not binded yet"):
        self._msg = _msg
    def __str__(self):
        return repr(self._msg)
class APKNotFoundException(Exception):
    def __init__(self, _msg):
        self._msg = _msg
    def __str__(self):
        return repr(self._msg)
class PackageUnbindedException(Exception):
    def __init__(self, _msg="Package not binded yet"):
        self._msg = _msg
    def __str__(self):
        return repr(self._msg)
class InvalidImageSize(Exception):
    def __init__(self, _size):
        self._size = _size
    def __str__(self):
        return repr(f"Invalid Size:{self._size}")
class Session(AndroidOperation):
    def __init__(self, _host, _port, _unique_session_id=None):
        self._host = _host
        self._port = _port
        self.closed = True
        self._unique_session_id = _unique_session_id
        self.adb = "adb "
        self._time_limit = None
    def start_session(self):
        self.connect_new_device(self._host, self._port)
        self.closed = False
        return self
    def get_device(self):
        return self._host+":"+self._port
    def stop_session(self):
        self.disconnect_device(self.get_device())
        self.closed = True
    def is_closed(self):
        return self.closed
    def get_session_id(self):
        return self._unique_session_id
    def set_time_limit(self, _time_limit):
        self._time_limit = _time_limit
        return self
    def get_time_limit(self):
        return self._time_limit
class SessionManager:
    def __init__(self):
        self._sessions = []
    def add_session(self, _open_session):
        self.sync_session()
        if self.validate_session_id(_open_session):
            self._sessions.append(_open_session)
    def sync_session(self):
        for _session in self._sessions:
            if _session.is_closed():
                self._sessions.remove(_session)
    def validate_session_id(self, _open_session):
        for _session in self._sessions:
            if _open_session.get_session_id() is None:
                return True
            elif _session.get_session_id() is _open_session.get_session_id():
                print(
                    f"Session ID:{_open_session.get_session_id()} is duplicate")
                return False
        return True
    def remove_session(self, _unique_session_id):
        for _session in self._sessions:
            if _session.get_session_id() is _unique_session_id:
                self._sessions.remove(_session)
    def remove_session(self, _open_session):
        if _open_session.is_closed():
            self._sessions.remove(_open_session)
        else:
            print("Session is opened can't remove session from SessionManager")
    def get_session_unique(self, _unique_session_id):
        for _session in self._sessions:
            if _session.get_session_id() is _unique_session_id:
                return _session
    def get_session_index(self, _index):
        return self._sessions[_index]
    def close_all_session(self):
        for _session in self._sessions:
            _session.stop_session()
    def remove_all_closed_session(self):
        for _session in self._sessions:
            if _session.is_closed():
                self._sessions.remove(_session)
class SessionUnbindedException(Exception):
    def __init__(self, _msg="Session not binded yet"):
        self._msg = _msg
    def __str__(self):
        return repr(self._msg)
class CodeLightTool:
    def __init__(self):
        self._session_manager = SessionManager()
        self._ao = AndroidOperation()
        self._ao.configure()
        self._binded_session = None
        self._binded_apk = None
        self._binded_app = None
        self._binded_device_storage = None
    def __verify_session(self):
        if self._binded_session is None:
            raise SessionUnbindedException()
    def __verify_apk(self):
        if self._binded_apk is None:
            raise APKUnbindedException()
        elif os.path.isfile(self._binded_apk) is False:
            raise APKNotFoundException(_msg=f"{self._binded_apk} not found")
    def __verify_app(self):
        if self._binded_app is None:
            raise PackageUnbindedException()
    def bind_device_storage(self, _device_storage):
        self._binded_device_storage = _device_storage
    def start_server(self):
        self._ao.start_server()
    def stop_server(self):
        self._ao.kill_server()
    def restart_server(self):
        self._ao.restart_server()
    def create_session(self, _host_ip, _host_port, _id):
        session = Session(_host_ip, _host_port, _id)
        session.start_session()
        self._session_manager.add_session(
            _open_session=session
        )
        return _id
    def bind_active_session(self, _id):
        self._binded_session = self._session_manager.get_session_unique(
            _unique_session_id=_id
        )
        print(self._binded_session)
    def set_shell_mode(self, _mode):
        self.__verify_session()
        self._binded_session.set_shell_mode(_mode=_mode)
    def remove_screen_lock(self):
        self.__verify_session()
        self._ao.remove_screen_lock(
            _connected_device_name=self._binded_session.get_device()
        )
    def bind_apk(self, _apk_location_on_computer):
        self._binded_apk = _apk_location_on_computer
        self.__verify_apk()
    def install_apk(self):
        self.__verify_session()
        self.__verify_apk()
        self._ao.install_apk(
            _connected_device_name=self._binded_session.get_device(),
            _installable_apk_location=self._binded_apk
        )
    def bind_app(self, _pkg):
        self._binded_app = _pkg
    def open_device_console(self):
        self.__verify_session()
        self._ao.open_device_console(
            _connected_device_name=self._binded_session.get_device()
        )
    def uninstall_app(self):
        self.__verify_session()
        self.__verify_app()
        self._ao.uninstall_app(
            _connected_device_name=self._binded_session.get_device(),
            _installed_apk_package=self._binded_app
        )
    def disconnect_device(self):
        self.__verify_session()
        self._binded_session.stop_session()
        self._session_manager.sync_session()
        self._binded_session = None
    def set_shell_mode(self, _mode="su"):
        self.__verify_session()
        self._binded_session.set_shell_mode(_mode=_mode)
    def record_screen(self, _where_to_store):
        self.__verify_session()
        self._ao.screen_recording(
            _connected_device_name=self._binded_session.get_device(),
            _where_in_device=self._binded_device_storage,
            _where_to_store=_where_to_store,
            _time_limit=self._binded_session.get_time_limit()
        )
    def take_screen_short(self, _where_to_store):
        self.__verify_session()
        self._ao.screen_short(
            _connected_device_name=self._binded_session.get_device(),
            _where_to_store=_where_to_store,
            _where_in_device=self._binded_device_storage
        )
    def listdir(self):
        self.__verify_session()
        self._ao.show_list_files_and_directories(
            _connected_device_name=self._binded_session.get_device(),
            _parent_folder=self._binded_device_storage
        )
    def import_object(self, _where_to_store):
        self.__verify_session()
        self._ao.import_file(
            _connected_device_name=self._binded_session.get_device(),
            _remote_file_or_folder=self._binded_device_storage,
            _where_to_store=_where_to_store
        )
    def export_object(self, _which_to_export):
        self.__verify_session()
        self._ao.export_file(
            _connected_device_name=self._binded_session.get_device(),
            _remote_folder=self._binded_device_storage,
            _computer_file=_which_to_export
        )
    def reboot_device(self):
        self.__verify_session()
        self._ao.reboot_device(
            _connected_device_name=self._binded_session.get_device()
        )
    def show_log(self):
        self.__verify_session()
        self._ao.show_all_log_cat(
            _connected_device_name=self._binded_session.get_device()
        )
    def systeminfo(self):
        self.__verify_session()
        self._ao.show_system_info(
            _connected_device_name=self._binded_session.get_device()
        )
    def show_packages(self):
        self.__verify_session()
        self._ao.package_manager(
            _connected_device_name=self._binded_session.get_device()
        )
    def launch(self):
        self.__verify_session()
        self.__verify_app()
        self._ao.launch_app(
            _connected_device_name=self._binded_session.get_device(),
            _app_package=self._binded_app
        )
    def grab_wpa(self, _location_in_computer):
        self.__verify_session()
        self._ao.grab_wpa(
            _connected_device_name=self._binded_session.get_device(),
            _where_in_device=self._binded_device_storage,
            _location=_location_in_computer,
            _callable=None
        )
    def show_wlan0_ip(self):
        self.__verify_session()
        self._ao.show_wlan0_ip(
            self._binded_session.get_device()
        )
    def pull_apk(self, _where_to_store):
        self.__verify_session()
        self.__verify_app()
        self._ao.pull_apk(
            _connected_device_name=self._binded_session.get_device(),
            _installed_app_package=self._binded_app,
            _pkg_with_name=self._binded_device_storage,
            _location=_where_to_store
        )
    def show_battery_info(self):
        self.__verify_session()
        self._ao.battery_info(
            _connected_device_name=self._binded_session.get_device()
        )
    def show_net_status(self):
        self.__verify_session()
        self._ao.net_status(
            _connected_device_name=self._binded_session.get_device()
        )
    def wifi_activation(self, _state="enable"):
        self.__verify_session()
        self._ao.wifi_activation(
            _connected_device_name=self._binded_session.get_device(),
            _wifi_status=_state
        )
    def unlock_boot_loader(self):
        self.__verify_session()
        AndroidOperation.unlock_oem(
            _connected_device_name=self._binded_session.get_device()
        )
    def fire_key_event(self, _key_code):
        self.__verify_session()
        self._ao.press_key(
            _connected_device_name=self._binded_session.get_device(),
            _key_code=_key_code
        )
    def show_current_activity(self):
        self.__verify_session()
        self._ao.show_current_activity(
            _connected_device_name=self._binded_session.get_device()
        )
    def app_visibility(self, _status="hide"):
        self.__verify_session()
        self.__verify_app()
        self._ao.app_visibility(
            _connected_device_name=self._binded_session.get_device(),
            _app_pkg=self._binded_app,
            _visibility=_status
        )
    def blue_tooth_activation(self, _status="true"):
        self.__verify_session()
        self._ao.blue_tooth_activation(
            _connected_device_name=self._binded_session.get_device(),
            _operation=_status
        )
    def make_a_call(self, _contact_number):
        self.__verify_session()
        self._ao.make_a_call(
            _connected_device_name=self._binded_session.get_device(),
            _contact_number=_contact_number
        )
class InvalidStorage(Exception):
    def __init__(self, _msg):
        self._msg = _msg
    def __str__(self):
        return repr(self._msg)
class InvalidPayLoadFile(Exception):
    def __init__(self, _msg):
        self._msg = _msg
    def __str__(self):
        return repr(self._msg)
class PayLoadFileNotFound(Exception):
    def __init__(self, _file_name, _msg):
        self._msg = _msg
        self._file_name = _file_name
    def __str__(self):
        return repr(f"FileName:{self._file_name} description:{self._msg}")
class SessionIdNullException(Exception):
    def __init__(self, _msg):
        self._msg = _msg
    def __str__(self):
        return repr(self._msg)
class DuplicateSessionId(Exception):
    def __init__(self, _msg):
        self._msg = _msg
    def __str__(self):
        return repr(self._msg)
class PayLoad:
    def __init__(self):
        self._target_name = None
        self._target_ip = None
        self._target_port = 5426
        self._storage_dir = ''
    @staticmethod
    def __validate_directory(_dir):
        if os.path.isdir(_dir) is False:
            raise InvalidStorage(_msg=f"Invalid directory:{_dir}")
    def __validate_file(self, _file):
        if os.path.isfile(f"{self._storage_dir}{_file}") is False:
            raise PayLoadFileNotFound(
                _file_name=_file, _msg="File not found in specified directory:"+self._storage_dir)
    def __configure_internal(self, _target_ip=None, _target_port=5426, _storage_dir=''):
        self._target_ip = _target_ip
        self._target_port = _target_port
        PayLoad.__validate_directory(_storage_dir)
        self._storage_dir = _storage_dir
    def __extract_payload_file_info(self, _target_pay_load):
        self.__validate_file(_file=_target_pay_load)
        with open(self._storage_dir+_target_pay_load, mode='r') as _f:
            self._target_name = _f.readline()
            self._target_ip = _f.readline()
            self._target_port_ = _f.readline()
        self._storage_dir = ''
    def set_payload_directory(self, _dir):
        PayLoad.__validate_directory(_dir=_dir)
        self._storage_dir = _dir
    def configure_payload(self, _target_ip=None, _target_port=5426):
        self.__configure_internal(
            _target_ip=_target_ip, _target_port=_target_port, _storage_dir=self._storage_dir)
    def configure_payload_file(self, _target_pay_load):
        self.__extract_payload_file_info(_target_pay_load=_target_pay_load)
    def show_payload_info(self):
        print("PayLoad Name:", self._target_name)
        print("PayLoad IP:", self._target_ip)
        print("PyaLoad PORT:", self._target_port)
    def get_name(self):
        return self._target_name
    def get_ip(self):
        return self._target_ip
    def get_port(self):
        return self._target_port
class MetaSession:
    def __init__(self, _valid_pay_load, _session_id):
        self._valid_pay_load = _valid_pay_load
        self._connection = socket.socket()
        self._is_active = False
        if _session_id is None:
            raise SessionIdNullException(_msg="Session id can't be None")
        self._session_id = _session_id
    def activate_session(self):
        try:
            self._connection.connect(
                (self._valid_pay_load.get_ip(), self._valid_pay_load.get_port()))
            self._is_active = True
        except IOError as e:
            print(e)
        return self
    def is_active(self):
        return self._is_active
    def fire_command(self, command=b'su'):
        self._connection.send(command)
    def get_output(self):
        return self._connection.recv(2048)
    def deactivate(self):
        self._connection.close()
        self._is_active = False
    def get_session_id(self):
        return self._session_id
class MetaSessionManager:
    def __init__(self):
        self._sessions = []
    def __sync_session(self):
        for _session in self._sessions:
            if _session.is_active() is False:
                self._sessions.remove(_session)
    def verify_session_id(self, _active_session):
        for _session in self._sessions:
            if _active_session.get_session_id() is _session.get_session_id():
                raise DuplicateSessionId(
                    _msg=f"Duplicate id:{_active_session.get_session_id()}")
    def add_active_session(self, _active_session):
        self.__sync_session()
        self.verify_session_id(_active_session=_active_session)
        if _active_session.is_active():
            self._sessions.append(_active_session)
    def remove_all_closed_session(self):
        self.__sync_session()
    def disconnect_all_session(self):
        for _session in self._sessions:
            _session.deactivate()
        self.__sync_session()
if __name__ == "__main__":
    print("Hello World!")
