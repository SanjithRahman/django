from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
from .forms import Applicantform
def index(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'eventapp/index.html', context)
def about(request,pk):
    event_single=Event.objects.get(pk=pk)
    if request.method == 'POST':
        print("I got a request from frontend")
        form=Applicantform(request.POST)
        if form.is_valid():
            applicant=form.save(commit=False)
            applicant.event=event_single
            applicant.save()

    form=Applicantform()
    context={
        'event':event_single,
        'form':form
    }
    return render(request, 'eventapp/form.html',context)
def eventdetails(request,pk):
    event_single=Event.objects.get(pk=pk)
    context={
        'event':event_single
    }
    return render(request,'eventapp/form.html')



