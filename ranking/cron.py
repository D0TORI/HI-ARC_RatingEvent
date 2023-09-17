from ranking.models import RatedUser
import requests
import datetime
import math
import json
import time
import ranking.ValidHanles



def RatingUpdate():
    print(datetime.datetime.now(), 'Rating Update Start')
    r = requests.get('https://solved.ac/api/v3/ranking/in_organization?page=1&organizationId=436')
    data = r.json()
    validhandles = ranking.ValidHanles.Handles.split('\n')
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

            change = RatedUser.objects.get(username=handle)
            change.userrating = rating
            try: change.save()
            except:
                print("Error in", handle)

    print(datetime.datetime.now(), 'Rating Update End')
