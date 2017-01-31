import urllib
response = urllib.urlopen('http://api.thingspeak.com/channels/103963/field/1/last.txt')
html=response.read()
print html
