#!/usr/bin/env python

from __future__ import division
from scapy.all import *

from scapy.layers import http
import pymongo
import mpd_insert
from collections import defaultdict
from datetime import datetime
stars = lambda n: "*" * n

				 
				 
hit_count={"89283":0,"262537":0,"791182":0,"2484135":0,"4219897":0}
mpd_name = "/var/www/html/www-itec.uni-klu.ac.at/ftp/datasets/DASHDataset2014/BigBuckBunny/2sec/"
for i in range (1,51):
	f_name = mpd_name + "BigBuckBunny_2s_mod" + str(i) + ".mpd"
	#print f_name
	mpd_insert.read_mpd(f_name)
	
