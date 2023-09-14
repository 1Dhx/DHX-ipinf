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
if f["status"] == "success":
    latitude = f["lat"]
    longitude = f["lon"]
    city = f["city"]
    country = f["country"]
    isp = f["isp"]
    status = f["status"]
    timezone = f["timezone"]
    AS  = f["as"]
    org = f["org"]
    print ( '\033[91m' + " ip : "+ '\033[34m' + '{ip}')
    print( '\033[91m' + "country : " +"\033[34m"+ '{country}')
    print ( '\033[91m' + "city : " + '\033[34m' + '{city}')
    print( '\033[91m' + 'lon : ' + '\033[34m' + '{longitude}')
    print('\033[91m' + 'lat : ' + '\033[34m' + '{latitude}')
    print ('\033[91m' + 'isp : ' + '\033[34m' + '{isp}')
    print ('\033[91m' + 'status : '+ '\033[34m' + '{status}')
    print('\033[91m' + 'timezone : ' + '\033[34m' + '{timezone}')
    print('\033[91m' + 'as : ' + '\033[34m' + '{AS}')
    print('\033[91m' + "org : " + '\033[34m' + '{org}')
    
else:
    status = f["status"]
    print('\033[91m'+"status:" + "\033[32m" + f" {status}\n")
    print('\033[91m' + "not connect")
    print("try in ather time")