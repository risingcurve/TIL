from tracemalloc import get_object_traceback
from django.db.models import Q, Count
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from .forms import QuestionForm, CommentForm

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pk')
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save()
            return redirect('eithers:detail', question.pk)
    else:
        question_form = QuestionForm()
    context = {
        'question_form': question_form,
    }
    return render(request, 'eithers/create.html', context)


def detail(request, question_pk):
    # 질문
    comment_form = CommentForm()
    total_count = Count('comment') # Count는 import해야 함.
    count_a = Count('comment', filter=Q(comment__pick=0)) # 값
    count_b = Count('comment', filter=Q(comment__pick=1)) # 값
    
    result = Question.objects.annotate(
                    total_count = total_count,
                    count_a = count_a,
                    count_b = count_b,
            )

    question = get_object_or_404(result, pk=question_pk)
    comments = question.comment_set.order_by('-pk')

    a_per = round(question.count_a / question.total_count * 100, 2)
    b_per = round(question.count_b / question.total_count * 100, 2)
    # a_per = round(question.count_a / question.total_count * 100, 2) if question.total_count != 0:
    # b_per = round(question.count_b / question.total_count * 100, 2) if question.total_count != 0:

    context = {
        'question': question,
        'comments': comments,
        'comment_form': comment_form,
        'a_per': a_per,
        'b_per': b_per,
    }
    return render(request, 'eithers/detail.html', context)


def comments_create(request, question_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question_id = question_pk
        comment.save()
    return redirect('eithers:detail', question_pk)


# def random(request):
#     pass
    
#     context = {
#         'question': question, 
#         'comments': comments,
#         'comment_form': comment_form,
#         'a_per': a_per, 
#         'b_per': b_per,
#     }

#     return render(request, 'eithers/detail.html', context)
