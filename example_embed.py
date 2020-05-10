# Example to embed com.cosmo.sploit.tools api
from com.cosmo.sploit.tools import AndroidOperation,DeviceConnection,ConsoleWindow,ADB
adb=ADB()#Server already started on initialization this feature will remove in future
adb.configure()#For platform & tools validation
dc=DeviceConnection()
cw=ConsoleWindow()
ao=AndroidOperation()
adb.start_server()
dc.connect_new_device(_host_ip="198.25.12.36",_host_port=5555)
ao.screen_short(_connected_device_name="198.25.12.36:5555","C:\User Name\Desktop\imported_image\")
ao.remove_screen_lock(_connected_device_name="198.25.12.36:5555")
ao.reboot_device()
cw.clear_src()
dc.disconnect_all_device()
adb.kill_server()
