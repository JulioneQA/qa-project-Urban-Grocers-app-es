import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH ,
                     json= body,
                     headers= data.headers    )

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


def post_new_client_kit(kit_body, name):
    return None
