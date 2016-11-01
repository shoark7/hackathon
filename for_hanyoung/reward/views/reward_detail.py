import datetime
import random
from django.shortcuts import render
from apis.youtube import search


__all__ = [
    'reward_detail',
]


def reward_detail(request):
    if request.method == 'POST':
        num = random.randint(1, 50)
        reward_list = search(request.POST['keyword'])
        reward = reward_list['items'][num]
        return render(request, 'reward/reward_detail.html', {'reward': reward})
