import gspread
import os
import sys
from oauth2client.service_account import ServiceAccountCredentials
import logging
import argparse
from glob import glob
import pandas

# -*- coding: utf-8 -*-
# coding: utf8

RSID = 'RSID'
CLASS = 'Class'
PHENOTYPE = 'Phenotype'
GENOTYPE = 'Genotype'
DISEASE = 'Desease'
MEDCINE = 'Medcine'
FLAG = 'Flag'

class ReadVarDB():
    """docstring for ClassName"""
    def __init__(self):
        pass

    def readGoogleSheet(self, options):
        """
        Read Google Sheet 
        """
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('googleSheetOauth-4e4b2db3f749.json', scope)

        gc = gspread.authorize(credentials)
        sheet1 = gc.open_by_key("1jUJOlICOH6VnyuALdU2VAc_Ci_ZVwdW-xc5kr_qkJHY").sheet1
        list_of_lists = sheet1.get_all_values()
        return list_of_lists
        
    def processVarDB(self, list_of_lists):
        var_type = {}
        class_snp = {}
        var_description = {}
        snp_pheno = {}
        snp_geno_flag = {}
        header = list_of_lists.pop(0)
        head_index = self.generHeadIndex(header)
        snp_index = head_index['RSID']
        class_index = head_index['Class']
        desease_index = head_index['Desease']
        pheno_index = head_index[PHENOTYPE]
        genotype_index = head_index[GENOTYPE]
        flag_index = head_index[FLAG]
        for li in list_of_lists:
            class_name = li[class_index]
            #print class_name
            rsid = li[snp_index]
            var_type[rsid] = class_name
            snp_pheno[rsid] = li[pheno_index]
            snp_geno = ''.join(sorted(li[genotype_index]))
            #class_snp[rsid] = class_name
            if rsid not in snp_geno_flag:
                snp_geno_flag[rsid] = {}
                snp_geno_flag[rsid][snp_geno] = li[flag_index] 
            if li[desease_index] != 'NA':
                var_description[rsid] = li[desease_index]
        #print var_description
        #print snp_geno_flag
        return var_type, var_description, snp_geno_flag
   
    def generTable(self, ):
        pass    
         
    def generHeadIndex(self, header):
        """
        """
        head_index = {}
        for col in range(0, len(header)):
            head_index[header[col]] = col
        return head_index
