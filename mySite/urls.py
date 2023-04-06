from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth.urls', namespace='user_auth')),
    path('user_auth/', include("django.contrib.auth.urls")),
    path('user_auth/', include("user_auth.urls")),
    path('playerTrainingSystem/', include('playerTrainingSystem.urls', namespace='playerTrainingSystem')),
]
