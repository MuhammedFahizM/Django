# import datetime

# class LogMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # This runs before the view
#         print(f"🕒 Request for {request.path} at {datetime.datetime.now()}")

#         # Call the view
#         response = self.get_response(request)

#         # This runs after the view
#         print(f"✅ Response sent for {request.path}\n")
#         return response

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from middleware_app import views
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the request is for the login or logout views
        if request.path == '/login/':
            # Handle login logic
            print("Login Request")
            # You can perform any additional actions related to login here
            
        elif request.path == '/logout/':
            # Handle logout logic
            print("Logout Request")
            # You can perform any additional actions related to logout here
        elif request.path == '/admin/' :
            print("Admin")
        elif request.user.is_authenticated:
            role = request.user.role
            print(role)
            if role == 'teacher' and not request.path.startswith('/teacher_home'):
                return redirect('teacher_home')
            elif role == 'student' and not request.path.startswith('/student_home'):
                return redirect('student_home')
            elif role == 'principal' and not request.path.startswith('/principal_home'):
                return redirect('principal_home')

        # Continue processing the request
