from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # colocar auth
    path('auth/', include('autenticacao.urls'))
]
