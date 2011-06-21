#!/usr/bin/env python
from __future__ import print_function, division
import os

def fix_lon_lat(string):
    direction = string[-1]
    whole, part = string[:-1].split()
    whole = float(whole)
    part = float(part)/60.
    location = whole + part
    if direction.upper() in ['S','W']:
        return -location
    else:
        return location


if __name__ == '__main__':
    stations = []
    icaos = []
    iatas = []
    synops = []
    lats = []
    lons = []
    elevs = []
    ps = []

    # Read in original file; strip out non-station lines
    fpath = os.path.join('../stations/data', 'stations.txt')
    flines = open(fpath, 'r').readlines()
    for f in flines[:]:
        if len(f) != 84: continue
        f.rstrip()
        stations.append(f[3:20].strip())
        icaos.append(f[20:26].strip())
        iatas.append(f[26:32].strip())
        synops.append(f[32:39].strip())
        lats.append(f[39:47].strip())
        lons.append(f[47:55].strip())
        elevs.append(int(f[55:59].strip()))
        ps.append(int(f[79:80].strip()))

    # Convert lat-lons from strings (DD MM) to decimals (DD.xx)
    lats = [fix_lon_lat(x) for x in lats]
    lons = [fix_lon_lat(x) for x in lons]

    outpath = os.path.join('../stations', 'sfc.py')
    outfile = open(outpath, 'w')
    outfile.write('#!/usr/bin/env python\n\n')
    outfile.write('__all__ = ["get_stn", "icao", "iata", "synop"]\n\n')
    func = """
def get_stn(stn):
    stn = stn.strip().upper()
    x = len(stn)
    if x == 3: return(iata[stn])
    elif x == 4: return(icao[stn])
    elif x == 5: return(synop[stn])
    else: print('Unable to process request...')

"""
    outfile.write(func)
    outfile.write('icao = {\n')
    for i in range(len(stations)):
        if icaos[i] != '':
            outfile.write('    "%s": [%.4f, %.4f, %i],\n' % (icaos[i],
                lons[i], lats[i], ps[i]))
    outfile.write('    }\n\n')

    outfile.write('iata = {\n')
    for i in range(len(stations)):
        if iatas[i] != '':
            outfile.write('    "%s": [%.4f, %.4f, %i],\n' % (iatas[i],
                lons[i], lats[i], ps[i]))
    outfile.write('    }\n\n')

    outfile.write('synop = {\n')
    for i in range(len(stations)):
        if synops[i] != '':
            outfile.write('    "%s": [%.4f, %.4f, %i],\n' % (synops[i],
                lons[i], lats[i], ps[i]))
    outfile.write('    }\n\n')
