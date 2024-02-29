from django import forms



class PdfReceiver(forms.Form):
    data = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control  '}))

