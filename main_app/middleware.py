from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

class LoginCheckMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user

        if user.is_authenticated:
            if user.user_type == "1": # Admin
                if modulename == "main_app.staff_views" or modulename == "main_app.student_views" or modulename == "main_app.EditResultView":
                    return redirect(reverse('admin_home'))
            
            elif user.user_type == "2": # Staff
                if modulename == "main_app.hod_views" or modulename == "main_app.student_views":
                    return redirect(reverse('staff_home'))
            
            elif user.user_type == "3": # Student
                if modulename == "main_app.hod_views" or modulename == "main_app.staff_views" or modulename == "main_app.EditResultView":
                    return redirect(reverse('student_home'))
            
            else:
                return redirect(reverse('login_page'))

        else:
            # Not authenticated
            allowed_modules = ["main_app.views", "django.contrib.auth.views", "django.contrib.admin.sites"]
            allowed_paths = [reverse('login_page'), reverse('user_login'), reverse('showFirebaseJS')]

            if modulename in allowed_modules or request.path in allowed_paths:
                pass
            else:
                return redirect(reverse('login_page'))
