from metapub import PubMedFetcher
fetch = PubMedFetcher()

print "Get paper information by PMID"
article = fetch.article_by_pmid('21931568')
print article.title
print article.journal, article.year, article.volume, article.issue
print article.authors

print '\nGet paper information by PMCID'

article = fetch.article_by_pmcid(2674488)
print article.title
print article.journal, article.year, article.volume, article.issue
print article.authors

