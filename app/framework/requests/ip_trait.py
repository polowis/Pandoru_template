import socket
import requests
import json
from ..util import *

def is_valid_ipv4_address(address):
    """Return true if valid IPv4 address"""
    try:
        if(isinstance(address, str) == False):
            raise socket.error
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            if(isinstance(address, str) == False):
                raise socket.error
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def is_valid_ipv6_address(address):
    """return true if valid ipv6 address"""
    try:
        if(isinstance(address, str) == False):
            raise socket.error
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True

def is_valid_ip(address):
    return is_valid_ipv4_address(address) or is_valid_ipv6_address(address)


class IP:
    """Class base to handle incoming user ip address"""
    def __init__(self, ip):
        self.ip = ip
        self.details = self.getDetails()
        self.address = self.get_address_name_by_ip()
        self.city = self.get_city_name_by_ip()
        self.state = self.get_state_name_by_ip()
        self.region = self.get_region_name_by_ip()
        self.country = self.get_country_name_by_ip()
        self.country_code = self.details["geoplugin_countryCode"]
    
    def get_country_name_by_ip(self):
        """return country name"""
        return self.details["geoplugin_countryName"]

    def get_city_name_by_ip(self):
        """return city name"""
        return self.details["geoplugin_city"]

    def get_state_name_by_ip(self):
        """return state name"""
        return self.details["geoplugin_region"]
    
    def get_region_name_by_ip(self):
        """return region name"""
        return self.details["geoplugin_region"]
    
    def get_address_name_by_ip(self):
        """Return countryName, regionName and cityName"""
        address = []
        address.append(self.country)

        if(len(self.state) >= 1):
            address.append(self.state)

        if(len(self.city) >=1):
            address.append(self.city)
        return ', '.join(address.reverse()) 
        

    def getDetails(self):
        """Return all you need to know about this ip address"""
        url = 'http://www.geoplugin.net/json.gp?ip={}'.format(self.ip)
        res = requests.get(url)
        j = json.loads(res.text)
        return j
