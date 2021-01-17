import os
from time import sleep
os.system("clear")

def cli_automation(n):
    while True:
            os.system("tput setaf  5")
            print()
            print("----------------------------AWS-CLI Installation---------------------------")
            os.system("tput setaf  7")
            if n == "local":
                       print()
                       print("""
                             \n
                             \t\t\t\t Press 1 : Install AWS-CLI
                             \t\t\t\t Press 2 : Configure AWS-CLI
                             \t\t\t\t Press 3 : Go Back to Previous Menu
                             """)
                       os.system("tput setaf 8")
                       ch = int(input("Enter your Choice: "))
                       print()
                       os.system("tput setaf 80")
                       if ch == 1:
                            print("Installing AWS-CLI.......")
                            os.system("pip3 install awscli")
                            print()
                            print("Successfully Installed.....")
                       elif ch == 2:
                            print("Configure your IAM .....")
                            print()
                            os.system("aws configure")
                       elif ch == 3:
                            exit()
                       else: 
                           print("please choose the appropriate option as mention above")
            elif n == "remote":
                       sleep(1)
                       print("""
                             \n
                             \t\t\t\t Press 1 : Install AWS-CLI
                             \t\t\t\t Press 2 : Configure AWS-CLI
                             \t\t\t\t Press 3 : Go Back to Previous Menu
                             """)
                       os.system("tput setaf 8")      
                       remote_ip = int(input("enter your Remote IP : "))
                       print()
                       ch = input("Enter your Choice: ")
                       print()
                       os.system("tput setaf 80")
                       if ch == '1':
                            print("Installing AWS-CLI.......")
                            os.system("ssh {} pip3 install awscli".format(remote_ip))
                            print()
                            print("Successfully installed.....")
                       elif ch == '2':
                            print("Configure your IAM .......")
                            os.system("ssh {} aws configure".format(remote_ip))
                       elif ch == '3':
                            exit()
                       else:
                            print("Please choose the appropriate option as mention above")     


 
sleep(1)
print()
n = input("on which system u want to login(local/remote: ")
cli_automation(n)
