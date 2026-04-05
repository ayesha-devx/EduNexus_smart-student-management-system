import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from main_app.models import CustomUser

email = 'admin@admin.com'
password = 'admin' # You can change this to anything more secure later!

if not CustomUser.objects.filter(email=email).exists():
    print("Creating EduNexus superuser...")
    # Creating with user_type=1 (Admin/HOD role)
    # Using Django's core create_superuser which handles all required fields.
    from django.contrib.auth import get_user_model
    User = get_user_model()
    User.objects.create_superuser(email=email, password=password, user_type="1")
    print("Superuser created successfully!")
else:
    print("Superuser already exists.")
