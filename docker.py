import os
os.system("clear")


def docker_automation(n):
 while True:  
    os.system("tput setaf 3")
    print("---------------------------Docker_Automation--------------------------------")
    os.system("tput setaf 6")
    
    print("""
    \n
    \t\t\t\t Press 1  : install docker
    \t\t\t\t Press 2  : Start the docker services
    \t\t\t\t Press 3  : Pull image from Docker hub
    \t\t\t\t Press 4  : Launch new Container
    \t\t\t\t Press 5  : Show all Container
    \t\t\t\t Press 6  : Remove Container
    \t\t\t\t Press 7  : Show all images
    \t\t\t\t Press 8  : Info of Docker
    \t\t\t\t Press 9  : Configure webserver inside the container
    \t\t\t\t Press 10 : Start container
    \t\t\t\t Press 11 : Stop Container
    \t\t\t\t Press 12 : Go back to main menu
    """)
    os.system("tput setaf 1")
    if n == "local": 
       d_ch = input("Enter your Choice: ")
       print()
       os.system("tput setaf 8")
       if int(d_ch) == 1:
            filename = input("enter the filename for docker repository: ")
            os.system("touch /etc/yum.repos.d/{}.repo".format(filename))
            yum_file = open("/etc/yum.repos.d/{}.repo".format(filename),"w")
            confg_yum = '''[docker]
                      baseurl = https://download.docker.com/linux/centos/7/x86_64/stable
                      gpgcheck = 0
                    '''
            yum_file.write("confg_yum")
            os.system("tput setaf 1")
            print("docker has been configured successfully.....")
            print("now installing the docker in your system")
            os.system("tput setaf 7")
            os.system("yum install docker-ce --nobest")
            os.system("tput setaf 1")
            print("docker is installed ") 
       elif int(d_ch) == 2:
            os.system("systemctl start docker")
            print("sevices has been started successfully....")    
       elif int(d_ch) == 3:
            image_name = input("Enter name of Image: ")
            print("Image Downloading....")
            os.system("docker pull {}".format(image_name))
            print("Image Sucessfully downloaded....")
       elif int(d_ch) == 4:
            value=input("Enter Container Name: ")
            image=input("Enter Image Name: ")
            print("Launching New OS......")
            os.system("docker run -dit --name {} {}".format(value, image))
            print("New OS Launched Successfully")
       elif int(d_ch) == 5:
            os.system("docker ps -a")
       elif int(d_ch) == 6:
            value=input("Enter name to remove docker Container: ")
            print("Removing Container....")
            os.system("docker rm -f {}".format(value))
            print("Container Removed Successfully....")
       elif int(d_ch) == 7:
            os.system("docker images")
       elif int(d_ch) == 8:
            os.system("Information of Docker....")
            os.system("docker info")
       elif int(d_ch) == 9:
            con_name = input("Enter Container Name: ")
            image_name = input("Enter Image Name: ")
            port = input("Enter Port Number to Expose the WebServer running on the top of Docker: ")
            print("Configuring Webserver.....")
            os.system('docker run -dit --name {} -p {}:80 {}'.format(con_name , port , image_name))
            os.system('docker exec -it {} yum install httpd -y'.format(con_name))
            os.system('sudo docker cp /root/automationtask/index.html {}:/var/www/html/'.format(con_name))
            os.system('sudo docker exec -it {} /usr/sbin/httpd'.format(con_name))
            print("Webserver Configured Successfully....")
       elif int(d_ch) == 10:
            c_name = input("Enter name of container: ")
            print("Starting Container....")
            os.system("docker start {}".format(c_name))
            print("Container Started Sucessfully...")
       elif int(d_ch) == 11:
            c_name = input("Enter name of container: ")
            print("Stopping Container....")
            os.system("docker stop {}".format(c_name))
            print("Container Stopped successfully....")
       elif int(d_ch) == 12:
            exit()
    if n == "remote":
       d_ch = input("Enter your Choice: ")
       remote_ip = input("enter the remote ip: ")
       print()
       os.system("tput setaf 8")
       if int(d_ch) == 1:
            filename = input("enter the filename for docker repository: ")
            os.system("ssh {} touch /etc/yum.repos.d/{}.repo".format(remote_ip,filename))
            yum_file = open("ssh {} /etc/yum.repos.d/{}.repo".format(remote_ip,filename),"w")
            confg_yum = '''[docker]
                      baseurl = https://download.docker.com/linux/centos/7/x86_64/stable
                      gpgcheck = 0
                    '''
            os.system("ssh {} yum_file.write({})".format(remote_ip,confg_yum))
            os.system("tput setaf 1")
            print("docker has been configured successfully.....")
            print("now installing the docker in your system")
            os.system("tput setaf 7")
            os.system("ssh {} yum install docker-ce --nobest".format(remote_ip))
            os.system("tput setaf 1")
            print("docker is installed ")
       elif int(d_ch) == 2:
            os.system("ssh {} systemctl start docker".format(remote_ip))
            print("sevices has been started successfully....")
       elif int(d_ch) == 3:
            image_name = input("Enter name of Image: ")
            print("Image Downloading....")
            os.system("ssh {} docker pull {}".format(remote_ip,image_name))
            print("Image Sucessfully downloaded....")
       elif int(d_ch) == 4:
            value=input("Enter Container Name: ")
            image=input("Enter Image Name: ")
            print("Launching New OS......")
            os.system("ssh {} docker run -dit --name {} {}".format(remote_ip,value, image))
            print("New OS Launched Successfully")
       elif int(d_ch) == 5:
            os.system("ssh {} docker ps -a".format(remote_ip))
       elif int(d_ch) == 6:
            value=input("Enter name to remove docker Container: ")
            print("Removing Container....")
            os.system("ssh {} docker rm -f {}".format(remote_ip,value))
            print("Container Removed Successfully....")
       elif int(d_ch) == 7:
            os.system("ssh {} docker images",format(remote_ip))
       elif int(d_ch) == 8:
            os.system("Information of Docker....")
            os.system("ssh {} docker info".format(remote_ip))
       elif int(d_ch) == 9:
            con_name = input("Enter Container Name: ")
            image_name = input("Enter Image Name: ")
            port = input("Enter Port Number to Expose the WebServer running on the top of Docker: ")
            print("Configuring Webserver.....")
            os.system('ssh {} docker run -dit --name {} -p {}:80 {}'.format(remote_ip,con_name , port , image_name))
            os.system('ssh {} docker exec -it {} yum install httpd -y'.format(remote_ip,con_name))

            os.system('ssh {} sudo docker exec -it {} /usr/sbin/httpd'.format(remote_ip,con_name))
            print("Webserver Configured Successfully....")
       elif int(d_ch) == 10:
            c_name = input("Enter name of container: ")
            print("Starting Container....")
            os.system("ssh {} docker start {}".format(remote_ip,c_name))
            print("Container Started Sucessfully...")
       elif int(d_ch) == 11:
            c_name = input("Enter name of container: ")
            print("Stopping Container....")
            os.system("ssh {} docker stop {}".format(remote_ip,c_name))
       elif int(d_ch) == 12:
            exit()

print()
os.system("tput setaf 4")
n = input("which system would you like to use(local/remote):  ")

print()
docker_automation(n)
   
