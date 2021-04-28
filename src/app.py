from flask import Flask, jsonify, request, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, User, Characters, Planets, Vehicles


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATATABASE_URI'] = "sqlite://database.db"
app.config['SQLLCHEMY_TRACK_MODIFICATIONS'] = False

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




#FAVORITES######









#CHARACTERS #######
@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.all()
    characters = list(map(lambda character: character.to_dict(), characters))
    return jsonify({"characters": characters, "message": "List of Characters"}), 200


@app.route('/characters', methods=['POST'])
def add_new_character():
    request_body = request.data
    decoded_object = json.loads(request_body)
    new_character = Characters()
    new_character.name = decoded_object['name'],
    new_character.height = decoded_object['height'],
    new_character.mass = decoded_object['mass'],
    new_character.hair_color = decoded_object['hair_color'],
    new_character.skin_color = decoded_object['skin_color'],
    new_character.eye_color = decoded_object['eye_color'],
    new_character.birth_year = decoded_object['birth_year'],
    new_character.gender = decoded_object['gender'],
    new_character.created = decoded_object['created'],
    new_character.edited = decoded_object['edited'],
    new_character.homeworld = decoded_object['homeworld'],
    new_character.url = decoded_object['url'],

    character.save()
    return jsonify(character.to_dict())



@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    character = Character.query.get(id)
    if not character:
        return jsonify({"message": "Character not Found, try with a valid character",}), 404
    character.delete()
    return jsonify({"message": "Character Deleted Successfully"}), 200



###############
#PLANETS
@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    planets = list(map(lambda planet: planet.to_dict(), planets))
    return jsonify({"planets": planets, "message": "List of Planets"}), 200


@app.route('/planets', methods=['POST'])
def add_new_planet():
    request_body = request.data
    decoded_object = json.loads(request_body)
    new_planet = Planets()
    new_planet.name = decoded_object['name'],
    new_planet.diameter = decoded_object['diameter'],
    new_planet.rotation_period = decoded_object['rotation_period'],
    new_planet.orbital_period = decoded_object['orbital_period'],
    new_planet.gravity = decoded_object['gravity'],
    new_planet.population = decoded_object['population'],
    new_planet.climate = decoded_object['climate'],
    new_planet.terrain = decoded_object['terrain'],
    new_planet.surface_water = decoded_object['surface_water'],
    new_planet.created = decoded_object['created'],
    new_planet.edited = decoded_object['edited'],
    new_planet.url = decoded_object['url'],

    planet.save()
    return jsonify(planet.to_dict())



@app.route('/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planet.query.get(id)
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
    vehicles = list(map(lambda vehicle: vehicle.to_dict(), vehicles))
    return jsonify({"vehicles": vehicles, "message": "List of Vehicles"}), 200


@app.route('/vehicles', methods=['POST'])
def add_new_vehicle():
    request_body = request.data
    decoded_object = json.loads(request_body)
    new_vehicle = vehicles()
    new_vehicle.name = decoded_object['name'],
    new_vehicle.model = decoded_object['model'],
    new_vehicle.starship_class = decoded_object['starship_class'],
    new_vehicle.manufacturer = decoded_object['manufacturer'],
    new_vehicle.cost_in_credits = decoded_object['cost_in_credits'],
    new_vehicle.length = decoded_object['length'],
    new_vehicle.crew = decoded_object['crew'],
    new_vehicle.passengers = decoded_object['passengers'],
    new_vehicle.max_atmosphering_speed = decoded_object['max_atmosphering_speed'],
    new_vehicle.hyperdrive_rating = decoded_object['hyperdrive_rating'],
    new_vehicle.MGLT = decoded_object['MGLT'],
    new_vehicle.cargo_capacity = decoded_object['cargo_capacity'],
    new_vehicle.consumables = decoded_object['consumables'],
    new_vehicle.pilots = decoded_object['pilots'],
    new_vehicle.created = decoded_object['created'],
    new_vehicle.edited = decoded_object['edited'],
    new_vehicle.url = decoded_object['url'],

    vehicle.save()
    return jsonify(vehicle.to_dict())


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