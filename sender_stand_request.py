import configuration
import requests
import data


def post_new_user (body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers
                         )


response=post_new_user(data.user_body).json()
auth_token=response['auth_token']

Headers2= {
    "content_type":"application/json",
    "Authorization": f'Bearer{auth_token}'
    }

def post_personal_kit(kitbody):
    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH,
                         json=kitbody,
                         headers=Headers2
                          )
