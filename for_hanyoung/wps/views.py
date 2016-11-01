from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from apis import sms
from member.models import MyUser
from django.conf import settings
# from members import MyUser
# Create your views here.
from django.contrib import messages

def wps_index(request):
    return render(request, 'root/index.html', {})

def wps_list(request):
    context = {}
    all_wps = MyUser.objects.all()
    if request.method == 'POST':
        message = request.POST.get('message')
        if message == '':
            message = '더 조는 것을 과시하지 않겠습니다.'
        # 추후 모두의 번호를 사용하도록 해야 됨.

        all_wps_phonenumbers = ','.join([wps.phonenumber for wps in all_wps])
        sms.send_sms(all_wps_phonenumbers, message)


        sms.send_sms('01024956962', message)
    context['all_wps'] = all_wps

    return render(request, 'wps/wps_list.html', context)



def wps_detail(request, student_id):
    one_wps = get_object_or_404(MyUser, id=student_id)
    if request.method == 'POST':
        message = request.POST['message']
        if not message:
            message = '졸지 마세요.'

        phonenumber = request.POST['phonenumber']
        sms.send_sms(phonenumber, message)
        messages.success(request, '성공적으로 문자가 발송되었습니다.')
        return redirect('wps:wps_detail', student_id)

    else:
        pass

    return render(request, 'wps/wps_detail.html', {'one_wps': one_wps})



