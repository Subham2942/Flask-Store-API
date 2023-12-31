from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, get_jwt_identity, create_refresh_token

from passlib.hash import pbkdf2_sha256 as pkb 

from models import UserModel

from db import db

from blocklist import BLOCKLIST

from schemas import UserSchema

blp = Blueprint("users", __name__, description="Operation on users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")
            
        user = UserModel(
            username=user_data["username"],
            password=pkb.hash(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()
            
        return {"message": "User created successfully"}, 201
        
@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()
        
        if user and pkb.verify(user_data["password"], user.password):
            access_tocken = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_tocken, "refresh_token": refresh_token}
        abort(401, message="Invalid credentials.")
        
@blp.route("/logout")
class userLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt().get("jti")
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}
@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        
        # In this case we are adding the refresh token to the blocklist, so we can  only ge t a non fresh token once in this case
        # If we don't want this we can skipthe next 2 lines of code
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        
        return {"access_token": new_token}, 200

@blp.route("/user/<int:user_id>")
class User(MethodView):
    """
    This resource can be useful when testing our Flask app.
    We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful
    when we are manipulating data regarding the users.
    """
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted."}, 200