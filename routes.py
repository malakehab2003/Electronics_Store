#!/usr/bin/python3
"""make the flask file"""


from flask import Flask, jsonify, abort, render_template
from models.base import session
from models.product import Product
from flask import render_template

app = Flask(__name__)

app.debug = True


@app.teardown_appcontext
def reload(exception):
    """ Reload session """
    session.remove()


@app.route('/api/products/', strict_slashes=False, methods=['GET'])
def products():
    """ Get all products in database """
    items = session.query(Product).all()
    list_all = []
    for item in items:
        list_all.append(item.short_serialize())
    return jsonify(list_all)


@app.route('/api/products/<int:id>', methods=['GET'], strict_slashes=False)
def product(id):
    """ get spcific product with product id"""
    item = session.query(Product).filter_by(id=id).first()
    if not item:
        abort(404)
    else:
        arg_item = item.serialize()
        return jsonify(arg_item)


@app.route('/')
def index():
    """ Index page """
    items = session.query(Product).all()
    list_all = []
    for item in items:
        list_all.append(item.short_serialize())
    return render_template(
        '/home_page_components/list.html', items=list_all)


@app.route('/product/<int:id>')
def showProduct(id):
    """ Product Details page """
    item = session.query(Product).filter_by(id=id).first()
    if not item:
        abort(404)
    else:
        arg_item = item.serialize()
        return render_template(
            '/product.html', product=arg_item)


@app.errorhandler(404)
def not_found(error):
    """ Handle 404 error """
    return 'Sorry this page does not exist'


if __name__ == '__main__':
    """run the flask app"""
    app.run(host='0.0.0.0', port=4000)
