from django import forms
from . import models


class UserForm(forms.Form):
    username = forms.CharField(label="username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))


class RegisterForm(forms.Form):
    gender = (
        ('male', "M"),
        ('female', "F"),
    )
    username = forms.CharField(label="username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="repeat password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='gender', choices=gender)

class CarForm(forms.Form):
    cartype = forms.CharField(label="cartype", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    plateNumber = forms.CharField(label="plateNumber", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    passengersNumber = forms.DecimalField(label="passengerNumber" ,max_value=99 , max_digits=3, decimal_places=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
    freeText = forms.CharField(label="freeText", max_length=128, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

class OwnerForm(forms.Form):
    ownernumber = forms.DecimalField(label="ownernumber" ,max_value=99 , max_digits=3, decimal_places=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
    share = forms.BooleanField(label="share", required=False, widget=forms.CheckboxInput())
    dest = forms.CharField(label="dest", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    earlytime = forms.DateTimeField(label="arrivaltime", widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    # latetime = forms.DateTimeField(label="latetime", widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    freeText = forms.CharField(label="freeText", max_length=128, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cartype = forms.CharField(label="cartype", max_length=128, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

class DriverForm(forms.Form):
    space = forms.DecimalField(label="space" ,max_value=99 , required=True, max_digits=3, decimal_places=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cartype = forms.CharField(label="cartype", max_length=128, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    freeText = forms.CharField(label="freeText", max_length=128, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

class ShareForm(forms.Form):
    sharenumber = forms.DecimalField(label="sharenumber" ,max_value=99 , required=True, max_digits=3, decimal_places=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dest = forms.CharField(label="dest", max_length=128, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    earlytime = forms.DateTimeField(label="earlytime", widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    latetime = forms.DateTimeField(label="latetime", widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))

class OwnereditForm(forms.ModelForm):
    ownernumber = forms.DecimalField(label="ownernumber" ,max_value=99 , max_digits=3, decimal_places=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cartype = forms.CharField(label="cartype", max_length=128, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dest = forms.CharField(label="dest", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    freeText = forms.CharField(label="freeText", max_length=128, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = models.Ride
        exclude = ['owner','sharer', 'carspace', 'status', 'ridedriver', 'endtime']

class SharereditForm(forms.ModelForm):
    groupnumber = forms.DecimalField(label="groupnumber" ,max_value=99 , max_digits=3, decimal_places=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = models.Relationship
        exclude = ['user', 'ride']