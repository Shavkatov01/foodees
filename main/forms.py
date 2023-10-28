from django import forms


class ContactForm(forms.Form):
    


    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.Textarea()
    # ceremony = forms.ChoiceField(CEREMONY)