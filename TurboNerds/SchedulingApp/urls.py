from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', views.Logins.logout_user, name='logout'),

    path('home/', views.HomeViews.home, name='home'),
    path('', views.HomeViews.home, name='home'),
    path('<str:email>', views.HomeViews.otherhome, name='otherhome'),

    path('register/', views.ProfileModification.register, name='register'),
    path('edit_information/<str:email>', views.ProfileModification.edit_profile, name='edit_profile'),
    path('course_information/', views.CourseInformation.course_assignment, name='course_assignment'),
    path('user_information/', views.CourseInformation.read_information, name='user_information'),

    path('assign_ta/<str:course>/<str:lab>', views.CourseInformation.assign_Tas, name='assign_ta'),
    path('assign_instructor/<str:course>', views.CourseInformation.assign_instructor, name='assign_instructor'),

    path('delete_user/<str:email>', views.ProfileModification.delete_user, name='delete_user'),
    path('delete_course/<str:course>', views.CourseInformation.delete_course, name='delete_course'),
    path('delete_lab/<str:lab>', views.CourseInformation.delete_lab, name='delete_lab'),
    path('delete_section/<str:section>', views.CourseInformation.delete_section, name='delete_section'),

    # path('course_creation/', views.CourseInformation.course_creation, name='course_creation'),
    # path('lab_creation/', views.CourseInformation.lab_creation, name='lab_creation'),
    # path('section_creation/', views.CourseInformation.section_creation, name='section_creation')
]
