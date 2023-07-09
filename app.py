"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake, defaultImage
from forms import AddCupcakeForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'chickenzarecool21837'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
app.app_context().push()
connect_db(app)
db.create_all()



@app.route('/')
def list_cupcakes():
    """render homepage"""
    form = AddCupcakeForm()
    return render_template('home.html',form=form)
    

@app.route('/api/cupcakes')
def get_cupcakes():
    """return all cupcakes"""
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """return single cupcake and update form"""
    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<flavor_string>')
def get_filtered_cupcakes(flavor_string):
    """return cupcakes based on string match"""
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.filter(Cupcake.flavor.ilike(f"%{flavor_string}%"))]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """create a cupcake"""
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json.get('image',defaultImage)

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    json_resp = jsonify(cupcake=new_cupcake.serialize())

    return (json_resp, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """Update an existing cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor',cupcake.flavor)
    cupcake.size = request.json.get('size',cupcake.size)
    cupcake.rating = request.json.get('rating',cupcake.rating)
    cupcake.image = request.json.get('image',cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())
    
@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Delete cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='Cupcake deleted')

@app.errorhandler(404)
def page_not_found(e):
    """render template for 404 message"""
    return render_template('404.html'), 404

    

