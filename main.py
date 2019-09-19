'''
Created on 15 sept. 2019

@author: david
'''
import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
