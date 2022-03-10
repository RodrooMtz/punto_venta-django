from django.shortcuts import render


# Create your views here.
def mesas(request):
    context = {
        'numero': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    }
    return render(request, 'mesas/mesas.html', context)
