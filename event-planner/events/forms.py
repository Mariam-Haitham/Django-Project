from django import forms
from .models import Event,Booking
from django.contrib.auth.models import User


class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type ='time'



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude =['owner']

        widgets={
        'date': DateInput(),
        'time': TimeInput(),
            } 




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields =['num_seats']