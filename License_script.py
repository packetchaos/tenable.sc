#!/usr/bin/env python3
#Disclaimer: This is NOT supported By Tenable!
#This script pull the licensing information from SC
from tenable.sc import TenableSC
sc = TenableSC("1.1.1.1")
sc.login("admin", "password")

def status_Check():
    sc_license = sc.status.status()
    active_ips = sc_license['activeIPs']
    licensed_ips = sc_license['licensedIPs']
    utilization = int(100 * int(active_ips) / int(licensed_ips))

    print("Your License Status")
    print("-------------------")
    print("Your Purchased license for this SC is : {} ".format(licensed_ips))
    print("Your License Usage is : {} ".format(active_ips))
    print("Your current utilization is : {}% ".format(utilization))

if __name__ == '__main__':
    status_Check()
