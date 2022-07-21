from django.views.generic.edit import CreateView
from .models import Subscriber
from . forms import SubscriberForm

class SubscriberCreateView(CreateView):
    model = Subscriber
    form_class = SubscriberForm
    