from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from data import DESIGNERS
app = Flask(__name__)
application = app

def get_ids_and_designers(source):
    ids_and_designer = []
    for row in source:
        id = row["id"]
        designer = row["designer"]
        ids_and_designer.append( [id, designer] )
    return ids_and_designer

def get_designer(source, id):
    for row in source:
        if id == str( row["id"] ):
            designer = row["designer"]
            link = row["links"]
            description = row["description"]
            id = str(id)
            return id, designer, link, description

@app.route('/')
@app.route('/index.html')
def index():
    ids_and_designer = get_ids_and_designers(DESIGNERS)
    return render_template('index.html', pairs=ids_and_designer)

@app.route('/designer/<id>.html')
def designer(id):
    id, designer, link, description = get_designer(DESIGNERS, id)
    return render_template('designer.html', id=id, designer=designer, link=link, description=description)

if __name__ == '__main__':
    app.run(debug=True)
