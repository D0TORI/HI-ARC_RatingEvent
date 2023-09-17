from django.shortcuts import render, redirect
from ranking.models import RatedUser
import requests
import math

# Create your views here.
def divRankAll(divN):
    if divN <= 0 or divN > 3: return []

    Users = list(RatedUser.objects.filter(userdiv=divN))
    Users.sort(key=lambda x:( -(x.userrating-x.seasonStartRating), -x.userrating))
    Rank = []
    idx = 1
    prevchange = 0
    for i in range(len(Users)):
        user = {}
        userdata = Users[i]

        user['username'] = userdata.username
        user['userrating'] = userdata.userrating
        user['seasonStartRating'] = userdata.seasonStartRating
        user['change'] = userdata.userrating - userdata.seasonStartRating
        user['color'] = '#000000'

        if i == 0 or prevchange != user['change']: idx = i + 1

        user['rank'] = idx
        prevchange = user['change']

        if (userdata.userrating >= 2700): user['color'] = '#FF0062'
        elif (userdata.userrating >= 2200): user['color'] = '#00B4FC'
        elif (userdata.userrating >= 1600): user['color'] = '#27E2A4'
        elif (userdata.userrating >= 800): user['color'] = '#EC9A00'
        elif (userdata.userrating >= 200): user['color'] = '#435F7A'
        elif (userdata.userrating >= 30): user['color'] = '#AD5600'
        else: user['color'] = '#000000'

        if user['rank'] == 1: user['rankcolor'] = '#EC9A00'
        elif user['rank'] <= 4: user['rankcolor'] = '#435F7A'
        elif user['rank'] <= 10: user['rankcolor'] = '#cd7f32'
        else: user['rankcolor'] = '#000000'

        Rank.append(user)
    return Rank

def div1(request):
    context = {}
    context['div'] = 1
    context['ranking'] = divRankAll(1)

    return render(request, 'ranking/index.html', context)

def div2(request):
    context = {}
    context['div'] = 2
    context['ranking'] = divRankAll(2)

    return render(request, 'ranking/index.html', context)

def div3(request):
    context = {}
    context['div'] = 3
    context['ranking'] = divRankAll(3)

    return render(request, 'ranking/index.html', context)