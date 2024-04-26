#!/usr/bin/python
"""
Author             : Prof Docal
contact            : aliesmansaray2004@gmail.com
Github             : https://github.com/Prof-Docal
"""

import sys
import os.path
import subprocess

ntfile = ['.modules', 'lib']

ubuntu = '' + str(open('.modules/jalurU.ms').read())
termux = '' + str(open('.modules/jalurT.ms').read())
termlb = '' + str(open('.modules/ngentot.ms').read())
instal = '' + str(open('.modules/IN.ms').read())


def _main_():
    if os.path.isdir('' + ubuntu.strip()):
        if os.getuid() != 0:
            print '[x] Failed: you must be root'
            sys.exit()

        if not os.path.isdir(ntfile[0]):
            print '[x] Failed: no directory modules'
            sys.exit()

        if not os.path.isdir(ntfile[1]):
            print '[x] Failed: no directory lib'
            sys.exit()
        else:

            print '' + instal.strip()

            # ==================================================================#

            os.system('python .modules/files/' + str(open('.modules/A.ms'
                      ).read()))
            os.system('python .modules/files/' + str(open('.modules/B.ms'
                      ).read()))
            os.system('python .modules/files/' + str(open('.modules/C.ms'
                      ).read()))
            os.system('python .modules/files/' + str(open('.modules/D.ms'
                      ).read()))
            os.system('python .modules/files/' + str(open('.modules/E.ms'
                      ).read()))
            os.system('python .modules/files/' + str(open('.modules/F.ms'
                      ).read()))
            os.system('python .modules/files/' + str(open('.modules/G.ms'
                      ).read()))
            os.system('python .modules/files/' + str(open('.modules/H.ms'
                      ).read()))

            # ==================================================================#

            if os.path.isdir('/usr/bin/lib'):
                os.system('rm -rf /usr/bin/lib')
                os.system('' + str(open('.modules/pindahU.ms').read()))
                os.system('' + str(open('.modules/PindahU.ms').read()))

            if not os.path.isdir('/usr/bin/lib'):
                os.system('' + str(open('.modules/pindahU.ms').read()))
                os.system('' + str(open('.modules/PindahU.ms').read()))

            # ==================================================================#

            print '' + str(open('.modules/DU.la').read())
            print '' + str(open('.modules/Du').read())
            os.system('python .JM.xn')

            # ==================================================================#

    if os.path.isdir('' + termux.strip()):
        if not os.path.isdir('' + termux.strip()):
            sys.exit()

        if not os.path.isdir(ntfile[0]):
            print '[x] Failed: no directory modules'
            sys.exit()

        if not os.path.isdir(ntfile[1]):
            print '[x] Failed: no directory lib'
            sys.exit()
        else:

            print '' + instal.strip()

            # ==============================================================#

            os.system('python2 .modules/' + str(open('.modules/A.ms'
                      ).read()))
            os.system('python2 .modules/' + str(open('.modules/B.ms'
                      ).read()))
            os.system('python2 .modules/' + str(open('.modules/C.ms'
                      ).read()))
            os.system('python2 .modules/' + str(open('.modules/D.ms'
                      ).read()))
            os.system('python2 .modules/' + str(open('.modules/E.ms'
                      ).read()))
            os.system('python2 .modules/' + str(open('.modules/F.ms'
                      ).read()))
            os.system('python2 .modules/' + str(open('.modules/G.ms'
                      ).read()))
            os.system('python2 .modules/' + str(open('.modules/H.ms'
                      ).read()))

            # ==============================================================#

            if os.path.isdir('' + termlb.strip()):
                os.system('' + str(open('.modules/pacar.ms').read()))
                os.system('' + str(open('.modules/pindahT.ms').read()))
                os.system('' + str(open('.modules/PINDAHT.txt').read()))

            if not os.path.isdir('' + termlb.strip()):
                os.system('' + str(open('.modules/pindahT.ms').read()))
                os.system('' + str(open('.modules/PINDAHT.txt').read()))

            # ==============================================================#

            print '' + str(open('.modules/DU.la').read())
            print '' + str(open('.modules/Du.txt').read())
            os.system('python2 .JM.xn && cd')


            # ==============================================================#

if __name__ == '__main__':
    _main_()
