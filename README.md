# Proyecto Urban Grocers 
# En este proyecto trabajamos como gestionar kits de productos para diferentes usuarios. en este se consideraron la creación de usuarios y kits de productos con diferentes comprobaciones en los nombres de los kits.
# el proyecto consta de 9 pruebas detalladas.

HERRAMIENTAS TRABAJADAS:

# Lenguajes: Python
# Librerias: Pytest se requiere para haer las pruebas
# Request: Permite hacer las solicitudes HTTP a la API

Lista de comprobación de las pruebas incluidas en la automatización para el campo Name
No. de prueba	Descripción	Código de respuesta esperados
1	Comprobar que el campo admite un caracter	201
2	Comprobar que el campo admite 511 caracteres	201
3	Comprobar que el campo NO admite 0 caracteres	400
4	Comprobar que el campo NO admite 512 caracteres	400
5	Comprobar que el campo admite caracteres especiales	201
6	Comprobar que el campo admite espacios	201
7	Comprobar que el campo admite números	201
8	Comprobar que la solitud marca error al enviarse sin el parametró name	400
9	Comprobar que el campo admite número y no string	400
Ejecuta todas las pruebas con el comando pytest create_kit_name_kit_test.py.
