from org.cosmo.sploit.codelight.codelighttool import CodeLightTool
clt=CodeLightTool()
clt.restart_server()
try:
 nox_debug_id=clt.create_session(_host_ip="localhost",_host_port="62001",_id="nox_vm_debug_identification")
 clt.bind_active_session(_id=nox_debug_id)
 clt.bind_device_storage(_device_storage="storage/emulated/legacy")
 clt.show_packages()
 while True:
     try:
      pkg=input("Enter app package you want to hide or unhide:")
      clt.bind_app(_pkg=pkg)
      flag=input("unhide/hide:")
      clt.app_visibility(_status=flag)
     except KeyboardInterrupt:
         break
 clt.disconnect_device()
 clt.stop_server()
except KeyboardInterrupt:
    print("Disconnecting unhandled")
    clt.disconnect_device()
    clt.stop_server()
