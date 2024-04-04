from django.db import models

# Aadhar Model creat
class Aadhar(models.Model):
    aadhar=models.IntegerField()
    def __str__(self):
        return str(self.aadhar)

class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_email = models.CharField(max_length=100)
    stu_contact = models.CharField(max_length=200)
    aadhar= models.OneToOneField(Aadhar,on_delete=models.CASCADE)
    def __str__(self):
        return self.stu_name