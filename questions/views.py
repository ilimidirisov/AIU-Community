

# Create your views here.
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Question, Answer, Faculty, UserProfile
from .serializers import QuestionSerializer, AnswerSerializer, FacultySerializer, UserProfileSerializer
#APIView, #ListAPIView, CreateAPIView, DeleteAPIView

class QuestionList(generics.ListCreateAPIView):
    """
    Get the list of all questions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    

# class AnswerList(generics.ListAPIView):
#     """
#     Get the list of all answers.
#     """
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer


class FacultyList(generics.ListAPIView):
    """
    Get the list of all faculties.
    """
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class AnswerList(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, question_id):
        """
        Get the list of answers for a specific question.
        """
        try:
            question = Question.objects.get(id=question_id)  # Fetch the question by its ID
        except Question.DoesNotExist:
            return Response({"detail": "Question not found."}, status=status.HTTP_404_NOT_FOUND)

        answers = question.answers.all()  # Access the related answers
        serializer = AnswerSerializer(answers, many=True)  # Serialize the answers
        return Response(serializer.data)  # Return serialized answers

    def post(self, request, question_id):
        """
        Post a new answer for a specific question.
        """
        try:
            question = Question.objects.get(id=question_id)  # Fetch the question
        except Question.DoesNotExist:
            return Response({"detail": "Question not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AnswerSerializer(data=request.data)  # Deserialize the incoming data
        if serializer.is_valid():
            serializer.save(question_id=question)  # Save the answer linked to the question
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created answer data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors if any
    
class UserProfileList(generics.ListCreateAPIView):
    """
    Список всех профилей пользователей или создание нового профиля.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Получение, обновление или удаление профиля пользователя по ID.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'  # Идентификация профиля по его 