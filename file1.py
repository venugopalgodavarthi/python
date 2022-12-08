import pandas as pd
import xmltodict
from bs4 import BeautifulSoup

# Read data
with open(r'C:\Users\QSP\.vscode\python\ExecHandler2', 'r')as xml1, open(r'C:\Users\QSP\.vscode\python\ExecHandler3', 'r') as xml2:

    xmlDict1 = xmltodict.parse(xml1.read())  # Parse XML
    xmlDict2 = xmltodict.parse(xml2.read())  # Parse XML

    # check diff entry names
    def check(file1, li):
        lo = []
        for i in range(0, len(file1)):
            if file1[i]['@name'] not in li:
                lo.append(file1[i]['@name'])
        return lo

    # os1 = xmlDict1['ls_config']['os_def']['group']
    # os2 = xmlDict2['ls_config']['os_def']['group']

    # # find out the list of entry names:
    # ol1 = [os1[i]['@name'] for i in range(0, len(os1))]
    # ol2 = [os2[i]['@name'] for i in range(0, len(os2))]
    # print(len(ol1))
    # print(len(ol2))

    # check(os1, ol2)
    # check(os2, ol1)
    # df = pd.DataFrame(data).T  # Create DataFrame and transpose it.
    # df.columns = cols
    # print(df)
    # os1 = xmlDict1['ls_config']['os_def']['entry']
    # os2 = xmlDict2['ls_config']['os_def']['entry']

    # # find out the list of entry names:
    # ol1 = [os1[i]['@name'] for i in range(0, len(os1))]
    # ol2 = [os2[i]['@name'] for i in range(0, len(os2))]
    # print(len(ol1))
    # print(len(ol2))

    # check(os1, ol2)
    # check(os2, ol1)

    xd1 = xmlDict1['ls_config']['job_def']['entry']
    xd2 = xmlDict2['ls_config']['job_def']['entry']

    # find out the list of entry names:
    list1 = [xd1[i]['@name'] for i in range(0, len(xd1))]
    list2 = [xd2[i]['@name'] for i in range(0, len(xd2))]
    print(len(list1))
    print(len(list2))

    print("-------------------file1---------------------")
    print(check(xd1, list2))
    print("-------------------file2---------------------")
    print(check(xd2, list1))
    data = [check(xd1, list2), check(xd2, list1)]

    df = pd.DataFrame(data).T  # Create DataFrame and transpose it.
    df.columns = ['file1', 'file2']
    print(df)
    # checkoption(xd1, list2)
    # checkoption(xd2, list1)

    # # for i in range(0, len(xd1)):
    # #     if xd1[i]['@name'] in xd2:
    # #         if xd1[i]['@name']
