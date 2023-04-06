from django.urls import path
from . import views

app_name = 'playerTrainingSystem'
urlpatterns = [
    path('', views.index, name='manage_players'),
    path('eligible_players/', views.eligible_players, name='eligible_players'),
    path('create_player/', views.createPlayer, name='create_player'),
    path('update_player/<int:pk>', views.updatePlayer, name='update_player'),
    path('delete_player/<int:pk>', views.deletePlayer, name='delete_player'),
]
