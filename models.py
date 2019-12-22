# models.py 
 
from app import db
 
class Restaurant(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    
    menuItems = db.relationship('MenuItem', backref='restaurant', lazy=True)

    def __repr__(self):
        return "Restaurant('{self.id}', '{self.name}')"

    @property
    def serialize(self):
        # Returns object data in easily serializeable format
        return {
            'id': self.id,
            'name': self.name,
        }


class MenuItem(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    course = db.Column(db.String(250))

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __repr__(self):
        return "MenuItem('{self.id}', '{self.name}', '{self.price}')"

    @property
    def serialize(self):
        # Returns object data in easily serializeable format
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'course': self.course,
            'description': self.description,
        }

