from django.shortcuts import render

def comingsoon(request):

    return render(request, 'index.html')

def LandingPage(request):

    return render(request, 'landing-page.html')