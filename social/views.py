from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from social.models import *
from social.forms import *


def feed(request):
    # request.get()
    post_list = Post.objects.all()
    # print(post_list)
    post_list = reversed(post_list)
    return render(request, "social/feed.html", locals())


def media(request):
    video_list = Video.objects.all()
    video_list = reversed(video_list)
    return render(request, "social/videos_feed.html", locals())


def reg_form(request):
    print("reg_form")
    if request.method == 'POST':
        print("postpost")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("savesave")
            form.save()
            return redirect("entrance")
    else:
        print("elseelse")
        form = RegistrationForm()
        return render(request, "social/registration_form.html", locals())


def logout(request):
    auth.logout(request)
    return redirect("entrance")


def entrance1(request):
    if request.user.id is not None:
        return redirect("social_feed")
    return redirect("entrance")


def add_new_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("social_feed")
        else:
            return render(request, "social/addnewpost.html", locals())
    return render(request, "social/addnewpost.html", locals())


def personal_page(request, id_user):
    user = UserPersonal.objects.get(user_id=id_user)
    link_site = str(id_user)
    comments = reversed(Commentary.objects.filter(commentary_link=link_site))
    return render(request, "social/personal_page.html", locals())


def authorization(request):
    if request.user.id is not None:
        auth.logout(request)
    form = AuthorizationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # form.save()
        username = form.cleaned_data.get('username')
        print(username)
        raw_password = form.cleaned_data.get('password')
        print(raw_password)
        user = auth.authenticate(username=username, password=raw_password)
        if user and user.is_active:
            auth.login(request, user)
            return redirect("social_feed")
    return render(request, "social/entrance.html", locals())


def add_comment(request, id_user):
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("social_feed")
    return render(request, "social/addcomment.html", locals())


def add_video(request):
    form = VideoForm(request.POST or None)
    form = VideoForm('DATA','DAFA','DADA')
    if request.method == "POST":
        if form.is_valid():
            # form.video_author.id = request.user.id
            form.save()
            return redirect("video_feed")
    return render(request, "social/addnewvideo.html", locals())


def show_video(request, id_video):
    video = Video.objects.get(pk=id_video)
    return render(request, "social/show_video.html", locals())


def edit_personal(request, id_user):
    person = UserPersonal.objects.get(user_id=id_user)
    form = EditPersonalForm(instance=person)
    if request.method == 'POST':
        form = EditPersonalForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("personal_page", request.user.id)
        else:
            return render(request, "social/editpersonal.html", locals())
    return render(request, "social/editpersonal.html", locals())


def personal_trucks(request, id_user):
    trucks_list = Truck.objects.filter(truck_owner_id=id_user)
    return render(request, "social/personal_trucks.html", locals())


def add_truck(request):
    form = TruckForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("personal_trucks", request.user.id)
        else:
            return render(request, "social/add_truck.html", locals())
    return render(request, "social/add_truck.html", locals())