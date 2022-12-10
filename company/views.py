from django.shortcuts import render
from .models import *
import pandas as pd
from django.core.paginator import Paginator
from datetime import datetime
import json

# Create your views here.
def statistics(request):
    return render(request,'statistics.html')


current_year = 2022


def index(request):
    context = {}
    if request.method != "POST":
        try:
            #  year_no = list(PresentYear.objects.all())[-1]
            #  print(year_no.year,"yes")
            #  year_no = year_no.year
            global current_year
            year_no = current_year
            print(current_year)
            database = CompanyDatabase.objects.filter(year=year_no).order_by("ctc")
       
        except:
            PresentYear.objects.create(year=datetime.now().strftime("%y"))
            year_no = datetime.now().strftime("%y")
        #print(year_no)
            database = CompanyDatabase.objects.filter(year=year_no).order_by("ctc")
    else:
        year_no = request.POST["yearno"]
        print(year_no)
        current_year = year_no
        database = CompanyDatabase.objects.filter(year=year_no).order_by("ctc")


    

    
    #print(database)

    page_number = request.GET.get('page')
    p = Paginator(database,per_page=10)

    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    

    y = PresentYear.objects.all()
    print(y)
    # database = list(database.values())
    #database = json.dumps(database)
    #print(database)

    context = {'page_obj': page_obj,"company":database,"year_no":int(current_year),"year":y}

    return render(request, "placement/index.html",context)

##################################################################################################################
def refresh(request):
    context ={}

    ########################

    existing_database = Company.objects.all()
    all_names = []
    for x in existing_database:
        all_names.append(x.name)

    #############################
    df = pd.read_excel("static\placement2022.xlsx",names=["company_name","Btech","Dual Degree","Mtech","Msc","Mba","total_offers","ctc","year"])
    print(df.info())
    #df.fillna(0,inplace= True)
    #df1.fillna(0,inplace= True)
    #df['total_offers'] = df["Btech"] + df["Mtech"]

    print(df["company_name"].value_counts())




    company_name = df["company_name"]






    #cgpa_cutoff = df["cgpa_cutoff"]
    ctc=df["ctc"]
    #base=df["base"]
    Btech = df["Btech"]
    DualDegree = df["Dual Degree"]
    Msc = df["Msc"]
    Mba = df["Mba"]
    Mtech = df["Mtech"]
    total_offers = df["total_offers"]
    #open_dream = df["open_dream"]
    year=df["year"]


    total_fields = len(company_name)
    for i in range(total_fields):
        if company_name[i] not in all_names:
            Company.objects.create(name = company_name[i])
            compins = Company.objects.get(name = company_name[i])
            CompanyDatabase.objects.create(name=compins,
                                    ctc=ctc[i],
                                    #cgpa=cgpa_cutoff[i],
                                    #base=base[i],
                                    Btech = Btech[i],
                                    Dtech = DualDegree[i],
                                    MSC = Msc[i],
                                    MBA = Mba[i],

                                    Mtech = Mtech[i],
                                    total_offers=total_offers[i],
                                    #open_dream=open_dream[i],
                                    year=year[i])
        elif company_name[i] in all_names:
            compins = Company.objects.get(name = company_name[i])
            companyobj = CompanyDatabase.objects.filter(name=compins)
            years = []
            for c in companyobj:
                years.append(c.year)

            if year[i] not in years:
                CompanyDatabase.objects.create(name=compins,
                                        ctc=ctc[i],
                                    #cgpa=cgpa_cutoff[i],
                                    #base=base[i],
                                    Btech = Btech[i],
                                    Dtech = DualDegree[i],
                                    MSC = Msc[i],
                                    MBA = Mba[i],
                                    
                                    Mtech = Mtech[i],
                                    total_offers=total_offers[i],
                                    #open_dream=open_dream[i],
                                    year=year[i])
            else:
                pass
        else:
            pass


    ##########################################
    try:
        year_no = list(PresentYear.objects.all())[0]
    except:
        year_no=PresentYear.objects.create(year=2022)

    database = CompanyDatabase.objects.filter(year=year_no.year)

    name=[]
    ctc=[]
    #cgpa=[]
    #base=[]
    #opendream=[]
    Btech = []
    DualDegree = []
    Mba = []
    Msc = []

    Mtech = []
    total_offers = []

    for d in database:
        name.append(d.name)
        Btech.append(d.Btech)
        Mtech.append(d.Mtech)
        ctc.append(d.ctc)
        DualDegree.append(d.Dtech)
        Mba.append(d.MBA)
        Msc.append(d.MSC)
        # cgpa.append(d.cgpa)
        # base.append(d.base)
        # opendream.append(d.open_dream)
        if int(d.total_offers) != -1:
            total_offers.append(int(d.total_offers))


    context = {
                "name":name,
                "Btech":Btech,
                "Metch":Mtech,
                "ctc":ctc,
                "Dualdegree":DualDegree,
                "Mba":Mba,
                "Msc":Msc,
                # "cgpa":cgpa,
                # "base":base,
                # "opendream":opendream,
                "company" :database,
                "max_offers": sum(total_offers),
                "year_no":year_no.year

    }
    return render(request, "placement/index.html",context)


##################################################################################################################

def highestctc(request,pk):
    context={}


    #year_no = list(PresentYear.objects.all())[0]
    year_no = PresentYear.objects.get(pk = pk)
    database = CompanyDatabase.objects.order_by("-ctc").filter(year=year_no.year)
   
    page_number = request.GET.get('page')
    p = Paginator(database,per_page=5)

    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    context = {'page_obj': page_obj,"year_no":year_no.year}

    # name=[]
    # ctc=[]
    # #cgpa=[]
    # #base=[]
    # #opendream=[]
    # Btech = []
    # DualDegree = []
    # Mba = []
    # Msc = []

    # Mtech = []
    # total_offers = []

    # for d in database:
    #     name.append(d.name)
    #     Btech.append(d.Btech)
    #     Mtech.append(d.Mtech)
    #     ctc.append(d.ctc)
    #     DualDegree.append(d.Dtech)
    #     Mba.append(d.MBA)
    #     Msc.append(d.MSC)
    #     # cgpa.append(d.cgpa)
    #     # base.append(d.base)
    #     # opendream.append(d.open_dream)
    #     if int(d.total_offers) != -1:
    #         total_offers.append(int(d.total_offers))


    # context = {
    #             "name":name,
    #             "Btech":Btech,
    #             "Metch":Mtech,
    #             "ctc":ctc,
    #             "Dualdegree":DualDegree,
    #             "Mba":Mba,
    #             "Msc":Msc,
    #             # "cgpa":cgpa,
    #             # "base":base,
    #             # "opendream":opendream,
    #             "company" :database,
    #             "max_offers": sum(total_offers),
    #             "year_no":year_no.year

    # }


    return render(request, "placement/ctc.html",context)
##################################################################################################################
def highestbase(request):
    context={}

    ##########################################
    year_no = list(PresentYear.objects.all())[0]
    database = CompanyDatabase.objects.order_by("-base").filter(year=year_no.year)
    name=[]
    ctc=[]
    #cgpa=[]
    #base=[]
    #opendream=[]
    Btech = []
    DualDegree = []
    Mba = []
    Msc = []

    Mtech = []
    total_offers = []

    for d in database:
        name.append(d.name)
        Btech.append(d.Btech)
        Mtech.append(d.Mtech)
        ctc.append(d.ctc)
        DualDegree.append(d.Dtech)
        Mba.append(d.MBA)
        Msc.append(d.MSC)
        # cgpa.append(d.cgpa)
        # base.append(d.base)
        # opendream.append(d.open_dream)
        if int(d.total_offers) != -1:
            total_offers.append(int(d.total_offers))


    context = {
                "name":name,
                "Btech":Btech,
                "Metch":Mtech,
                "ctc":ctc,
                "Dualdegree":DualDegree,
                "Mba":Mba,
                "Msc":Msc,
                # "cgpa":cgpa,
                # "base":base,
                # "opendream":opendream,
                "company" :database,
                "max_offers": sum(total_offers),
                "year_no":year_no.year

    }
    return render(request, "placement/base.html",context)

 
##################################################################################################################
def highestoffers(request,pk):
    context={}

    ##########################################
    #year_no = list(PresentYear.objects.all())[0]
    year_no = PresentYear.objects.get(pk = pk)
    database = CompanyDatabase.objects.order_by("-total_offers").filter(year=year_no.year)

    page_number = request.GET.get('page')
    p = Paginator(database,per_page=5)

    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    context = {'page_obj': page_obj,"year_no":year_no.year}







    # name=[]
    # ctc=[]
    # #cgpa=[]
    # #base=[]
    # #opendream=[]
    # Btech = []
    # DualDegree = []
    # Mba = []
    # Msc = []

    # Mtech = []
    # total_offers = []

    # for d in database:
    #     name.append(d.name)
    #     Btech.append(d.Btech)
    #     Mtech.append(d.Mtech)
    #     ctc.append(d.ctc)
    #     DualDegree.append(d.Dtech)
    #     Mba.append(d.MBA)
    #     Msc.append(d.MSC)
    #     # cgpa.append(d.cgpa)
    #     # base.append(d.base)
    #     # opendream.append(d.open_dream)
    #     if int(d.total_offers) != -1:
    #         total_offers.append(int(d.total_offers))


    # context = {
    #             "name":name,
    #             "Btech":Btech,
    #             "Metch":Mtech,
    #             "ctc":ctc,
    #             "Dualdegree":DualDegree,
    #             "Mba":Mba,
    #             "Msc":Msc,
    #             # "cgpa":cgpa,
    #             # "base":base,
    #             # "opendream":opendream,
    #             "company" :database,
    #             "max_offers": sum(total_offers),
    #             "year_no":year_no.year

    # }


    return render(request, "placement/offers.html",context)
##################################################################################################################
def cgpa(request):
    context={}

    ##########################################
    year_no = list(PresentYear.objects.all())[0]
    database = CompanyDatabase.objects.order_by("-cgpa").filter(year=year_no.year)

    name=[]
    ctc=[]
    #cgpa=[]
    #base=[]
    #opendream=[]
    Btech = []
    DualDegree = []
    Mba = []
    Msc = []

    Mtech = []
    total_offers = []

    for d in database:
        name.append(d.name)
        Btech.append(d.Btech)
        Mtech.append(d.Mtech)
        ctc.append(d.ctc)
        DualDegree.append(d.Dtech)
        Mba.append(d.MBA)
        Msc.append(d.MSC)
        # cgpa.append(d.cgpa)
        # base.append(d.base)
        # opendream.append(d.open_dream)
        if int(d.total_offers) != -1:
            total_offers.append(int(d.total_offers))


    context = {
                "name":name,
                "Btech":Btech,
                "Metch":Mtech,
                "ctc":ctc,
                "Dualdegree":DualDegree,
                "Mba":Mba,
                "Msc":Msc,
                # "cgpa":cgpa,
                # "base":base,
                # "opendream":opendream,
                "company" :database,
                "max_offers": sum(total_offers),
                "year_no":year_no.year

    }
    


    return render(request, "placement/cgpa.html",context)
##################################################################################################################

last_year = datetime.now().strftime("%y")

def change_year(request):

    context = {}

    #year_no = list(PresentYear.objects.all())[0]

    if request.method == "POST":
        yearno = request.POST["yearno"]
        if yearno == 0:
            yearno = 2022
        global last_year
        last_year = yearno
        #year_no.year = yearno
        #year_no.save()
        database = CompanyDatabase.objects.filter(year=yearno).order_by("ctc")
    else:
        yearno = last_year
        database = CompanyDatabase.objects.filter(year = yearno).order_by("ctc")

    page_number = request.GET.get('page')
    p = Paginator(database,per_page=5)

    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    

    y = PresentYear.objects.all()

    context = {'page_obj': page_obj,"company":database,"year_no":yearno,"year":y}


    

    return render(request, "placement/index.html",context)





def companydetail(request,pk):
    x = CompanyDatabase.objects.get(pk = pk)
    company = CompanyDatabase.objects.filter(name = x.name)
    context = {'company':company}
    print(company)
    return render(request,"placement/companydetail.html",context)


