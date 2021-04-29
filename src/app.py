from flask import Flask, json, jsonify, request, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, User, Characters, Favorite_Characters , Planets, Favorite_Planets, Vehicles, Favorite_Vehicles


app = Flask(__name__)
app.url_map.strict_slashes = False #no errores si incluyo o no un / en una ruta ó endpoints
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"


db.init_app(app)
Migrate(app, db)
CORS(app)
manager = Manager(app)
manager.add_command("db", MigrateCommand)



@app.route('/')
def main():
    return render_template('index.html')


#USERS #######
@app.route('/user', methods=['GET'])
def get_users():
    user = User.query.all()
    all_user = list(map(lambda user: user.to_dict(), user))
    return jsonify(all_user), 200 


@app.route('/users', methods=['POST'])
def add_new_user():
    request_body = request.data
    decoded_object = json.loads(request_body)
    user = User()
    user.username = decoded_object(['username'])
    user.email = decoded_object(['email'])
    user.password = decoded_object(['password'])
    user.save()
    return jsonify(user.to_dict())



@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({
            "message": "User not Found, try with a valid user",}), 404
    user.delete()
    return jsonify({"message": "User Deleted Successfully"}), 200



#CHARACTERS #######
@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.all()
    if not characters:
        return jsonify({"message": "Empty List, please add something",}), 404
    else:
        characters = list(map(lambda character: character.serialize(), characters))
        return jsonify({"characters": characters}), 200


@app.route('/characters', methods=['POST'])
def add_new_character():
    request_body = request.data
    new_character = Characters()
    new_character.name = request.json.get('name')
    new_character.height = request.json.get('height')
    new_character.mass = request.json.get('mass')
    new_character.hair_color = request.json.get('hair_color')
    new_character.skin_color = request.json.get('skin_color')
    new_character.eye_color = request.json.get('eye_color')
    new_character.birth_year = request.json.get('birth_year')
    new_character.gender = request.json.get('gender')
    new_character.created = request.json.get('created')
    new_character.edited = request.json.get('edited')
    new_character.homeworld = request.json.get('homeworld')
    new_character.url = request.json.get('url')

    new_character.save()
    return jsonify(new_character.serialize())


## DELETE
@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    character = Characters.query.get(id)
    if not character:
        return jsonify({"message": "Character not Found, try with a valid character",}), 404
    character.delete()
    return jsonify({"message": "Character Deleted Successfully"}), 200



###############
#PLANETS
@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    if not planets:
        return jsonify({"message": "Empty List, please add something",}), 404
    else:
        planets = list(map(lambda planet: planet.serialize(), planets))
        return jsonify({"planets": planets}), 200



@app.route('/planets', methods=['POST'])
def add_new_planet():
    request_body = request.data
    new_planet = Planets()
    new_planet.name = request.json.get('name')
    new_planet.diameter = request.json.get('diameter')
    new_planet.rotation_period = request.json.get('rotation_period')
    new_planet.orbital_period = request.json.get('orbital_period')
    new_planet.gravity = request.json.get('gravity')
    new_planet.population = request.json.get('population')
    new_planet.climate = request.json.get('climate')
    new_planet.terrain = request.json.get('terrain')
    new_planet.surface_water = request.json.get('surface_water')
    new_planet.created = request.json.get('created')
    new_planet.edited = request.json.get('edited')
    new_planet.url = request.json.get('url')

    new_planet.save()
    return jsonify(new_planet.serialize())



@app.route('/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planets.query.get(id)
    if not planet:
        return jsonify({
            "message": "Planet not Found, try with a valid planet",}), 404
    planet.delete()
    return jsonify({"message": "Planet Deleted Successfully"}), 200


################
#VEHICLES
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicles.query.all()
    if not vehicles:
        return jsonify({"message": "Empty List, please add something",}), 404
    else:
        vehicles = list(map(lambda vehicle: vehicle.serialize(), vehicles))
        return jsonify({"vehicles": vehicles}), 200


@app.route('/vehicles', methods=['POST'])
def add_new_vehicle():
    request_body = request.data
    new_vehicle = vehicles()
    new_vehicle.name = request.json.get('name')
    new_vehicle.model = request.json.get('model')
    new_vehicle.starship_class = request.json.get('starship_class')
    new_vehicle.manufacturer = request.json.get('manufacturer')
    new_vehicle.cost_in_credits = request.json.get('cost_in_credits')
    new_vehicle.length = request.json.get('length')
    new_vehicle.crew = request.json.get('crew')
    new_vehicle.passengers = request.json.get('passengers')
    new_vehicle.max_atmosphering_speed = request.json.get('max_atmosphering_speed')
    new_vehicle.hyperdrive_rating = request.json.get('hyperdrive_rating')
    new_vehicle.cargo_capacity = request.json.get('cargo_capacity')
    new_vehicle.consumables = drequest.json.get('consumables')
    new_vehicle.pilots = request.json.get('pilots')
    new_vehicle.created = request.json.get('created')
    new_vehicle.edited = request.json.get('edited')
    new_vehicle.url = request.json.get('url')

    new_vehicle.save()
    return jsonify(new_vehicle.serialize())


@app.route('/vehicles/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if not vehicle:
        return jsonify({
            "message": "Vehicle not Found, try with a valid vehicle",}), 404
    vehicle.delete()
    return jsonify({"message": "Vehicle Deleted Successfully"}), 200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    manager.run()
    #app.run(host='0.0.0.0', port=3245, debug=True)