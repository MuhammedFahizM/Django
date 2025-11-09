from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def home(request):
    return render(request,'logout.html')

def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request,username = uname,password = pwd)

    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        return render(request,"login.html")


def logoutview(request):
    logout(request)
    return redirect('login')


def sign_up(request):
    uform = UserCreationForm(request.POST)
    if request.method == "POST":
        if uform.is_valid():
            uname = uform.cleaned_data.get('username')
            pwd = uform.cleaned_data.get('password1')
            email = uform.cleaned_data.get('email')
            user1 = User.objects.create_user(username=uname,password=pwd,email=email)
            user1.save()
            user = authenticate(request,username = uname,password = pwd)
            login(request,user)
            return redirect('login')
    else:
        uform = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form' : uform})
            
def reset(request):
    return render(request,"registration/ResetPassword.html")

def resetPassword(request):
    print("reset view is called")
    responseDic = {}
    try:
        usern = request.POST['uname']
        reciepient = request.POST['email']
        pwd = request.POST['password']

        # subject = "Password reset"

        try:
            user = User.objects.get(username=usern)
            if user is not None:
                user.set_password(pwd)
                user.save()

                #send_mail (subject,messssage,email_host_user,[reciepient])
                responseDic["errmsg"] = "Password reset successfully"
                return render(request,"registration/ResetPassword.html",responseDic)
        except Exception as  e:
            print(e)
            responseDic['errmsg'] = "Email does not exist"
            return render(request,"registration/ResetPassword.html",responseDic)
    except Exception as e:
        print(e)
        responseDic['errmsg'] = "Failed to reset password"
        return render(request,"registration/ResetPassword.html",responseDic)









