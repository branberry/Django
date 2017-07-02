from django.db import models

# Create your models here.
class Question(models.Model):
    questionText = models.CharField(max_length=200)
    pubDate = models.DateTimeField('Date Published')

class Choice(models.Model):
    # ForeignKey represents the connection between the two classes
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

