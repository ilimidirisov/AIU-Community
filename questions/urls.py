from django.urls import path
from .views import QuestionList, FacultyList,AnswerList, UserProfileList, UserProfileDetail

urlpatterns = [
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('questions/<int:question_id>/answers/', AnswerList.as_view(), name='question-list'),


    # path('answers/', AnswerList.as_view(), name='answer-list'),
    path('faculties/', FacultyList.as_view(), name='faculty-list'),
    # Получить список всех профилей или создать новый
    path('user-profiles/', UserProfileList.as_view(), name='user-profile-list'),
    
    # Получить, обновить или удалить конкретный профиль по ID
    path('user-profiles/<int:id>/', UserProfileDetail.as_view(), name='user-profile-detail'),
]
