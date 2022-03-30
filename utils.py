from wand.image import Image
import os

def resize_photo(name):
    ny = Image(filename=os.getcwd()+'/images/'+name)
    ny.resize(140,140)
    ny.save(filename=os.getcwd()+'/images/'+name)