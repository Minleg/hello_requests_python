import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Die Hard_(movie)')

print(page_py.summary[0:160])