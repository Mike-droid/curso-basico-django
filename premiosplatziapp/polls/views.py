from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        # * La variable ahora está disponible en index.html
        "latest_question_list": latest_question_list
    })


def detail(request, question_id):
    return HttpResponse(f'You are watching the question # {question_id}')


def results(request, question_id):
    return HttpResponse(f'You are watching the results from the question # {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting to the question # {question_id}')
