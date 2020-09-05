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
from PIL import Image
from com.cosmo.sploit.codelight.exception.codelightexceptions import InvalidImageSize
from colorama import Fore,init,Back
class ConsoleImage:
    def __init__(self,_image_path):
        init()
        self._image=Image.open(_image_path)
    def __verify_size(self):
        if self._image.size == (64,64) or self._image.size == (32,32):
            return True
        raise InvalidImageSize(_size=self._image.size)
    def draw_image(self):
        self.__verify_size()
        size= self._image.size
        for y in range(size[1]):
            for x in range(size[0]):
                if self._image.getpixel((x, y))[3] > 0:
                    print(f"{Fore.GREEN}", end="1")
                else:
                    print(f"{Back.BLACK}", end=" ")
            print(Back.BLACK + "")

