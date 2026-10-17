from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

app_name = 'products'

router = routers.SimpleRouter()
router.register('', views.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls))
]



# Fora dos conchetes do urlpatterns, depois de todo o codigo insisra a seguinte linha
# para declarar a pasta caminho e raiz para arquivos que sera enviados atraves de 
# forms de upload.

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
