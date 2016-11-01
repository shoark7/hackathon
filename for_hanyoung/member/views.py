from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib import messages
from member.models import MyUser

# Create your views here.
def signup(request):
    context = {}
    message = ''
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
    return HttpResponse('hi')