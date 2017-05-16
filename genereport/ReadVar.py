import logging
import argparse
from glob import glob
import os
import sys
import pandas

class ReadVar():
    """docstring for ClassName"""
    def __init__(self):
        pass

    def readExcel(self, options):
        """
        Read excel file 
        """
        # Gene	RSID	Study	Genotype	Judgement
        file_name = options.snp
        xl = pandas.ExcelFile(file_name)
        #print xl.sheet_names
        df1 = xl.parse('Sheet1', header=None, names = ["Gene", "RSID", "Study", "Genotype", "Judgement"])

        #for line in df1.iterrows():
        #    print line
        #    print type(line)     # <type 'tuple'> 
        #    print type(line[1])  # <class 'pandas.core.series.Series'>
        #print type(df1)
        return df1
