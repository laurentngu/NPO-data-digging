# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:52:34 2017
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

import time
start_time=time.time()

line_number=0
date_time=[]
with open ("X:\_ViewTemplate_FSTP3796_14_16102017_092346PM_CELL2G.scsv") as input_file:
    for line in input_file:
        line_number=line_number+1
        column_number=0
        for nb_sdc_down in line.split(';'):
            column_number=column_number+1
            if (line_number==3):
               date_time.append(nb_sdc_down) 
            if (column_number==1):
                cellname=nb_sdc_down
            if (line_number>=4 and column_number>=2):
                try:
                    cell_float=float(nb_sdc_down)
                    if (cell_float>=1 and cell_float <=10):
                    #if (cell_float>=80 and cell_float <=100):
                        print (cellname +";"+date_time[column_number-1]+";"+nb_sdc_down+";SDCCH_static_unavailable_nb_avg")
                        save_cell=cell_float
                except ValueError:
                    pass #print(cell+" is not a float")
print ("time spent= "+str(round(time.time()-start_time,7))+" seconds")
input_file.close()
