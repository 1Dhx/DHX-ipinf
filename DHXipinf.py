import os
import pprint
os.system("clear")
# banner
print('''\033[34m
DHX IP IFORMATION
--- ******** ---
   * _!!!!_ *
  * /  \   \ *
 *  (<o><o>)  *
 *  \>_db_</  *
  *   |vv|   *
   *  (__)  *
--- ******** ---
YOUTUBE:  https://youtube.com/@DHXCode?si=hyiZeayKjcDQiITn
\033[32m
'''
)
#library

try:
        import requests
except:
        os.system("pip install requests")
        import requests
        os.system("clear")
        print('''\033[34m
DHX IP IFORMATION
--- ******** ---
   * _!!!!_ *
  * /  \   \ *
 *  (<o><o>)  *
 *  \>_db_</  *
  *   |vv|   *
   *  (__)  *
--- ******** ---
YOUTUBE:  https://youtube.com/@DHXCode?si=hyiZeayKjcDQiITn

\033[32m
'''
)
#make session and get date
ip = input("type RHOST >>>>>>>")
url = f"https://ip-api.com/json/{ip}"
f = requests.get(url).json()
#scan ports
try:
        os.system("clear")
        print('##############port info##############')
        os.system(f"nmap -A {ip}")
except:
        os.syste("pkg update; pkg upgrade; pkg install nmap -y")
        os.sytem("clear")
        print('\034[34m ##############port info##############')
        os.system(f"nmap -A {ip}")


#information to ip
print ("_____________________________________________")
print ("###############info ip########################")
if ["status"] == "success":
    latitude = ["lat"]
    longitude = ["lon"]
    city = ["city"]
    country = ["country"]
    isp = ["isp"]
    status = ["status"]
    timezone = ["timezone"]
    proxy  = ["proxy"]
    org = ["org"]
    print ( '\033[91m' + " ip : "+ '\033[34m' + '{ip}')
    print( '\033[91m' + "country : " +"\033[34m"+ f['{country}'])
    print ( '\033[91m' + "city : " + '\033[34m' + f['{city}'])
    print( '\033[91m' + 'lon : ' + '\033[34m' + f['{longitude}'])
    print('\033[91m' + 'lat : ' + '\033[34m' + f['{latitude}'])
    print ('\033[91m' + 'isp : ' + '\033[34m' + f['{isp}'])
    print ('\033[91m' + 'status : '+ '\033[34m' + f['{status}'])
    print('\033[91m' + 'timezone : ' + '\033[34m' + f['{timezone}'])
    print('\033[91m' + 'as : ' + '\033[34m' + f['{proxy}'])
    print('\033[91m' + "org : " + '\033[34m' + f['{org}'])
    
else:
    status = ["status"]
    print('\033[91m'+"status:" + "\033[32m" + f ['status']+'\n')
    print('\033[91m' + "not connect")
    print("try in ather time")
