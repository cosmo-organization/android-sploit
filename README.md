# AndroidSploitAPI
Android Sploit API for Python development on windows or linux both

# Prequisite on Windows

pip install colorama<br>
python main.py<br>
or use com.cosmo.sploit.tools to embed in your own application
# Prequisite on Linux
# Skip adb.rar for Linux
pip install colorama<br>
python3 main.py<br>
or use com.cosmo.sploit.tools to embed in your own application
When you start main.py ask for installing adb if you have already installed press y to continue or n for install
<a href="https://github.com/sonuaryan7644/AndroidSploitAPI.git"> Download</a>
# Welcome to Cosmo
# using Android Sploit API
# Enable debuging mode in developer option
# example start and restart and kill ADB server
from com.cosmo.sploit.tools import ADB<br>
adb=ADB()<br>
adb.start_server() #start server for perform operation<br>
adb.restart_server() #restart server<br>
adb.kill_server() #kill server<br>
# example remove lock-screen
from com.cosmo.sploit.tools import Session,ADB<br>
adb=ADB()<br>
adb.start_server()<br>
s=Session("localhost","62001") #  62001 port is only work for Nox 5555 for android devices and enter IP address<br>
s.start_session()<br>
s.remove_screen_lock(s.get_device(),_su='') # su is used for super user mode use _su='su' on super user supported device or emulater<br>
adb.kill_server()<br>

