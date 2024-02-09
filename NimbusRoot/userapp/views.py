from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def card(request):
    return render(request, 'card.html')