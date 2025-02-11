import configuration
import requests
import data


def post_personal_kit(kitbody):
    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH,
                         json=kitbody,
                         headers=data.headers)

def post_new_client_kit(kit_body,auth_token):
    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH,
                         json=kitbody,
                         headers=auth_token)
