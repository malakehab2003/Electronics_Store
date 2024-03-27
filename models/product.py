from flask import jsonify
from sqlalchemy import DateTime, Double, ForeignKey, Text, Column, BigInteger, func
from sqlalchemy.orm import relationship
from models.base import Base
from models.category import product_category
from models.brand import Brand
from models.condition import Condition


class Product(Base):

    __tablename__ = 'product'

    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    image_url = Column(Text, nullable=False)
    availability = Column(Text, nullable=False)
    on_sale = Column(Text, nullable=False)
    price = Column(Double, nullable=False)
    currency = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(),
                        onupdate=func.now(), nullable=False)

    brand_id = Column(BigInteger, ForeignKey('brand.id'))
    brand = relationship('Brand')
    categories = relationship(
        'Category', secondary=product_category, back_populates='products')
    condition_id = Column(BigInteger, ForeignKey('condition.id'))
    condition = relationship('Condition')

    def short_serialize(self):
        """only a short list for home page"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image_url': self.image_url,
            'availability': self.availability,
            'on_sale': self.on_sale,
            'price': self.price,
            'currency': self.currency,
            'condition': self.condition.serialize().get('name') if self.condition else "New",
        }

    def serialize(self):
        """ create attrs of the product as dict """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image_url': self.image_url,
            'availability': self.availability,
            'on_sale': self.on_sale,
            'price': self.price,
            'currency': self.currency,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'brand': self.brand.serialize() if self.brand else None,
            'condition': self.condition.serialize() if self.condition else None,
            'categories': [category.serialize() for category in self.categories],
        }
