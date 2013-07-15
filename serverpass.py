#!/usr/bin/python
import getpass,os,subprocess,argparse,glob


####CONFIG
passpath="./"
deletepath="/tmp/"
enc_protocol="aes256"
format=".cy"


####FUNCTIONS

def sget(stringtoprint):
    try:
        name=str(raw_input(stringtoprint))
        return name
    except KeyboardInterrupt:
        print "\nKeyboard Interruption"
        exit

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
    if checkfile(passpath+str(name)+str(format)):
        print str(name)+" password file already exists"
    else:
         password=get_password()
         file=open(passpath+str(name),"w")
         file.write(password)
         file.close()
         print "Enter MASTER PASSWORD"
         os.system("openssl enc -"+str(enc_protocol)+" -in "+str(passpath)+str(name)+" -out "+str(passpath)+str(name)+str(format))
         os.system("shred "+str(passpath)+str(name)+" -u")
         print invert(name)+" was successfully added"

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
def delete_pass():
    print "Stored Passwords"
    list_pass()
    to_delete=sget("Select a password to delete\n")
    to_delete2=passpath+invert(to_delete)+format
    os.remove(to_delete2)
    print to_delete+" was successfully removed"

def list_pass():
    constraint=passpath+str("*")+format
    for i in glob.glob(constraint):
        stored_pass = i.replace(passpath, "")
        stored_pass2 = invert(stored_pass.replace(format, ""))
        print stored_pass2
        
        

####MAIN
parser = argparse.ArgumentParser()
parser.add_argument("-a","--add", help="Add password",action="store_true")
parser.add_argument("-d","--delete", help="Delete password",action="store_true")
parser.add_argument("-g","--get", help="Get your stored password",action="store_true")
parser.add_argument("-l","--list", help="List your stored passwords",action="store_true")
args = parser.parse_args()
if args.get:
    get_pass()
elif args.add:
    add_pass()
elif args.list:
    list_pass()
elif args.delete:
    delete_pass()
else:
    parser.print_help()
    
##ask_option()

##COPYRIGHT 2013 Pablo Hinojosa 
#site:pablohinojosa.is
#Version: 1.1 (11/07/2013)
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
