import data
import sender_stand_request

# funcion para el cambio de los valores en el parametro "name"
def get_kit_body(name_kit):
    current_body = data.kit_body.copy()
    current_body['name'] = name_kit
    return current_body

# Función para generar el "authToken"
def get_new_user_token():
    resp_user = sender_stand_request.post_personal_kit(data.user_body.copy())
    value_token = resp_user.json()["authToken"]
    new_value_token = data.headers.copy()
    new_value_token["Authorization"] = f"Bearer {value_token}"
    # Guardar el token de autenticación
    return new_value_token

# función para pruebas positivas
def positive_assert(name_kit):
    kit_body = get_kit_body(name_kit)

    positive_kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert positive_kit_response.status_code == 201
    assert positive_kit_response.json()['name'] == name_kit

# función para pruebas negativas
def negative_assert(name_kit):
    kit_body = get_kit_body(name_kit)
    negative_kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert negative_kit_response.status_code == 400
    assert negative_kit_response.json()['code'] == 400

# prueba 1 el numero permitido de caracteres (1)

def test_numero_permitido_de_caracteres_1():
    positive_assert("a")

# prueba 2 el numero permitido de caracteres (511)

def test_numero_permitido_de_caracteres_511():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# prueba 3 el número de caracteres es menor que la cantidad permitida (0)

def test_numero_de_caracteres_0():
    negative_assert("")

# prueba 4 	El número de caracteres es mayor que la cantidad permitida (512)

def test_numero_permitido_de_caracteres_512():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


#5 	Se permiten caracteres especiales ()

def test_numero_caracteres_especiales_permitidos_():
    positive_assert("№%@")


#6 Se permiten espacios (A Aaa)

def test_se_permiten_espacios():
    positive_assert(" A Aaa ")

 #7 Se permiten números (123)

def test_se_permiten_números():
    positive_assert("123")

#8 El parámetro no se pasa en la solicitud: kit_body = ()

def test_el_parametro_no_se_pasa_en_la_solicitud():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert(kit_body)

#9 	Se ha pasado un tipo de parámetro diferente (número): kit_body = ( "name": 123 )

def test_el_parametro_no_se_pasa_en_solicitud():
    negative_assert(123)
