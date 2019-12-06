from django.shortcuts import render, redirect
from .forms import *
from .models import *


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['teamId'] = form.cleaned_data['teamId']
            teamId = request.session['teamId']
            allQuestion = QuestionQuiz.objects.all()[:30]
            response = render(request, 'quiz.html', {'teamId': teamId, 'allQuestion': allQuestion})
            response.set_cookie('teamId', form.cleaned_data['teamId'])
            return response
    else:
        print("HI")
        form = RegistrationForm()
        return render(request, "registration.html", {'form': form})


def quiz(request):
    if request.method == 'POST':
        if request.COOKIES['teamId'] == request.session['teamId']:
            #teamId = request.COOKIES['teamId']
            allQuestion = QuestionQuiz.objects.all()[:28]
            return render(request, 'result.html', {"allQuestion": allQuestion, 'teamId': teamId})
        else:
            form = RegistrationForm()
            return render(request, 'registration.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})


def result(request):
    if request.method == 'POST':
        if request.COOKIES['teamId'] == request.session['teamId']:


            team = request.POST.get('teamId')
            A1 = request.POST.get('A1')
            A2 = request.POST.get('A2')
            A3 = request.POST.get('A3')
            A4 = request.POST.get('A4')
            A5 = request.POST.get('A5')
            A6 = request.POST.get('A6')
            A7 = request.POST.get('A7')
            A8 = request.POST.get('A8')
            A9 = request.POST.get('A9')
            A10 = request.POST.get('A10')
            A11 = request.POST.get('A11')
            A12 = request.POST.get('A12')
            A13 = request.POST.get('A13')
            A14 = request.POST.get('A14')
            A15 = request.POST.get('A15')
            A16 = request.POST.get('A16')
            A17 = request.POST.get('A17')
            A18 = request.POST.get('A18')
            A19 = request.POST.get('A19')
            A20 = request.POST.get('A20')
            A21 = request.POST.get('A21')
            A22 = request.POST.get('A22')
            A23 = request.POST.get('A23')
            A24 = request.POST.get('A24')
            A25 = request.POST.get('A25')
            A26 = request.POST.get('A26')
            A27 = request.POST.get('A27')
            A28 = request.POST.get('A28')
            A29 = request.POST.get('A29')
            A30 = request.POST.get('A30')
            ans = Answer(team=team, A1=A1, A2=A2, A3=A3, A4=A4, A5=A5,
                                  A6=A6, A7=A7, A8=A8, A9=A9, A10=A10,
                                  A11=A11, A12=A12, A13=A13, A14=A14, A15=A15,
                                  A16=A16, A17=A17, A18=A18, A19=A19, A20=A20,
                                  A21=A21, A22=A22, A23=A23, A24=A24, A25=A25,
                                  A26=A26, A27=A27, A28=A28, A29=A29, A30=A30)
            # ans = Answer(team=team, A1=A1)
            ans.save()
            return render(request, 'result.html')
