from django.shortcuts import render, redirect
from .models import Player
from .forms import PlayerForm

# Create your views here.
def index(request):
    """
    Renders a view that displays a list of all player objects.

    Retrieves all player objects from the database using the Player.objects.all() method and passes them as a context
    dictionary to the 'manage_players.html' template. The template is then rendered using the render() function.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object containing the rendered template.
    :rtype: HttpResponse
    """
    players = Player.objects.all()
    context = {'players': players}
    return render(request, 'manage_players.html', context)

def eligible_players(request):
    """
    Renders a view that displays a list of eligible player objects.

    Retrieves all player objects from the database using the Player.objects.all() method, filters them to include only
    those that are eligible for selection, and passes them as a context dictionary to the 'view_players.html' template.
    The template is then rendered using the render() function.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object containing the rendered template.
    :rtype: HttpResponse
    """
    players = Player.objects.all()
    context = {'players': players}
    return render(request, 'view_players.html', context)

def createPlayer(request):
    """
    Creates a new player object using data submitted through a form.

    Renders a form using the PlayerForm class and handles POST requests to create a new player object based on the
    submitted data. If the request is not a POST request, the form is rendered as a blank form.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object containing the rendered form.
    :rtype: HttpResponse
    """
    form = PlayerForm()
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playerTrainingSystem:manage_players')
    context = {'form': form}
    return render(request, 'player_form.html', context)

def updatePlayer(request, pk):
    """
    Renders a view that displays a form for updating an existing player object.

    Retrieves the player object with the specified id from the database using the Player.objects.get() method, and
    creates a form instance for that player using the PlayerForm() class. If the request method is POST, the form is
    updated with the submitted data using the same PlayerForm() class, validated, and saved to the database using the
    form.save() method. If the form is valid, the view redirects to the 'manage_players' view. If the request method
    is GET, the view renders the player_form.html template with the form instance as context.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param pk: The id of the player object to be updated.
    :type pk: int
    :return: The HTTP response object containing the rendered template.
    :rtype: HttpResponse
    """
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
    """
    Deletes a player object from the database.

    :param request: The request object containing metadata about the request.
    :type request: HttpRequest
    :param pk: The unique identifier for the player object to be deleted.
    :type pk: int
    :return: A redirect to the manage_players view if the request method is POST,
             otherwise a render of the delete_player.html template.
    :rtype: HttpResponse
    """
    player = Player.objects.get(id=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('playerTrainingSystem:manage_players')
    context = {'player': player}
    return render(request, 'delete_player.html', context)
