from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Exam,Question
from results.models import Result



def exam_list(request):
    exams=Exam.objects.all()
    data=[]

    for exam in exams:
        data.append({
            "id":exam.id,
            "title":exam.title
        })
    return JsonResponse({"exams":data})

def question_list(request,exam_id):
    questions=Question.objects.filter(exam=exam_id)
    data=[]

    for q in questions:
        data.append({
            "question":q.question_text,
            "options":{
                "A":q.option_a,
                "B":q.option_b,
                "C":q.option_c,
                "D":q.option_d
            }
        })
    return JsonResponse({"questions":data})



@login_required
def take_exam(request,exam_id):
    questions=Question.objects.filter(exam_id=exam_id)

    if request.method=="POST":
        score=0
        for q in questions:
            selected=request.POST.get(f"q{q.id}")
            if selected == q.correct_option:
                score+=1

        Result.objects.create(
            student=request.user.student,
            exam_id=exam_id,
            score=score
        )
        return redirect('student_result',request.user.student.id)
    return render(request,"exams/take_exam.html",{"questions":questions})


