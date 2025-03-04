from marshmallow import Schema, fields, ValidationError
#lambda funcion flecha
#el validate es para filtros customizados
class Pokemon_Favorite_Schema(Schema):

    pokemon_id = fields.Str(
        required=True,
        validate=lambda x:len(x)>0,
        error_messages={
            "required": "Algo salio mal"
        }
    )

