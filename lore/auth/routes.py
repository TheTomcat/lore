from flask import request
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_jwt_identity, jwt_required)

from lore.auth import bp
from lore.models.user import User

# https://yasoob.me/posts/how-to-setup-and-deploy-jwt-auth-using-react-and-flask/

@bp.post("/login")
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).first()
    if username != "test" or password != "test":
        return {"message": "Bad username or password"}, 401
    if not user:
        return {"message", "Invalid authentication"}, 403
    access_token = create_access_token(identity=user.user_id, fresh=True)
    refresh_token = create_refresh_token(identity=user.user_id)
    return {'access_token':access_token, 'refresh_token':refresh_token}

@bp.post("/refresh")
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return {'access_token':access_token}