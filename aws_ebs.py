import os
os.system("clear")

while True:
           
            os.system("tput setaf  6")
            print("---------------------Elastic Block Volume (EBS) Automation---------------------")
            os.system("tput setaf  7")

            print("""
            \n
           \t\t Press 1 : To Create new Volume
           \t\t Press 2 : Attach Volume to Specific Instance
           \t\t Press 3 : Dettach Volume
           \t\t Press 4 : Delete Volume
           \t\t Press 5 : Show Volumes
           \t\t Press 6 : Mount and Partition
           \t\t Press 7 : Go to Back menu
            """)
            vol_ch = int(input("Enter your Choice: "))
            os.system("tput setaf 1")
            if vol_ch == 1:
                az = input("Enter Availablity Zone to Create EBS Volume: ")
                ebs_size = input("Enter Size to create EBS Volume: ")
                print("Creating New Volume ....")
                os.system('aws ec2 create-volume --availability-zone {} --size {}'.format(az , ebs_size))
                print("New Volume Created Successfully....")
            elif vol_ch == 2:
                ebs_vid = input("Enter EBS Volume ID to Attach to EC2 Instance: ")
                ec2_id = input("Enter EC2 Instance ID to attach EBS Volume: ")
                print("Attaching Volume to instance.....")
                os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(ebs_vid , ec2_id))
                print("Successfully Volume attached to the instance.......") 
            elif vol_ch == 3:
                v_id = input("Enter volume id: ")
                print("Detaching Volume.......")
                os.system("aws ec2 detach-volume --volume-id {}".format(v_id))
                print("Volume Dettached Successfully.....")
            elif vol_ch == 4:
                 v_id = input("Enter volume id: ")
                 print("\Deleting Volume....")
                 os.system("aws ec2 delete-volume --volume-id {}".format(v_id))
                 print("Successfully deleted Volume...")
            elif vol_ch == 5:
                os.system("aws ec2  describe-volumes")
            elif vol_ch == 6:
               ip = input("Enter Public IP of EC2: ")
               ky = input("Enter Private Key Name For Login Into EC2 : ")
               os.system('ssh -l ec2-user {} -i {}.pem sudo fdisk -l'.format(ip , ky))
               na = input("\nEnter Partition Name: ")
               nb = input("Enter directory name: ") 
               os.system("ssh -l ec2-user {} -i {}.pem sudo mkdir {}".format(ip,ky,nb))
               os.system('ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 {}'.format(ip , ky , na))
               os.system('ssh -l ec2-user {} -i {}.pem sudo mount {}  {}'.format(ip , ky , na,nb))
               os.system('ssh -l ec2-user {} -i {}.pem sudo df -hT'.format(ip , ky))
            elif vol_ch == 7:
               exit()
