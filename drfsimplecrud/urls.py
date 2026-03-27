from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # 👈 IMPORTANTE

urlpatterns = [
    path('', lambda request: redirect('/api/projects/')),  # 👈 REDIRECCIÓN
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),
]