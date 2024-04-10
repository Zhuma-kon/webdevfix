from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Company, Vacancy

def get_company_list(request):
    companies = Company.objects.all()
    data = [{'id': company.id, 'name': company.name, 'city': company.city} for company in companies]
    return JsonResponse(data, safe=False)

def get_company(request, id):
    company = get_object_or_404(Company, id=id)
    data = {
        'id': company.id,
        'name': company.name,
        'description': company.description,
        'city': company.city,
        'address': company.address
    }
    return JsonResponse(data)

def get_company_vacancies(request, id):
    company = get_object_or_404(Company, id=id)
    vacancies = company.vacancies.all()
    data = [{'id': vacancy.id, 'name': vacancy.name, 'salary': vacancy.salary} for vacancy in vacancies]
    return JsonResponse(data, safe=False)

def get_vacancy_list(request):
    vacancies = Vacancy.objects.all()
    data = [{'id': vacancy.id, 'name': vacancy.name, 'salary': vacancy.salary} for vacancy in vacancies]
    return JsonResponse(data, safe=False)

def get_vacancy(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    data = {
        'id': vacancy.id,
        'name': vacancy.name,
        'description': vacancy.description,
        'salary': vacancy.salary,
        'company': vacancy.company.name
    }
    return JsonResponse(data)

def get_top_ten_vacancies(request):
    top_vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = [{'id': vacancy.id, 'name': vacancy.name, 'salary': vacancy.salary} for vacancy in top_vacancies]
    return JsonResponse(data, safe=False)