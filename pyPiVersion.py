#!/usr/bin/env python
# Copyright (c) 2012 Christian Bayer

#pyPiVersion.py reads revision and serial from /proc/cpuinfo 
#and prints some additional data. newer versions are available 
#on https://github.com/cavebeat/pyPiVersion

##########################################################################
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################

__author__ = "Ing. Christian Bayer"
__copyright__ = "Copyright 2012"
__credits__ = ["Christian Bayer"]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Christian Bayer"
__email__ = "chri.bayer@gmail.com"
__status__ = "testing"


myInputFile = open("/proc/cpuinfo", "r")

hardware = "#"
stickybit = "#"

for line in myInputFile.readlines():
    if line.find("Hardware") != -1:
        hardware = line[11:18]
    if line.find("Revision") != -1:
        #print line[11:14]
        revision = line[11:15]
        if revision == "1000":
            stickybit = revision[0:3]
            revision = line[14:18]
    if line.find("Serial") != -1:
        serial = line[11:]
myInputFile.close()

if hardware != "BCM2708":
	print "This is not a Raspberry Pi Board"
else:	
	if revision == "beta":
		print "Revision Number: ", revision, ", <-- Beta Board"
	elif revision == "0002":
		print "Revision Number: ", revision, ", Model B from Q1 2012, PCB revision 1.0, 256Mb, first production run"
	elif revision == "0003":
		print "Revison Number: ", revision, ", Model B from Q3 2012, PCB revision 1.0, 256Mb, ECN0001 is the request to not fit D14 and replace F1 and F2 with 0 ohm."
	elif revision == "0004":
		print "Revision Number: ", revision, ", Model B from Q3 2012, PCB revision 2.0, 256Mb, changes on 1V8 Power Rail, added mounting holes, removed polyfuses for +5V USB power rail, added 8pin P5 header, 2pin P6 header for reset"
	elif revision == "0005":
		print "Revision Number: ", revision, ", Model B from Q3 2012, PCB revision 2.0, 512Mb, changes on 1V8 Power Rail, added mounting holes, removed polyfuses for +5V USB power rail, added 8pin P5 header, 2pin P6 header for reset"
	else:
		print "Revision Number: ", revision, ",  <-- please update Firmware or update pyPiVersion.py again and run it again"	
	print "Your serial number is: ", serial,
if stickybit == "100":
    print "Your sticky bit is set: ", stickybit

	
