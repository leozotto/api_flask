from my_app import db

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    genero = db.Column(db.String(100))
    temporadas = db.Integer(db.Integer)
    media = db.Float(db.Float)
    active  = db.Integer(db.Integer)


    def __init__(self,titulo,genero,temporadas,media,active):
        self.titulo = titulo
        self.genero = genero
        self.temporadas = temporadas
        self.media = media
        self.active = active

    def __repr__(self):
        return 'Console {0}'.format(self.id)