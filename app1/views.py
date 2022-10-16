import sys

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from app1.models import user, education, experience, course, skill
from app1.forms import experienceForm, courseForm, skillForm, userUpdateForm, educationUpdateForm, aboutForm

from django.shortcuts import get_object_or_404


# Create your views here.


def show_user_info(request, id):
    u = user.objects.get(user_id=id)
    edu = education.objects.filter(user_id=id)
    ex = experience.objects.filter(user_id=id)
    cour = course.objects.filter(user_id=id)
    s = skill.objects.filter(user_id=id)
    return render(request, 'final.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})


def show_user(request, id):
    u = user.objects.get(user_id=id)
    edu = education.objects.filter(user_id=id)
    ex = experience.objects.filter(user_id=id)
    cour = course.objects.filter(user_id=id)
    s = skill.objects.filter(user_id=id)
    return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})


def log(request):
    return render(request, 'login.html')


def login(request):
    p = request.POST.get("password")
    e = request.POST.get("username")
    try:
        u = user.objects.get(user_email=e, user_password=p)
    except:
        e = "Invalid username or password"
        return render(request, 'login.html', {'error': e})
    edu = education.objects.filter(user_id=u.user_id)
    ex = experience.objects.filter(user_id=u.user_id)
    cour = course.objects.filter(user_id=u.user_id)
    s = skill.objects.filter(user_id=u.user_id)
    return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})


def register(request):
    return render(request, 'register.html')


def registerDone(request):
    fn = request.POST.get('firstname')
    ln = request.POST.get('lastname')
    age = request.POST.get('age')
    ph = request.POST.get('phone')
    e = request.POST.get('email')
    p = request.POST.get('password')
    c = request.POST.get('city')
    co = request.POST.get('country')
    jt = request.POST.get('joptitle')
    user.objects.create(user_first_name=fn, user_password=p, user_email=e,
                        user_age=age, user_city=c, user_country=co, user_jop_title=jt, user_phone=ph,
                        user_last_name=ln)
    return redirect('resume:log')


def userUpdate(request, id):
    u = user.objects.get(user_id=id)
    form = userUpdateForm(request.POST, instance=u)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            edu = education.objects.filter(user_id=id)
            ex = experience.objects.filter(user_id=id)
            cour = course.objects.filter(user_id=id)
            s = skill.objects.filter(user_id=id)
            return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})
    return render(request, 'user_edit.html', {'user': form})


def userDelete(request, id):
    u = user.objects.get(user_id=id)
    return render(request, 'user_delete.html', {'u': u})


def deletedUser(request, id):
    u = user.objects.get(user_id=id)
    edu = education.objects.filter(user_id=id)
    ex = experience.objects.filter(user_id=id)
    s = skill.objects.filter(user_id=id)
    c = course.objects.filter(user_id=id)
    for i in c:
        i.delete()
    for i in edu:
        i.delete()
    for i in s:
        i.delete()
    for i in ex:
        i.delete()
    u.delete()
    return render(request, 'login.html')


def educationSave(request, id):
    if request.method == 'POST':
        form = educationUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            u = user.objects.get(user_id=id)
            edu = education.objects.filter(user_id=id)
            ex = experience.objects.filter(user_id=id)
            cour = course.objects.filter(user_id=id)
            s = skill.objects.filter(user_id=id)
            return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})
    form = educationUpdateForm()
    return render(request, 'education_add.html', {'edu': form})


def educationDelete(request, id, userID):
    edu = education.objects.get(education_id=id)
    edu.delete()
    u = user.objects.get(user_id=userID)
    edu = education.objects.filter(user_id=userID)
    ex = experience.objects.filter(user_id=userID)
    cour = course.objects.filter(user_id=userID)
    s = skill.objects.filter(user_id=userID)
    return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})


def experienceSave(request, id):
    if request.method == 'POST':
        form = experienceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            u = user.objects.get(user_id=id)
            edu = education.objects.filter(user_id=id)
            ex = experience.objects.filter(user_id=id)
            cour = course.objects.filter(user_id=id)
            s = skill.objects.filter(user_id=id)
            return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})
    form = experienceForm()
    return render(request, 'experience_add.html', {'ex': form})


def experienceDelete(request, id, userID):
    ex = experience.objects.get(experience_id=id)
    ex.delete()
    u = user.objects.get(user_id=userID)
    edu = education.objects.filter(user_id=userID)
    ex = experience.objects.filter(user_id=userID)
    cour = course.objects.filter(user_id=userID)
    s = skill.objects.filter(user_id=userID)
    return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})


def courseSave(request, id):
    if request.method == 'POST':
        form = courseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        u = user.objects.get(user_id=id)
        edu = education.objects.filter(user_id=id)
        ex = experience.objects.filter(user_id=id)
        cour = course.objects.filter(user_id=id)
        s = skill.objects.filter(user_id=id)
        return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})
    form = courseForm()
    return render(request, 'course_add.html', {'cour': form})


def courseDelete(request, id, userID):
    cour = course.objects.get(course_id=id)
    cour.delete()
    u = user.objects.get(user_id=userID)
    edu = education.objects.filter(user_id=userID)
    ex = experience.objects.filter(user_id=userID)
    cour = course.objects.filter(user_id=userID)
    s = skill.objects.filter(user_id=userID)
    return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})


def skillSave(request, id):
    if request.method == 'POST':
        form = skillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            u = user.objects.get(user_id=id)
            edu = education.objects.filter(user_id=id)
            ex = experience.objects.filter(user_id=id)
            cour = course.objects.filter(user_id=id)
            s = skill.objects.filter(user_id=id)
            return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})
    form = skillForm()
    return render(request, 'skill_add.html', {'s': form})


def skillDelete(request, id, userID):
    s = skill.objects.get(skill_id=id)
    s.delete()
    u = user.objects.get(user_id=userID)
    edu = education.objects.filter(user_id=userID)
    ex = experience.objects.filter(user_id=userID)
    cour = course.objects.filter(user_id=userID)
    s = skill.objects.filter(user_id=userID)
    return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})


def aboutAdd(request, id):
    u = user.objects.get(user_id=id)
    form = aboutForm(request.POST, instance=u)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            edu = education.objects.filter(user_id=id)
            ex = experience.objects.filter(user_id=id)
            cour = course.objects.filter(user_id=id)
            s = skill.objects.filter(user_id=id)
            return render(request, 'resume.html', {"user": u, "edu": edu, "ex": ex, "cour": cour, "s": s})
    return render(request, 'about_add.html', {'u': form})
