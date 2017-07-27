from app import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), index=True, unique=True)
    shortDescription = db.Column(db.String(100), index=True, unique=True)
    description = db.Column(db.String(100), index=True, unique=True)
    mainImage = db.Column(db.String(100), index=True, unique=True)
    images = db.relationship("Image", backref='inProject', lazy='dynamic')

    def __repr__(self):
        return '<Project %r>' % self.title


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.Integer, db.ForeignKey('project.id'))
    imagePath = db.Column(db.String(100), index=True, unique=True)

    def __repr__(self):
        return '<Image %r>' % self.imagePath
