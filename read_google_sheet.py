import gspread
import os
import sys
from oauth2client.service_account import ServiceAccountCredentials

# coding: utf8
#reload(sys)
#sys.setdefaultencoding('utf-8')
#sys.setdefaultencoding('gbk')
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/xie186/snpedia_fetch/SNPreport"


scope = ['https://spreadsheets.google.com/feeds']

#scope = [
#    'https://spreadsheets.google.com/feeds',
#    'https://www.googleapis.com/auth/drive'
#]
credentials = ServiceAccountCredentials.from_json_keyfile_name('googleSheetOauth-4e4b2db3f749.json', scope)

gc = gspread.authorize(credentials)

#1jUJOlICOH6VnyuALdU2VAc_Ci_ZVwdW-xc5kr_qkJHY
#wks = gc.open("snp_database.xlsx").sheet1
wks = gc.open_by_key("1jUJOlICOH6VnyuALdU2VAc_Ci_ZVwdW-xc5kr_qkJHY")
for sheet in wks:
    print sheet
#print wks

sheet1 = gc.open_by_key("1jUJOlICOH6VnyuALdU2VAc_Ci_ZVwdW-xc5kr_qkJHY").sheet1
list_of_lists = sheet1.get_all_values()

for li in list_of_lists:
    print li[0]
    #for ele in li:
    #    pass
        #print ele

print sys.getdefaultencoding()

#1jUJOlICOH6VnyuALdU2VAc_Ci_ZVwdW-xc5kr_qkJHY

file_list = gc.openall()
print file_list
