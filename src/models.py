from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

### user uno a muchos (characters, vehicles y planets FAVS)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    favorites = db.relationship('Favorites', cascade = 'all, delete', backref = 'user', uselist = False)

    ## metodo para guardar en base de dato
    def save(self):
        db.session.add(self)
        db.session.commit()
    #update base de dato de user
    def update(self):
        db.session.commit()
    #delete en base de dato
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def check_password(self, password):
        return safe_str_cmp()

    #se encarga de devolver mi objeto de python en un obj serializable
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            # password no va por prevencion de privacidad
        }

    ## CONEXION A ALL FAVORITOS 
    def serialize_user_with_favorite(self):
        return {
            "id": self.id,
            "username": self.username,
            "favorites": {
                "characters": self.favorites.characters.serialize(),
                "planets": self.favorites.planets.serialize(),
                "vehicles": self.favorites.vehicles.serialize()
            }
        }

########




# TABLA GENERAL FAVORITOS
class Favorites(db.Model):
    __tablename__ = 'favorites'
    ## ID TABLA
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

 ## RELACION CON LA TABLA  ALL_FAVS a TABLAS PIVOTTE CON CHARACTERS, PLANETS y VEHICLES
    characters = db.relationship('Characters', secondary='favorites_characters')
    planets = db.relationship('Planets', secondary='favorites_planets')
    vehicles = db.relationship('Vehicles', secondary='favorites_vehicles')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "user": {
                "id":self.user.id,
                "username": self.user.username
            },
            "characters": self.get_fav_characters(),
            "planets": self.get_fav_planets(),
            "vehicles": self.get_fav_vehicles()
        }
    
    def get_fav_characters(self):
        return list(map(lambda characters: characters.serialize(), self.characters))
    
    def get_fav_planets(self):
        return list(map(lambda planets: planets.serialize(), self.planets))

    def get_fav_vehicles(self):
        return list(map(lambda vehicles: vehicles.serialize(), self.vehicles)) 



######### ------<



#######
# TABLAS PIVOTTE
class Favorites_Characters(db.Model):
    __tablename__ = 'favorites_characters'
    id_favorites = db.Column(db.Integer, db.ForeignKey('favorites.id'), primary_key=True)
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)

########

class Favorites_Planets(db.Model):
    __tablename__ = 'favorites_planets'
    id_favorites = db.Column(db.Integer, db.ForeignKey('favorites.id'), primary_key=True)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), primary_key=True)
    
###########

class Favorites_Vehicles(db.Model):
    __tablename__ = 'favorites_vehicles'
    id_favorites = db.Column(db.Integer, db.ForeignKey('favorites.id'), primary_key=True)
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), primary_key=True)

########




##  >--------
# MUCHOS CHARACTERS
class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(100), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(100), nullable=False)
    eye_color = db.Column(db.String(100), nullable=False)
    birth_year = db.Column(db.String(100), nullable=False)
    homeworld = db.Column(db.String(100), nullable=False)
    #Link tabla pivotte
    favorites = db.relationship('Favorites', secondary='favorites_characters', backref='character')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "homeworld": self.homeworld,
        }
#########


########
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.String(100), nullable=False)
    orbital_period = db.Column(db.String(100), nullable=False)
    gravity = db.Column(db.String(100), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.String(100), nullable=False)
    favorites = db.relationship('Favorites', secondary='favorites_planets', backref='planet')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
        }
#########

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    starship_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.String(250), nullable=False)
    length = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    max_armosphering_speed = db.Column(db.String(250), nullable=False)
    hyperdrive_rating = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(250), nullable=False)
    consumables = db.Column(db.String(250), nullable=False)
    pilots = db.Column(db.String(250), nullable=False)
    favorites = db.relationship('Favorites', secondary='favorites_vehicles', backref='vehicle')


    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "passengers": self.passengers,
            "max_armosphering_speed": self.max_armosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "pilots": self.pilots,
        }


