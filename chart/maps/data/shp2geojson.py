# http://geospatialpython.com/2013/07/shapefile-to-geojson.html
from json import dumps

import shapefile
import sys

# read the shapefile
fname = sys.argv[1][:-4]
reader = shapefile.Reader('%s.shp' % fname)
fields = reader.fields[1:]
field_names = [field[0] for field in fields]

for sr in reader.shapeRecords():
    atr = dict(zip(field_names, sr.record))
    if isinstance(atr['nome'], bytes):
        atr['nome'] = atr['nome'].decode('latin1')

    print(atr)
    geom = sr.shape.__geo_interface__
    buffer = dict(type="Feature", geometry=geom, properties=atr)
   
    # write the GeoJSON file
    geojson = open("%s-%s.json" % (fname, atr['sigla']), "w")
    geojson.write(
        dumps({
            "type": "FeatureCollection",
            "features": [buffer]
        }, indent=2) + "\n"
    )
geojson.close()
