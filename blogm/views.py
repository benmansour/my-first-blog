from django.shortcuts import render

def post_list(request):
    return render(request, 'blogm/post_list.html', {})
