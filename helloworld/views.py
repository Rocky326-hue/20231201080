from django.shortcuts import render

def index(request):
    """个人信息页面视图"""
    # 学生信息
    student_info = {
        'name': '王斌',  # 姓名：王斌
        'student_id': '20231201080'  # 学号：20231201080
    }
    
    context = {
        'name': student_info['name'],
        'student_id': student_info['student_id']
    }
    
    return render(request, 'helloworld/index.html', context)