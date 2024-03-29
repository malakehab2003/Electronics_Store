#!/usr/bin/python3
"""make the flask file"""


from flask import Flask, jsonify, abort, render_template, request, url_for
from models.base import session
from models.product import Product
from flask import render_template

import stripe
SECRET_KEY = "sk_test_51NS1MqJJ7rtMTuJ7RS6QE9MjOrgy9uKsKADlVPXoL2hHSiv7pkTOpJPUdvOL2Hp2Iv6WLaJgiTZZ00nFsKe9v8Bd00K7h0HK7A"
PUBLIC_KEY = "pk_test_51NS1MqJJ7rtMTuJ7lWhwOufrqLSoSDY3sAqSvGyP82UKnWjFZ4lVrEjyTQkXUmGoDq4z23ZZMzspAfCDejAY5Wdg00kDTtnUdC"
stripe.api_key = SECRET_KEY

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
            '/product.html', product=arg_item, public_key=PUBLIC_KEY)


@app.route('/purchase', methods=['POST'])
def purchase():
    """ Purchase a product """
    id = request.form.get('product_id')
    item = session.query(Product).filter_by(id=id).first()
    stripe_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    # price in cents
                    'unit_amount_decimal': str(float(item.price)*100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=url_for('success', _external=True),
        cancel_url=url_for('showProduct', _external=True,  id=item.id),
    )
    return {'id': stripe_session.id}


@app.route('/success')
def success():
    return render_template('/after_purchase.html', success=True)


@app.route('/cancel')
def cancel():
    return render_template('/after_purchase.html', success=True)


@app.errorhandler(404)
def not_found(error):
    """ Handle 404 error """
    return 'Sorry this page does not exist'


if __name__ == '__main__':
    """run the flask app"""
    app.run(host='0.0.0.0', port=4000)
