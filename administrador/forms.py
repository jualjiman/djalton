from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phonenumber = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Numero telefonico'}))
    message = forms.CharField(widget=forms.Textarea,widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}))