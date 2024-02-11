from django.shortcuts import render

def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)

def aboutPage(request):
    """ Go to about us page """
    return render(request, "general/about-us.html")