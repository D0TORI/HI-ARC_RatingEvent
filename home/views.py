from django.shortcuts import render, redirect
from ranking.models import RatedUser
import requests
import math
import time
import random

import ranking.cron
import ranking.ValidHandles

def killAllDB():
    Users = RatedUser.objects.all()
    for i in Users:
        i.delete()

# Create your views here.
def CreateDBbysolved():
    r = requests.get('https://solved.ac/api/v3/ranking/in_organization?page=1&organizationId=436')
    data = r.json()
    validhandles = ranking.ValidHandles.Handles.split('\n')
    cnt = data['count']
    page = math.ceil(cnt/50)
    for i in range(1, page+1):
        r = requests.get('https://solved.ac/api/v3/ranking/in_organization?page='+str(i)+'&organizationId=436')
        data = r.json()
        users = data['items']
        for user in users:
            handle = user['handle']
            rating = user['rating']

            if handle not in validhandles:
                continue

            if (rating >= 1600): div = 1
            elif (rating >= 800): div = 2
            else: div = 3

            newUser = RatedUser(
                username = handle,
                seasonStartRating = rating,
                userrating = rating,
                userdiv = div
            )

            #test code
            #newUser.seasonStartRating -= (random.randrange(0, rating+1)//100)

            try: newUser.save()
            except: pass

def divRank(divN):
    if divN <= 0 or divN > 3: return []

    Users = list(RatedUser.objects.filter(userdiv=divN))
    Users.sort(key=lambda x:( -(x.userrating-x.seasonStartRating), -x.userrating))
    Rank = []
    for i in range(5):
        user = {}

        if len(Users) <= i:
            user['username'] = '.'
            user['change'] = 0
            user['color'] = '#000000'

            Rank.append(user)
            continue

        userdata = Users[i]

        user['username'] = userdata.username
        user['change'] = userdata.userrating - userdata.seasonStartRating
        user['color'] = '#000000'

        if (userdata.userrating >= 2700): user['color'] = '#FF0062'
        elif (userdata.userrating >= 2200): user['color'] = '#00B4FC'
        elif (userdata.userrating >= 1600): user['color'] = '#27E2A4'
        elif (userdata.userrating >= 800): user['color'] = '#EC9A00'
        elif (userdata.userrating >= 200): user['color'] = '#435F7A'
        elif (userdata.userrating >= 30): user['color'] = '#AD5600'
        else: user['color'] = '#000000'

        Rank.append(user)
    return Rank


def mainpage(request):
    context = {}

    context['div1'] = divRank(1)
    context['div2'] = divRank(2)
    context['div3'] = divRank(3)
    return render(request, 'home/index.html', context)