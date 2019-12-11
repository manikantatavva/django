from django.shortcuts import render
from .models import fakedata
from django.http.response import HttpResponse
import faker
fake=faker.Faker()
def fake (request):
    for i in range(1000):
        first_name=fake.first_name()
        last_name=fake.last_name()
        job=fake.job()
        sal=fake.sal()
        email=fake.email()
        city=fake.city()
        dob=fake.date_time()
        address=fake.address()


        data=fakedata(
            first_name=first_name,
            last_name=last_name,
            job=job,
            sal=sal,
            email=email,
            city=city,
            dob=dob,
            address=address
        )
        data.save()
    return HttpResponse("data inserted")

def fetchingdata(request):
    fdata=fakedata.objects.all()
    return render(request,'fakedata.html',{'fdata':fdata})
