from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def set_session(request):
    request.session['favorite_color'] = 'blue'
    return redirect('get_session')

def get_session(request):
    color = request.session.get('favorite_color','Not set')
    return render(request,'session.html', {'color' : color})

def delete_session(request):
    request.session.flush() # completly clesr an reset data for the current user
    return render(request,'session.html', {'color' : 'Session Deleted'})




def set_cookie(request):
    response = HttpResponse('Cookie is Set')
    response.set_cookie('user_name','Fahiz',max_age = 60*60*24*7) # 1 week
    return response

def get_cookie(request):
    user_name = request.COOKIES.get('user_name','Guest')
    return HttpResponse(f'Hello,{user_name}!')

def delete_cookie(request):
    response = HttpResponse('Cookie Deleted!')
    response.delete_cookie('user_name')
    return response
