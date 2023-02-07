from django.forms import ModelForm
from .models import Subscription

class SubscriptionModelForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ['hive_id','service','start_date', 'end_date']



