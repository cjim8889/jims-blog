from app.articles import bp
from app.models import db, Article

from flask import render_template, request, jsonify
from app.algolia import index

import json


@bp.route('/new', methods=['POST'])
def newArticle():
    data = request.get_json(silent=True)
    
    if(data is None or 'title' not in data or 'content' not in data):
        return jsonify({'status':'error'})
    
    art = Article(title=data['title'], content=data['content'])
    art.add()

    retJson = {'title':art.title, 'content':art.content}



    return jsonify(retJson)

@bp.route('/search', methods=['POST'])
def searchArticlePost():
    data = request.get_json(silent=True)

    if(data is None or 'query' not in data or len(data['query']) == 0):
        return jsonify({'status':'error'})

    return jsonify(index.search(data['query']))

@bp.route('/search', methods=['GET'])
def searchArticleGet():
    pass