from django.shortcuts import render
from .models.course import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {"data_courses": courses})


def course_detail(request):
    course = {
        "course_title": "Django Aplicaciones",
        "course_links": "course_lessons",
        "course_image": "images/curso_2.jpg",
        "info_course": {
            "lessons": 79,
            "duration": 8,
            "instructor": "Ricardo C"
        },
        "course_content": [
            {
                "id": 1,
                'name': "Introducción al curso",
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
            }
        ]
    }
    return render(request, 'courses/course_detail.html', {"data_course": course})


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
