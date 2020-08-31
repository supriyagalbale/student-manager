from django.db import models
from django.urls import reverse
import uuid


# Create your models here.

class Courses(models.Model):
    ccode = models.IntegerField(primary_key=True, help_text="Enter Course Code")
    cname = models.CharField(max_length=20, help_text="Enter Course Name")
    coursefee = models.IntegerField(help_text="Enter Course Fees")
    duration = models.CharField(max_length=4)
    prereq = models.CharField(max_length=100)

    def __str__(self):
        return str(self.ccode)

    def get_absolute_url(self):
        return reverse('course-detail', args=[str(self.ccode)])


class Batches(models.Model):
    batchcode = models.IntegerField(primary_key=True, help_text="Enter Batch Code")
    ccode = models.ForeignKey('Courses', on_delete=models.SET_NULL, null=True)
    stdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    timings = models.CharField(max_length=8, help_text="Enter Timings")

    def __str__(self):
        return str(self.batchcode)

    def get_absolute_url(self):
        return reverse('batche-detail', args=[str(self.batchcode)])


class Students(models.Model):
    admno = models.IntegerField(primary_key=True, default=uuid.uuid4, help_text="Unique Student ID")
    batchcode = models.ForeignKey('Batches', on_delete=models.SET_NULL, null=True)
    rollno = models.IntegerField(help_text="Enter Roll Number")
    fullname = models.CharField(max_length=50, help_text="Enter Full Name")
    fathername = models.CharField(max_length=50, help_text="Enter Fathers Name")
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=12, help_text="Enter Contact no")
    dj = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.admno)

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.admno)])


class Payments(models.Model):
    rpctno = models.IntegerField(primary_key=True, help_text="Enter Receipt Number")
    amdno = models.ForeignKey('Students', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(help_text="Enter Amount")
    paydate = models.DateField()
    remarks = models.CharField(max_length=200, help_text="Enter Remarks")

    def __str__(self):
        return str(self.rpctno)

    def get_absolute_url(self):
        return reverse('payment-details', args=[str(self.id)])



