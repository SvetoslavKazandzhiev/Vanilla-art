from django.shortcuts import render

from artportal.about.models import About


def about_view(request):
    about = About.objects.all()
    context = {
        'about': about,
    }
    return render(request, 'about.html', context)