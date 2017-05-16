import re
from pubmed import PubMed

string = 'xxssdfd [PMID 22833195][PMID 26415670]'

pmid = re.compile('PMID *(\d+)')

list_pmid = pmid.findall(string)

print list_pmid
if list_pmid:
    pass
    for pmid in list_pmid:
        # http://www.ncbi.nlm.nih.gov/pubmed/26471457
        
        pm = PubMed(pmid)
        print pm.title
        print pm.authors
        print pm.pub_date
        print pm.journal_name
        print pm.journal_full_name

string = re.sub(r'\[PMID *\d+\]', '', string)
print string
