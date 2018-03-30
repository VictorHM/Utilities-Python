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

#TODO: hacer la función recursiva para poder entrar en todos los directorios que haya
#la recursividad se basará en si hay o no subdirectorios
def CopyFiles(origPath, finalPath, fileFormat):
    for foldername, subfolders, filenames in os.walk(origPath):
        for sub in subfolders:
            for fold, subs, files in os.walk(sub):
                for file in files:
                    if(file.endswith(fileFormat)):
                        fullpath = os.path.join(foldername, fold, file)
                        shutil.copy(fullpath, finalPath)


def CopyRecursive(origPath, finalPath, fileFormat):
    for foldername, subfolders, filenames in os.walk(origPath):
        if(subfolders):
            for subfold in subfolders:
                CopyRecursive(subfold, finalPath, fileFormat)
                
        fullpath = os.path.join(foldername, subfold, file)
                        shutil.copy(fullpath, finalPath)
os.chdir(r'D:\Librerias de programas\Calibre')
print('Directorio actual: ' + os.getcwd())

origpath = os.getcwd()
destpath = r'D:\Librerias de programas\Documentos\Documentos y libros\Programación y tecnología\PythonTest'
#recorrer cada subdirectorio y obtener el path del archivo PDF
CopyFiles(origpath, destpath, r'.pdf')
##for foldername, subfolders, filenames in os.walk(r'D:\Librerias de programas\Calibre'):
##    print('Foldername ', foldername)
##    for sub in subfolders:
##        print('Present subfolder: ' + sub)
##        for fold, subs, files in os.walk(sub):
####            print('Folder ')
####            print(fold)
####            print('Files ')
####            print(files)
####            print(' Subs ')
####            print(subs)
####            input("Pulsa una tecla para continuar...")
##            for file in files:
##                    if(file.endswith('.pdf')):
##                        print('Copiando archivo ' + file + ' desde ' + foldername)
##                        fullpath = os.path.join(foldername, fold, file)
##                        print('Fullpath: ' + fullpath)
##                        shutil.copy(fullpath, r'D:\Librerias de programas\Documentos\Documentos y libros\Programación y tecnología\PythonTest')
print('End')
