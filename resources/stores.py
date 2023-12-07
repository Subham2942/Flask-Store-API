import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models import StoreModel
from schemas import StoreSchema
from db import db

blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route('/store/<int:store_id>')
class store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        
        return store
        
    
    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted"}


@blp.route("/store")
class storeList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
    
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        
        new_store = StoreModel(**store_data)
        
        try:
            db.session.add(new_store)
            db.session.commit()
            
        except IntegrityError:
            abort(400, message="A store with that name already exists")
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the store to database")
        
        return new_store