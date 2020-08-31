from django.contrib import admin

# Register your models here.
from .models import Courses,Batches, Students, Payments

admin.site.register(Courses)
admin.site.register(Batches)
admin.site.register(Students)
admin.site.register(Payments)
