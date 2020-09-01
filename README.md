# AndroidSploitAPI
Android Sploit API for Python development on cross-platform
<br>
<table>
<tr>
 <th>version</th>
 <th>Features</th>
 <th>Download</th>
</tr>
<tr>
  <td>1.0</td>
  <td>core feature final</td>
  <td><a href="#">Download</a></td>
</tr>
<tr>
  <td>1.1</td>
  <td>CodeLight feature</td>
  <td><a href="#">Download</a></td>
</tr>
<tr>
  <td>1.1.a</td>
  <td>Upcomming dynamic error reporting</td>
  <td><a href="#">Download</a></td>
</tr>

```Help on class ADB in module com.cosmo.sploit.tools:

class ADB(builtins.object)
 |  ADB is responsible for containing basic functions of Android Debug Bridge
 |  
 |  Methods defined here:
 |  
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  adb_c(self, sub_command)
 |      Use adb_c to command in adb
 |      adb=ADB()
 |      adb.adb_c("-s localhost:62001 -shell rm test.txt")
 |      There are several function which uses adb_c to command
 |  
 |  configure(self)
 |      configure is used to configure automatically on linux or windows.
 |      Now it's become empty and run on cross platform
 |  
 |  kill_server(self)
 |      Same as adb kill-server
 |  
 |  restart_server(self)
 |      Sam as adb kill-server & start-server
 |  
 |  start_server(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
```
</table>