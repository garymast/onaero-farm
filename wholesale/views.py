from django.shortcuts import render

# Create your views here.

def wholesale_page(request):
    """A view to return the about us page"""
    
    return render(request, 'wholesale/wholesale.html')