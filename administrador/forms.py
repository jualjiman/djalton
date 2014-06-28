from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phonenumber = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)