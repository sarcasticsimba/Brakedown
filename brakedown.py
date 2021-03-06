#!/usr/bin/env python

import os
import re
import shutil
import sys
import argparse

#Parsing parameters
parser = argparse.ArgumentParser()
parser.add_argument("path", nargs="?", default=os.getcwd())
args = parser.parse_args()
if os.path.exists(os.path.join(os.getcwd(), args.path)):
	stylespath = os.path.join(os.getcwd(), args.path, "styles")
	imagepath = os.path.join(os.getcwd(), args.path)
elif os.path.exists(args.path):
	stylespath = os.path.join(args.path, "styles")
	imagepath = args.path
else:
	print("Path doesn't exist!")
	quit()

#Creating directory
os.chdir(imagepath)
if os.path.exists("styles"):
	shutil.rmtree("styles")
	os.mkdir("styles")
else:
	os.mkdir("styles")

#Creating CSS
os.chdir(stylespath)
css = open("styles.css", "w")
tempStyles = open("template.css", "w")
tempStyles.write(".datauri {\n\twidth: 50px;\n\theight: 50px;\n\tbackground-repeat: no-repeat;\n\tbackground-size: 50px 50px;\n}\n\n")
tempStyles.close()
os.chdir("..")
svgs = [img for img in os.listdir(imagepath) if img.lower().endswith(".svg")]
names = [] #Used to format HTML
for svg in svgs:
	image = open(svg, "r")
	names.append(os.path.splitext(svg)[0])
	css.write("." + os.path.splitext(svg)[0] + " {\n\tbackground-image: url('data:image/svg+xml,")
	css.write(re.sub("\n|\t", "", image.read()))
	css.write("');\n}\n\n")
	image.close()
css.close()

#Formatting sample HTML document
os.chdir(stylespath)
html = open("template.html", "w+")
html.write("<html>\n\t<head>\n\t\t<link rel='stylesheet' type='text/css' href='styles.css'></link>\n\t\t<link rel='stylesheet' type='text/css' href='template.css'></link>\n\t</head>\n\t<body style='background-color: #eee'>\n\t\t<h1>SVG Icons</h1>")
for classname in names:
	html.write("\n\t\t<h3>" + classname + "</h3><div class = 'datauri " + classname + "'></div>")
html.write("\n\t</body>\n</html>")