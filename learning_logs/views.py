from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

# Create your views here.
def index(request):
    """The index web page for learning log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all the topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Shows a specific topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # Data has not been sent it
        form = TopicForm()
    else:
        # Data POST is sent it
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Shows the new form or not valid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

