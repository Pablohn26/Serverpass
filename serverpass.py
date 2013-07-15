#!/usr/bin/python
import getpass,os,subprocess


####CONFIG
passpath="./"
enc_protocol="aes256"
format=".cy"
deletepath="/tmp/"

####FUNCTIONS

def sget(stringtoprint):
    try:
        name=str(raw_input(stringtoprint))
        return name
    except KeyboardInterrupt:
        print "\nKeyboard Interruption"
        exit

def ask_option():
    print "1.Add pass"
    print "2.Get pass"
    option=sget("Option (type only the number):")
    if option==str(1):
        add_pass()
    elif option==str(2):
        get_pass()
    else:
        print "wrong option :("

def get_user():
    return sget("Insert user:\n")

def get_password():
    return getpass.getpass()

def invert(var):
        return var[::-1]

def checkfile(path):
    if os.path.isfile(path):
        return True
    else:
        return False

def add_pass():
    name=get_user()
    name=invert(name)
    if checkfile(passpath+str(name)):
        print str(name)+" password file already exists"
    else:
         password=get_password()
         file=open(passpath+str(name),"w")
         file.write(password)
         file.close()
         print "Enter MASTER PASSWORD"
         os.system("openssl enc -"+str(enc_protocol)+" -in "+str(passpath)+str(name)+" -out "+str(passpath)+str(name)+str(format))
         os.system("shred "+str(passpath)+str(name)+" -u")

def get_pass():
    name=get_user()
    name=invert(name)
    if checkfile(passpath+str(name)+str(format)):
        os.system("openssl enc -d -"+str(enc_protocol)+" -in "+str(passpath)+str(name)+str(format)+" -out "+str(deletepath)+"something.old")
        os.system("cat "+str(deletepath)+"something.old")
        os.system("shred "+str(deletepath)+"something.old"+" -u")
        print ""

    else:
        print "Username not found!"
        exit
    

####MAIN
ask_option()

##COPYRIGHT 2013 Pablo Hinojosa 
#site:pablohinojosa.is
#Version:05/07/2013
##LICENSE
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
