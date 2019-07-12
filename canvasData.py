#!/usr/bin/env python3
# 
# This program 
# 1- pulls data from canvas 
# 2- unpacks the files
# 3- checks for errors
#

# echo a date in a nice format
import datetime
import sys
from canvasFunctions import *
import numpy as np


logFile = datetime.datetime.now().strftime("%Y%m%d-%H%M")
sys.stderr = open('/data/informatica/canvas/log/' + logFile + '.error', 'w')
sys.stdout = open('/data/informatica/canvas/log/' + logFile + '.log', 'w')
 
# 1 - Sync the data from Canvas 
sync_data_from_canvas()

#  2 - Get Table Lists
canvas_table = get_canvas_table_list()
master_table = get_master_table_list()

#  3 - unpack each file
unpack_canvas_data(master_table)

clean_canvas_files(master_table)

#  4 - error checking
# check_for_issues(canvas_table, master_table)
