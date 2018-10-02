## Load the ipaddress module for IPv4 operations and the OS module for executing the ping utility.
import ipaddress
import os

## Opens the included file activeAddresses.txt in write mode. Output of the command is stored here.
activeAddresses = open("activeAddresses.txt", "w")

## Take user inputed network ID and network prefix, then store the resulting subnet information into
## --variable subnetID
subnetID = ipaddress.ip_network(input('Enter network ID with CIDR prefix appended - > '), strict=False)

## for loop logic for pinging each usable ip address [in order]:
# --iterate through each usable IP address in "subnetID" using the hosts() function, 
# --convert each IP address into a string.
# --ping the IP address, requesting one echo reply with a timeout of 8ms for speed. 
# --print whether an echo reply was received and write the output to activeAddresses.txt 
for i in subnetID.hosts():
    hostAddress = str(i)
    result = str(os.system("ping -n 1 -w 8 " + hostAddress))
    print(result)
    if "0" in result:
        print(hostAddress + " is active", file=activeAddresses)
    else:
        print(hostAddress + " may NOT be active", file=activeAddresses)

## Close the activeAddresses.txt file
activeAddresses.close()

## Planned features:
# --the ability to detect OS in order to specify appropriate parameters for ping utility
