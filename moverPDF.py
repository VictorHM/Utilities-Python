#Mover archivos de un directorio a otro
#Especificamente, tras transformar libros con calibre
#se extraen los pdfs de los directorios que crea

import os, shutil, re

# Function CopyFiles(string, string, string)
#Copy the specified files from original path to destination
#
# origPath: the original path where the files are (posibly inside subfolders)
# finalPath: final destination where to copy the files
# fileFormat: file format of the files we want to copy to destination

def CopyFiles(origPath, finalPath, fileFormat):
    for foldername, subfolders, filenames in os.walk(origPath):
        for sub in subfolders:
            for fold, subs, files in os.walk(sub):
                for file in files:
                    if(file.endswith(fileFormat)):
                        fullpath = os.path.join(foldername, fold, file)
                        shutil.copy(fullpath, finalPath)

# TODO This recursive function still doesn't work as expected
# Work in Progress
def CopyRecursive(origPath, finalPath, fileFormat):
    for foldername, subfolders, filenames in os.walk(origPath):
        if(subfolders):
            for subfold in subfolders:
                CopyRecursive(subfold, finalPath, fileFormat)
                
        fullpath = os.path.join(foldername, subfold, file)
        shutil.copy(fullpath, finalPath)

# POINT OF ENTRY
os.chdir(r'/media/victor/USB/Libros/Calibre Portable/Calibre Library/')
print('Directorio actual: ' + os.getcwd())

origpath = os.getcwd()
destpath = r'/home/victor/Documents/Libros/'
print('Starting to gather and copying files...')
#recorrer cada subdirectorio y obtener el path del archivo PDF
CopyFiles(origpath, destpath, r'.pdf')
print('End')
