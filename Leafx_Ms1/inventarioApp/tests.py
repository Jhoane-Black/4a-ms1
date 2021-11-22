from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.

class TestAPI(TestCase):

    # Test endpoints Autenticación

    def test_signUp(self):
        client = APIClient()
        response = client.post(
            '/rest-auth/registration/', 
            {
                "username": "test_signUp",
                "password1": "test_signUp2021",
                "password2": "test_signUp2021",
                "email": "test_signUp@leaf.com"
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_login(self):
        client = APIClient()
        response = client.post(
            '/rest-auth/login/', 
            {
                "username": "leaf",
                "password": "grupo4mintic"
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('key' in  response.data.keys(), True)


    # Test endpoints Proveedor
    
    def test_get_proveedor(self):
        client = APIClient()
        response = client.get('/inventario/proveedor/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_proveedor(self):
        client = APIClient()
        response = client.get('/inventario/proveedor/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('user' in  response.data.keys(), True)
        self.assertEqual('nombre' in  response.data.keys(), True)      
        self.assertEqual('direccion' in  response.data.keys(), True)
        self.assertEqual('nit' in  response.data.keys(), True)


    def test_create_proveedor(self):
        client = APIClient()
        response = client.post(
            '/inventario/proveedor/', 
            {
                "user": 1,
                "nombre": "Vivero Los Laureles",
                "direccion": "laureles medellin",
                "nit": 156156165
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('user' in  response.data.keys(), True)
        self.assertEqual('nombre' in  response.data.keys(), True)      
        self.assertEqual('direccion' in  response.data.keys(), True)
        self.assertEqual('nit' in  response.data.keys(), True)


    def test_update_proveedor(self):
        client = APIClient()
        response = client.put(
            '/inventario/proveedor/1/',
            {
                "user": 1,
                "nombre": "Garden",
                "direccion": "via el caimo",
                "nit": 123456789
            }, 
            format='json') 

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('user' in  response.data.keys(), True)
        self.assertEqual('nombre' in  response.data.keys(), True)      
        self.assertEqual('direccion' in  response.data.keys(), True)
        self.assertEqual('nit' in  response.data.keys(), True)


    def test_delete_proveedor(self):
        client = APIClient()
        response = client.delete('/inventario/proveedor/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Test endpoints Producto

    def test_get_productos(self):
        client = APIClient()
        response = client.get('/inventario/producto/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_producto(self):
        client = APIClient()
        response = client.get('/inventario/producto/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('nombre' in  response.data.keys(), True)
        self.assertEqual('precio' in  response.data.keys(), True)
        self.assertEqual('stock' in  response.data.keys(), True)
        self.assertEqual('proveedor' in  response.data.keys(), True)


    def test_create_producto(self):
        client = APIClient()
        response = client.post(
            '/inventario/producto/', 
            {
                "nombre": "Girasol",
                "precio": 11000,
                "stock": 25,
                "proveedor": 1
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('nombre' in  response.data.keys(), True)
        self.assertEqual('precio' in  response.data.keys(), True)
        self.assertEqual('stock' in  response.data.keys(), True)
        self.assertEqual('proveedor' in  response.data.keys(), True)


    def test_update_producto(self):
        client = APIClient()
        response = client.put(
            '/inventario/producto/1/',
            {
                "nombre": "Canasta",
                "precio": 5000,
                "stock": 18,
                "proveedor": 1
            }, 
            format='json') 

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('nombre' in  response.data.keys(), True)
        self.assertEqual('precio' in  response.data.keys(), True)
        self.assertEqual('stock' in  response.data.keys(), True)
        self.assertEqual('proveedor' in  response.data.keys(), True)


    def test_delete_producto(self):
        client = APIClient()
        response = client.delete('/inventario/producto/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
    # Test endpoints Cliente
    
    def test_get_cliente(self):
        client = APIClient()
        response = client.get('/inventario/cliente/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_cliente(self):
        client = APIClient()
        response = client.get('/inventario/cliente/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('user' in  response.data.keys(), True)
        self.assertEqual('nombre' in  response.data.keys(), True)      
        self.assertEqual('direccion' in  response.data.keys(), True)


    def test_create_cliente(self):
        client = APIClient()
        response = client.post(
            '/inventario/cliente/', 
            {
                "user": 1,
                "nombre": "Python",
                "direccion": "calle 50 - 10",
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('user' in  response.data.keys(), True)
        self.assertEqual('nombre' in  response.data.keys(), True)      
        self.assertEqual('direccion' in  response.data.keys(), True)


    def test_update_cliente(self):
        client = APIClient()
        response = client.put(
            '/inventario/cliente/1/',
            {
                "user": 1,
                "nombre": "Python",
                "direccion": "calle 50 - 10",
            }, 
            format='json') 

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('user' in  response.data.keys(), True)
        self.assertEqual('nombre' in  response.data.keys(), True)      
        self.assertEqual('direccion' in  response.data.keys(), True)
 

    def test_delete_cliente(self):
        client = APIClient()
        response = client.delete('/inventario/cliente/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Test endpoints Comentario
    
    def test_get_comentario(self):
        client = APIClient()
        response = client.get('/inventario/comentario/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        


    def test_get_comentario(self):
        client = APIClient()
        response = client.get('/inventario/comentario/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('calificacion' in  response.data.keys(), True)
        self.assertEqual('comentario' in  response.data.keys(), True)      
        self.assertEqual('creacion' in  response.data.keys(), True)
        self.assertEqual('producto' in  response.data.keys(), True)
        self.assertEqual('cliente' in  response.data.keys(), True)


    def test_create_comentario(self):
        client = APIClient()
        response = client.post(
            '/inventario/comentario/', 
            {
                "calificacion": 4,
                "comentario": "Llego bien el producto pero se demoró la entrega",
                "creacion": "2021-11-12",
                "producto": 1,
                "cliente": 1
            },
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('calificacion' in  response.data.keys(), True)
        self.assertEqual('comentario' in  response.data.keys(), True)      
        self.assertEqual('creacion' in  response.data.keys(), True)
        self.assertEqual('producto' in  response.data.keys(), True)
        self.assertEqual('cliente' in  response.data.keys(), True)


    def test_update_comentario(self):
        client = APIClient()
        response = client.put(
            '/inventario/comentario/1/',
            {
                "calificacion": 2,
                "comentario": "Esto es una prueba",
                "creacion": "2021-11-12",
                "producto": 1,
                "cliente": 1
            }, 
            format='json') 

        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('calificacion' in  response.data.keys(), True)
        self.assertEqual('comentario' in  response.data.keys(), True)      
        self.assertEqual('creacion' in  response.data.keys(), True)
        self.assertEqual('producto' in  response.data.keys(), True)
        self.assertEqual('cliente' in  response.data.keys(), True)


    def test_delete_comentario(self):
        client = APIClient()
        response = client.delete('/inventario/comentario/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Test endpoints Resumen

    def test_get_comentariosdeproducto(self):
        client = APIClient()
        response = client.get('/inventario/resumen/producto/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_comentariosdecliente(self):
        client = APIClient()
        response = client.get('/inventario/resumen/cliente/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_get_productosdeproveedor(self):
        client = APIClient()
        response = client.get('/inventario/resumen/proveedor/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)    