from flask_sqlalchemy import SQLAlchemy
##instancia del modelo sql alchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    usernamename = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False, unique=False )
    email = db.Column(db.String(100), nullable=False, unique=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }
########

    
class Favorite_Characters(db.Model):
    __tablename__ = 'favorite_characters'
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    id_characters = db.Column(db.Integer, db.ForeignKey("characters.id", ondelete='CASCADE'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "id_characters": self.id_characters,
        }
########


class Favorite_Planets(db.Model):
    __tablename__ = 'favorite_planets'
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    id_planets = db.Column(db.Integer, db.ForeignKey("planets.id", ondelete='CASCADE'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "id_planets": self.id_planets,
        }
########


class Favorite_Vehicles(db.Model):
    __tablename__ = 'favorite_vehicles'
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    id_vehicles = db.Column(db.Integer, db.ForeignKey("vehicles.id", ondelete='CASCADE'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "id_vehicles": self.id_vehicles,
        }
########



class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250), db.ForeignKey("planet_id_resident.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "gender": self.gender,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "created": self.created,
            "edited": self.edited,
            "homeworld": self.homeworld,
            "url": self.url,
        }
#########


class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    planet_id_resident = db.Column(db.Integer, db.ForeignKey("homeworld.id"), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
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
            "created": self.created,
            "edited": self.edited,
            "url": self.url,
        }
#########



class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    consumables = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
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
            "created": self.created,
            "edited": self.edited,
            "url": self.url,
        }

