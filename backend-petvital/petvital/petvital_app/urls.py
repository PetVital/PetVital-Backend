from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    
    path('mascotas/create/', MascotaCreateView.as_view(), name='mascotas-create'),
    path('mascotas/list/', MascotaListView.as_view(), name='mascotas-list'),
    path('mascotas/<int:mascota_id>/', MascotaUpdateDeleteView.as_view(), name='mascotas-update-delete'),

    path('citas/create/', CitaCreateView.as_view(), name='citas-create'),
    path('citas/list/', CitaListView.as_view(), name='citas-list'),
    path('citas/<int:id>/', CitaUpdateDeleteView.as_view(), name='citas-update-delete'),
]
