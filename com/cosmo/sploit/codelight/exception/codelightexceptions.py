class SessionUnbindedException(Exception):
    def __init__(self,_msg="Session not binded yet"):
        self._msg=_msg
    def __str__(self):
        return repr(self._msg)
class APKUnbindedException(Exception):
    def __init__(self,_msg="APK is not binded yet"):
        self._msg=_msg
    def __str__(self):
        return repr(self._msg)
class APKNotFoundException(Exception):
    def __init__(self,_msg):
        self._msg=_msg
    def __str__(self):
        return repr(self._msg)
class PackageUnbindedException(Exception):
    def __init__(self,_msg="Package not binded yet"):
        self._msg=_msg
    def __str__(self):
        return repr(self._msg)
class InvalidImageSize(Exception):
    def __init__(self,_size):
        self._size=_size
    def __str__(self):
        return repr(f"Invalid Size:{self._size}")
class DeviceStorageUnbindedException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return repr("Device Storage not specified")
class DeviceFileUnbindedException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return repr("Device File not specified")
class FaultInAPIException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return repr("API not working properly")