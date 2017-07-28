#!/usr/bin/python

import gdal
import h5py
import osr
import sys
import numpy as np
from matplotlib import cm

expand_data = lambda h5: h5['Geophysical Data'][:,:,0]

def get_band(data, ct):
	index = lambda val: 0 if val<=-32767 else int(val/100.*5.08+51.8+0.5)
	r = np.ndarray((1800,3600), np.byte)
	g = np.ndarray((1800,3600), np.byte)
	b = np.ndarray((1800,3600), np.byte)
	a = np.ndarray((1800,3600), np.byte)
	for y in range(1800):
		for x in range(3600):
			color = ct.GetColorEntry(index(data[y][x]))
			r[y][x] = color[0]
			g[y][x] = color[1]
			b[y][x] = color[2]
			a[y][x] = color[3]
	return (r,g,b,a)


def make_colortable():
	cm.jet.N = 1000
	ct = gdal.ColorTable(gdal.GPI_RGB)
	for i in range(cm.jet.N):
		ct.SetColorEntry(i, map(lambda x:int(x*255), cm.jet(i)))
	return ct


def array_to_raster(outfile, data):
	ct = make_colortable()
	band = get_band(data,ct)

	driver = gdal.GetDriverByName('GTiff')
	out = driver.Create(outfile, 3600, 1800, 4, gdal.GDT_Byte)
	out.SetGeoTransform((0.0, 0.1, 0, 90, 0, -0.1))

	ci = (gdal.GCI_RedBand, gdal.GCI_GreenBand, gdal.GCI_BlueBand,gdal.GCI_AlphaBand)
	for i in range(4):
		b = out.GetRasterBand(i+1)
		b.SetColorInterpretation(ci[i])
		b.WriteArray(band[i])
		b.FlushCache()
	srs = osr.SpatialReference()
	srs.ImportFromEPSG(4326)
	out.SetProjection(srs.ExportToWkt())


def averaged_data(files):
	val = np.zeros((1800,3600),np.int32)
	count = np.zeros((1800,3600),np.int16)

	for f in files:
		h5 = h5py.File(f)
		data = expand_data(h5)
		h5.close()

		mask = data>-99
		tmp = np.zeros((1800,3600),np.int16)
		tmp[mask] = 1
		count = np.add(count,tmp)

		tmp = np.copy(data)
		tmp[np.logical_not(mask)] = 0.
		val = np.add(val, tmp)

	mask = (count == 0)
	val[mask] =-32767 
	count[mask] = 1
	return np.divide(val.astype(np.double), count.astype(np.double))

if(__name__=='__main__'):
	data = averaged_data(sys.argv[2:])
	array_to_raster(sys.argv[1], data)

