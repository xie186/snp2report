#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import argparse
from glob import glob
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from genereport.ReadVar import ReadVar
from genereport.ReadVarDB import ReadVarDB
from genereport.ReportDoc import ReportDoc
class GeneReport:
    """docstring for ClassName"""

    def __init__(self):
        """Initiate GeneReport"""

    def generateReport(self, options):
        """
        Create index for bwameth
        """    
        readVar = ReadVar()
        snp_data = readVar.readExcel(options)
        
        readVarDB = ReadVarDB()
        list_of_lists = readVarDB.readGoogleSheet(options)
        var_type, var_description, snp_geno_flag = readVarDB.processVarDB(list_of_lists)
        #print snp_geno_flag

        #readVarDB.generTable(snp_data, snp_geno_flag, document)
        reportDoc = ReportDoc()
        document = reportDoc.readTemplate(options)
        
        reportDoc.generTable(snp_data, snp_geno_flag, document)
        reportDoc.generRep(snp_data, var_type, var_description, document)
        document.save(options.output)
        
if __name__ == '__main__':

    parser = argparse.ArgumentParser('GeneReport')

    parser.add_argument('-s', '--snp', metavar='snp', \
        help='SNP files from the company', required=True)
    parser.add_argument('-j', '--json', metavar='json', \
        help='JSON file for Google Drive', default = 'googleSheetOauth-4e4b2db3f749.json')
    parser.add_argument('-k', '--key', metavar='GoogleSheetKey', \
        help='JSON file for Google Drive', default = '1jUJOlICOH6VnyuALdU2VAc_Ci_ZVwdW-xc5kr_qkJHY')
    parser.add_argument('-t', '--template', metavar='template', \
        help='Template file', default = 'reportTemplate.docx')
    parser.add_argument('-o', '--output', metavar='output', \
        help='Output docx', default = 'output.docx') 

    options = parser.parse_args()

    geneReport = GeneReport()
    list_of_lists = geneReport.generateReport(options)
