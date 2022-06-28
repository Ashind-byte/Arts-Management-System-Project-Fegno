from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import datetime

# Create your views here.
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from .forms import RegForm
from .models import Winner, Event, Registration


@login_required
def pub_results(request):
    winners = Winner.objects.select_related('rid','rid__user_id','rid__event_name')


    return render(request, 'pub_results.html', {"winners": winners})

@login_required
def upcoming_events(request):
    lists = Event.objects.all().filter(registration_closing_date__gt=timezone.now())
    return render(request, 'upcoming_events.html', {"lists": lists})




@login_required
def current_events(request):
    ongoing_events = Event.objects.all().filter(registration_closing_date=timezone.now())
    return render(request, 'ongoing-events.html', {"events": ongoing_events})



@method_decorator(login_required, 'dispatch')
class CurrentEventDetailView(DetailView):
    model = Event
    template_name = 'upcoming_event_details.html'
    context_object_name = 'details'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        reg,created = Registration.objects.get_or_create(event_name=self.object, user_id=request.user)
        if created:
            messages.success(request,"you have successfully registered to {}".format(self.object.event_name))
        else:
            messages.warning(request,"You have already registered to {}".format(self.object.event_name))
        return self.get(request,*args,**kwargs)


@login_required
def scoreboard(request):
    score_lists = Winner.get_house_points()


    return render(request,'scoreboard.html', {"scores":score_lists})

def check_for_conflict(first_event, other_event):
    if first_event.from_date <  other_event.to_date and other_event.from_date < first_event.to_date:
        return True
    else:
        return False

def registered_events(request):

    all_reg_events = list(Registration.objects.select_related('user_id', 'event_name').filter(user_id=request.user).order_by('event_name__from_date'))

    conflict_directory = {}
    for regn in all_reg_events:
        conflict_directory[regn.id] = []
        for other_regn in all_reg_events:
            if other_regn.id != regn.id:
                conflict = check_for_conflict(regn.event_name, other_regn.event_name)
                if conflict:
                    conflict_directory[regn.id].append(other_regn)
                    #messages.warning(request, f'There is a conflict with {other_regn.event_name} and you have to contact the admin to change the registration details.')

    for regn in all_reg_events:
        regn.conflits = conflict_directory[regn.id]

    return render(request, 'registered.html', {"reg": all_reg_events})
