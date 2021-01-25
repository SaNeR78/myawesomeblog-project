from django.shortcuts import render, get_object_or_404
from .models import Event

# Create your views here.
def home(request):
	# events = Event.objects.all().order_by('-id')
	events = Event.objects.all().order_by('-id')[:3]
	return render(request, 'events/home.html', {'events': events})

def showblog(request):
	events = Event.objects.all().order_by('-id')
	return render(request, 'events/blog.html', {'events': events})

def details(request, event_id):
	events = get_object_or_404(Event, pk=event_id)
	return render(request, 'events/detailed_post.html', {'events': events})
