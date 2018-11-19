from algoliasearch import algoliasearch

client = algoliasearch.Client("QZ178MWVKS", '4484cdce65052d5e2c8b772811109aaf')
index = client.init_index('dev_flask')
index.set_settings({"searchableAttributes": ["title", "content"]})

def addArticle(art):
    
    data = {"title":art.title, "content":art.content}
    res = index.add_object(data)

    return res