from app import db

class Fabric(db.Model):
    __tablename__ = 'fabrics'

    id = db.Column(db.Integer, primary_key = True)
    pattern = db.Column(db.String(64))

    def __repr__(self):
        return f'pattern: {self.pattern}'
