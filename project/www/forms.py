

from django import forms
from .models import Category,Product

class CategoryForm(forms.ModelForm):

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    discription = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Discription'}))


    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    price = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    discription = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Discription'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Choose a photo'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'placeholder': 'Select a Category'}))

    class Meta:
        model = Product
        fields = '__all__'


