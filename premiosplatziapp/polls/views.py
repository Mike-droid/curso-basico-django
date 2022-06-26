from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        # * La variable ahora está disponible en index.html
        "latest_question_list": latest_question_list
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {
        "question": question
    })


def results(request, question_id):
    return HttpResponse(f'You are watching the results from the question # {question_id}')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "¡No elegiste una respuesta! 😕"
        })
    else:  # * Si todo salió bien entonces haz este bloque
        selected_choice.votes += 1
        selected_choice.save()
        # ! Es buena práctica hacer redirect después de que el usuario usó un formulario
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
