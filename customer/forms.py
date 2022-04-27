from django.db.models import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('__all__')
        exclude = ['user']

class NewOrder(ModelForm):
    class Meta:
        model = Order 
        fields = ('__all__')

class NewCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = ('__all__')

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class NewProduct(ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')