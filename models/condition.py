from sqlalchemy import Text, Column, BigInteger
from sqlalchemy.orm import relationship

from models.base import Base


class Condition(Base):

    __tablename__ = 'condition'

    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)

    products = relationship('Product', back_populates='condition')
