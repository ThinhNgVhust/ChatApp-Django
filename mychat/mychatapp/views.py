from django.shortcuts import render
from .models import Profile,Friend
# Create your views here.
def index(request):
    user_profile = request.user.profile
    friends = user_profile.friends.all()
    context = {"user":user_profile,"friends":friends}
    return render(request,"mychatapp/index.html",context)
def detail(request,pk):
    friend = Friend.objects.get(profile_id=pk)
    context = {"friend":friend}
    return render(request,"mychatapp/detail.html",context)