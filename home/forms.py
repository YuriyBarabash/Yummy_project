from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) < 3:
    #         raise forms.ValidationError('Name is too short')
    #     return name

    class Meta:
        model = Reservation
        fields = ('name', 'phone', 'email', 'date', 'time', 'people_number', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone', 'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'data-rule': 'email', 'data-msg': 'Please enter a valid email'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date', 'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Time', 'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}),
            'people_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '# of people', 'data-rule': 'minlen:1', 'data-msg': 'Please enter at least 1 chars'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }



