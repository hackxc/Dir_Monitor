#!/usr/bin/python
#-*- coding:utf-8 -*-
import os,sys
import shutil
from optparse import OptionParser

def main():
    print(u'\n监听中...\n')
    while True:
        for dirpath, dirnames, files in os.walk(Ldirname):
           if dirpath not in dirname:
               print('[+]Find dirname：',dirpath)
               dirname.append(dirpath)
           if files not in dirname:
               for file in files:
                   if file not in dirname:
                       dirfile = os.path.join(dirpath,file)
                       print('[+]Find file：', dirfile)
                       dirname.append(file)
                       if(Spath):
                           shutil.move(dirfile, '%s%s'%(Spath,file))

if __name__ == '__main__':
    usage='%s -l <Listen dirname> -s <Save the path>'%os.path.basename(sys.argv[0])
    parser = OptionParser(usage=usage)
    parser.add_option("-l",dest="dirname",help="Listen dirname")
    parser.add_option("-s",dest="path",help="Save the path")
    (options, args) = parser.parse_args()
    try:
        Ldirname = options.dirname
        Spath = options.path
        dirname = []
        for dirpath, dirnames, files in os.walk(Ldirname):
            dirname.append(dirpath)
            for file in files:
                dirname.append(file)
        main()
    except:
        print(usage)