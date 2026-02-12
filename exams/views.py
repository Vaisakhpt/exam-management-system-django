from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Exam,Question
from results.models import Result


def calculate_score(questions,post_data):
    score=0
    for q in questions:
        selected=post_data.get(f"q{q.id}")
        if selected == q.correct_option:
            score+=1
        return score
    
def exam_list(request):
    exams=Exam.objects.all()

    if not exams.exists():
        return JsonResponse(
            {"status":"error","message":"No exams avaialable"},status=404
        )

    data=[]
    for exam in exams:
        data.append({
            "id":exam.id,
            "title":exam.title,
            "total_marks":exam.total_marks,
            "date":exam.date
        })
    return JsonResponse(
        {
            "status":"success",
            "count":exams.count(),
            "exams":data
        },
        status=200
    )

def question_list(request,exam_id):
    questions=Question.objects.filter(exam=exam_id)

    if not questions.exists():
        return JsonResponse(
            {"status":"error","message":"No questions found for this exam"},status=404
        )

    data=[]
    for q in questions:
        data.append({
            "id":q.id,
            "question":q.question_text,
            "options":{
                "A":q.option_a,
                "B":q.option_b,
                "C":q.option_c,
                "D":q.option_d
            }
        })
    return JsonResponse(
        {"status":"success","exam_id":exam_id,"questions":data},status=200
    )



@login_required
def take_exam(request,exam_id):
    questions=Question.objects.filter(exam_id=exam_id)

    if not questions.exists():
        return JsonResponse({"status":"error","message":"No questions available for this exam"},status=404
        )

    if Result.objects.filter(
        student=request.user.student,
        exam_id=exam_id).exists():
        return JsonResponse({"status":"error","message":"Exam already attempted"},status=400
        )    

    if request.method=="POST":
        score=calculate_score(questions,request.POST)

        Result.objects.create(
            student=request.user.student,
            exam_id=exam_id,
            score=score
        )
        return redirect('student_result',request.user.student.id)

    
    return render(request,"exams/take_exam.html",{"questions":questions})


