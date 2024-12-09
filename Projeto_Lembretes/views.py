from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
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
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'Projeto_Lembretes/new_topic.html', context)

def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request, 'Projeto_Lembretes/new_entry.html', context)

def edit_entry(request,entry_id):
    entry = Entry.object.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'Projeto_Lembretes/edit_entry.html', context)