from sqlalchemy import Text, Column, BigInteger
from sqlalchemy.orm import relationship

from models.base import Base


class Brand(Base):
    """ create the brand table which contain the brand of the product """
    __tablename__ = 'brand'

    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)

    products = relationship('Product', back_populates='brand')

    # create the serialize function to return dict with all attrs
    def serialize(self):
        """create attrs of the brand as dict"""
        return {
            'id': self.id,
            'name': self.name
        }
