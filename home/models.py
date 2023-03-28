from django.db import models

# Create your models here.
class departments(models.Model):
    dept_name=models.CharField(max_length=100)
   
    dept_descriptions=models.TextField()
    img=models.ImageField(upload_to='departments')
    def __str__(self):

        return '{}'.format(self.dept_name)
    
class doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=100)
    dept_name=models.ForeignKey(departments,on_delete=models.CASCADE)
    doc_img=models.ImageField(upload_to='doctors')
    def __str__(self):

        return self.doc_name + ' -'+ self.doc_spec
        

class appoinment(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=100)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
    def __str__(self):

        return '{}'.format(self.p_name)
