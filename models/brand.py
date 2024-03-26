from sqlalchemy import Text, Column, BigInteger
from sqlalchemy.orm import relationship

from models.base import Base


class Brand(Base):
    __tablename__ = 'brand'

    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)

    products = relationship('Product', back_populates='brand')

    def serialize(self):
        """create attrs of the brand as dict"""
        return {
            'id': self.id,
            'name': self.name
        }
