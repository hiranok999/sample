from PIL import Image
import sys
import os
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))
# imgid=1
# img = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/sample" + str(imgid) + ".png", "r")
img = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/webpage" + ".png", "r")
print(img)
txt = tool.image_to_string(
    img,
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
print(txt)
# txt is a Python string
