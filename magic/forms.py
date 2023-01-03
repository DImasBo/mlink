from django import forms

from magic.models import MagicURL


class MagicURLCreateForm(forms.ModelForm):
    origin_url = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Shorten your link'}))

    class Meta:
        model = MagicURL
        fields = ('origin_url',)
