import os
os.system("clear")
from time import sleep

def Key_automation(n):
    while True:
            print()
            os.system("tput setaf  5")
            print("----------------------------Key-pair Automation-------------------------------------")
            os.system("tput setaf  7")
            if n == "local":
                       print()                
                       print("\t\t\t\t Press 1 : Create Key pair \n \t\t\t\t Press 2 : Delete Key pair \n\t\t\t\t Press 3 : Show key pair \n\t\t\t\t Press 4 : Go to Back Menu \n")
                       os.system("tput setaf 8")
                       ch = int(input("Enter your Choice: "))
                       print()
                       os.system("tput setaf 80")
                       if ch == 1:
                            name = input("Enter name of key: ")
                            print("Creating Key-pair.......")
                            os.system("aws ec2 create-key-pair --key-name {}".format(name))
                            print("Successfully Created key_pair.....")
                       elif ch == 2:
                   
                            del_name = input("Enter name of key: ")
                            print("Deleting Key-pair.....")
                            os.system("aws ec2 delete-key-pair --key-name {}".format(del_name))
                            print("Key-pair deleted successfully.....")
                       elif ch  == 3:
                            key_name = input("Enter name of key: ")
                            os.system("aws ec2 describe-key-pairs --key-name {}".format(key_name))
                       elif ch == 4:
                            exit()
               
            if n == "remote":
                       print()
                       sleep(1)
                       print("""
                             \n
                              \t\t\t\t Press 1 : Create Key pair
                              \t\t\t\t Press 2 : Delete Key pair
                              \t\t\t\t Press 3 : Show key pair
                              \t\t\t\t Press 4 : Go to Back Menu
                              """)
                       os.system("tput setaf 8")
                      
                       remote_ip = input("enter your Remote IP : ")
                       print()
                       ch = input("Enter your Choice: ")
                       print()
                       os.system("tput setaf 80")
                       if ch == 1:
                            name = input("Enter name of key: ")
                            print("Creating Key-pair.......")
                            os.system("ssh {} aws ec2 create-key-pair --key-name {}".format(remote_ip,name))
                            print("Successfully Created key_pair.....")
                       elif ch == 2:
                   
                            del_name = input("Enter name of key: ")
                            print("Deleting Key-pair.....")
                            os.system("ssh {} aws ec2 delete-key-pair --key-name {}".format(remote_ip,del_name))
                            print("Key-pair deleted successfully.....")
                       elif ch  == 3:
                            key_name = input("Enter name of key: ")
                            os.system("ssh {} aws ec2 describe-key-pairs --key-name {}".format(remote_ip,key_name))
                       elif ch == 4:
                            exit()



sleep(1)
os.system("tput setaf 2")
print()
n = input("on which system you want to login(Local/Remote): ")
Key_automation(n)

