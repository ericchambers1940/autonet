import ipaddress
import os
activeAddresses = open("activeAddresses.txt", "w")

subnetID = ipaddress.ip_network(input('Enter network ID with CIDR prefix appended - > '), strict=False)
for i in subnetID.hosts():
    hostAddress = str(i)
    result = str(os.system("ping -n 1 -w 5 " + hostAddress))
    print(result)
    if "0" in result:
        print(hostAddress + " is active", file=activeAddresses)
    else:
        print(hostAddress + " may NOT be active", file=activeAddresses)

activeAddresses.close()