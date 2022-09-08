from contextlib import redirect_stderr
import json
from django.shortcuts import render,redirect
from .models import Profile,Friend,ChatMessage
from .forms import ChatMessageForm
from django.http import JsonResponse

# Create your views here.
def index(request):
    user_profile = request.user.profile
    friends = user_profile.friends.all()
    context = {"user":user_profile,"friends":friends}
    return render(request,"mychatapp/index.html",context)


def detail(request,pk):
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id = friend.profile.id)
    form = ChatMessageForm()
    chats = ChatMessage.objects.all()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit = False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = profile
            chat_message.save()
            return redirect("detail",pk = friend.profile.id)
    context = {"friend":friend,"form":form,"user":user, "profile":profile,"chats":chats}
    return render(request,"mychatapp/detail.html",context)
def sentMessages(request,pk):
    data = json.loads(request.body)
    new_chat = data["msg"]
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id = friend.profile.id)
    new_chat_message = ChatMessage.objects.create(body = new_chat,msg_sender =request.user.profile,msg_receiver =profile) # seen default is False
    print(new_chat)
    return JsonResponse(new_chat_message.body,safe=False)