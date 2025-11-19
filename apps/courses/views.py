from django.shortcuts import render, get_object_or_404
from .models.course import Course
from django.db.models import Q
from django.core.paginator import Paginator


def course_list(request):
    courses = Course.objects.all()
    querry = request.GET.get('search_querry')
    if querry:
        courses = courses.filter(
            Q(title__icontains=querry) | Q(owner__first_name__icontains=querry)
        )

    paginator = Paginator(courses, 8)
    page_number = request.GET.get('page')
    courses_pag = paginator.get_page(page_number)

    querry_params = request.GET.copy()
    if "page" in querry_params:
        querry_params.pop("page")
    querry_string = querry_params.urlencode()

    return render(request, 'courses/courses.html', {
        "data_courses": courses_pag,
        "query": querry,
        "querry_string": querry_string
    })


def course_detail(request, slug):
    couser = get_object_or_404(Course, slug=slug)
    modules = couser.modules.prefetch_related('contents')  # type: ignore
    total_content = sum(module.contents.count() for module in modules)

    return render(request, 'courses/course_detail.html', {
        "data_course": couser,
        "data_modules": modules,
        "total_content": total_content
    })


def course_lessons(request, slug):
    course = get_object_or_404(Course, slug=slug)
    course_title = course.title
    moudeles = course.modules.prefetch_related('contents')  # type: ignore
    return render(request, 'courses/course_lessons.html', {
        "data_title": course_title,
        "data_modules": moudeles
    })
