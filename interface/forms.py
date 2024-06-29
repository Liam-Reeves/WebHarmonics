from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'style': 'width: 300px;'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 300px; height: 200px;'}))

