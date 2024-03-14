from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from django.http import HttpResponseNotAllowed
from .forms import QuestionForm,AnswerForm
# Create your views here.
def index(request):
    question_list=Question.objects.order_by('-create_date')
    context={'question_list': question_list}
    return render(request,'pybo/question_list.html',context)
    #render 함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    context={'question':question}
    return render(request,'pybo/question_detail.html',context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST': # "저장하기" 버튼을 클릭한 경우
        form = QuestionForm(request.POST)
        if form.is_valid(): #form이 유효한지를 검사
            question = form.save(commit=False) #form에 저장된 데이터로 Question 데이터를 저장하기 위한 코드 , commit=False는 임시 저장
            question.create_date = timezone.now() #form.save()를 수행하면 Question 모델의 create_date에 값이 없다는 오류가 발생할 것
            question.save()
            return redirect('pybo:index')
    else: # "질문 등록하기" 버튼을 클릭한 경우
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)