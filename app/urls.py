from django.urls import path
from app.views import *

urlpatterns = [
    
    path('table/', view_table, name='table'),
    path('create/', view_create, name='create'),
    path('delete/<id>/', view_delete, name="delete"),
    path('update/<id>/', view_update, name='update'),



]