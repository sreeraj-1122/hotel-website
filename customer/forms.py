from django import forms

from .models import roombooking,contact

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=roombooking
        fields='__all__'

        widgets={
            'check_in' : DateInput(),'check_out':DateInput(),
            
        }
        labels={
            'name': "Name: ",
            'email': "Email: ",
            'phone': "Phone Number: ",
            'check_in': "Check In : ",
            'check_out': "Check Out: ",
            'room': "Room Name: ",
            'adults': "Adults: ",
            'childs': "Childrens: ",
            'request': "Special request: ",
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'
