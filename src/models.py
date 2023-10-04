from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):#(FATHER)
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    #Relacion con FavPlanets 
    favPlanets = db.relationship("FavPlanets", backref="user")
    #Relacion con FavCharacters 
    favCharacters = db.relationship("FavCharacters", backref="user")

#Esto se debe repetir en cada tabla
    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
#Aqui debemos crear nuestras tablas para las relaciones
class Planets(db.Model): #(FATHER)
    __tablename__ = "planets"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    populations = db.Column(db.String(50), unique=False, nullable=False)
    rotation_period = db.Column(db.String(50), unique=False, nullable=False)
    orbital_period = db.Column(db.String(50), unique=False, nullable=False)
    diameter = db.Column(db.String(50), unique=False, nullable=False)
    gravity = db.Column(db.String(50), unique=False, nullable=False)
    terrain = db.Column(db.String(50), unique=False, nullable=False)
    surface_water = db.Column(db.String(50), unique=False, nullable=False)
    climate = db.Column(db.String(50), unique=False, nullable=False)

    #Relacion con el FavPlanets (Father)
    favPlanets = db.relationship("FavPlanets", backref="planets")

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "created": self.created,
            "populations": self.populations,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "climate": self.climate,
        }

class FavPlanets(db.Model):
    __tablename__ = "favPlanets"
  
    id = db.Column(db.Integer, primary_key=True)
    #Relacion con la tabla User
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #Relacion con la tabla de Planets
    planets_id = db.Column(db.Integer, db.ForeignKey("planets.id"))


    def __repr__(self):
        return '<FavPlanets %r>' % self.id

    def serialize(self):
        return {
            "planets": self.planets.serialize(),
        }

class Characters(db.Model): #(Father)
    __tablename__ = "characters"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), unique=True, nullable=False)
    birth_year = db.Column(db.String(50), unique=False, nullable=False)
    species = db.Column(db.String(50), unique=False, nullable=False)
    height = db.Column(db.String(50), unique=False, nullable=False)
    mass = db.Column(db.String(50), unique=False, nullable=False)
    gender = db.Column(db.String(50), unique=False, nullable=False)
    hair_color = db.Column(db.String(50), unique=False, nullable=False)
    skin_color = db.Column(db.String(50), unique=False, nullable=False)
    homeworld = db.Column(db.String(50), unique=False, nullable=False)
    
    #Relacion con FavCharacters 
    favCharacters = db.relationship("FavCharacters", backref="characters")

    def __repr__(self):
        return '<Characters %r>' % self.full_name

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "birth_year": self.birth_year,
            "species": self.species,
            "height": self.height,
            "mass": self.mass,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "homeworld": self.homeworld,
            "created": self.created,
        }
    
class FavCharacters(db.Model):
    __tablename__ = "favCharacters"

    id = db.Column(db.Integer, primary_key=True)
    #Relacion con la tabla User
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    characters_id = db.Column(db.Integer, db.ForeignKey("characters.id"))

    def __repr__(self):
        return '<FavCharacters %r>' % self.id

    def serialize(self):
        return {
            "character": self.character.serialize()
        }
    