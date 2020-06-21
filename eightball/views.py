from django.shortcuts import render
import random
import redis

# Create your views here.
redisClient = redis.Redis(host='localhost', port=6379, db=0)

def index(request):
    file = open(r'eightball/eightball.txt')
    eightball = file.readlines()
    eightball = eightball[random.randint(0, len(eightball) -1)]
    result = len(redisClient.keys("eightball:*"))
    redisClient.set("eightball:"+str(result), eightball)
    return render(request, 'eightball/index.html', {'eightball': eightball})