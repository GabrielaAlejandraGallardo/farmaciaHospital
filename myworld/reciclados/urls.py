from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 
app_name = 'reciclados'
urlpatterns = [
 
    path('', views.inicio, name='inicio'),
    path('indexM', views.indexM, name='indexM'),
    path('addM/', views.addM, name='addM'),
    path('addM/addrecordM/', views.addrecordM, name='addrecordM'),
    path('delete/<int:idMaterial>', views.delete, name='delete'),
    path('updateM/<int:idMaterial>', views.updateM, name='updateM'),
    path('updateM/updaterecordM/<int:idMaterial>', views.updaterecordM, name='updaterecordM'),
    path('violenciaDeGenero/', views.violenciaDeGenero, name='violenciaDeGenero'),
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 









