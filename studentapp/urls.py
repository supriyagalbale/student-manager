from django.urls import path, include
from .views import *

urlpatterns=[

    path('',Home, name='home'),
    path('aboutus', AboutUs, name= 'about' ),
    path('course/courselist', CourseListPdf),
    path('payment/receipt/<int:code>', ReceiptPdf),

    path('students', StudentList.as_view(), name='students'),
    path('students/<int:admno>', StudentDetail, name='student_detail'),
    path('students/create', AddStudents.as_view(), name='add_students'),
    path('students/<int:pk>/update', UpdateStudentDetails.as_view(), name='update_student_details'),
    path('students/<int:pk>/delete', DeleteStudentDetails.as_view(), name='delete_student_details'),

    path('batch', BatchList.as_view(), name='batches'),
    path('batch/create', AddBatch.as_view(), name='add_batch'),
    path('batch/<int:batchcode>', BatchDetail, name='batch_detail'),
    path('batch/<int:pk>/update', UpdateBatchDetail.as_view(), name='update_batch_details'),
    path('batch/<int:pk>/delete', DeleteBatchDetails.as_view(), name='delete_batch_details'),

    path('course', CourseList.as_view(), name='courses'),
    path('course/create', AddCourse.as_view(), name='add_course'),
    path('course/<int:ccode>', CourseDetail, name='course_detail'),
    path('course/<int:pk>/update', UpdateCourseDetail.as_view(), name='update_course_details'),
    path('course/<int:pk>/delete', DeleteCourseDetails.as_view(), name='delete_course_details'),
    path('courses/create', courses_create, name='courses_create'),

    path('payment', PaymentList.as_view(), name='payments'),
    path('payment/create', AddPayment.as_view(), name='add_payment'),
    path('payment/<int:code>', PaymentDetail, name='payment_detail'),
    path('payment/<int:pk>/update', UpdatePaymentDetail.as_view(), name='update_payment_details'),
    path('payment/<int:pk>/delete', DeletePaymentDetails.as_view(), name='delete_payment_details'),



]