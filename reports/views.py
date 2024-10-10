from django.shortcuts import render, get_object_or_404
from .models import Report

# Create your views here.
def report_list(request):
    reports = Report.objects.all()
    return render(request, 'reports/reports.html', {'reports': reports})

def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'reports/report_detail.html', {'report': report})

def reports_view(request):
    return render(request, 'reports/reports.html')
