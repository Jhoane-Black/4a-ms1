from django.urls import path
from .views import ProveedorListCreate, ProveedorUpdateDelete, \
        ProductoListCreate, ProductoUpdateDelete, ClienteListCreate, \
        ClienteUpdateDelete, ComentarioListCreate, ComentarioUpdateDelete \

urlpatterns = [
    path('proveedor/', ProveedorListCreate.as_view()),
    path('proveedor/<pk>/', ProveedorUpdateDelete.as_view()),
    path('producto/', ProductoListCreate.as_view()),
    path('producto/<pk>/', ProductoUpdateDelete.as_view()),
    path('cliente/', ClienteListCreate.as_view()),
    path('cliente/<pk>/', ClienteUpdateDelete.as_view()),
    path('comentario/', ComentarioListCreate.as_view()),
    path('comentario/<pk>/', ComentarioUpdateDelete.as_view())
]