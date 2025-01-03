import data
import sender_stand_request

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = name
    return current_kit_body
def positive_assert_for_kit_body(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_body['name']

def negative_assert_code_400(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400

#1 el numero permitido de caracteres (1)

def test_numero_permitido_de_caracteres_1():
    kit_body = get_kit_body("a")
    positive_assert_for_kit_body(kit_body)


#2 el numero permitido de caracteres (511)

def test_numero_permitido_de_caracteres_511():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert_for_kit_body(kit_body)

#3 el numero de caracteres es menor que la cantidad permitida (0)

def test_numero_de_caracteres_0():
    kit_body = get_kit_body("")
    positive_assert_for_kit_body(kit_body)

#4 	El número de caracteres es mayor que la cantidad permitida (512)

def test_numero_permitido_de_caracteres_512():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    positive_assert_for_kit_body(kit_body)

#5 	Se permiten caracteres especiales (№%@)

def test_numero_caracteres_especiales_permitidos_(№%@):
    kit_body = get_kit_body("№%@")
    positive_assert_for_kit_body(kit_body)

#6 Se permiten espacios (A Aaa)

def test_se_permiten_espacios(A Aaa):
    kit_body = get_kit_body("A Aaa")
    positive_assert_for_kit_body(kit_body)

 #7 Se permiten números (123)

def test_se_permiten_números(123):
    kit_body = get_kit_body("123")
    positive_assert_for_kit_body(kit_body)

#8 El parámetro no se pasa en la solicitud: kit_body = { }

def test_el_parametro_no_se_pasa_en_la_solicitud{}:
    kit_body = get_kit_body("")
    positive_assert_for_kit_body(kit_body)

#9 	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }

def test_el_parametro_no_se_pasa_en_la_solicitud{}:
    kit_body = get_kit_body("")
    positive_assert_for_kit_body(kit_body)
