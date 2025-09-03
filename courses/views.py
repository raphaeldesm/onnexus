from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Content

def course_list(request):
    paid_courses = Course.objects.filter(is_buyable=True).select_related('instructor')
    free_courses = Course.objects.filter(is_buyable=False).select_related('instructor')
    context = {
        'paid_courses': paid_courses,
        'free_courses': free_courses,
    }
    return render(request, 'courses/course_list.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Course.objects.prefetch_related('modules__contents'), pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def content_detail(request, content_pk):
    content = get_object_or_404(Content, pk=content_pk)
    course = content.module.course

    # Lógica para navegação (Anterior/Próximo)
    all_contents = list(Content.objects.filter(module__course=course).order_by('module__order', 'order'))
    
    current_index = -1
    for i, item in enumerate(all_contents):
        if item.pk == content.pk:
            current_index = i
            break

    prev_content = all_contents[current_index - 1] if current_index > 0 else None
    next_content = all_contents[current_index + 1] if current_index < len(all_contents) - 1 else None

    context = {
        'course': course,
        'content': content,
        'prev_content': prev_content,
        'next_content': next_content,
    }
    return render(request, 'courses/course_content.html', context)