from marshmallow import Schema, fields, ValidationError
#lambda funcion flecha
#el validate es para filtros customizados
class Pokemon_Favorite_Schema(Schema):
    user_id = fields.Str(
        required=True,
        validate=lambda x:len(x)>0,
        error_messages={
            "required": "El nombre es requerido"
        }
        
    )
    pokemon_id = fields.Str(
        required=True,
        validate=lambda x:len(x)>0,
        error_messages={
            "required": "La contraseña es requerido"
        }
    )

