##############################################################################
# Get full Counter Pages Printers v.0.1 - Development for Victor Sued  - 2016#
#                           Python 3.5 / Copyright ©2016.                    #
##############################################################################

import urllib3
from bs4 import BeautifulSoup

def getCounterHP500(ip):
    http = urllib3.PoolManager()
    url = 'https://' + ip + '/hp/device/InternalPages/Index?id=UsagePage'
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "html.parser")
    table = soup.find('td', id="UsagePage.EquivalentImpressionsTable.Print.Total")
    return round(int(table.get_text().replace(',','')))

def getCounterHP2055(ip):
    http = urllib3.PoolManager()
    url = 'http://' + ip + '/hp/device/info_configuration.htm'
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "html.parser")
    table = soup.find_all('td', {'class': 'itemFont'})
    return round(int(table[16].get_text().replace(',', '')))

def getCounterLexE360(ip):
    http = urllib3.PoolManager()
    url = 'http://' + ip + '/cgi-bin/dynamic/printer/config/reports/deviceinfo.html'
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "html.parser")    
    table = soup.find_all('td')
    return int(table[5].get_text().replace('= ', ''))



