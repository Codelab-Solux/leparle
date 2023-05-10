from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base.forms import *
from base.models import *
from django.db.models import Q

# Create your views here.


@login_required(login_url='login')
def home(req):
    user = req.user
    sectors = Sector.objects.all()
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    if user.role.sec_level >= 1:
        courses = Course.objects.filter(
        Q(title__icontains=query)
        | Q(subtitle__icontains=query)
        | Q(sector__name__icontains=query)
    )
    else:
        courses = Course.objects.filter(
        Q(title__icontains=query)
        | Q(subtitle__icontains=query), sector=user.sector
    )
        
    context = {
        "home_page": "active",
        'title': 'home',
        'courses': courses,
        'sectors': sectors,

    }
    return render(req, 'base/index.html', context)

@login_required(login_url='login')
def about(req):
    context = {
        "about_page": "active",
        'title': 'about',

    }
    return render(req, 'base/about.html', context)

@login_required(login_url='login')
def sectors(req):
    user = req.user
    courses = Course.objects.all()
    sectors = Sector.objects.all()
    context = {
        "sectors_page": "active",
        'title': 'sectors',
        'courses': courses,
        'sectors': sectors,

    }
    return render(req, 'base/sectors.html', context)


@login_required(login_url='login')
def sector_details(req, pk):
    user = req.user
    curr_sector = Course.objects.get(id=pk)
    rel_courses = Course.objects.filter(sector=curr_sector)
    sectors = Sector.objects.all()
    context = {
        "courses_page": "active",
        'title': 'courses',
        'rel_courses': rel_courses,
        'sectors': sectors,

    }
    return render(req, 'base/sector.html', context)


@login_required(login_url='login')
def courses(req):
    user = req.user
    sectors = Sector.objects.all()
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    if user.role.sec_level >= 1:
        courses = Course.objects.filter(
        Q(title__icontains=query)
        | Q(subtitle__icontains=query)
        | Q(sector__name__icontains=query)
    )
    else:
        courses = Course.objects.filter(
        Q(title__icontains=query)
        | Q(subtitle__icontains=query), sector=user.sector
    )

    context = {
        "home_page": "active",
        'title': 'home',
        'courses': courses,
        'sectors': sectors,

    }
    return render(req, 'base/courses.html', context)

@login_required(login_url='login')
def course_details(req, pk):
    user = req.user
    curr_course = Course.objects.get(id=pk)
    rel_courses = Course.objects.filter(sector=curr_course.sector)
    sectors = Sector.objects.all()
    context = {
        "courses_page": "active",
        'title': 'courses',
        'rel_courses': rel_courses,
        'curr_course': curr_course,
        'sectors': sectors,

    }
    return render(req, 'base/course.html', context)


@login_required(login_url='login')
def blog(req):
    user = req.user
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    if user.role.sec_level >= 1:
        blogposts = Blogpost.objects.filter(
        Q(title__icontains=query)
        | Q(subtitle__icontains=query)
        | Q(sector__name__icontains=query)
    )
    else:
        blogposts = Blogpost.objects.filter(
        Q(title__icontains=query)
        | Q(subtitle__icontains=query), sector=user.sector
    )

    context = {
        "blog_page": "active",
        'title': 'home',
        'blogposts': blogposts,

    }
    return render(req, 'base/blog.html', context)

@login_required(login_url='login')
def blogpost(req, pk):
    user = req.user
    curr_post = Blogpost.objects.get(id=pk)
    rel_posts = Blogpost.objects.filter(sector=curr_post.sector)
    sectors = Sector.objects.all()
    context = {
        "blogpost_page": "active",
        'title': 'blogpost',
        'rel_posts': rel_posts,
        'curr_post': curr_post,
        'sectors': sectors,

    }
    return render(req, 'base/blogpost.html', context)


@login_required(login_url='login')
def dashboard(req):
    user = req.user
    if user.role.sec_level >= 3:
        sectors = Sector.objects.all()
        courses = Course.objects.all()
        blogposts = Blogpost.objects.all()

        secform = SectorForm()
        if req.method == 'POST':
            form = SectorForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('sectors')

        courseform = CourseForm()
        if req.method == 'POST':
            form = CourseForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('courses')

        blogform = BlogpostForm()
        if req.method == 'POST':
            form = BlogpostForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('blog')

    else:
        return redirect(req.META.get('HTTP_REFERER'))
    
    context = {
        "dashboard_page": "active",
        'title': 'dashboard',
        'blogposts': blogposts,
        'courses': courses,
        'sectors': sectors,
        'secform': secform,
        'courseform': courseform,
        'blogform': blogform,

    }
    return render(req, 'base/dashboard.html', context)

