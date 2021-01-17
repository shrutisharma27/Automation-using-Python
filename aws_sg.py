import os
from time import sleep
os.system("clear")

def aws_sg(n):
  while True:
      print()
      os.system("tput setaf 2")
      print("-----------------------Security Group Automation------------------------")
          
      os.system("tput setaf  7")
      if n == "local": 
            print("""
                  \t\t\t\t Press 1 : Create new security group
                  \t\t\t\t Press 2 : Delete Security group
                  \t\t\t\t Press 3 : Add Ingress Rules
                  \t\t\t\t Press 4 : Show Security Groups
                  \t\t\t\t Press 5 : Go to Back Menu
                   """)
            os.system("tput setaf 3")
            print()
            sg_ch1 = input("Enter your choice: ")
            print()
            os.system("tput setaf 8")
            if int(sg_ch1) == 1:
                sg_name = input("Enter Security group Name: ")
                sg_des = input("Enter Security group description: ")
                print("Creating New Security group....")
                os.system("aws ec2 create-security-group --group-name {0} --description {1}".format(sg_name,sg_des))
                print("Successfully created security group....")
            elif int(sg_ch1) == 2:
                sg_id=input("Enter Security group id you want to delete:  ")
                print("Deleting Security group...")
                os.system("aws ec2 delete-security-group --group-id {}".format(sg_id))
                print("Successfully deleted Security group....")
            elif int(sg_ch1) == 3:
                sg_id = input("Enter Security Group ID : ")
                ip_protocol = input("Enter IP Protocol: ")
                port_no = input("Enter Port No: ")
                cidr=input("Input Ip Ranges : ")
                print("Authorizing Security group....")
                os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(sg_id , ip_protocol , port_no , cidr))
                print("Sucessfully authorize security group...")
            elif int(sg_ch1) == 4:
                sg_id2 = input("Enter group id : ")
                sg_name1 = input("Enter name of Security Group: ")
                os.system("aws ec2 describe-security-groups --group-ids {} --group-names {}".format(sg_id2,sg_name1))
            elif int(sg_ch1) == 5:
                exit()

    
      if n == "remote": 
            print("""
                  \n
                  \t\t\t\t Press 1 : Create new security group
                  \t\t\t\t Press 2 : Delete Security group
                  \t\t\t\t Press 3 : Add Ingress Rules
                  \t\t\t\t Press 4 : Show Security Groups
                  \t\t\t\t Press 5 : Go to Back Menu
                  """)
            os.system("tput setaf 3")
            print()
            sg_ch1 = input("Enter your choice: ")
            print()
            os.system("tput setaf 8")
            if int(sg_ch1) == 1:
                sg_name = input("Enter Security group Name: ")
                sg_des = input("Enter Security group description: ")
                print("Creating New Security group....")
                os.system("ssh {} aws ec2 create-security-group --group-name {0} --description {1}".format(remote_ip,sg_name,sg_des))
                print("Successfully created security group....")
            elif int(sg_ch1) == 2:
                sg_id=input("Enter Security group id you want to delete:  ")
                print("Deleting Security group...")
                os.system("ssh {} aws ec2 delete-security-group --group-id {}".format(remote_ip,sg_id))
                print("Successfully deleted Security group....")
            elif int(sg_ch1) == 3:
                sg_id = input("Enter Security Group ID : ")
                ip_protocol = input("Enter IP Protocol: ")
                port_no = input("Enter Port No: ")
                cidr=input("Input Ip Ranges : ")
                print("Authorizing Security group....")
                os.system("ssh {} aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(remote_ip,sg_id , ip_protocol , port_no , cidr))
                print("Sucessfully authorize security group...")
            elif int(sg_ch1) == 4:
                sg_id2 = input("Enter group id : ")
                sg_name1 = input("Enter name of Security Group: ")
                os.system("ssh {} aws ec2 describe-security-groups --group-ids {} --group-names {}".format(remote_ip,sg_id2,sg_name1))
            elif int(sg_ch1) == 5:
                exit()

sleep(1)
print()
n = input("on which system u want to login(local/remote: ")
aws_sg(n)

