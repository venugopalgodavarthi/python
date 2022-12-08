import xmltodict

with open(r'.setup.xml', 'r')as xml1:
    xmlDict1 = xmltodict.parse(xml1.read())
print(xmlDict1['setup']['workspace'][0]['ClioSoft']['repository'][0])

print(xmlDict1['setup']['workspace'][0]['NoDm'])
