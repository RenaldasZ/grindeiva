from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='subject', max_length=255, required=True)
    full_name = forms.CharField(label='full_name', max_length=255, required=True)
    email = forms.EmailField(label='email', required=True)
    question = forms.CharField(label='question', max_length=2000, required=True, widget=forms.Textarea)

    class Meta:
        fields = ('subject', 'full_name', 'email', 'question')
