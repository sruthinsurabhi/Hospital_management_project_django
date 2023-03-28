from django import forms
from .models import appoinment
class Date_input(forms.DateInput):
   input_type='date'

class BookingForm(forms.ModelForm):

    class Meta:
      
      model=appoinment
      fields='__all__'
      widgets={
         'booking_date': Date_input(),}
      labels={'p_name':'Patient Name',
              'p_phone':'Phone Number',
              'p_email':'E-mail',
              'doc_name':'Name of Doctor',
              'booking_date':'Booking Date'}
   
       
    
     


 