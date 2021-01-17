import os
from time import sleep

os.system("tput setaf 3")
os.system("clear")
print("\n")
print("------------------------------------------------------------------------------\n")
print()
print("                    Welcome to the Automation World                       ")
print()
print("-------------------------------------------------------------------------------\n")

                
while True:
   sleep(1)
   os.system("tput setaf 5")
   print("\t\t\t\t HERE's A LIST !!")
   sleep(1)
   os.system("tput setaf 3")
   print("\t\t\t\t 1] Linux automation \n \t\t\t\t 2] Hadoop automation \n \t\t\t\t 3] AWS Cloud Automation \n \t\t\t\t 4] Docker Automation \n \t\t\t\t 5] Webserver \n \t\t\t\t 6] LVM Services \n ")
   sleep(1)
   os.system("tput setaf 6")
   print("Which automation would you like  to choose :")
   m = input("")
   if m == "1":
      os.system("python3 linux_automation.py")
   elif m == "2":
      os.system("python3 hadoop_automation.py")
   elif m == "3":
      os.system("python3 aws.py")
   elif m == "4":
      os.system("python3 docker.py")
   elif m == "5":
      os.system("python3 webserver.py") 
   elif m == "6":
      os.system("python3 lvm.py") 
 
       
          







