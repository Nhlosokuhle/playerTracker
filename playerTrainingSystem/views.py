from django.shortcuts import render, redirect
from .models import Player
from .forms import PlayerForm

# Create your views here.
def index(request):
    players = Player.objects.all()
    context = {'players': players}
    return render(request, 'manage_players.html', context)

def eligible_players(request):
    players = Player.objects.all()
    context = {'players': players}
    return render(request, 'view_players.html', context)

def createPlayer(request):
    form = PlayerForm()
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playerTrainingSystem:manage_players')
    context = {'form': form}
    return render(request, 'player_form.html', context)

def updatePlayer(request, pk):
    player = Player.objects.get(id=pk)
    form = PlayerForm(instance=player)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('playerTrainingSystem:manage_players')
    context = {'form': form}
    return render(request, 'player_form.html', context)

def deletePlayer(request, pk):
    player = Player.objects.get(id=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('playerTrainingSystem:manage_players')
    context = {'player': player}
    return render(request, 'delete_player.html', context)
