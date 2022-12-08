import pandas as pd
import xmltodict

# Read data
with open(r'C:\Users\QSP\.vscode\python\ExecHandler2', 'r')as xml1, open(r'C:\Users\QSP\.vscode\python\ExecHandler3', 'r') as xml2:
    xmlDict1 = xmltodict.parse(xml1.read())  # Parse XML
    xmlDict2 = xmltodict.parse(xml2.read())  # Parse XML

    # find out the list of job_def entry names:
    xd1 = xmlDict1['ls_config']['job_def']['entry']
    xd2 = xmlDict2['ls_config']['job_def']['entry']

    u = [i for i in xd1 if i not in xd2]
    print(len(u))

    l = [i for i in xd2 if i not in xd1]
    print(len(l))

    def extract(u, l):
        lp = []
        for k in u:
            for m in l:
                jo = []
                if k['@name'] == m['@name']:
                    o = [i for i in k['option'] if i not in m['option']]
                    p = [i for i in m['option'] if i not in k['option']]
                jo += [[k['@name'], {"file1": p, "file2": o}]]
            lp += [jo]
        for i in lp:
            print(i)
    print('-----------------------file1-------------------')
    extract(u, l)
    print('-----------------------file2-------------------')
    extract(l, u)
