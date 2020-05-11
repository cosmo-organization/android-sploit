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
#Welcome to Cosmo
#using Android Sploit API
#example start and restart and kill ADB server
from com.cosmo.sploit.tools import ADB
adb=ADB()
adb.start_server()//start server for perform operation

adb.restart_server()//restart server
adb.kill_server()//kill server
