#!/usr/bin/env python

from flask import Blueprint, request, jsonify
from pymongo import MongoClient


fruit_store = Blueprint('fruit_store', __name__)
client = MongoClient('mongodb://mongodb', 27017, username='mongo', password='123456789')
db = client['FruitOrder']
collection = db['OrderCollection']


@fruit_store.route('/order', methods=['POST'])
def order():
    req_data = request.get_json()
    collection.insert_one(req_data)
    return 'Order success!!!'


@fruit_store.route('/report', methods=['GET'])
def report():
    _from = request.args.get('from', type=int)
    to = request.args.get('to', type=int)
    orders = collection.find({'date': {'$gt': _from, '$lt': to}})
    result = []
    for _order in orders:
        _order['_id'] = str(_order['_id'])
        result.append(_order)
    return jsonify(result)
