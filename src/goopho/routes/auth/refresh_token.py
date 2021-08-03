from flask import ( request, 
                    jsonify, 
                    make_response
                   )


from flask_restful import (Resource, 
                           abort
                          )


from flask_jwt_extended import (create_access_token, 
                                jwt_required,
                                get_jwt_identity
                                )



class RefreshToken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user)
        return {'access_token': new_token}, 200