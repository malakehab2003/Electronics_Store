from sqlalchemy import Text, Column, BigInteger
from sqlalchemy.orm import relationship

from models.base import Base


class Condition(Base):
    """ create the condition table which contain the condition of the product """
    __tablename__ = 'condition'

    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)

    products = relationship('Product', back_populates='condition')

    # create the serialize function to return dict with all attrs
    def serialize(self):
        """create attrs of the condition as dict"""
        return {
            'id': self.id,
            'name': self.name
        }
