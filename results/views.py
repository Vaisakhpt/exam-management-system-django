from django.http import JsonResponse
from .models import Result

def student_result(request,student_id):
    results=Result.objects.filter(student_id=student_id)

    if not results.exists():
        return JsonResponse(
            {"status":"error","message":"No results found for this students"},status=404
        )

    data=[]
    for result in results:
        data.append({
            "student":result.student.user.username,
            "exam":result.exam.title,
            "score":result.score,
            "total_marks":result.exam.total_marks
        })
    return JsonResponse(
        {"status":"success","results":data},status=200
    )
