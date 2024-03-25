from sqlalchemy import ForeignKey, Table, Text, Column, BigInteger
from sqlalchemy.orm import relationship

from models.base import Base

product_category = Table('product_category', Base.metadata,
                         Column('product_id', BigInteger, ForeignKey(
                             'product.id'), primary_key=True),
                         Column('category_id', BigInteger, ForeignKey(
                             'category.id'), primary_key=True)
                         )


class Category(Base):

    __tablename__ = 'category'

    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)

    products = relationship(
        'Product', secondary=product_category, back_populates='categories')
