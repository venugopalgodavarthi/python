import xmltodict

with open(r'.setup.xml', 'r')as xml1:
    xmlDict1 = xmltodict.parse(xml1.read())

li = []
for wspace in xmlDict1['setup']['workspace']:
    if type(wspace['ClioSoft']['repository']) in [list, tuple]:
        for resp in wspace['ClioSoft']['repository']:
            li += [[wspace['@id'], resp['@id'], resp['@name'], resp['@root']]]
    else:
        li += [[wspace['@id'], wspace['ClioSoft']['repository']
                ['@id'], wspace['ClioSoft']['repository']
                ['@name'], wspace['ClioSoft']['repository']['@root']]]

    if type(wspace['NoDm']['repository']) in [list, tuple]:
        for resp in wspace['NoDm']['repository']:
            li += [[wspace['@id'], resp['@id'], resp['@name'], resp['@root']]]
    else:
        li += [[wspace['@id'], wspace['NoDm']['repository']
                ['@id'], wspace['NoDm']['repository']
                ['@name'], wspace['NoDm']['repository']['@root']]]

print("WORKSPACE", '         ', 'repository',
      '          ', 'Name', '          ', 'Root')
print("----"*30)
for data in li:
    print(data[0], '        ', data[1], '        ',
          data[2], '          ', data[3])

# question2
getlist = [i[3] for i in li]
testlist = ['/home/iwinfratest/zNoDM_Clio/cliosoft/cliosoft.[user].default123',
            '/home/iwinfratest/zNoDM_Clio/cliosoft/cliosoft.[user].default1235']+getlist

for tvalue in testlist:
    if tvalue in getlist:
        for actualvalue in li:
            if tvalue == actualvalue[3]:
                print(actualvalue[1], actualvalue[0])
            else:
                print("not match")


# if i == j[3]:
#     print(j[1], j[0])
#     temp=False
# elif temp==False:
#     print("no match")
