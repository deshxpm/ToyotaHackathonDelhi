from django.db import models


class Profile(models.Model):
    schoolName = models.CharField(max_length=500, blank=False, null=False,)
    teamName   = models.CharField(max_length=200, blank=False, null=False)
    emailT1 = models.EmailField()
    emailT2 = models.EmailField()
    contactT1 = models.CharField(max_length=20)
    contactT2 = models.CharField(max_length=20)
    nameT1 = models.CharField(max_length=50, blank=False, null=False)
    nameT2 = models.CharField(max_length=50, blank=False, null=False)
    teamId = models.CharField(max_length=20)
    nameTeacher = models.CharField(max_length=20)
    emailTeacher = models.EmailField()
    contactTeacher = models.CharField(max_length=20)
    schoolAddress = models.TextField( )


class Question(models.Model):
    # qId = models.AutoField(primary_key=True)
    question = models.TextField( blank=False, null=False)
    A = models.CharField(max_length=1000, blank=False, null=False)
    B = models.CharField(max_length=1000, blank=False, null=False)
    C = models.CharField(max_length=1000, blank=False, null=False)
    D = models.CharField(max_length=1000, blank=False, null=False)
    # answer = models.CharField(max_length=1, blank=False, null=False)


class QuestionQuiz(models.Model):
    qId = models.AutoField(primary_key=True)
    question = models.TextField( blank=False, null=False)
    A = models.CharField(max_length=1000, blank=False, null=False)
    B = models.CharField(max_length=1000, blank=False, null=False)
    C = models.CharField(max_length=1000, blank=False, null=False)
    D = models.CharField(max_length=1000, blank=False, null=False)



class Answer(models.Model):
    team = models.CharField(max_length=20, blank=True, null=True)
    A1 = models.CharField(max_length=1, blank=True, null=True)
    A2 = models.CharField(max_length=1, blank=True, null=True)
    A3 = models.CharField(max_length=1, blank=True, null=True)
    A4 = models.CharField(max_length=1, blank=True, null=True)
    A5 = models.CharField(max_length=1, blank=True, null=True)
    A6 = models.CharField(max_length=1, blank=True, null=True)
    A7 = models.CharField(max_length=1, blank=True, null=True)
    A8 = models.CharField(max_length=1, blank=True, null=True)
    A9 = models.CharField(max_length=1, blank=True, null=True)
    A10 = models.CharField(max_length=1, blank=True, null=True)
    A11 = models.CharField(max_length=1, blank=True, null=True)
    A12 = models.CharField(max_length=1, blank=True, null=True)
    A13 = models.CharField(max_length=1, blank=True, null=True)
    A14 = models.CharField(max_length=1, blank=True, null=True)
    A15 = models.CharField(max_length=1, blank=True, null=True)
    A16 = models.CharField(max_length=1, blank=True, null=True)
    A17 = models.CharField(max_length=1, blank=True, null=True)
    A18 = models.CharField(max_length=1, blank=True, null=True)
    A19 = models.CharField(max_length=1, blank=True, null=True)
    A20 = models.CharField(max_length=1, blank=True, null=True)
    A21 = models.CharField(max_length=1, blank=True, null=True)
    A22 = models.CharField(max_length=1, blank=True, null=True)
    A23 = models.CharField(max_length=1, blank=True, null=True)
    A24 = models.CharField(max_length=1, blank=True, null=True)
    A25 = models.CharField(max_length=1, blank=True, null=True)
    A26 = models.CharField(max_length=1, blank=True, null=True)
    A27 = models.CharField(max_length=1, blank=True, null=True)
    A28 = models.CharField(max_length=1, blank=True, null=True)
    A29 = models.CharField(max_length=1, blank=True, null=True)
    A30 = models.CharField(max_length=1, blank=True, null=True)
