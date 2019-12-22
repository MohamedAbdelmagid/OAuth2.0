from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///restaurantmenu.db')
DB_session = scoped_session(sessionmaker(bind=engine))


Base = declarative_base()
Base.query = DB_session.query_property


def init_db():
    import models
    # Create tables
    Base.metadata.create_all(engine)


# class Restaurant(Base):
#     __tablename__ = 'restaurant'
   
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

#     @property
#     def serialize(self):
#        """Return object data in easily serializeable format"""
#        return {
#            'name'         : self.name,
#            'id'           : self.id,
#        }
 
# class MenuItem(Base):
#     __tablename__ = 'menu_item'


#     name =Column(String(80), nullable = False)
#     id = Column(Integer, primary_key = True)
#     description = Column(String(250))
#     price = Column(String(8))
#     course = Column(String(250))
#     restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
#     restaurant = relationship(Restaurant)


#     @property
#     def serialize(self):
#        """Return object data in easily serializeable format"""
#        return {
#            'name'         : self.name,
#            'description'         : self.description,
#            'id'         : self.id,
#            'price'         : self.price,
#            'course'         : self.course,
#        }



# engine = create_engine('sqlite:///restaurantmenu.db')
 

# Base.metadata.create_all(engine)
