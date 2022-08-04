#!usr/bin/python3

import subprocess
import optparse
import re


def search_mac_adress(string):
    return re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', str(string)).group(0)


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC adress")
    parser.add_option("-m", "--mac", dest="new_mac_adress", help="New MAC adress")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac_adress:
        parser.error("[-] Please specify a new MAC adress, use --help for more info")
    return options


def set_new_mac_adress(interface, new_mac_adress):
    print("Changing MAC adress for " + interface + " to " + new_mac_adress)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac_adress, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)


def get_mac_adress_from_interface(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_adress_search_result = search_mac_adress(ifconfig_result)

    if mac_adress_search_result:
        return mac_adress_search_result
    else:
        print("[-] Could not read MAC adress")


options = get_arguments()
current_mac_adress = get_mac_adress_from_interface(options.interface)
print("Current MAC adress for interface " + options.interface + " is ; " + current_mac_adress)

set_new_mac_adress(options.interface, options.new_mac_adress)

new_mac_adress = get_mac_adress_from_interface(options.interface)
if new_mac_adress == options.new_mac_adress:
    print("[+] MAC adress was successfully changed to " + new_mac_adress + ".")
else:
    print("[-] MAC adress dit not get changed")
