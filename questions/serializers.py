from rest_framework import serializers
from .models import Question, Answer, Faculty, UserProfile

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'name', 'question_text', 'created_at', 'faculty_id', 'user_id']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'question_id', 'created_at', 'likes', 'user_id']

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__' 

class UserProfileSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(read_only=True)  
    
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'bio', 'faculty', 'profile_picture', 'resume', 'github_link', 'linkedin_link', 'created_at']
