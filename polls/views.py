from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice

# get questions
def index(request):
    context = {
        'questions': Question.objects.order_by('-pub_date')[:5]
    }
    return render(request, 'polls/index.html', context)

# show question details for vote
def detail(request, question_id):
    try:
        context = {
            'question': Question.objects.get(pk=question_id)
        }
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', context)

# show vote results
def results(request, question_id):
    context = {
        'question': get_object_or_404(Question, pk=question_id)
    }
    return render(request, 'polls/results.html', context)

# submit vote
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You did not select a choice'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results_data(request, question_id):
    vote_data = []
    question = Question.objects.get(pk=question_id)
    votes = question.choice_set.all()

    for i in votes:
        vote_data.append({i.choice_text:i.votes})
    print(vote_data)
    return JsonResponse(vote_data, safe=False)


