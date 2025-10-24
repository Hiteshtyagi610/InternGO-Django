from django.shortcuts import render

def detail(request):
    return render(request, 'internships/detail.html')

def list(request):
    return render(request, 'internships/list.html')

def post(request):
    return render(request, 'internships/post.html')

def internship_list(request):
    return render(request, 'internships/internship_list.html')

