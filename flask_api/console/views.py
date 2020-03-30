import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.console.models import Console
from my_app import api, db

console = Blueprint('console',__name__)

parser = reqparse.RequestParser()
parser.add_argument('titulo',type=str)
parser.add_argument('genero',type=str)
parser.add_argument('temporadas',type=int)
parser.add_argument('media',type=float)
parser.add_argument('active',type=int)

@console.route("/")
@console.route("/home")
def home():
    return "Catálogo de Consoles"

class ConsoleAPI(Resource):
    def get(self,id=None,page=1):
        if not id:
            consoles = Console.query.paginate(page,10).items
        else:
            consoles = [Console.query.get(id)]
        if not consoles:
            abort(404)
        res = {}
        for con in consoles:
            res[con.id] = {
                'titulo' : con.titulo,
                'genero' : con.genero,
                'temporadas' : con.temporadas
                'media' : con.media
                'active' : con.active

            }
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        titulo = args['titulo']
        genero = args['genero']
        temporadas = args['temporadas']
        media = args['media']
        active = args['active']

        con = Console(titulo,genero,temporadas,media,active)
        db.session.add(con)
        db.session.commit()
        res = {}
        res[con.id] = {
                'titulo' : con.titulo,
                'genero' : con.genero,
                'temporadas' : con.temporadas
                'media' : con.media
                'active' : con.active
        }
        return json.dumps(res)

api.add_resource(
    ConsoleAPI,
    '/api/console',
    '/api/console/<int:id>',
    '/api/console/<int:id>/<int:page>'
)