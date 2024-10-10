from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Equipment, Experiment, LabTest, LabTestRequest, LabReport, LabResultVerification
from .forms import EquipmentForm, ExperimentForm, LabTestRequestForm, LabReportForm, LabResultVerificationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import FormView
from .models import LabTest
from .forms import LabTestForm

def request_lab_test(request):
    if request.method == 'POST':
        form = LabTestRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab_test_list')
    else:
        form = LabTestRequestForm()
    return render(request, 'labmanagement/request_lab_test.html', {'form': form})

def view_lab_report(request, pk):
    lab_test = get_object_or_404(LabTest, pk=pk)
    return render(request, 'labmanagement/lab_test_report.html', {'lab_test': lab_test})

# Equipment Views
def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'labmanagement/equipment_list.html', {'equipment': equipment})

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'labmanagement/add_equipment.html', {'form': form})

def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    return render(request, 'labmanagement/equipment_detail.html', {'equipment': equipment})

def experiment_detail(request, pk):
    experiment = get_object_or_404(Experiment, pk=pk)
    return render(request, 'labmanagement/experiment_detail.html', {'experiment': experiment})

# Experiment Views
def experiment_list(request):
    experiments = Experiment.objects.all()
    return render(request, 'labmanagement/experiment_list.html', {'experiments': experiments})


def labmanagement_view(request):
    return render(request, 'labmanagement/labmanagement.html')

def view_reports(request):
    # Logic to display patient reports
    return render(request, 'labmanagement/view_reports.html')

@login_required
def enter_report(request, pk):
    lab_test = get_object_or_404(LabTest, pk=pk)
    if request.method == 'POST':
        form = LabReportForm(request.POST)
        if form.is_valid():
            lab_report = form.save(commit=False)
            lab_report.lab_test = lab_test
            lab_report.save()
            lab_test.status = 'COMPLETED'
            lab_test.save()
            return redirect('test_list')
    else:
        form = LabReportForm()
    return render(request, 'labmanagement/report_entry.html', {'form': form, 'lab_test': lab_test})

@login_required
def verify_result(request, pk):
    lab_test = get_object_or_404(LabTest, pk=pk)
    if request.method == 'POST':
        form = LabResultVerificationForm(request.POST)
        if form.is_valid():
            verification = form.save(commit=False)
            verification.lab_test = lab_test
            verification.verified_by = request.user
            verification.save()
            lab_test.status = 'VERIFIED'
            lab_test.save()
            return redirect('test_list')
    else:
        form = LabResultVerificationForm()
    return render(request, 'labmanagement/verify_results.html', {'form': form, 'lab_test': lab_test})

# @login_required
# def test_list(request):
#    lab_tests = LabTest.objects.all()
#    return render(request, 'labmanagement/test_list.html', {'lab_tests': lab_tests})

@login_required
def test_list(request):
    tests = LabTest.objects.all()
    return render(request, 'labmanagement/test_list.html', {'tests': tests})

@login_required
def submit_test_request(request):
    if request.method == 'POST':
        form = LabTestRequestForm(request.POST)
        if form.is_valid():
            test_request = form.save(commit=False)
            test_request.requester = request.user
            test_request.save()
            return redirect('test_list')
    else:
        form = LabTestRequestForm()
    return render(request, 'labmanagement/test_request_form.html', {'form': form})

@login_required
def report_entry(request, pk):
    test_request = get_object_or_404(LabTestRequest, pk=pk)
    if request.method == 'POST':
        form = LabReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.test_request = test_request
            report.save()
            return redirect('test_list')
    else:
        form = LabReportForm()
    return render(request, 'labmanagement/report_entry.html', {'form': form})

@login_required
def verify_results(request, pk):
    report = get_object_or_404(LabReport, pk=pk)
    if request.method == 'POST':
        form = LabResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.report = report
            result.verified = True
            result.verified_by = request.user
            result.date_verified = timezone.now()
            result.save()
            return redirect('test_list')
    else:
        form = LabResultForm()
    return render(request, 'labmanagement/verify_results.html', {'form': form})

# Complete Report View
@login_required
def complete_report(request, report_id):
    # Logic to complete a patient report
    from .models import PatientReport  # Import inside the function
    report = get_object_or_404(PatientReport, id=report_id)
    if request.method == 'POST':
        report.completed = True
        report.save()
        return redirect('patient_reports')
    return render(request, 'labmanagement/complete_report.html', {'report': report})

# Pending Requests View
@login_required
def pending_requests(request):
    # Logic to display pending lab requests
    from .models import PendingRequest  # Import inside the function
    requests = PendingRequest.objects.filter(is_completed=False)
    return render(request, 'labmanagement/pending_requests.html', {'requests': requests})

# Patient Reports View
@login_required
def patient_reports(request):
    from .models import PatientReport  # Import inside the function
    reports = PatientReport.objects.all()
    return render(request, 'labmanagement/patient_reports.html', {'reports': reports})

# Logistic Management View
@login_required
def logistic_management(request):
    from .models import Logistic  # Import inside the function
    logistics = Logistic.objects.all()
    return render(request, 'labmanagement/logistics.html', {'logistics': logistics})

def logistic_view(request):
    # Your logic here
    return render(request, 'stores/logistics_overview.html')


@login_required
def report_detail(request, pk):
    report = get_object_or_404(PatientReport, pk=pk)
    return render(request, 'labmanagement/report_detail.html', {'report': report})

@login_required
def pending_requests(request):
    requests = PendingRequest.objects.filter(is_completed=False)
    return render(request, 'labmanagement/pending_requests.html', {'requests': requests})


# Lab Test Views
@login_required
def lab_tests(request):
    tests = LabTest.objects.all()
    return render(request, 'labmanagement/lab_tests.html', {'tests': tests})


@login_required
def submit_test_request(request):
    if request.method == 'POST':
        form = LabTestRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test_list')
    else:
        form = LabTestRequestForm()
    return render(request, 'labmanagement/submit_test_request.html', {'form': form})


@login_required
def verify_result(request, pk):
    lab_test = get_object_or_404(LabTest, pk=pk)
    if request.method == 'POST':
        form = LabResultVerificationForm(request.POST)
        if form.is_valid():
            verification = form.save(commit=False)
            verification.lab_test = lab_test
            verification.verified_by = request.user
            verification.save()
            lab_test.status = 'Verified'
            lab_test.save()
            return redirect('test_list')
    else:
        form = LabResultVerificationForm()
    return render(request, 'labmanagement/verify_result.html', {'form': form, 'lab_test': lab_test})


@login_required
def test_list(request):
    tests = LabTest.objects.all()
    return render(request, 'labmanagement/test_list.html', {'tests': tests})


@login_required
def report_entry(request, pk):
    test_request = get_object_or_404(LabTestRequest, pk=pk)
    if request.method == 'POST':
        form = LabReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.test_request = test_request
            report.save()
            return redirect('test_list')
    else:
        form = LabReportForm()
    return render(request, 'labmanagement/report_entry.html', {'form': form})

class LabTestListView(ListView):
    model = LabTest
    template_name = 'labmanagement/labtest_list.html'
    context_object_name = 'labtests'

class LabTestDetailView(DetailView):
    model = LabTest
    template_name = 'labmanagement/labtest_detail.html'
    context_object_name = 'labtest'

class LabTestCreateView(CreateView):
    model = LabTestRequest
    form_class = LabTestRequestForm
    template_name = 'labmanagement/labtestrequest_form.html'
    success_url = '/labmanagement/labtestrequests/'

class LabTestUpdateView(UpdateView):
    model = LabTest
    template_name = 'labmanagement/labtest_form.html'
    fields = ['name']
    success_url = reverse_lazy('labtest-list')

class LabTestDeleteView(DeleteView):
    model = LabTest
    template_name = 'labmanagement/labtest_confirm_delete.html'
    success_url = reverse_lazy('labtest-list')


# LabTestRequest Views

class LabTestRequestListView(ListView):
    model = LabTestRequest
    template_name = 'labmanagement/labtestrequest_list.html'
    context_object_name = 'labtest_requests'

class LabTestRequestDetailView(DetailView):
    model = LabTestRequest
    template_name = 'labmanagement/labtestrequest_detail.html'
    context_object_name = 'labtest_request'

class LabTestRequestCreateView(CreateView):
    model = LabTestRequest
    template_name = 'labmanagement/labtestrequest_form.html'
    fields = ['test', 'patient_name']
    success_url = reverse_lazy('labtestrequest-list')

class LabTestRequestUpdateView(UpdateView):
    model = LabTestRequest
    template_name = 'labmanagement/labtestrequest_form.html'
    fields = ['test', 'patient_name']
    success_url = reverse_lazy('labtestrequest-list')

class LabTestRequestDeleteView(DeleteView):
    model = LabTestRequest
    template_name = 'labmanagement/labtestrequest_confirm_delete.html'
    success_url = reverse_lazy('labtestrequest-list')


# LabReport Views

class LabReportListView(ListView):
    model = LabReport
    template_name = 'labmanagement/labreport_list.html'
    context_object_name = 'labreports'

class LabReportDetailView(DetailView):
    model = LabReport
    template_name = 'labmanagement/labreport_detail.html'
    context_object_name = 'labreport'

class LabReportCreateView(CreateView):
    model = LabReport
    template_name = 'labmanagement/labreport_form.html'
    fields = ['test_request', 'report_data']
    success_url = reverse_lazy('labreport-list')

class LabReportUpdateView(UpdateView):
    model = LabReport
    template_name = 'labmanagement/labreport_form.html'
    fields = ['test_request', 'report_data']
    success_url = reverse_lazy('labreport-list')

class LabReportDeleteView(DeleteView):
    model = LabReport
    template_name = 'labmanagement/labreport_confirm_delete.html'
    success_url = reverse_lazy('labreport-list')

# For lab test
class LabTestFormView(FormView):
    template_name = 'labmanagement/labtest_form.html'
    form_class = LabTestForm
    success_url = '/labmanagement/labtest_list/'  # Redirect after a successful form submission

    def form_valid(self, form):
        # Process the form data
        form.save()
        return super().form_valid(form)

def send_notification(user, message):
    notification = Notification.objects.create(user=user, message=message)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user.id}",
        {
            "type": "send_notification",
            "message": message,
        }
    )
