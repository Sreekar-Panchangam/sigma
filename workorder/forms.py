from django import forms

class HoistWorkOrderFilterForm(forms.Form):
    wonumber = forms.IntegerField(required=False, label='Work Order Number')
    customer = forms.CharField(max_length=100, required=False, label='Company Name')
    city = forms.CharField(max_length=100, required=False, label='City')
    capacity = forms.CharField(max_length=10, required=False, label='Capacity')
    sales_rep = forms.CharField(max_length=10, required=False, label='Sales Representative')
    start_date = forms.DateField(required=False, label='Start Date')
    end_date = forms.DateField(required=False, label='End Date')
