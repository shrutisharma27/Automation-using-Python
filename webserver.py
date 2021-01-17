import os
from time import sleep

def webserver(n):
          if n == "local":
             os.system("tput setaf 7")
             print("----------------------------Configuring_WebServer----------------------------------\n")
             print()
             sleep(1)
             os.system("yum install httpd -y")
             os.system("systemctl start httpd")
             os.system("cp index.html /var/www/html")
             os.system("systemctl stop firewalld")
             os.system("setenforce 0")
             os.system("tput setaf 1")
             print("Your webserver is configured successfully")
             os.system("firefox")
      
          elif n == "remote":
             os.system("tput setaf 7")
             print("----------------------------Configuring_WebServer----------------------------------\n")
             print()
             sleep(1)
             os.system("tput setaf 3")
             remote_ip = input("enter the remote IP: ")
             os.system("ssh {} yum install httpd -y".format(remote_ip))
             os.system("ssh {} systemctl start httpd".format(remote_ip))
             os.system("ssh {} systemctl stop firewalld".format(remote_ip))
             os.system("ssh {} setenforce 0".format(remote_ip))
             os.system("tput setaf 1")
             print("Your webserver is configured successfully")
           

sleep(1)
print()
n = input("In which system you want to login (Local/Remote): ")
webserver(n)


