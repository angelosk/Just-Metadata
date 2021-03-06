'''
This is a module that can gathers whois information about the
loaded IP addresses
'''

from ipwhois.ipwhois import IPDefinedError
from ipwhois import IPWhois
from common import helpers


class IntelGather:

    def __init__(self):
        self.cli_name = "Whois"
        self.description = "This module gathers whois information"

    def gather(self, all_ips):

        for path, incoming_ip_obj in all_ips.items():

            if incoming_ip_obj[0].ip_whois == "":

                try:
                    print("Gathering whois information about " + incoming_ip_obj[0].ip_address)
                    ip_whois = IPWhois(incoming_ip_obj[0].ip_address)
                    incoming_ip_obj[0].ip_whois = ip_whois.lookup()
                except IPDefinedError:
                    print(helpers.color("[*] Error: Private IP address, skipping IP!", warning=True))
        return
