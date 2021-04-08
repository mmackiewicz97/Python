import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
ksiazki = [
    {'id': 0,
     'tytul': 'Chlopi',
     'autor': 'Władysław Reymont',
     'nr': '1'
     },
    {'id': 1,
     'tytul': 'Zbrodnia i Kara',
     'autor': 'Fiodor Dostojewski',
     'nr': '2'
     },
    {'id': 2,
     'tytul': 'Lalka',
     'autor': 'Bolesław Prus',
     'nr': '3'
    },
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Witaj na stronie poświęconej książkom.</h1><p>Dostęp do API przez /api/v1/ksiazki</p>"

@app.route('/api/v1/ksiazki/all', methods=['GET'])
def api_all():
    return jsonify(ksiazki)

@app.route('/api/v1/ksiazki', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
        if request.args.get('tytul'):
            tytul = request.args.get('tytul')
            ksiazki[id]['tytul'] = tytul
            print("Zmieniono tytuł: ", tytul)
        if request.args.get('autor'):
            autor = request.args.get('autor')
            ksiazki[id]['autor'] = autor
            print("Zmieniono autora: ", autor)
        if request.args.get('nr'):
            nr = request.args.get('nr')
            ksiazki[id]['nr'] = nr
            print("Zmieniono numer: ", nr)
    else:
        return "Błąd! Podano złe id."
    return jsonify(ksiazki[id])

app.run()
