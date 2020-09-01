from com.cosmo.sploit.tools import *
ADB.__doc__ = '''
 ADB is responsible for containing basic functions of Android Debug Bridge
'''
ADB.adb_c.__doc__ = '''
 Use adb_c to command in adb
 adb=ADB()
 adb.adb_c("-s localhost:62001 -shell rm test.txt")
 There are several function which uses adb_c to command
'''
ADB.configure.__doc__ = '''
 configure is used to configure automatically on linux or windows.
 Now it's become empty and run on cross platform
'''
ADB.kill_server.__doc__ = '''
 Same as adb kill-server
'''
ADB.restart_server.__doc__='''
 Sam as adb kill-server & start-server
'''
DeviceConnection.__doc__ = '''
 dc=DeviceConnection() #parent ADB
 #use ADB functions via DeviceConnection
 #or
'''
if __name__ == "__main__":
    help(ADB)