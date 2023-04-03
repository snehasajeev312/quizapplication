from django.urls import path
from quizapp import views
from django.views.generic import TemplateView
urlpatterns=[
    path("register",views.SignUpView.as_view(),name="signup"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("signout",views.signout_view,name="signout"),
    path("home",views.HomeView.as_view(),name="home"),
    path("subhome",views.HomeSubView.as_view(),name="home-frst"),
    path("quizes/home",views.QuizHomeView.as_view(),name="quiz-home"),
    path("questions/all/<str:cat>/<str:mode>/",views.QuestListView.as_view(),name="question-list"),
    path("quiz/record/",views.QuizRecordView.as_view(),name="quiz-record")
]