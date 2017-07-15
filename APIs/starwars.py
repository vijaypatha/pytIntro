import urllib2
import json

def starWars(query):
    url = 'http://swapi.co/api/people'
    data = json.load(url)
    json_obj = url
    for item in json_obj[object]:
        print item['name']
starWars('Luke')
