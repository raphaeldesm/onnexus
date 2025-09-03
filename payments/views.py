from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course

@login_required
def payment_page(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    context = {
        'course': course
    }
    return render(request, 'payments/payment.html', context)
