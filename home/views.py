from django.shortcuts import render

# Create your views here.


def index(request):
    """A view to return the index page"""

    return render(request, "home/index.html")

def about_us(request):
    """A view to return the about us page"""

    return render(request, "home/about-us.html")
