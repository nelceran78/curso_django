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
    modules = couser.modules.prefetch_related('contents')
    return render(request, 'courses/course_detail.html', {
        "data_course": couser,
        "data_modules": modules})


def course_lessons(request):
    lesson = {
        "course_title": "Django Aplicaciones",
        "progress": 20,
        "course_content": [
            {
                "id": 1,
                'name': "Introducción al curso",
                "total_lessons": 6,
                "complete_lessons": 3,
                "lessons": [
                    {
                        "name": "Qué aprenderás en el curso",
                        "type": "video",
                    },
                    {
                        "name": "Cómo usar la plataforma",
                        "type": "article"
                    }
                ]
            },
            {
                "id": 2,
                'name': "Principios de Django",
                "total_lessons": 12,
                "complete_lessons": 0,
                "lessons": [
                    {
                        "name": "Introducción a Django",
                        "type": "video",
                    },
                    {
                        "name": "Instalar Django",
                        "type": "article"
                    }
                ]
            }
        ]
    }
    return render(request, 'courses/course_lessons.html', {"data_lesson": lesson})
