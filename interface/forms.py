from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100, required = True, widget = forms.TextInput(attrs={'style': 'width: 250px; height: 50px;', 'placeholder': 'Name' }))

    email = forms.EmailField(max_length = 200, required = True, widget = forms.EmailInput(attrs={'style': 'width: 250px; height: 50px;', 'placeholder': 'Email' }) )

    message = forms.CharField(max_length=1500, required = False, widget = forms.Textarea(attrs={'style': 'width: 300px; height: 200px;', 'placeholder': 'Message' }))

