from flask_sqlalchemy import SQLAlchemy
from google.cloud import firestore

from app.algolia import addArticle

db = firestore.Client()

class Article(object):
    collection = db.collection('Article')

    def __repr__(self):
        return f'Id: {self.id} Title: {self.title}'
    
    def __init__(self, uploadAlgolia=True,**kwargs):
        
        self.title = kwargs['title']
        self.content = kwargs['content']
        self.algoliaId = None

        if(uploadAlgolia):
            ret = addArticle(self)
            self.algoliaId = ret['objectID']

    def add(self):

        doc_ref = Article.collection.document(self.title)
        doc_ref.set({'content' : self.content, 'algoliaId' : self.algoliaId})
