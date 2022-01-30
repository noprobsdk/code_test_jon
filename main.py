# Imports
import json
from tkinter import font

import background as background
import family as family
import requests

# My Apis
henriksData = requests.get('https://i.thonhotels.no/pub/sf/FormLink?_ri_=X0Gzc2X%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNzeweOReTlDTzaEAyiJwwnagf0zbvLjGVXyjLNpLOfhKLX%3DjLpkLxHNLgHggLgNLjKLgQghVXMtX%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNMSh8D17tza0mWUqfpywqNGlGqW5kJ HYPERLINK "https://i.thonhotels.no/pub/sf/FormLink?_ri_=X0Gzc2X%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNzeweOReTlDTzaEAyiJwwnagf0zbvLjGVXyjLNpLOfhKLX%3DjLpkLxHNLgHggLgNLjKLgQghVXMtX%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNMSh8D17tza0mWUqfpywqNGlGqW5kJ&_ei_=Erdv7PMYfAm0WU0r9JH49_wmGS4.&_di_=t61475eoe4q8sm30kdnv2a5src77j1tgcqjvlp95rh6e65fep620RS_ENDPOINThttps://login2.responsys.netRS_PASSWORDkioSDKAQ8390dj!kjcvjhdKjdyuzshstyRS_USERNAMEAPI@ARCHIVE"& HYPERLINK "https://i.thonhotels.no/pub/sf/FormLink?_ri_=X0Gzc2X%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNzeweOReTlDTzaEAyiJwwnagf0zbvLjGVXyjLNpLOfhKLX%3DjLpkLxHNLgHggLgNLjKLgQghVXMtX%3DAQpglLjHJlTQGkj48Jzb15yuAIPol4glMnyNMSh8D17tza0mWUqfpywqNGlGqW5kJ&_ei_=Erdv7PMYfAm0WU0r9JH49_wmGS4.&_di_=t61475eoe4q8sm30kdnv2a5src77j1tgcqjvlp95rh6e65fep620RS_ENDPOINThttps://login2.responsys.netRS_PASSWORDkioSDKAQ8390dj!kjcvjhdKjdyuzshstyRS_USERNAMEAPI@ARCHIVE"_ei_=Erdv7PMYfAm0WU0r9JH49_wmGS4.')
data = henriksData.json()
print(data)
thisdict = {}

# Python Test6
table = '<tr> <td> # </td> <td> Folder </td> <td> Table_ </td> <td> Riid </td> </tr>'
talNr = 1
for innerData in data['data']:
    table += '<tr>'
    table += '<td>' + str(talNr) + '<td/>'
    table += '<td>' + innerData['folder'] + '</td>'
    table += '<td>' + innerData['table'] + '</td>'
    table += '<td>' + innerData['riid_'] + '</td> '
    table += '</tr>'
    talNr += 1

    key = innerData['table']
    if key in thisdict:
        thisdict[key].append(innerData)
    else:
        thisdict[key] = [innerData]

tables = []

# HTML Test6
html_content = f"""
<html> 
<head> 
</head>
 <style>
table {{
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}}

td, th {{
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}}

tr:nth-child(even) {{
  background-color: #dddddd;
}}
</style>
<h1>
<table>
{table}
</table>
</h1>
<body>
</body>
</html>"""

with open("test6.html", "w") as html_file:
    html_file.write(html_content)
    print('Html 6 success')

# Python Test 7

for key, value in thisdict.items():
    table = '<tr> <td> # </td> <td> Folder </td> <td> Riid </td> </tr>'
    talNr = 1
    for innerData in value:
        table += '<tr>'
        table += '<td>'+str(talNr)+'<td/>'
        table += '<td>'+innerData['folder']+'</td>'
        table += '<td>'+innerData['table']+'</td>'
        table += '<td>'+innerData['riid_']+'</td> '
        table += '</tr>'
        talNr += 1
    newTable = key+'<table>'+table+'</table>'
    tables.append(newTable)

opgave7Content=''
for x in tables:
    opgave7Content += x

# HTML Test 7
html_content = f"""
<html> 
<head> 
</head>
 <style>
table {{
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}}

td, th {{
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}}

tr:nth-child(even) {{
  background-color: #dddddd;
}}
</style>
<h1>
<table>
{opgave7Content}
</table>
</h1>
<body>
</body>
</html>"""

with open("test7.html", "w") as html_file:
    html_file.write(html_content)
    print('Html 7 success')

# Python Test 8
numberRow = 0
headerRow = '<tr> <td> # </td> <td> Folder </td> <td> Table_ </td> <td> Riid </td> </tr>'
table8 = ''
talNr = 1
tableList8 = []

for innerData in data['data']:
    if numberRow <= 99:
        table8 += '<tr>'
        table8 += '<td>'+str(talNr)+'<td/>'
        table8 += '<td>'+innerData['folder']+'</td>'
        table8 += '<td>'+innerData['table']+'</td>'
        table8 += '<td>'+innerData['riid_']+'</td> '
        table8 += '</tr>'
        talNr += 1
        numberRow += 1
    else:
        newTable = '<table>' + headerRow + table8+'</table> <br>'
        tableList8.append(newTable)
        talNr = 1
        numberRow = 0
        table8=''

opgave8Content=''
for x in tableList8:
    opgave8Content += x


# HTML Test 8
html_content = f"""
<html> 
<head> 
</head>
 <style>
table {{
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}}

td, th {{
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}}

tr:nth-child(even) {{
  background-color: #dddddd;
}}
</style>
<h1>
<table>
{opgave8Content}
</table>
</h1>
<body>
</body>
</html>"""

with open("test8.html", "w") as html_file:
    html_file.write(html_content)
    print('Html 8 success')