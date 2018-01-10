# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:52:34 2017

updated on 10/01/2018
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

import time,re,os
start_time=time.time()

filenames = ['1_ViewTemplate_FSTP3796_4_10012018_111137AM_CELL2G.scsv', '2_ViewTemplate_FSTP3796_5_10012018_111508AM_CELL2G.scsv' \
,'3_ViewTemplate_FSTP3796_6_10012018_112905AM_CELL2G.scsv','4_ViewTemplate_FSTP3796_7_10012018_114511AM_CELL2G.scsv'\
,'5_ViewTemplate_FSTP3796_8_10012018_121713PM_CELL2G.scsv','6_ViewTemplate_FSTP3796_9_10012018_123020PM_CELL2G.scsv'\
,'7_ViewTemplate_FSTP3796_10_10012018_010258PM_CELL2G.scsv','8_ViewTemplate_FSTP3796_13_10012018_012830PM_CELL2G.scsv',\
'9_ViewTemplate_FSTP3796_14_10012018_015128PM_CELL2G.scsv','10_ViewTemplate_FSTP3796_15_10012018_020729PM_CELL2G.scsv']
with open('C:\\PYTHON_REGIS\\CONCAT.scsv', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
outfile.close()

line_number=0
date_time=[]
with open ('C:\\PYTHON_REGIS\\FINAL_A_to_L.scsv','w') as outfile:
    with open ("C:\\PYTHON_REGIS\\CONCAT.scsv") as input_file:
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
                        match1=re.search(r'09:00|10:00|11:00|12:00|13:00|14:00|15:00|16:00|17:00|18:00|19:00|20:00',date_time[column_number-1])
                        match2=re.search(r'G1$|G2$|G3$|G4|g1$|g2$|g3$|g4$',cellname)
                       # match3=re.search('^((?!D[1-4]).)*$',cellname)
                        if (cell_float>=1 and cell_float <=3 and match1 and match2):
                        #if (cell_float>=80 and cell_float <=100):
                            outfile.write(cellname +";"+date_time[column_number-1]+";"+nb_sdc_down+";SDCCH_static_unavailable_nb_avg"+"\n")
                            save_cell=cell_float
                    except ValueError:
                        pass #print(cell+" is not a float")
    print("time spent= "+str(round(time.time()-start_time,7))+" seconds")
input_file.close()
outfile.close()
#os.remove("C:\\PYTHON_REGIS\\CONCAT.scsv")
