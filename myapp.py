#!/usr/bin/python3
"""
`myapp` is a module that supplies backend functionalities
for a RESTFul API.
This mimicks a car api where clients can query different Routes
and get results based on the queried Route.
All return values are in JSON format.
"""


from sqlalchemy import func
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, abort, make_response, request, jsonify


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/api_db'
db = SQLAlchemy(app)


# DB Schemas (Tables)
class Make(db.Model):
    __tablename__ = "make_table"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    make = db.Column(db.String(100), nullable=False, unique=True)
    origin = db.Column(db.String(100))
    make_model = db.relationship("MakeModel", back_populates="make", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"ID->{self.id} Make->{self.name} Origin->{self.origin}"


class MakeModel(db.Model):
    __tablename__ = "model_table"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(100), nullable=False, unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(200))
    make_id = db.Column(db.Integer, db.ForeignKey('make_table.id'), nullable=False)    
    
    make = db.relationship("Make", back_populates="make_model", lazy=True)
    make_model_trim = db.relationship("MakeModelTrim", back_populates="make_model", lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"Make-id->{self.make_id} Model->{self.name}"


class MakeModelTrim(db.Model):
    __tablename__ = "trim_table"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trim_name = db.Column(db.String(100), nullable=False, unique=True)
    engine_type = db.Column(db.String(100), nullable=False)
    horse_power = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    fuel_type = db.Column(db.String(100), nullable=False)
    transmission = db.Column(db.Integer, nullable=False)
    features = db.Column(db.String(200), nullable=False)
    make_model_id = db.Column(db.Integer, db.ForeignKey('model_table.id'), nullable=False)
    
    make_model = db.relationship("MakeModel", back_populates="make_model_trim", lazy=True)
    user_trim = db.relationship("User", back_populates="user_make_model_trim", lazy=True, cascade="all, delete-orphan")
    user_trim_review = db.relationship("UserReview", back_populates="user_review_trim", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"Trim-name->{self.trim_name} Engine_type->{self.engine_type} Features->{self.features}"


class User(db.Model):
    __tablename__ = "user_table"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    country = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(20), nullable=False)
    trim_id = db.Column(db.Integer, db.ForeignKey('trim_table.id'), nullable=False) 
    
    user_make_model_trim = db.relationship("MakeModelTrim", back_populates="user_trim", lazy=True)
    user_review = db.relationship("UserReview", back_populates="user_review_r", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"User->{self.username} Email->{self.email} Country->{self.country} Sex->{self.sex}"

class UserReview(db.Model):
    __tablename__ = "review_table"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trim_id = db.Column(db.Integer, db.ForeignKey('trim_table.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)
    rating = db.Column(db.Float)
    review = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=func.now())

    user_review_r = db.relationship("User", back_populates="user_review", lazy=True)
    user_review_trim = db.relationship("MakeModelTrim", back_populates="user_trim_review", lazy=True)

    def __repr__(self):
        return f"Rating->{self.rating} Review->{self.review}"


# Helper functions
def create_tables():
    with app.app_context():
        db.create_all()

# Defualt 404 Error handler
@app.errorhandler(404)
def _handler_api(exception):
    """Hanldes 404 page not found error"""
    return make_response(jsonify(error="Not found"), 404)

# Routes
@app.route("/makes", methods=["GET"], strict_slashes=False)
def get_makes():
    makes = Make.query.all()
    if makes:
        make_list = [{"id": make.id, "make": make.make, "origin": make.origin} for make in makes]
        response = make_response(jsonify({"Makes": make_list}))
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200
        return response
    else:
        abort(404)

@app.route("/makes/<int:make_id>", methods=["GET"], strict_slashes=False)
def get_make(make_id):
    """ Returns a make by make id """
    make = Make.query.filter_by(id=make_id).first()
    if not make:
        abort(404)
    make_dict = {}
    make_dict["id"] = make.id
    make_dict["make"] = make.make
    make_dict["origin"] = make.origin
    response = make_response(jsonify({"Make": make_dict}))
    response.headers["Content-Type"] = "application/json"
    response.status_code = 200
    return response

@app.route("/makes/<int:make_id>", methods=["DELETE"], strict_slashes=False)
def delete_make(make_id):
    """ Deletes a make by make id """
    make = Make.query.filter_by(id=make_id).first()
    if not make:
        abort(404)
    db.session.delete(make)
    db.session.commit()
    response = make_response(jsonify({"message": "deleted"}))
    response.status_code = 201
    return response

@app.route("/makes/<int:make_id>", methods=["PUT"], strict_slashes=False)
def update_make(make_id):
    """ Updates make by id """
    make = Make.query.filter_by(id=make_id).first()
    if not make:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, "Not JSON")
    make.make = data.get("make")
    make.origin = data.get("origin")
    db.session.commit()
    response = make_response(jsonify({"message": "updated"}))
    response.status_code = 201
    return response

@app.route("/makes", methods=["POST"], strict_slashes=False)
def create_makes():
    """ Creates a new make """
    data = request.get_json()
    if not data:
        abort(400, "Not JSON")
    if "make" not in data:
        abort(400, "Missing make")
    if "origin" not in data:
        abort(400, "Missing origin")
    make = data.get("make")
    origin = data.get("origin")
    new_make = Make(make=make, origin=origin)
    db.session.add(new_make)
    db.session.commit()
    response = make_response(jsonify({"message": "created"}))
    response.status_code = 201
    return response

@app.route("/make_models", methods=["GET"], strict_slashes=False)
def get_make_models():
    """ Returns all models for all makes """
    makes = MakeModel.query.all()
    if makes:
        model_list = [{"id": models.id, "model": models.model, "year": models.year, "description": models.description, "make_id": models.make_id} for models in makes]
        response = make_response(jsonify({"Models": model_list}))
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200
        return response
    else:
        abort(404)

@app.route("/make_models/<int:make_id>", methods=["GET"], strict_slashes=False)
def get_make_model(make_id):
    """ Returns the models of a particular make by make id """
    make = MakeModel.query.get(make_id)
    if not make:
        abort(404)
    make = MakeModel.query.filter_by(make_id=make_id).all()
    model_list = [{"id": models.id, "model": models.model, "year": models.year, "description": models.description, "make_id": models.make_id} for models in make]
    response = make_response(jsonify({"Models": model_list}))
    response.headers["Content-Type"] = "application/json"
    response.status_code = 200
    return response

@app.route("/make_models/<int:make_id>", methods=["POST"], strict_slashes=False)
def create_make_models(make_id):
    """ Creates a model by make id """
    data = request.get_json()
    if not data:
        abort(400, "Not JSON")
    if "model" not in data:
        abort(400, "Missing model")
    if "year" not in data:
        abort(400, "Missing year")
    if "description" not in data:
        abort(400, "Missing description")
    make_ids = Make.query.get(make_id)
    if not make_ids:
        abort(400, "Make ID does not exist")
    model = data.get("model")
    year = data.get("year")
    description = data.get("description")
    new_model = MakeModel(model=model, year=year, description=description, make_id=make_id)
    db.session.add(new_model)
    db.session.commit()
    response = make_response(jsonify({"message": "created"}))
    response.status_code = 201
    return response

@app.route("/make_models/<int:model_id>", methods=["DELETE"], strict_slashes=False)
def delete_model(model_id):
    """ Deletes a model by model id """
    model = MakeModel.query.filter_by(id=model_id).first()
    if not model:
        abort(404)
    db.session.delete(model)
    db.session.commit()
    response = make_response(jsonify({"message": "deleted"}))
    response.status_code = 201
    return response

@app.route("/make_models/<int:model_id>", methods=["PUT"], strict_slashes=False)
def update_model(model_id):
    """ Updates model by model id """
    model = MakeModel.query.filter_by(id=model_id).first()
    if not model:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, "Not JSON")
    model.model = data.get("model")
    model.year = data.get("year")
    model.description = data.get("description")
    db.session.commit()
    response = make_response(jsonify({"message": "updated"}))
    response.status_code = 201
    return response


@app.route("/make_model_trim", methods=["GET"], strict_slashes=False)
def get_trims():
    """ Returns all trims of all makes """
    trims = MakeModelTrim.query.all()
    if trims:
        trim_list = [{"id": trim.id, "trim_name": trim.trim_name, "engine_type": trim.engine_type, "horse_power": trim.horse_power, "price": trim.price, "fuel_type": trim.fuel_type, "transmission": trim.transmission, "features": trim.features, "make_model_id": trim.make_model_id} for trim in trims]
        response = make_response(jsonify({"Trims": trim_list}))
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200
        return response
    else:
        abort(404)

@app.route("/make_model_trim/<int:model_id>", methods=["GET"], strict_slashes=False)
def get_trim(model_id):
    """ Returns all trims of a particular model """
    trim = MakeModelTrim.query.filter_by(make_model_id=model_id).first()
    if not trim:
        abort(400, "Invalid model id")
    trims = MakeModelTrim.query.filter_by(make_model_id=model_id).all()
    trim_list = [{"id": trim.id, "trim_name": trim.trim_name, "engine_type": trim.engine_type, "horse_power": trim.horse_power, "price": trim.price, "fuel_type": trim.fuel_type, "transmission": trim.transmission, "features": trim.features, "make_model_id": trim.make_model_id} for trim in trims]
    response = make_response(jsonify({"Trims": trim_list}))
    response.headers["Content-Type"] = "application/json"
    response.status_code = 200
    return response

@app.route("/make_model_trim/<int:model_id>", methods=["POST"], strict_slashes=False)
def create_trim(model_id):
    """ Creates a trim for a particular model """
    data = request.get_json()
    if not data:
        abort(400, "Not JSON")
    if "trim_name" not in data:
        abort(400, "Missing trim name")
    if "engine_type" not in data:
        abort(400, "Missing engine type")
    if "horse_power" not in data:
        abort(400, "Missing HP")
    if "price" not in data:
        abort(400, "Missing price")
    if "fuel_type" not in data:
        abort(400, "Missing fuel type")
    if "transmission" not in data:
        abort(400, "Missing transmission")
    if "features" not in data:
        abort(400, "Missing features")
    make_model_id = MakeModel.query.get(model_id)
    if not make_model_id:
        abort(400, "Model ID does not exist")
    trim_name = data.get("trim_name")
    engine_type = data.get("engine_type")
    horse_power = data.get("horse_power")
    price = data.get("price")
    fuel_type = data.get("fuel_type")
    transmission = data.get("transmission")
    features = data.get("features")
    trim = MakeModelTrim(trim_name=trim_name, engine_type=engine_type, horse_power=horse_power, price=price, fuel_type=fuel_type, transmission=transmission, features=features, make_model_id=model_id)
    db.session.add(trim)
    db.session.commit()
    response = make_response(jsonify({"message": "created"}))
    response.status_code = 201
    return response

@app.route("/make_model_trim/<int:trim_id>", methods=["DELETE"], strict_slashes=False)
def delete_trim(trim_id):
    """ Deletes a trim by trim id """
    trim = MakeModelTrim.query.filter_by(id=trim_id).first()
    if not trim:
        abort(404)
    db.session.delete(trim)
    db.session.commit()
    response = make_response(jsonify({"message": "deleted"}))
    response.status_code = 201
    return response

@app.route("/make_model_trim/<int:trim_id>", methods=["PUT"], strict_slashes=False)
def update_trim(trim_id):
    """ Updates trim by trim id """
    trim = MakeModelTrim.query.filter_by(id=trim_id).first()
    if not trim:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, "Not JSON")
    trim.trim_name = data.get("trim_name")
    trim.engine_type = data.get("engine_type")
    trim.horse_power = data.get("horse_power")
    trim.price = data.get("price")
    trim.fuel_type = data.get("fuel_type")
    trim.transmission = data.get("transmission")
    trim.features = data.get("features")
    db.session.commit()
    response = make_response(jsonify({"message": "updated"}))
    response.status_code = 201
    return response

@app.route("/users", methods=["GET"], strict_slashes=False)
def get_users():
    """ Returns all users """
    users = User.query.all()
    if users:
        user_list = [{"id": user.id, "username": user.username, "email": user.email, "country": user.country, "state": user.state, "zip_code": user.zip_code, "age": user.age, "sex": user.sex, "trim_id": user.trim_id} for user in users]
        response = make_response(jsonify({"Users": user_list}))
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200
        return response
    else:
        abort(404)

@app.route("/users/<int:trim_id>", methods=["GET"], strict_slashes=False)
def get_user(trim_id):
    """ Returns all users of a particular trim by trim_id """
    trim = User.query.filter_by(trim_id=trim_id).all()
    if not trim:
        abort(404)
    user_list = [{"id": user.id, "username": user.username, "email": user.email, "country": user.country, "state": user.state, "zip_code": user.zip_code, "age": user.age, "sex": user.sex, "trim_id": user.trim_id} for user in trim]
    response = make_response(jsonify({"Trim-Users": user_list}))
    response.headers["Content-Type"] = "application/json"
    response.status_code = 200
    return response

@app.route("/users_trim/<int:trim_id>", methods=["POST"], strict_slashes=False)
def create_user(trim_id):
    """ Creates a new user for a particular trim by trim id """
    data = request.get_json()
    if not data:
        abort(400, "Not JSON")
    if "username" not in data:
        abort(400, "Missing username")
    if "email" not in data:
        abort(400, "Missing email")
    if "country" not in data:
        abort(400, "Missing country")
    if "state" not in data:
        abort(400, "Missing state")
    if "zip_code" not in data:
        abort(400, "Missing zip_code")
    if "age" not in data:
        abort(400, "Missing age")
    if "sex" not in data:
        abort(400, "Missing sex")
    make_model_trim_id = MakeModelTrim.query.get(trim_id)
    if not make_model_trim_id:
        abort(404, "Trim ID does not exist")
    username = data.get("username")
    email = data.get("email")
    country = data.get("country")
    state = data.get("state")
    zip_code = data.get("zip_code")
    age = data.get("age")
    sex = data.get("sex")
    user_trim = User(username=username, email=email, country=country, state=state, zip_code=zip_code, age=age, sex=sex, trim_id=trim_id)
    db.session.add(user_trim)
    db.session.commit()
    response = make_response(jsonify({"Message": "created"}))
    response.status_code = 201
    return response

@app.route("/users_trim/<int:user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """ Deletes a user by user id """
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    response = make_response(jsonify({"message": "deleted"}))
    response.status_code = 201
    return response

@app.route("/users_trim/<int:user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    """ Updates user by user id """
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, "Not JSON")
    user.username = data.get("username")
    user.email = data.get("email")
    user.country = data.get("country")
    user.state = data.get("state")
    user.zip_code = data.get("zip_code")
    user.age = data.get("age")
    user.sex = data.get("sex")
    db.session.commit()
    response = make_response(jsonify({"message": "updated"}))
    response.status_code = 201
    return response

@app.route("/users_reviews", methods=["GET"], strict_slashes=False)
def get_reviews():
    """ Returns all users reviews """
    reviews = UserReview.query.all()
    if reviews:
        review_list = [{"id": review.id, "trim_id": review.trim_id, "user_id": review.user_id, "rating": review.rating, "review": review.review, "created_at": review.created_at} for review in reviews]
        response = make_response(jsonify({"Reviews": review_list}))
        response.status_code = 200
        return response
    else:
        abort(404)

@app.route("/users_reviews/<int:trim_id>", methods=["GET"], strict_slashes=False)
def get_user_review(trim_id):
    """ Returns user reviews for a particular trim  by trim id """
    trim = UserReview.query.filter_by(trim_id=trim_id).first()
    if not trim:
        abort(400, "No review for trim")
    reviews = UserReview.query.filter_by(trim_id=trim_id).all()
    review_list = [{"id": review.id, "trim_id": review.trim_id, "user_id": review.user_id, "rating": review.rating, "review": review.review, "created_at": review.created_at} for review in reviews]
    response = make_response(jsonify({"Reviews": review_list}))
    response.status_code = 200
    return response


@app.route("/users_reviews/<int:user_id>/<int:trim_id>", methods=["POST"], strict_slashes=False)
def create_review(user_id, trim_id):
    """ creates a new review based on the user id and trim id """
    data = request.get_json()
    if not data:
        abort(404, "Not JSON")
    if "rating" not in data:
        abort(400, "Missing rating")
    if "review" not in data:
        abort(400, "Missing review")
    user = User.query.get(user_id)
    if not user:
        abort(400, "User ID does not exist")
    trim = MakeModelTrim.query.get(trim_id)
    if not trim:
        abort(400, "Trim does not exist")
    rating = data.get("rating")
    review = data.get("review")
    created_at = datetime.utcnow()
    user_review = UserReview(trim_id=trim_id, user_id=user_id, rating=rating, review=review, created_at=created_at)
    db.session.add(user_review)
    db.session.commit()
    response = make_response(jsonify({"message": "created"}))
    response.status_code = 201
    return response


@app.route("/users_trim/<int:user_id>/<int:review_id>", methods=["DELETE"], strict_slashes=False)
def delete_review(user_id, review_id):
    """ Deletes a review by user_id and review id """
    review = UserReview.query.filter_by(id=review_id).first()
    if not review:
        abort(404)
    user = UserReview.query.filter_by(user_id=user_id).first()
    if not user:
        abort(404)
    db.session.delete(review)
    db.session.commit()
    response = make_response(jsonify({"message": "deleted"}))
    response.status_code = 201
    return response

@app.route("/users_trim/<int:user_id>/<int:review_id>", methods=["PUT"], strict_slashes=False)
def update_review(user_id, review_id):
    """ Updates a review by user_id and review id """
    review = UserReview.query.filter_by(id=review_id).first()
    if not review:
        abort(404)
    user = UserReview.query.filter_by(user_id=user_id).first()
    if not user:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, "Not JSON")
    review.rating = data.get("rating")
    review.review = data.get("review")
    created_at = datetime.utcnow()
    review.created_at = created_at
    db.session.commit()
    response = make_response(jsonify({"message": "updated"}))
    response.status_code = 201
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
