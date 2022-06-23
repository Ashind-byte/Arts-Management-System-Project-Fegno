from django.forms import ModelForm

from Events.models import Registration


class RegForm(ModelForm):
    class Meta:
        model = Registration
        fields = ('event_name', 'event_name')