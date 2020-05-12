from com.cosmo.sploit.tools import Session,SessionManager,AndroidOperation
from com.cosmo.sploit.codelight.exception.codelightexceptions import SessionUnbindedException,APKUnbindedException,APKNotFoundException,PackageUnbindedException
import os
class CodeLightTool:
    def __init__(self):
        self._session_manager=SessionManager()
        self._ao=AndroidOperation()
        self._ao.configure()
        self._binded_session=None
        self._binded_apk=None
        self._binded_app=None

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

    def start_server(self):
        self._ao.start_server()
    def stop_server(self):
        self._ao.kill_server()
    def restart_server(self):
        self._ao.restart_server()
    def create_session(self,_host_ip,_host_port,_id):
        session=Session(_host_ip,_host_port,_id)
        session.start_session()
        self._session_manager.add_session(_open_session=session)
        return _id
    def bind_active_session(self,_id):
        self._binded_session=self._session_manager.get_session_unique(_unique_session_id=_id)
        print(self._binded_session)
    def set_shell_mode(self,_mode):
        self.__verify_session()
        self._binded_session.set_shell_mode(_mode=_mode)
    def remove_screen_lock(self):
        self.__verify_session()
        self._ao.remove_screen_lock(_connected_device_name=self._binded_session.get_device())
    def bind_apk(self,_apk_location_on_computer):
         self._binded_apk=_apk_location_on_computer
         self.__verify_apk()
    def install_apk(self):
        self.__verify_session()
        self.__verify_apk()
        self._ao.install_apk(_connected_device_name=self._binded_session.get_device(),_installable_apk_location=self._binded_apk)
    def bind_app(self,_pkg):
        self._binded_app=_pkg
    def open_device_console(self):
        self.__verify_session()
        self._ao.open_device_console(_connected_device_name=self._binded_session.get_device())
    def uninstall_app(self):
        self.__verify_session()
        self.__verify_app()
        self._ao.uninstall_app(_connected_device_name=self._binded_session.get_device(),_installed_apk_package=self._binded_app)
    def disconnect_device(self):
        self.__verify_session()
        self._binded_session.stop_session()
        self._session_manager.sync_session()
        self._binded_session=None

