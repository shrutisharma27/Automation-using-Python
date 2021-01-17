import os
from time import sleep
os.system("clear")
while True:
    print()
    os.system("tput setaf  2")
    print("-----------------------------------AWS_Automation---------------------------------")
    os.system("tput setaf  6")
    sleep(1)
    print("\t\t\t\t Menu_option:")
    os.system("tput setaf 4")  
    print("""
             \t\t\t\t 1 : AWS-cli installation 
             \t\t\t\t 2 : key pair
             \t\t\t\t 3 : Security group
             \t\t\t\t 4 : EC2 instance
             \t\t\t\t 5 : S3 bucket
             \t\t\t\t 6 : EBS Volume
             \t\t\t\t 7 : Go to Main Menu
             """)
    os.system("tput setaf 8")
    aws_choice = input("Enter Your Choice: ")            
    if int(aws_choice) == 1:
        os.system("python3 aws_cli.py")
    if int(aws_choice) == 2:
        os.system("python3 aws_key.py")
    elif int(aws_choice) == 3:
        os.system("python3 aws_sg.py")
    elif int(aws_choice) == 4:
        os.system("python3 aws_ec2.py")
    elif int(aws_choice) == 5:
        os.system("python3 aws_s3.py")
    elif int(aws_choice) == 6:
        os.system("python3 aws_ebs.py")
    elif int(aws_choice) == 7:
        exit()
    else:
        print("Invalid Option")
