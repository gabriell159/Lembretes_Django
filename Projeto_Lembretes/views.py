from django.shortcuts import render
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse


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

def new_topic(request):
    if request.method != 'POST':
        # Nenhum dado enviado,criacao do formulario
        form = TopicForm()
    else:
        # Dados de post submetido,processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            #reversed usa o name de URLS para redirecionar,nao é a melhor pratica
            return HttpResponseRedirect(reversed('topic'))
    context = {'form': form}
    return render(request, 'Projeto_Lembretes/new_topic.html', context)