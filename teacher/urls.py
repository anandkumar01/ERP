from django.urls import path,re_path,include
from . import views

app_name='teacher'

urlpatterns = [
    path('homepage/', views.index, name='index'),
    path('logout/',views.logout,name='logout'),
    path('login/',views.login,name='login'),
    path('timetable/',views.timetable,name="timetable"),
	path('attendance/',include('attendance.urls')),
    re_path(r'^$',views.index,name="index"),
    path("subject/",views.subject,name="subject"),
	path("coordinator/login/",views.coordinatorlogin,name="coordinator"),
    path('about/',views.about,name="about"),
    path('your-timetable/',views.teachertimetable,name="teacher_timetable"),
    path('forget/',views.forget,name='forget'),
    path('mail/',views.forgot_mail),
    path('marks/',views.marks,name="marks"),
    path('marks-studentlist',views.studentlist),
    path('mark-marks',views.mark_marks),
]
