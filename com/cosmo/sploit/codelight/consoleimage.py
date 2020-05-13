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

