import os
from time import sleep
os.system("clear")

def aws_s3(n):
  while True:
       os.system("clear")
       os.system("tput setaf  5")
       print("--------------------------------Storage(S3) Automation------------------------")
          
       os.system("tput setaf  7")
       if n == "local":   
            print("""
            \n
            \t\t\t\t Press 1 : Create New S3 Bucket
            \t\t\t\t Press 2 : Delete S3 bucket
            \t\t\t\t Press 3 : Upload object in S3 bucket
            \t\t\t\t Press 4 : Delete object in S3 bucket
            \t\t\t\t Press 5 : Delete S3 bucket
            \t\t\t\t Press 6 : Go back to main menu
            """)
            os.system("tput setaf 3")
            bucket_ch = input("Enter your Choice: ")
            if int(bucket_ch) == 1:
                s3_name = input("Enter S3 bucket name that must be unique: ")
                #region = input("Enter name of region: ")
                print("Creating S3 Bucket.....")
                os.system('aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1'.format(s3_name))
                print("S3 bucket created successfully....")
            elif int(bucket_ch) == 2:
                s3_name = input("Enter S3 Bucket name: ")
                print("Deleting S3 bucket...")
                os.system("aws s3api delete-bucket --bucket {} --region ap-south-1".format(s3_name))
                print("Successfully deleted S3 bucket.....")
            elif int(bucket_ch) == 3:
                object_name = input("Enter Object name to put inside S3 bucket: ")
                s3_name = input("Enter S3 Bucket name: ")
                print("Uploading object....")
                os.system('aws s3 cp /root/my-workspace-main/{} s3://{} --acl public-read'.format(object_name , s3_name))
                print("Successfully uploaded object in S3 bucket...")
            elif int(bucket_ch) == 4:
                s3_name = input("Enter S3 bucket name: ")
                object_name = input("Enter object name: ")
                print("Deleting object....")
                os.system('aws s3 rm s3://{}/{}'.format(s3_name , object_name))
                print("Successfully deleted object...")
            elif int(bucket_ch) == 5:
                s3_name = input("Enter name of bucket: ")
                region = input("Enter region name: ")
                print("Deleting S3 Bucket....")
                os.system("aws s3api delete-bucket --bucket {} --region {}".format(s3_name,region))
                print("Successfully S3 bucket successfully....")
            elif int(bucket_ch) == 6:
                exit()

        
       if n == "remote":
            sleep(1)   
            print("""
            \n
            \t\t\t\t Press 1 : Create New S3 Bucket
            \t\t\t\t Press 2 : Delete S3 bucket
            \t\t\t\t Press 3 : Upload object in S3 bucket
            \t\t\t\t Press 4 : Delete object in S3 bucket
            \t\t\t\t Press 5 : Delete S3 bucket
            \t\t\t\t Press 6 : Go back to main menu
            """)
            os.system("tput setaf 3")
            remote_ip = input("enter the remote ip: ")
            os.system("tput setaf 4")
            bucket_ch = input("Enter your Choice: ")
            os.system("tput setaf 5")
            if int(bucket_ch) == 1:
                s3_name = input("Enter S3 bucket name that must be unique: ")
                #region = input("Enter name of region: ")
                print("Creating S3 Bucket.....")
                os.system('ssh {} aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1'.format(remote_ip,s3_name))
                print("S3 bucket created successfully....")
            elif int(bucket_ch) == 2:
                s3_name = input("Enter S3 Bucket name: ")
                print("Deleting S3 bucket...")
                os.system("ssh {} aws s3api delete-bucket --bucket {} --region ap-south-1".format(remote_ip,s3_name))
                print("Successfully deleted S3 bucket.....")
            elif int(bucket_ch) == 3:
                object_name = input("Enter Object name to put inside S3 bucket: ")
                s3_name = input("Enter S3 Bucket name: ")
                print("Uploading object....")
                os.system('ssh {} aws s3 cp /root/my-workspace-main/{} s3://{} --acl public-read'.format(remote_ip,object_name , s3_name))
                print("Successfully uploaded object in S3 bucket...")
            elif int(bucket_ch) == 4:
                s3_name = input("Enter S3 bucket name: ")
                object_name = input("Enter object name: ")
                print("Deleting object....")
                os.system('ssh {} aws s3 rm s3://{}/{}'.format(remote_ip,s3_name , object_name))
                print("Successfully deleted object...")
            elif int(bucket_ch) == 5:
                s3_name = input("Enter name of bucket: ")
                region = input("Enter region name: ")
                print("Deleting S3 Bucket....")
                os.system("ssh {} aws s3api delete-bucket --bucket {} --region {}".format(remote_ip,s3_name,region))
                print("Successfully S3 bucket successfully....")
            elif int(bucket_ch) == 6:
                exit()

sleep(1)
os.system("tput setaf 2")
print()
n = input("on which system you want to login(local/remote): ")
aws_s3(n)    
