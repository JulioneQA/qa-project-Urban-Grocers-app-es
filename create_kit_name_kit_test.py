import data
import sender_stand_request

# funcion para el cambio de los valores en el parametro "name"
def get_kit_body(name_kit):
    current_body = data.kit_body.copy()
    current_body['name'] = name_kit()
    return current_body

# Función para generar el "authToken"
def get_new_user_token():
    # Crear un nuevo usuario
    user_body = data.user_body
    resp_user = sender_stand_request.post_new_user(user_body)
    # Guardar el token de autenticación
    return resp_user.json()["authToken"]

# función para pruebas positivas
def positive_assert(kit_body):
    positive_kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert positive_kit_response.status_code == 201
    assert positive_kit_response.json()['code'] == kit_body['code']

# función para pruebas negativas
def negative_assert(kit_body):
    negative_kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert negative_kit_response.status_code == 400
    assert negative_kit_response.json()['code'] == kit_body['code']

def negative_assert_no_name(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

# prueba 1 el numero permitido de caracteres (1)

def test_numero_permitido_de_caracteres_1():
    kit_body = get_kit_body("a")
    positive_assert_for_kit_body(kit_body)

def positive_assert_for_kit_body():
    pass

# prueba 2 el numero permitido de caracteres (511)

def test_numero_permitido_de_caracteres_511():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert_for_kit_body(kit_body)

# prueba 3 el numero de caracteres es menor que la cantidad permitida (0)

def test_numero_de_caracteres_0():
    kit_body = get_kit_body("")
    negative_assert(kit_body)

# prueba 4 	El número de caracteres es mayor que la cantidad permitida (512)

def test_numero_permitido_de_caracteres_512():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(kit_body)

#5 	Se permiten caracteres especiales ()

def test_numero_caracteres_especiales_permitidos_():
    kit_body = get_kit_body("\"№%@\",")
    positive_assert_for_kit_body(kit_body)

#6 Se permiten espacios (A Aaa)

def test_se_permiten_espacios( Aaa):
    kit_body = get_kit_body(" A Aaa ")
    positive_assert_for_kit_body(kit_body)

 #7 Se permiten números (123)

def test_se_permiten_números():
    kit_body = get_kit_body()
    positive_assert_for_kit_body(kit_body)

#8 El parámetro no se pasa en la solicitud: kit_body = ()

def test_el_parametro_no_se_pasa_en_la_solicitud():
    kit_body = get_kit_body("")
    negative_assert(kit_body)

#9 	Se ha pasado un tipo de parámetro diferente (número): kit_body = ( "name": 123 )

def test_el_parametro_no_se_pasa_en_la_solicitud():
    kit_body = get_kit_body("")
    negative_assert(kit_body)
