import datetime
import random
from django.shortcuts import render
from apis.youtube import search
from reward.models import Reward


__all__ = [
    'reward_main',
]


def reward_main(request):
    context = {}
    rewards = Reward.objects.all()
    start_day = datetime.datetime(2016, 9, 26)
    today = datetime.datetime.today()
    finish_day = datetime.datetime(2016, 12, 9)

    today_start_time = datetime.datetime.combine(today.date(), datetime.time(13, 0, 0))
    today_finish_time = datetime.datetime.combine(today.date(), datetime.time(18, 0, 0))


    current_time = round((today - start_day) / (finish_day - start_day) * 100, 4)
    current_time2 = round((today - today_start_time) / (today_finish_time - today_start_time) * 100, 4)

    context['current_time'] = current_time
    context['current_time2'] = current_time2

    context['rewards'] = rewards

    return render(request, 'reward/reward_main.html', context)
