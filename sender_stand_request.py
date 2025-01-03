import configuration
import requests
import data

def get_new_user_token(sender_stand_request=None):
    # Crear un nuevo usuario
    user_body = data.user_body
    resp_user = sender_stand_request.post_new_user(user_body)
    # Guardar el token de autenticación
    return resp_user.json()["authToken"]

auth_token = get_new_user_token()

Headers2= {
    "content_type":"application/json",
    "Authorization": f'Bearer{auth_token}'
    }

def post_personal_kit(kitbody):
    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH,
                         json=kitbody,
                         headers=Headers2)