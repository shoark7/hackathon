from django.shortcuts import redirect
from reward.models import Reward

__all__ = [
    'reward_add',
]


def reward_add(request):
    if request.method == "POST":
        Reward.objects.create(name=request.POST.get('name'))
        return redirect('reward:reward_main')
