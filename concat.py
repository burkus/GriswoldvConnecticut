#! python
# Concatenate the slides into a single file
import os
from os.path import isfile

slidesPath = os.getcwd() + r"\slides"
slideFiles = os.listdir(slidesPath)

slides = ""
for file in slideFiles:
    if "posix" in os.name:
        filePath = slidesPath + '/' + file
    else:
        filePath = slidesPath + "\\" + file
    html = open(filePath, 'r').read()
    slides += html

def writeConcatFile(contents):
    concatFilePath = os.getcwd()
    if "posix" in os.name:
        concatFilePath += '/concat.html'
    else:
        concatFilePath += r"\concat.html"
    if isfile(concatFilePath):
        os.remove(concatFilePath)
    concatFile = open('concat.html', 'w+')
    concatFile.write(contents)

templateFilePath = os.getcwd() + r"\template.html"
templateFileHtml = open(templateFilePath, "r").read()
finalString = ""
if "$" in templateFileHtml:
    insertIndex = templateFileHtml.find('$')
    preInsertString = templateFileHtml[0:insertIndex]
    postInsertString = templateFileHtml[insertIndex + 1:]
    finalString = preInsertString + slides + postInsertString
    writeConcatFile(finalString)
