from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from artportal.art_app.models import Art
from artportal.topics.models import Topics


@method_decorator(login_required, name='dispatch')
class TopicsView(ListView):
    template_name = 'topics.html'
    model = Topics
    context_object_name = 'topics'


def topic_type(request):
    context = {
        'art': Art.objects.all(),
    }
    return render(request, 'topics/sections/topic-sections-graphic.html', context)


def topic_type_other(request):
    context = {
        'art': Art.objects.all(),
    }
    return render(request, 'topics/sections/topic-sections-other.html', context)


def topic_type_photography(request):
    context = {
        'art': Art.objects.all(),
    }
    return render(request, 'topics/sections/topic-sections-photography.html', context)


def topic_type_fine_art(request):
    context = {
        'art': Art.objects.all(),
    }
    return render(request, 'topics/sections/topic-sections-fine-art.html', context)


def topic_type_jewellery(request):
    context = {
        'art': Art.objects.all(),
    }
    return render(request, 'topics/sections/topic-sections-jewellery.html', context)
