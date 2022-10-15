from django.urls import path
from . import views

app_name = "resume"

urlpatterns = [
    path('final/(?P<id>)w+)', views.show_user_info, name='final'),
    path('resume/(?P<id>)w+)',views.show_user,name='showresume'),
    path('useredit/(?P<id>)\w+)', views.userUpdate, name='edit'),
    path('userdelete/(?P<id>)\w+)', views.userDelete, name='delete'),
    path('deleted/(?P<id>)\w+)',views.deletedUser,name='deleted'),
    path('log',views.log,name='log'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('educationAdd/(?P<id>)\w+)', views.educationSave, name='educationAdd'),
    path('educationDelete/(?P<id>)\w+)/(?P<userID>)\w+)', views.educationDelete, name='educationDelete'),
    path('experienceAdd/(?P<id>)\w+', views.experienceSave, name='experienceAdd'),
    path('experienceDelete/(?P<id>)\w+)/(?P<userID>)\w+)', views.experienceDelete, name='experienceDelete'),
    path('courseAdd/(?P<id>)\w+', views.courseSave, name='courseAdd'),
    path('courseDelete/(?P<id>)\w+)/(?P<userID>)\w+)', views.courseDelete, name='courseDelete'),
    path('skillAdd/(?P<id>)\w+', views.skillSave, name='skillAdd'),
    path('skillDelete/(?P<id>)\w+)/(?P<userID>)\w+)', views.skillDelete, name='skillDelete'),
    path('aboutAdd/(?P<id>)\w+', views.aboutAdd, name='aboutAdd'),

]
