from django.shortcuts import render
from django.views import generic
from .models import Students
from .models import Batches
from .models import Courses
from .models import Payments
from django.urls import  reverse_lazy
from django.views.generic.edit import  CreateView
from django.views.generic.edit import  UpdateView
from django.views.generic.edit import  DeleteView
from django.http import HttpResponse
from django_xhtml2pdf.utils import generate_pdf
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CourseAdd, CoursesForm


# Create your views here.
def Home(request):
    return render(request, 'home.html', None)

def AboutUs (request):
    pass

def CourseListPdf(request):
    #add user authentication
    if request.user.is_authenticated:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Deposition'] = 'attachment; filename="output.pdf"'
        context = {'course': Courses.objects.all()}
        result = generate_pdf('course_pdf.html', file_object=response, context=context)
        return result
    else:
        return HttpResponse("Please Login to access the reports")

def ReceiptPdf(request, code):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Deposition'] = 'attachment; filename="output.pdf"'
    context = {'payment': Payments.objects.get(pk=code)}
    result = generate_pdf('payment_detail.html', file_object=response, context=context)
    return result


class StudentList(LoginRequiredMixin, generic.ListView):                #LoginRequiredMixins help to authenticate the page (in order to use this include a library)
    model= Students
    context_object_name = 'students'
    queryset = Students.objects.all()
    template_name = 'student_list.html'

@login_required
def StudentDetail(request, admno):
    student = Students.objects.get(pk=admno)
    context = {'student': student}
    return render(request, 'student_detail.html', context)

class AddStudents(CreateView):
    model = Students
    fields = '__all__'
    template_name = 'student_form.html'
    success_url = reverse_lazy('students')

class UpdateStudentDetails(UpdateView):
    model = Students
    fields = '__all__'
    template_name = 'student_form.html'
    success_url = reverse_lazy('home')

class DeleteStudentDetails(DeleteView):
    model = Batches
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('students')


class BatchList(generic.ListView):
    model = Batches
    context_object_name = 'batches'
    queryset = Batches.objects.all()
    template_name = 'batch_list.html'

class AddBatch(CreateView):
    model = Batches
    fields = '__all__'
    template_name = 'batch_form.html'
    success_url = reverse_lazy('batches')

@login_required
def BatchDetail(request, batchcode):                              #functions can be authenticated using decorator anter including a library on top
    batch = Batches.objects.get(pk=batchcode)
    context = {'batch': batch}
    return render(request, 'batch_detail.html', context)

class UpdateBatchDetail(UpdateView):
    model = Batches
    fields = '__all__'
    template_name = 'batch_form.html'
    success_url = reverse_lazy('batches')

class DeleteBatchDetails(DeleteView):
    model = Batches
    template_name = 'batch_confirm_delete.html'
    success_url = reverse_lazy('batches')


class CourseList(generic.ListView):
    model = Courses
    context_object_name = 'courses'
    queryset = Courses.objects.all()
    template_name = 'course_list.html'

class AddCourse(CreateView):
    model = Courses
    fields = '__all__'
    template_name = 'course_form.html'
    success_url = reverse_lazy('courses')

def CourseDetail(request, ccode):
    course = Courses.objects.get(pk=ccode)
    context = {'course': course}
    return render(request, 'course_detail.html', context)

class UpdateCourseDetail(UpdateView):
    model = Courses
    fields = '__all__'
    template_name = 'course_form.html'
    success_url = reverse_lazy('courses')

class DeleteCourseDetails(DeleteView):
    model = Courses
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('courses')

@login_required
def courses_create(request):                                                       #firstly GET method is called to load the form which will be done by
                                                                                    #else block
    if request.method =="POST":
        courses_form = CoursesForm(data=request.POST)
        if courses_form.is_valid():
            courses = courses_form.save()
            return render(request, "course_list.html")
    else:
        courses_form = CoursesForm()
        return render(request, "course_form.html",{"form":courses_form})





class PaymentList(generic.ListView):
    model = Payments
    context_object_name = 'payments'
    queryset = Payments.objects.all()
    template_name = 'payment_list.html'

class AddPayment(CreateView):
    model = Payments
    fields = '__all__'
    template_name = 'payment_form.html'
    success_url = reverse_lazy('payments')

def PaymentDetail(request, code):
    payment = Payments.objects.get(rpctno=code)
    context = {'payment': payment}
    return render(request, 'payment_detail.html', context)

class UpdatePaymentDetail(UpdateView):
    model = Payments
    fields = '__all__'
    template_name = 'payment_form.html'
    success_url = reverse_lazy('payments')

class DeletePaymentDetails(DeleteView):
    model = Payments
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('payments')






