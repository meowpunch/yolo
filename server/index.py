#!C:\Users\Dururyu\AppData\Local\Programs\Python\Python37-32\python.exe
print("content-type:text/html; charset=UTF-8\n")
print()
import cgi, os
files = os.listdir('src')
listStr = ''
for item in files:
    file_name = item.split('.')
    if file_name[0] != "default": #default.jpg 를 읽는 경우는 제외시킨다.
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=file_name[0])

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value + '.jpg'
else:
    pageId = 'default.jpg'
print('''<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="00.css">
  </head>
  <body>
    <h3>CCTV_Location</h3>
    <!--The div element for the map -->
    <div id="map"></div>
    <script src="00.js"></script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD4B5pf3hKDdLRdPSIdeO8TAQ7Wmli9w78&callback=initMap">
    </script>
    <img src="src/{jpgName}" style="height:300px;display:inline-flex">
    <ol>
        {listStr}
    </ol>
  </body>
</html>
'''.format(listStr = listStr, jpgName = pageId))
