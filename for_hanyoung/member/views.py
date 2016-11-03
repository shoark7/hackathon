from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib import messages
from member.models import MyUser
from django.contrib.auth import login as auth_login , authenticate as auth_authenticate,\
    logout as auth_logout

# Create your views here.
def signup(request):
    context = {}
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            phonenumber = form.cleaned_data['phonenumber']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            full_name = form.cleaned_data['full_name']
            image = form.cleaned_data['image']
            is_hanyoung = form.cleaned_data.get('is_hanyoung', False)
            is_wps = form.cleaned_data.get('is_wps', False)
            github_address = form.cleaned_data['github_address']

            if password1 == password2 and 'github' in github_address:
                user = MyUser.objects.create_user(
                    username=username,
                    password=password1,
                    full_name=full_name,
                    image=image,
                    is_hanyoung=is_hanyoung,
                    is_wps=is_wps,
                    phonenumber=phonenumber,
                    github_address=github_address,
                )
                message = messages.success(request, '성공적으로 가입되었습니다.')
                return redirect('wps:wps_list')
            elif password1 != password2:
                message = messages.warning(request, '입력하신 비밀번호가 다릅니다.')

            elif 'github' not in github_address:
                message = messages.warning(request, '입력하신 주소는 깃허브 주소가 아닙니다.')
        else:
            message = '적절하지 않은 입력입니다.'
            context['form'] = form
            context['message'] = message

    else:
        form = SignupForm()
        context['form'] = form
    return render(request, 'member/signup.html', context)


def login(request):
    next = request.GET.get('next')
    context = {'username':'', 'password':''}
    if request.method == 'POST':
        try:
            username = request.POST['username']
            print('Username is ' + username)
            password = request.POST['password']
            # if username is None or password is None:
            #     raise KeyError
        except KeyError:
            return HttpResponse('아이디와 비밀번호는 필수 입력사항입니다.')
        else:
            user = auth_authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, '로그인에 성공했습니다.')
                return redirect(next)
            else:
                messages.error(request, '로그인에 실패했습니다.')
                context.update({'username': username, 'password': password})
                return render(request, 'member/login.html', context)
    else:
        return render(request, 'member/login.html', context)

def logout(request):
    next = request.GET.get('next')
    auth_logout(request)
    return redirect(next)

