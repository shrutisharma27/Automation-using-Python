import os
from time import sleep
os.system("clear")

def aws_ec2(n):
  while True: 
      print()
      os.system("tput setaf 6") 
      print("-----------------------Elastic Cloud (EC2) Automation---------------------------")
      os.system("tput setaf  7")
      if n == "local":     
            print("""
                  \n
                  \t\t Press 1 : Create New EC2 Instance
                  \t\t Press 2 : Start Specific Instance
                  \t\t Press 3 : Stop Instance
                  \t\t Press 4 : Terminate Instance
                  \t\t Press 5 : Show all instances
                  \t\t Press 6 : Go to back menu
                  """)
            os.system("tput setaf 8 ")
            ec2_ch = input("Enter your choice: ")
            if int(ec2_ch) == 1:
                ami = input("Enter AMI id to Launch Instance: ")
                instance_type = input("Enter Instance type: ")
                count = input("Enter Number of Instances to launch: ")
                subnet_id = input("Enter Subnet id: ")
                sg_id1 = input("Enter Security Group Id to attach to the Instance: ")
                key = input("Enter Key to attach to ec2 Instance: ")
                print("Launching New EC2 Instance.....")
                os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}'.format(ami , instance_type , count ,subnet_id, sg_id1 , key))
                print("Instance launched Successfully......")
            elif int(ec2_ch) == 3:
                id = input("Enter Instance id to stop Ec2 instances: ")
                print("Stopping Instance.......")
                os.system("aws ec2 stop-instances --instance-ids {}".format(id))
                print("Insatnce stopped Successfully....")
            elif int(ec2_ch) == 2:
                id = input("Enter Instance id to start Ec2 instances: ")
                print("Starting Instance.....")
                os.system("aws ec2 start-instances --instance-ids {}".format(id))
                print("Instance Started successfully......")
            elif int(ec2_ch) == 4:
                id = input("Enter Instance id to terminate Ec2 instances: ")
                print("Terminating instance...")
                os.system("aws ec2 terminate-instances --instance-ids {}".format(id))
                print("Instance terminated successfully.....")
            elif int(ec2_ch) == 5:
                print("Showing Instances....")
                os.system("aws ec2 describe-instances")
            elif int(ec2_ch) == 6:
                exit() 
     
      if n == "remote":     
            print("""
            \n
            \t\t Press 1 : Create New EC2 Instance
            \t\t Press 2 : Start Specific Instance
            \t\t Press 3 : Stop Instance
            \t\t Press 4 : Terminate Instance
            \t\t Press 5 : Show all instances
            \t\t Press 6 : Go to back menu
            """)
            print()
            os.system("tput setaf 10")
            remote_ip = input("enter your remote IP: ")
            print()
            ec2_ch = input("Enter your choice: ")
            os.system("tput setaf 3")
            if int(ec2_ch) == 1:
                ami = input("Enter AMI id to Launch Instance: ")
                instance_type = input("Enter Instance type: ")
                count = input("Enter Number of Instances to launch: ")
                subnet_id = input("Enter Subnet id: ")
                sg_id1 = input("Enter Security Group Id to attach to the Instance: ")
                key = input("Enter Key to attach to ec2 Instance: ")
                print("Launching New EC2 Instance.....")
                os.system('ssh {} aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}'.format(remote_ip,ami , instance_type , count ,subnet_id, sg_id1 , key))
                print("Instance launched Successfully......")
            elif int(ec2_ch) == 3:
                id = input("Enter Instance id to stop Ec2 instances: ")
                print("Stopping Instance.......")
                os.system("ssh {} aws ec2 stop-instances --instance-ids {}".format(remote_ip,id))
                print("Insatnce stopped Successfully....")
            elif int(ec2_ch) == 2:
                id = input("Enter Instance id to start Ec2 instances: ")
                print("Starting Instance.....")
                os.system("ssh {} aws ec2 start-instances --instance-ids {}".format(remote_ip,id))
                print("Instance Started successfully......")
            elif int(ec2_ch) == 4:
                id = input("Enter Instance id to terminate Ec2 instances: ")
                print("Terminating instance...")
                os.system("ssh {} aws ec2 terminate-instances --instance-ids {}".format(remote_ip,id))
                print("Instance terminated successfully.....")
            elif int(ec2_ch) == 5:
                print("Showing Instances....")
                os.system("ssh {} aws ec2 describe-instances".format(remote_ip))
            elif int(ec2_ch) == 6:
                exit()


sleep(1)
os.system("tput setaf 2")
print()
n = input("on which system you want to login(local/remote): ")
aws_ec2(n)

