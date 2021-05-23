#JWT
from flask_jwt_extended import JWTManager, get_jwt_identity, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

from flask import Flask, json, jsonify, request, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, User, Characters, Favorites_Characters , Planets, Favorites_Planets, Vehicles, Favorites_Vehicles, Favorites


app = Flask(__name__)
app.url_map.strict_slashes = False #no errores si incluyo o no un / en una ruta ó endpoints
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['JWT_SECRET_KEY'] = ""


db.init_app(app)
Migrate(app, db) 
CORS(app)
jwt = JWTManager(app)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


@app.route('/')
def main():
    return render_template('index.html')

## REGISTER ####
@app.route('/register', methods = ['POST'])
def get_register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username:
        return jsonify({"fail": "the username is required"}), 400
    if not password:
        return jsonify({"fail": "the password is required"}), 400
    user = User.query.filter_by(username = username).first()
    if user: return jsonify({"fail": "the username is already taken, try a new one"})

    user = User()
    user.username = username
    user.password = generate_password_hash(password)
    user.save()
    return jsonify({
        "success": "user created successfully",
        "user": user.serialize()
    }), 201
#### PROFILE
@app.route('/profile')
@jwt_required()
def get_profile():
    current_user = get_jwt_identity()
    return jsonify({
        "success": "private route",
        "user": current_user
    }), 200

## LOGIN#######
@app.route('/login', methods = ['POST'])
def get_login():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username:
        return jsonify({"fail": "Username required to login"}), 400
    if not password:
        return jsonify({"fail": "password required to login"}), 400
    user = User.query.filter_by(username = username).first()
    if not user:
        return jsonify({"fail": "the username or password is incorrect"}), 401
    if not check_password_hash(user.password, password):
        return jsonify({"fail": "the username or password is incorrect"}), 401

    access_token = create_access_token(identity = username)
    return jsonify({"token": access_token}), 200


#USERS #######
@app.route('/users', methods=['GET', 'POST'])
@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_users(id=None):
    if request.method == 'GET':
        if id is not None:
            user = User.query.get(id)
            if not user:
                return jsonify({
                    "Fail": "user not found, try another one"}), 404
            return jsonify({
                "success": "user Found",
                "user": user.serialize()
        }), 200
        else:
            users = User.query.all()
            users = list(map(lambda user: user.serialize(), users))
        return jsonify({
            "users": users,
            "Total Amount of users": len(users)
        }), 200 

    if request.method == 'POST':
        request_body = request.data
        new_user = User()
        new_user.username = request.json.get('username')
        new_user.email = request.json.get('email')
        new_user.password = request.json.get('password')

        new_user = User()
        new_user.username = username
        new_user.password = password
        favorites = Favorites()
        new_user.favorites = favorite
        new_user.save()
        return jsonify(new_user.serialize())


    if request.method == 'PUT':
        pass 

    if reques.method == 'DELETE':
        user = User.query.get(id)
        if not user:
            return jsonify({"Error": "user not found"}), 404
        user.delete()
        return jsonify({"success": "user deleted correctly"}), 200



@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({
            "message": "User not Found, try with a valid user",}), 404
    user.delete()
    return jsonify({"message": "User Deleted Successfully"}), 200




############ FAVORITES METHODS

#GET FAV 
@app.route('/users/<int:user_id>/favorites', methods=['GET', 'POST', 'PUT', 'DELETE'])
def favorites(user_id=None):
    if request.method == 'GET':
        if user_id is not None:
            users = User.query.all()
            if user_id > len(users):
                return jsonify({"fail": "this user doesn't exist, try a valid one"}), 404
            user = User.query.get(user_id)
            if not user.favorites:
                return jsonify({"fail": "the user doesn't have any favorites"})
            return jsonify({
                    "success": "Favorite List Found",
                    "favorites": user.favorites.serialize()}), 200
        else:
            users = User.query.all()
            users = list(map(lambda user: user.serialize(), users))

    if request.method == 'POST':
        character_id = request.json.get('character_id')
        planet_id = request.json.get('planet_id')
        vehicle_id = request.json.get('vehicle_id')

        user = User.query.filter_by(id = user_id).first()
        if not user:
            return jsonify({
                "Error": "This user doesn't exist, try a valid one"})
        
        character = Characters.query.filter_by(id = character_id).first()
        planet = Planets.query.filter_by(id = planet_id).first()
        vehicle = Vehicles.query.filter_by(id = vehicle_id).first()

        favorites = Favorites()
        user.favorites = favorites
        favorites.characters.append(character)
        favorites.planets.append(planet)
        favorites.vehicles.append(vehicle)

        favorites.save()
        user.update()
        return jsonify({"favorite":favorite.serialize()})

    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        favorite = Favorite.query.get(id)
        if not favorite:
            return jsonify({"error": "Fail to delete, favorite not found"}), 404
        favorite.delete()
        return jsonify({"success": "favorite deleted correctly"}), 200



#CHARACTERS #######
@app.route('/characters', methods=['GET'])
@app.route('/characters/<int:id>', methods=['GET'])
def get_characters(id=None):
    if id is not None:
        character = Characters.query.get(id)
        if not character:
            return jsonify({"fail": "Character can't be found"}), 404
        return jsonify({
            "success": "character successfully found",
            "character": character.serialize()
            }), 200
    else:
        characters = Characters.query.all()
        characters = list(map(lambda character: character.serialize(), characters))
        return jsonify({
            "characters": characters,
            "total": len(characters)        
        }), 200


@app.route('/characters', methods=['POST'])
def add_new_character():
    request_body = request.data
    new_character = Characters()
    new_character.name = request.json.get('name')
    new_character.gender = request.json.get('gender')
    new_character.height = request.json.get('height')
    new_character.mass = request.json.get('mass')
    new_character.hair_color = request.json.get('hair_color')
    new_character.skin_color = request.json.get('skin_color')
    new_character.eye_color = request.json.get('eye_color')
    new_character.birth_year = request.json.get('birth_year')
    new_character.homeworld = request.json.get('homeworld')

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
@app.route('/planets/<int:id>', methods=['GET'])
def get_planets(id=None):
    if id is not None:
        planet = Planets.query.get(id)
        if not planet:
            return jsonify({"message": "Empty List, please add something",}), 404
        return jsonify({
             "success": "planet successfully found"
             }), 200
    else:
        planets = Planets.query.all()
        planets = list(map(lambda planet: planet.serialize(), planets))
        return jsonify({
            "planets": planets,
            "total": len(planets)
        }), 200



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
@app.route('/vehicles/<int:id>', methods=['GET'])
def get_vehicles(id=None):
    if id is not None:
        vehicle = Vehicles.query.get(id)
        if not vehicle:
            return jsonify({"fail": "Vehicle can't be found"}), 404
        return jsonify({
            "success": "Vehicle successfully found"
        }), 200
    else:
        vehicles = Vehicles.query.all()
        vehicles = list(map(lambda vehicle: vehicle.serialize(), vehicles))
        return jsonify({
            "vehicles": vehicles,
            "total": len(vehicles)
            }), 200


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


    new_vehicle.save()
    return jsonify(new_vehicle.seserialize())


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