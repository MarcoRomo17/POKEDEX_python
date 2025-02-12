from marshmallow import Schema, fields, ValidationError
#lambda funcion flecha
#el validate es para filtros customizados
class UserSchema(Schema):
    name = fields.Str(
        required=True,
        validate=lambda x:len(x)>0,
        error_messages={
            "required": "El nombre es requerido"
        }
        
    )
    password = fields.Str(
        required=True,
        validate=lambda x:len(x)>0,
        error_messages={
            "required": "La contraseña es requerido"
        }
    )

    email = fields.Str(
        required=True,
        validate=lambda x:"@utma.edu.mx"in x ,
        error_messages={
            "required": "El email es requerido"
        }
    )