import pandas as pd
import xmltodict
from bs4 import BeautifulSoup

# Read data
xml_data = open(r'C:\Users\QSP\.vscode\python\properties.xml', 'r').read()
xmlDict = xmltodict.parse(xml_data)  # Parse XML
cols = xmlDict['root'].keys()
data = []

for i in xmlDict['root']:
    child = xmlDict['root'][i]
    data.append([child[subchild]['#text'] for subchild in child])

df = pd.DataFrame(data).T  # Create DataFrame and transpose it.
df.columns = cols
print(df)
