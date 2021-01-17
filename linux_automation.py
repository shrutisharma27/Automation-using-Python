import os 
from time import sleep


def linux_automation(n):
         if n == "local":
                     os.system("tput setaf 9")
                     print()
                     print("----------------------------LINUX_AUTOMATION----------------------------------\n")
                     while True:
                         os.system("tput setaf 80")
                         sleep(1)
                         print("Menu list :")
                         os.system("tput setaf 10")
                         sleep(1)
                         print(" 1] Show Date \n 2] Show Calender \n 3] Show RAM Usage \n 4] To check the storage \n 5] To list down all the files and directories \n 6] To run any linux command \n 7] Parition \n 8] Go back to main menu \n")
                         r = input("enter your choices : ")
                         print()
                         os.system("tput setaf 7")
                         if r == "1":
                             os.system("date")
                         elif r == "2":
                             os.system("cal")
                         elif r == "3":
                             os.system("free -m")
                         elif r == "4":
                             os.system("df -h")
                         elif r == "5":
                             os.system("ls")
                         elif r == "6":
                             os.system("input(" ")")
                         elif r == "7":
                             os.system("fdisk -l")
                             hard_disk = input("enter the name of the hard disk : ")
                             os.system("fdisk hard_disk")
                             os.system("mkfs.ext4 hard_disk")
                             dir_name = input("enter the directory name : ")
                             os.system("mount hard_disk drive_name")
                             os.system("tput setaf 3")
                             print("---created successfully---")
                             os.system("tput setaf 7")
                             os.system("df -h")
                         elif r == "8":
                             exit()
                         else:
                             print("select options as mention")

         elif n == "remote":
                     os.system("tput setaf 9")
                     remote_ip = input("enter the remote OS IP : ")
                     print()
                     os.system("tput setaf 7")
                     print("----------------------------LINUX_AUTOMATION----------------------------------\n")
                     while True:
                         os.system("tput setaf 80")
                         print("\t\t\tMenu list :")
                         os.system("tput setaf 10")
                         print(" 1] Show Date \n 2] Show Calender \n 3] Show RAM Usage \n 4] To check the storage \n 5] To list down all the files and directories \n 6] To run any linux command \n 7] Partition \n 8] Go back to Main Menu \n")
                         r = input("Enter your choice: ")
                         print()
                         os.system("tput setaf 7")
                         if r == "1":
                             os.system("ssh {} date".format(remote_ip))
                         elif r == "2":
                             os.system("ssh {} cal".format(remote_ip))
                         elif r == "3":
                             os.system("ssh {} free -m".format(remote_ip))
                         elif r == "4":
                             os.system("ssh {} df -h".format(remote_ip))
                         elif r == "5":
                             os.system("ssh {} ls".format(remote_ip))
                         elif r == "6":
                             linux_cmd = input("enter the linux command : ")
                             os.system("ssh {} {}".format(remote_ip,linux_cmd))  
                         elif r == "7":
                             os.system('ssh {} fdisk -l'.format(remote_ip))
                             hd_name = input("Enter the name of the hard disk: ")
                             os.system('ssh {} fdisk {} '.format(remote_ip,hd_name))
                             os.system('ssh {} mkfs.ext4 {}'.format(remote_ip,hd_name))
                             dir_name = input("Enter the directory name :")
                             os.system('ssh {} mount {} {}'.format(remote_ip,hd_name,dir_name))
                             os.system("tput setaf 3")
                             print("------Created Successfully-------")
                             os.system("tput setaf 7")
                             os.system("df -h")
                         elif r == "8":
                             exit()
                         else:                                                                               print("select options as mention ")




sleep(1)
print()
n = input("In which system do you want to login (Local/Remote): ")
linux_automation(n)
