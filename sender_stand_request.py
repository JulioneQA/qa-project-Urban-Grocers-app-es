import configuration
import requests
import data


def post_personal_kit(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit_body,auth_token):
    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH,
                         json=kit_body,
                         headers=auth_token)

