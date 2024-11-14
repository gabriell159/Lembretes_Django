from django.shortcuts import render
from .models import Topic


def index(request):
    return render(request, 'Projeto_Lembretes/index.html')


def topics(request):
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'Projeto_Lembretes/topics.html',context)

def topic(request,topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic':topic , 'entries':entries }
    return render(request, 'Projeto_Lembretes/topic.html', context)