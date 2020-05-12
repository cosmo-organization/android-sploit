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
cl.disconnect_device() # if this step execute then session id 1 is destroyed permanentely you need to create one
# if session is not disconnect a session then you can't use same id to create another session use another id
#End for First Device

#For Second Device

cl.create_session(_host_ip="localhost",_host_port="5555",_id="1")
cl.bind_active_session("1")
cl.remove_screen_lock()
cl.bind_apk(_apk_location_on_computer="C:\\Users\\User Name\\YourDirectory\\Test.apk")
cl.install_apk()
cl.bind_app(_pkg="com.cosmo.android.tool.metasploit") #this package is already binded you can skip this step or bind your own package to continue
cl.uninstall_app()
cl.disconnect_device()

#End for Second Device

#For n devices



#end for n devices

cl.stop_server()
