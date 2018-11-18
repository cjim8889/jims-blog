from flask_sqlalchemy import SQLAlchemy
from app.algolia import addArticle

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(256), index=True)
    content = db.Column(db.String(2048), index=True)
    algoliaId = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return f'Id: {self.id} Title: {self.title}'
    
    def __init__(self, uploadAlgolia=True,**kwargs):

        super(Article, self).__init__(**kwargs)

        if(uploadAlgolia):
            ret = addArticle(self)
            self.algoliaId = ret['objectID']
