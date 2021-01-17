import os
from time import sleep


def lvm_automation(n):
  while True:
    print()
    os.system("tput setaf  3")
    print("----------------------Logical Volume Management(LVM) Automation----------------\t\t")
    os.system("tput setaf  6")
    sleep(1)
    if n  == "local": 
       print("""
                \n 
                \t\t Press 1  : Create Physical Volume
                \t\t Press 2  : Show all Physical volumes
                \t\t Press 3  : Create Volume Group
                \t\t Press 4  : Show all Volume Groups
                \t\t Press 5  : Add more Hard Disks in Volume Group
                \t\t Press 6  : Create Logical Partitions
                \t\t Press 7  : Format partitions
                \t\t Press 8  : Mount partitions on folder
                \t\t Press 9  : Extend Partitons
                \t\t Press 10 : Shrink Partitions
                \t\t Press 11 : Show all Hard Disks
                \t\t Press 12 : Show all logical volumes
                \t\t Press 13 : Remove Physical Volume
                \t\t Press 14 : Remove Volume group
                \t\t Press 15 : Remove Logical Volume
                \t\t Press 16 : Go back to main menu

                Note : Make sure to  attach your physical devices first  
                """)
       lv_ch = input("Enter your Choice: ")
       if int(lv_ch) == 1:
            os.system("fdisk -l")
            print()
            n = input("Enter the number which you want to create Physical Volume: ") 
            for i in range(int(n)):
                print()
                n1 = input("Enter {} disk name: ".format(i))
                os.system("pvcreate {}".format(n1))
                os.system("pvdisplay {}".format(n1))
       elif int(lv_ch) == 2:
            os.system("pvdisplay")
       elif int(lv_ch) == 3:
            c = input("Enter the name of Volume group: ")
            os.system("vgcreate {0} {1}".format(c,n1))
            os.system("vgdisplay {0}".format(c))
       elif int(lv_ch) == 4:
            os.system("vgdisplay")
       elif int(lv_ch) == 5:
            pvname = input("Enter PV name: ")
            os.system("vgextend {0} {1}".format(c,pvname))
            os.system("vgdisplay {0}".format(c))
       elif int(lv_ch) == 6:
            s = input("Enter the size of LV: ")
            n2 = input("Enter the name of LV: ")
            vg = input("Enter name of volume group: ")
            os.system("lvcreate --size {0}G --name {1} {2}".format(s,n2,vg))
            os.system("lvdisplay {0}".format(n2))
       elif int(lv_ch) == 7:
            os.system("clear")
            while True:
                print("""
                \n
                \t\t\t Press 1 : mkfs.ext4
                \t\t\t Press 2 : resize2fs
                \t\t\t Press 3 : Go back to previous menu
                """)
                fmt_ch = input("Enter your choice: ")
                if int(fmt_ch) == 1:
                    vg = input("Enter name of volume group: ")
                    lv = input("Enter name of logical volume: ")
                    os.system("mkfs.ext4 /dev/{0}/{1}".format(vg,lv))
                elif int(fmt_ch) == 2:
                    vg1 = input("Enter name of volume group: ")
                    lv1 = input("Enter name of logical VOlume: ")
                    os.system("resize2fs /dev/{0}/{1}".format(vg1,lv1))
                    os.system("df -H")
                elif int(fmt_ch) == 3:
                    break
       elif int(lv_ch) == 8:
            
            f1 = input("Enter the name of file: ")
            os.system("mkdir /{0}".format(f1))
            vgname = input("Enter name of Volume Group: ")
            lvname = input("Enter name of Logical Volume: ")
            os.system("mount /dev/{}/{} {}".format(vgname,lvname,f1))
            os.system("df -H")
       elif int(lv_ch) == 9:
           
            s1 = input("Enter the size which you want to extend: ")
            vg = input("Enter name of volume group: ")
            lv = input("Enter name of logical VOlume: ")
            os.system("lvextend --size +{0}G /dev/{1}/{2}".format(s1,vg,lv))
       elif int(lv_ch) == 10:
           
            s2 = input("Enter the size which you want to make your lv: ")
            vg = input("Enter name of volume group: ")
            lv = input("Enter name of logical Volume: ")
            filename = input("Enter name of file which you want to unmount: ")
            os.system("umount {}".format(filename))
            os.system("e2fsck -f /dev/{}/{}".format(vg,lv))
            os.system("resize2fs /dev/iiec/lv1 {}G".format(s2))
            os.system("lvreduce --size {0}G /dev/{1}/{2} -y".format(s2,vg,lv))
            os.system("mount /dev/{}/{} {}".format(vg,lv,filename))
       elif int(lv_ch) == 11:
            os.system("fdisk -l")
       elif int(lv_ch) == 12:
            os.system("lvdisplay")
       elif int(lv_ch) == 13:
            pvname = input("Enter name of Physical volume: ")
            os.system("pvremove {}".format(pvname))
       elif int(lv_ch) == 14:
            vgname = input("Enter name of Volume Group: ")
            os.system("vgremove {}".format(vgname))
       elif int(lv_ch) == 15:
            lvname = input("Enter name of LVM: ")
            vg_n = input("Enter name of Volume group: ")
            os.system("umount /dev/{}/{}".format(vg_n,lvname))
            os.system("lvremove /dev/{}/{}".format(vg_n,lvname))
       elif int(lv_ch) == 16:
            exit()

    elif n == "remote":
        os.system("tput setaf 5")
        remote_ip = input("enter the remote OS IP : ")
        print()
        print("""
                \n
                \t\t Press 1  : Create Physical Volume
                \t\t Press 2  : Show all Physical volumes
                \t\t Press 3  : Create Volume Group
                \t\t Press 4  : Show all Volume Groups
                \t\t Press 5  : Add more Hard Disks in Volume Group
                \t\t Press 6  : Create Logical Partitions
                \t\t Press 7  : Format partitions
                \t\t Press 8  : Mount partitions on folder
                \t\t Press 9  : Extend Partitons
                \t\t Press 10 : Shrink Partitions
                \t\t Press 11 : Show all Hard Disks
                \t\t Press 12 : Show all logical volumes
                \t\t Press 13 : Remove Physical Volume
                \t\t Press 14 : Remove Volume group
                \t\t Press 15 : Remove Logical Volume
                \t\t Press 16 : Go back to main menu

                Note : Make sure to  attach your physical devices first
                """)
        if int(lv_ch) == 1:
            os.system("ssh {} tput setaf 3".format(remote_ip))
            os.system("ssh {} fdisk -l".format(remote_ip))

            n = input("Enter the number which you want to create Physical Volume: ")
            for i in range(int(n)):
                n1 = input("ssh {} Enter {} disk name: ".format(remote_ip,i))
                os.system("ssh {} pvcreate {}".format(remote_ip,n1))
                os.system("ssh {} pvdisplay {}".format(remote_ip,n1))
        elif int(lv_ch) == 2:
            os.system("ssh {} pvdisplay".format(remote_ip))
        elif int(lv_ch) == 3:
          
            c = input("Enter the name of Volume group: ")
            os.system("ssh {} vgcreate {0} {1}".format(remote_ip,c,n1))
            os.system("ssh {} vgdisplay {0}".format(remote_ip,c))
        elif int(lv_ch) == 4:
            os.system("ssh {} vgdisplay".format(remote_ip))
        elif int(lv_ch) == 5:
            pvname = input("Enter PV name: ")
            os.system("ssh {} vgextend {0} {1}".format(remote_ip,c,pvname))
            os.system("ssh {} vgdisplay {0}".format(remote_ip,c))
        elif int(lv_ch) == 6:
            s = input("Enter the size of LV: ")
            n2 = input("Enter the name of LV: ")
            vg = input("Enter name of volume group: ")
            os.system("ssh {} lvcreate --size {0}G --name {1} {2}".format(remote_ip,s,n2,vg))
            os.system("ssh {} lvdisplay {0}".format(remote_ip,n2))
        elif int(lv_ch) == 7:
            os.system("clear")
            while True:
                print("""
                \n
                \t\t\t Press 1 : mkfs.ext4
                \t\t\t Press 2 : resize2fs
                \t\t\t Press 3 : Go back to previous menu
                """)
                fmt_ch = input("Enter your choice: ")
                if int(fmt_ch) == 1:
                    vg = input("Enter name of volume group: ")
                    lv = input("Enter name of logical VOlume: ")
                    os.system("ssh {} mkfs.ext4 /dev/{0}/{1}".format(remote_ip,vg,lv))
                elif int(fmt_ch) == 2:
                    vg1 = input("Enter name of volume group: ")
                    lv1 = input("Enter name of logical VOlume: ")
                    os.system("ssh {} resize2fs /dev/{0}/{1}".format(remote_ip,vg1,lv1))
                    os.system("ssh {} df -h".format(remote_ip))
                elif int(fmt_ch) == 3:
                    break
        elif int(lv_ch) == 8:
         
            f1 = input("Enter the name of file: ")
            os.system("ssh {} mkdir /{0}".format(remote_ip,f1))
            vgname = input("Enter name of Volume Group: ")
            lvname = input("Enter name of Logical Volume: ")
            os.system("ssh {} mount /dev/{}/{} {}".format(remote_ip,vgname,lvname,f1))
            os.system("ssh {} df -h".format(remote_ip))
        elif int(lv_ch) == 9:
       
            s1 = input("Enter the size which you want to extend: ")
            vg = input("Enter name of volume group: ")
            lv = input("Enter name of logical VOlume: ")
            os.system("ssh {} lvextend --size +{0}G /dev/{1}/{2}".format(remote_ip,s1,vg,lv))
        elif int(lv_ch) == 10:
            
            s2 = input("Enter the size which you want to make your lv: ")
            vg = input("Enter name of volume group: ")
            lv = input("Enter name of logical Volume: ")
            filename = input("Enter name of file which you want to unmount: ")
            os.system("ssh {} umount {}".format(remote_ip,filename))
            os.system("ssh {} e2fsck -f /dev/{}/{}".format(remote_ip,vg,lv))
            os.system("ssh {} resize2fs /dev/iiec/lv1 {}G".format(remote_ip,s2))
            os.system("ssh {} lvreduce --size {0}G /dev/{1}/{2} -y".format(remote_ip,s2,vg,lv))
            os.system("ssh {} mount /dev/{}/{} {}".format(remote_ip,vg,lv,filename))
        elif int(lv_ch) == 11:
            os.system("ssh {} fdisk -l".format(remote_ip))
        elif int(lv_ch) == 12:
            os.system("ssh {} lvdisplay".format(remote_ip))
        elif int(lv_ch) == 13:
            pvname = input("Enter name of Physical volume: ")
            os.system("ssh {} pvremove {}".format(remote_ip,pvname))
        elif int(lv_ch) == 14:
            vgname = input("Enter name of Volume Group: ")
            os.system("ssh {} vgremove {}".format(remote_ip,vgname))
        elif int(lv_ch) == 15:
            lvname = input("Enter name of LVM: ")
            vg_n = input("Enter name of Volume group: ")
            os.system("ssh {} umount /dev/{}/{}".format(remot_ip,vg_n,lvname))
            os.system("ssh {} lvremove /dev/{}/{}".format(remote_ip,vg_n,lvname))
        elif int(lv_ch) == 16:
            exit()


sleep(1)
print()
n = input("In which system you want to login (Local/Remote): ")
lvm_automation(n)
