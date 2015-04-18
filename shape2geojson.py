import sys
import shapefile

# read the shapefile
print 'Reading data from', sys.argv[1], 'to', sys.argv[2]
reader = shapefile.Reader(sys.argv[1])
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
	atr = dict(zip(field_names, sr.record))
	geom = sr.shape.__geo_interface__
	buffer.append(dict(type="Feature", geometry=geom, properties=atr)) 

# write the GeoJSON file
from json import dumps
geojson = open(sys.argv[2], "w")
geojson.write(dumps({"type": "FeatureCollection", "features": buffer}, indent=2, encoding='iso8859-1') + "\n")
geojson.close()
