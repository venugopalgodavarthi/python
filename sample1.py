import pandas as pd
import xmltodict

# Read data
with open(r'C:\Users\QSP\.vscode\python\ExecHandler2', 'r')as xml1, open(r'C:\Users\QSP\.vscode\python\ExecHandler3', 'r') as xml2:
    xmlDict1 = xmltodict.parse(xml1.read())  # Parse XML
    xmlDict2 = xmltodict.parse(xml2.read())  # Parse XML

    cols = ['1.10.3', '2.0.4']
    # check diff entry names

    def check(file1, li):
        return [file1[i]['@name'] for i in range(0, len(file1)) if file1[i]['@name'] not in li]

    def List_Count(data):
        return [data[i]['@name'] for i in range(0, len(data))]

    # find out the list of os_def group names:
    os1 = xmlDict1['ls_config']['os_def']['group']
    os2 = xmlDict2['ls_config']['os_def']['group']
    data = [check(os1, List_Count(os2)), check(os2, List_Count(os1))]
    df = pd.DataFrame(data).T
    df.columns = cols
    print("-------------os_def group level different----------------")
    print(df)

    # find out the list of os_def entry names:
    os1 = xmlDict1['ls_config']['os_def']['entry']
    os2 = xmlDict2['ls_config']['os_def']['entry']
    data = [check(os1, List_Count(os2)), check(os2, List_Count(os1))]
    df = pd.DataFrame(data).T
    df.columns = cols
    print("-------------os_def entry level different----------------")
    print(df)

    # find out the list of job_def entry names:
    xd1 = xmlDict1['ls_config']['job_def']['entry']
    xd2 = xmlDict2['ls_config']['job_def']['entry']
    data = [check(xd1, List_Count(xd2)), check(xd2, List_Count(xd1))]
    df = pd.DataFrame(data).T
    df.columns = cols
    print("-------------job_def entry different----------------")
    print(df)

    # find out the list of site_def entry names:
    xd1 = xmlDict1['ls_config']['site_def']['definition']
    xd2 = xmlDict2['ls_config']['site_def']['definition']
    data = [check(xd1, List_Count(xd2)), check(xd2, List_Count(xd1))]
    df = pd.DataFrame(data).T
    df.columns = cols
    print("-------------site_def different----------------")
    print(df)
