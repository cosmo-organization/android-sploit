'''
@author Sonu Aryan(cosmo-developer)
BSD 3-Clause License

Copyright (c) 2020, Cosmo Org
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
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