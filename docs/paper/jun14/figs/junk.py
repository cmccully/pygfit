#!/usr/bin/python

import pyfits
import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FormatStrFormatter

import matplotlib

#matplotlib.rcParams['axes.formatter.limits']= -7,7
#pyplot.ticklabel_format(style='sci',axis='x',scilimits=(-7,7))

#Format tickmarks on Axes
majorFormatter = FormatStrFormatter('%0.3f')
#xform = NullFormatter()
minorFormatter = FormatStrFormatter('%.1f')



class label_hider(ticker.Formatter):
	def __init__( self, to_hide, format ):
		self.hide = to_hide
		self.format = format
	def __call__( self, a, pos=None ):
		return '' if a == self.hide else self.format % a

pyplot.rcParams.update( {'legend.fontsize': 'medium', 'legend.numpoints': 1, 'figure.subplot.wspace': 0, 'figure.subplot.hspace': 0, }  )

cat = pyfits.open( '/scratch1/cmancone/sizes_wfc3/fits/pygfit/29/separation_test/ch1/results.cat' )[1].data

cat = cat[cat['mag']-cat['mag_brightest']<5]

cleaned = cat[cat['nearest']/1.66 > 1.0]

#pyplot.ticklabel_format(style='sci',axis='x',scilimits=(-0,0))




ax=pyplot.subplot( 121 )
#ax.yaxis.set_major_formatter(majorFormatter)
ax.xaxis.set_major_formatter(majorFormatter)
ax.set_xscale( 'log' )
#pyplot.gca().ticklabel_format(axis='x',style='sci',scilimits=(1,4))
ax.plot( cleaned['flux_ratio'], cleaned['mag']-cleaned['mag_input'], 'ko', ms=2 )
pyplot.xlabel( 'Flux Ratio' )
pyplot.ylabel( 'Mag Diff (In-Out)' )
#pyplot.axvline( 0.5, color='black', lw=2 )
ax.axis( ymin=-3, ymax=3, xmax=20, xmin=6e-2 )
[ xmin, xmax, ymin, ymax ] = ax.axis()
#pyplot.gca().xaxis.set_major_formatter( label_hider( xmax, '%.0f' ) )

cleaned = cat[cat['flux_ratio'] > 1.0]
##cleaned = cat
#pyplot.subplot( 122 )
#pyplot.plot( cleaned['nearest']/1.66, cleaned['mag']-cleaned['mag_input'], 'ko', ms=2 )
#pyplot.xlabel( 'Separation/FWHM' )
#pyplot.gca().yaxis.set_major_formatter( ticker.NullFormatter() )
#pyplot.axis( ymin=-3, ymax=3, xmin=0.0 )
##pyplot.gca().xaxis.set_major_formatter( label_hider( 0, '%.2f' ) )
##pyplot.axvline( 0.6, color='black', lw=2 )

pyplot.gcf().set_size_inches( (8.,4.5) )
pyplot.savefig( 'ps/close_sim.eps' )
pyplot.clf()