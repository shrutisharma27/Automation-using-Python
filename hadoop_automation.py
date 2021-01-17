import os
os.system("clear")

while True:              
       os.system("tput setaf  3")
       print("-----------------------------Hadoop_Automation------------------------------")
      
       os.system("tput setaf  7")
       print("""
             \n
           \t\t\t Press 1  : Install Hadoop Requirements
           \t\t\t Press 2  : Configure Name Node
           \t\t\t Press 3  : Configure Data Node
           \t\t\t Press 4  : Configure Hadoop Client
           \t\t\t Press 5  : Limit The Data Node Storage
           \t\t\t Press 6  : Upload Data To Hadoop Cluster
           \t\t\t Press 7  : Read Client Data from Hadoop Cluster
           \t\t\t Press 8  : Delete Client Data
           \t\t\t Press 9  : Stop Name Node
           \t\t\t Press 10 : Stop Data Node
           \t\t\t Press 11 : Exit
            """)
       ch = input("Enter your choice : ") 
       if int(ch) == 1:
           os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
           os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm  --force')
           print("\nHadoop Requirements Sucessfully Installed In Name Node")
           ab = input("Enter Your Data Node IP :")
           os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(ab))
           os.system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(ab))
           print("\n\tHadoop Requirements Sucessfully Installed In Data Node")
           bb = input("Enter Your Client Node IP :")
           os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(bb))
           os.system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(bb))
           os.system("tput setaf 9")
           print("\n\tHadoop Requirements Sucessfully Installed In Client Node")
           
       elif int(ch) == 2:
           dir = input("Enter your Name Node directory name : ")
           print("Configuring hdfs-site.xml file ............")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
           os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
           os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
           os.system('echo -e "<name>dfs.name.dir</name>" >> /root/hdfs-site.xml')
           os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dir))
           os.system('echo -e "</property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
           os.system('rm -rf /etc/hadoop/hdfs-site.xml')
           os.system('cp  /root/hdfs-site.xml  /etc/hadoop')
           os.system('rm -rf /root/hdfs-site.xml')
           print("\n\tFormatting the Name Node ..............................")
           print()
           os.system('hadoop namenode -format')
           print()
           print()
           nip = input("Enter Name Node IP :")
           print("Configuring core-site.xml file ...........")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
           os.system('echo -e "</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('rm -rf /etc/hadoop/core-site.xml')
           os.system('cp  /root/core-site.xml  /etc/hadoop')
           os.system('rm -rf /root/core-site.xml')
           print("\n\t Starting Hadoop Name Node Services .............................")
           os.system('hadoop-daemon.sh start namenode') 
           os.system('jps')

       elif int(ch) == 3:
           dip = input("\t\tEnter Data Node IP : ")
           dio = input("\t\tEnter your Data Node directory name : ")
           print("\t\t\t\tConfiguring hdfs-site.xml file ............")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
           os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
           os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
           os.system('echo -e "<name>dfs.data.dir</name>" >> /root/hdfs-site.xml')
           os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dio))
           os.system('echo -e "</property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
           os.system('scp  /root/hdfs-site.xml  {}:/etc/hadoop'.format(dip))
           os.system('rm -rf /root/hdfs-site.xml')
           niq = input("Enter Name Node IP :")
           print("\t\t\t\tConfiguring core-site.xml file ...........")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(niq))
           os.system('echo -e "</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(dip))
           os.system('rm -rf /root/core-site.xml')
           print("\n\t Starting Hadoop Data Node Services .............................")
           os.system('ssh {} hadoop-daemon.sh start datanode'.format(dip))
           os.system('ssh {} jps'.format(dip))
           print("\n\t Showing Hadoop Cluster Report ..............................")
           os.system('ssh {} hadoop dfsadmin -report'.format(dip))

      
       elif int(ch) == 4:
           os.system("tput setaf 6")
           yu = input("Enter Name Node IP : ")
           print("Configuring core-site.xml file ...........")
           ip = input("\nEnter Client IP : ")
           
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(yu))
           os.system('echo -e "</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(ip))
           print("\t\tHadoop Client Sucessfully Configured.........")

       elif int(ch) == 5:
           os.system("tput setaf 5")
           ip = input("\n Enter Data Node IP : ")
           si = input("\n Do You want to extend/reduce Data Node Storage? : ")
           os.system("tput setaf 2")
           if si == "extend":
               os.system('ssh {} df -hT'.format(ip))
               ex = input("\nHow much you want to extend? : ")
               vg = input("Enter Your Volume Group Name : ")
               lv = input("Enter Your Logical Volume Name : ")
               os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
               print("Sucessfully Extended the  Data Node Storage ")
               os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
               os.system('ssh {} df -hT'.format(ip))
           elif si == "reduce":
               os.system('ssh {} df -hT'.format(ip))
               ex = input("\nHow much you want to reduce? : ")
               vg = input("Enter Your Volume Group Name : ")
               lv = input("Enter Your Logical Volume Name : ")
               os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
               print("Sucessfully Reduced Data Node Storage ")
               os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
               os.system('ssh {} df -hT'.format(ip))
       
       elif int(ch) == 6:
           ci = input("Enter Client IP : ")
           fiz = input("Enter The Name of File You want to upload on Hadoop Cluster : ")
           os.system('ssh {} hadoop fs -put {} /'.format(ci , fiz))
           print("File Sucessfully Uploaded .......................")
           os.system('ssh {} hadoop fs -ls /'.format(ci))

       elif int(ch) == 7:
           co = input("tEnter Client IP : ")
           fii = input("Enter Your File Name : ")
           os.system('ssh {} hadoop fs -cat /{}'.format(co , fii))

       elif int(ch) == 8:
           ty = input("tEnter Client IP : ")
           foi = input("Enter Your File Name : ")
           os.system('ssh {} hadoop fs -rm /{}'.format(ty , foi))
           print("Sucessfully Deleted File {} ".format(foi))
       
       elif int(ch) == 9:
           os.system('hadoop-daemon.sh stop namenode')
           os.system('jps')

       elif int(ch) == 10:
           ip = input("\nEnter Data Node IP : ")
           os.system('ssh {} hadoop-daemon.sh stop datanode'.format(ip))
           os.system('ssh {} jps'.format(ip))
       
       elif int(ch) == 11:
           exit()



