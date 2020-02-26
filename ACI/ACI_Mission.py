#MISSION.should you chose to accept it

#You will be using the same skills from the lab you just went through. Look for the word MISSION, your challenge will
#be replacing the word MISSION with appropriate python keyword. GOOD LUCK!!

import required libraries
from acitoolkit.acitoolkit import Session
from acitoolkit import Faults
import json
import requests
import ciscosparkapi

URL = 'https://sandboxapicdc.cisco.com'
LOGIN = 'admin'
PASSWORD = 'ciscopsdt'

requests.packages.urllib3.disable_warnings() # Disable warning message
fault_count = {"total": 0, "critical": 0}

# connect to the apic
session = Session(URL, LOGIN, PASSWORD)
session.login()
# <Response [200]> --> If you do not see this response the login did not work

# MISSION: Create an instance of the toolkit class representing ACI Faults
# Hint: the class is called "Faults" and takes no parameters
faults_obj = MISSION()

#Use python dir() functionality to find out properties of class "faults_obj"
#You can see print out different faults properties
#You will need some of the properties in order to complete the mission in next section of the code
dir(faults_obj)

# Monitor the Faults on the APIC
faults_obj.subscribe_faults(session)
while faults_obj.has_faults(session):
    if faults_obj.has_faults(session):
        faults = faults_obj.get_faults(session)

        if faults is not None:
            for fault in faults:
                message = []
                fault_count["total"] += 1
                if fault is not None and fault.severity in ["critical"]:
                    fault_count["critical"] += 1
                    # MISSION: Each fault object has several properties describing the fault.
                    #       Complete each line below with the correct property.
                    #       The first two are already complete.
                    #       Use python dir() functionality to find out properties of object "faults_obj" in the last section 
                    #       to be used in below code to print out different faults properties
                    #       dir(faults_obj)
                    message.append( "****************")
                    message.append( "    Description         : " + fault.descr)
                    message.append( "    Distinguished Name  : " + fault.dn)
                    message.append( "    Rule                : " + fault.MISSION)
                    message.append( "    Severity            : " + fault.MISSION)
                    message.append( "    Type                : " + fault.MISSION)
                    message.append( "    Domain              : " + fault.MISSION)
                    print("\n".join(message))
                    
# Print completion message
print("{} Faults were found.\n  {} listed above are critical".format(fault_count["total"], fault_count["critical"]))

#replace "TOKEN" with personal access token you generated using aci_toolkit lab.
#generate a room_id by adding Room_Id bot to the room and use that room_id below

token = "TOKEN"
room_id = "room_id"

# MISSION: use the appropriate http method to print the result in Webex Teams room
spark = ciscosparkapi.CiscoSparkAPI(access_token=token)
message = spark.messages.MISSION(roomId=room_id, text="{} Faults were found.\n  {} listed above are critical"
                                .format(fault_count["total"], fault_count["critical"]))
exit()

      
