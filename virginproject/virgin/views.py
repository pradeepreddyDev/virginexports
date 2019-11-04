from django.shortcuts import render, redirect

from virgin.forms import ContactedForm, DetailsForm
from .models import Cms, Blog, Projects, Category, ProductCategory, ProductCategoryImages, ProductSubCategory, Banners


# Create your views here.


def index(request):
    banners = Banners.objects.all()
    products1 = ProductCategory.objects.get(enable_on_home=True, id=1)
    products2 = ProductCategory.objects.get(enable_on_home=True, id=2)
    products3 = ProductCategory.objects.get(enable_on_home=True, id=3)
    about = Cms.objects.get(id=1)
    con = Cms.objects.get(id=2)

    dicts = ProductCategory.objects.all()
    for dict in dicts:
        dicts['subcat'] = ProductSubCategory.objects.filter(category_id=dict['id'])
    print(dicts)

    return render(request, 'index.html', {'banners': banners, 'products1': products1, 'products2': products2,
                                          'products3': products3, 'about': about, 'contact': con})


def productcategory(request, id):
    cms = ProductCategory.objects.get(id=id)
    product = ProductCategoryImages.objects.filter(category_id=id)
    return render(request, 'productcategory.html', {'product': product, 'cms': cms})


def productsubcategory(request):
    return render(request, 'productsubcategory.html', {'productsubcategory': productsubcategory})


def about(request):
    cms = Cms.objects.get(id=1)
    return render(request, 'about.html', {'about': cms})


def projects(request):
    cms = Cms.objects.get(id=3)
    pog = Projects.objects.filter().order_by('-id')
    cat = Category.objects.filter().order_by('id')
    return render(request, 'projects.html', {'projects': pog, 'cms': cms, 'cat': cat})


def granite(request):
    cms = Cms.objects.get(id=5)
    pog = Granite.objects.filter().order_by('-id')
    return render(request, 'granite.html', {'granite': pog, 'cms': cms})


def contact(request):
    con = Cms.objects.get(id=2)
    return render(request, 'contact.html', {'contact': con})


def blog(request):
    cms = Cms.objects.get(id=4)
    blog = Blog.objects.filter().order_by('-id')
    return render(request, 'blog.html', {'blog': blog, 'cms': cms})


def blogdetail(request, id):
    cms = Cms.objects.get(id=4)
    blog = Blog.objects.get(id=id)
    return render(request, 'blog-detail.html', {'blog': blog, 'cms': cms})


def send(request):
    if request.method == "POST":
        form = ContactedForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('contact/')
    else:
        return render(request, "virgin/contact.html")
