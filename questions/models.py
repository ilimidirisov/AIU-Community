from django.db import models

# Create your models here.


class Faculty(models.Model): 
    college_uni = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=50)
    question_text = models.TextField()
    faculty_id = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    user_id = 1
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    

class Answer(models.Model):
    answer_text = models.TextField()
    question_id = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    user_id = 1
    likes = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Answer to {self.question_id.name}"


from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=50)  # User's name
    email = models.EmailField(unique=True)  # Unique email
    bio = models.TextField(blank=True, null=True)  # Optional bio
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True, related_name='users')  # Faculty association
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Profile photo
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)  # Resume in PDF
    github_link = models.URLField(blank=True, null=True)  # GitHub profile link
    linkedin_link = models.URLField(blank=True, null=True)  # LinkedIn profile link
    created_at = models.DateTimeField(auto_now_add=True)  # Record creation timestamp

    def __str__(self) -> str:
        return self.name

