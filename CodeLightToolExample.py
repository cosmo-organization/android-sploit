from com.cosmo.sploit.codelight.codelighttool import CodeLightTool
cl=CodeLightTool()
cl.start_server()
#For First Device
cl.create_session(_host_ip="localhost",_host_port="62001",_id="1")
cl.bind_active_session("1")
cl.remove_screen_lock()
cl.bind_apk(_apk_location_on_computer="C:\\Users\\User Name\\YourDirectory\\File.apk")
cl.install_apk()
cl.bind_app(_pkg="com.cosmo.android.tool.metasploit")
cl.uninstall_app()
cl.disconnect_device()
#End for First Device

#For Second Device

cl.create_session(_host_ip="localhost",_host_port="5555",_id="1")
cl.bind_active_session("1")
cl.remove_screen_lock()
cl.bind_apk(_apk_location_on_computer="C:\\Users\\User Name\\YourDirectory\\Test.apk")
cl.install_apk()
cl.bind_app(_pkg="com.cosmo.android.tool.metasploit")
cl.uninstall_app()
cl.disconnect_device()

#End for Second Device

#For n devices



#end for n devices

cl.stop_server()
