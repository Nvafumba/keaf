from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Person

# Create your views here.
@login_required
def index(request):
    records = Person.objects.all()
    person_count = Person.objects.count()
    # Count males and females
    male_count = Person.objects.filter(gender='M').count()
    female_count = Person.objects.filter(gender='F').count()
    return render(request, 'core/index.html', {
        'records':records, 
        'person_count': person_count,
        'male_count': male_count,
        'female_count': female_count,
        })



