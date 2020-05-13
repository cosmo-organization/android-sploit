from com.cosmo.sploit.core import \
    Session,\
    SessionManager,\
    AndroidOperation
from com.cosmo.sploit.codelight.exception.codelightexceptions import \
    SessionUnbindedException,\
    APKUnbindedException,\
    APKNotFoundException,\
    PackageUnbindedException
import os
class CodeLightTool:
    def __init__(self):
        self._session_manager=SessionManager()
        self._ao=AndroidOperation()
        self._ao.configure()
        self._binded_session=None
        self._binded_apk=None
        self._binded_app=None
        self._binded_device_storage=None
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
    def bind_device_storage(self,_device_storage):
        self._binded_device_storage=_device_storage
    def start_server(self):
        self._ao.start_server()
    def stop_server(self):
        self._ao.kill_server()
    def restart_server(self):
        self._ao.restart_server()
    def create_session(self,_host_ip,_host_port,_id):
        session=Session(_host_ip,_host_port,_id)
        session.start_session()
        self._session_manager.add_session(
            _open_session=session
        )
        return _id
    def bind_active_session(self,_id):
        self._binded_session=self._session_manager.get_session_unique(
            _unique_session_id=_id
        )
        print(self._binded_session)
    def set_shell_mode(self,_mode):
        self.__verify_session()
        self._binded_session.set_shell_mode(_mode=_mode)
    def remove_screen_lock(self):
        self.__verify_session()
        self._ao.remove_screen_lock(
            _connected_device_name=self._binded_session.get_device()
        )
    def bind_apk(self,_apk_location_on_computer):
         self._binded_apk=_apk_location_on_computer
         self.__verify_apk()
    def install_apk(self):
        self.__verify_session()
        self.__verify_apk()
        self._ao.install_apk(
            _connected_device_name=self._binded_session.get_device(),
            _installable_apk_location=self._binded_apk
        )
    def bind_app(self,_pkg):
        self._binded_app=_pkg
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
        self._binded_session=None
    def set_shell_mode(self,_mode="su"):
        self.__verify_session()
        self._binded_session.set_shell_mode(_mode=_mode)
    def record_screen(self,_where_to_store):
        self.__verify_session()
        self._ao.screen_recording(
            _connected_device_name=self._binded_session.get_device(),
            _where_in_device=self._binded_device_storage,
            _where_to_store=_where_to_store,
            _time_limit=self._binded_session.get_time_limit()
        )
    def take_screen_short(self,_where_to_store):
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
    def import_object(self,_where_to_store):
        self.__verify_session()
        self._ao.import_file(
            _connected_device_name=self._binded_session.get_device(),
            _remote_file_or_folder=self._binded_device_storage,
            _where_to_store=_where_to_store
        )

    def export_object(self,_which_to_export):
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
    def grab_wpa(self,_location_in_computer):
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
    def pull_apk(self,_where_to_store):
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
    def wifi_activation(self,_state="enable"):
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
    def fire_key_event(self,_key_code):
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
    def app_visibility(self,_status="hide"):
        self.__verify_session()
        self.__verify_app()
        self._ao.app_visibility(
            _connected_device_name=self._binded_session.get_device(),
            _app_pkg=self._binded_app,
            _visibility=_status
        )
    def blue_tooth_activation(self,_status="true"):
        self.__verify_session()
        self._ao.blue_tooth_activation(
            _connected_device_name=self._binded_session.get_device(),
            _operation=_status
        )
    def make_a_call(self,_contact_number):
        self.__verify_session()
        self._ao.make_a_call(
            _connected_device_name=self._binded_session.get_device(),
            _contact_number=_contact_number
        )

