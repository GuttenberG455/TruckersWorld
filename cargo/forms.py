from django.forms import ModelForm
from cargo.models import *


class FreightForm(ModelForm):
    class Meta:
        model = Freight
        fields = ["freight_description", "freight_comment", "freight_category", "freight_length", "freight_width",
                  "freight_height", "freight_weight", "freight_first_date", "freight_latest_date",
                  "freight_address_start", "freight_address_finish"]
