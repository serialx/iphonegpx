import sqlite3
from datetime import datetime, timedelta

s = sqlite3.connect('./consolidated.db')

c = s.cursor()

c.execute('select Timestamp, Latitude, Longitude from CellLocation where HorizontalAccuracy <= 1000')

data = []

for r in c:
    timestamp_apple, lat, long_ = r
    date = datetime(2001, 1, 1) + timedelta(seconds=timestamp_apple)
    data.append((date, lat, long_))

print """<?xml version="1.0" encoding="UTF-8" standalone="no" ?>

<gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" creator="Oregon 400t" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd">
  <metadata>
    <link href="http://www.garmin.com">
      <text>Garmin International</text>
    </link>
    <time>""" + data[0][0].isoformat() + """</time>
  </metadata>
  <trk>
    <name>Example GPX Document</name>
    <trkseg>"""

for (date, lat, long_) in data:
    print '<trkpt lat="%s" lon="%s">' % (lat, long_)
    print '<time>%s</time>' % date.isoformat()
    print '</trkpt>'


print """    </trkseg>
  </trk>
</gpx>"""
