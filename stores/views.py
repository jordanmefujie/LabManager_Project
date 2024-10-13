from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Commodity, StockHistory
from .forms import CommodityForm
from .models import Logistic
from .forms import AddCommodityForm
from django.urls import reverse
from .forms import UpdateLogisticsForm, UpdateLogisticsForm

def view_stores(request):
    # Logic to fetch logistics data if needed
    logistics = LogisticItem.objects.all()  # Replace LogisticItem with your actual model name, Replace this with actual logic to fetch logistics data
    context = {
        'logistics': logistics,
    }
    return render(request, 'stores/view_stores.html', context)

# Logistics Overview View
def logistics_overview(request):
    logistics = Logistic.objects.all()
    return render(request, 'stores/logistics_overview.html', {'logistics': logistics})

# Logistic Detail View
def logistic_detail(request, pk):
    logistic = get_object_or_404(Logistic, pk=pk)
    return render(request, 'stores/logistic_detail.html', {'logistic': logistic})

# Stock Calendar View
def stock_calendar(request):
    logistics = Logistic.objects.all().order_by('stocked_date')
    return render(request, 'stores/stock_calendar.html', {'logistics': logistics})

def view_stores(request):
    # Logic to view all logistics
    return render(request, 'stores/view_stores.html')

def add_commodity(request):
    if request.method == 'POST':
        form = CommodityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commodity_list')  # Redirect to a list view of commodities
    else:
        form = CommodityForm()
    return render(request, 'stores/add_commodity.html', {'form': form})


def delete_commodity(request, pk):
    commodity = get_object_or_404(Commodity, pk=pk)

    if request.method == 'POST':
        # Log the deletion in StockHistory
        StockHistory.objects.create(
            commodity=commodity,
            action='Deleted',
            quantity=commodity.quantity
        )
        
        # Mark commodity as deleted
        commodity.deleted = True
        commodity.save()

        messages.success(request, f'Commodity "{commodity.name}" deleted successfully!')
        return redirect('commodity_list')

    return render(request, 'stores/confirm_delete.html', {'commodity': commodity})

def stock_history(request):
    history = StockHistory.objects.all()
    return render(request, 'stores/stock_history.html', {'history': history})

def logistics_dashboard(request):
    # Fetch data
    commodities = Commodity.objects.all()
    restocks = StockHistory.objects.filter(status='restocked')
    usage_history = StockHistory.objects.filter(status='used')

    # Filters
    category = request.GET.get('category')
    status = request.GET.get('status')
    date = request.GET.get('date')

    if category:
        commodities = commodities.filter(category=category)
    if status:
        commodities = commodities.filter(status=status)
    if date:
        usage_history = usage_history.filter(usage_date=date)

    return render(request, 'stores/logistics_dashboard.html', {
        'commodities': commodities,
        'restocks': restocks,
        'usage_history': usage_history,
    })

def add_commodity(request):
    if request.method == 'POST':
        form = AddCommodityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Commodity added successfully.')
            return redirect('commodity_list')  # Redirect to a commodity list page after adding
    else:
        form = AddCommodityForm()
    return render(request, 'stores/add_commodity.html', {'form': form})

def delete_commodity(request, pk):
    commodity = get_object_or_404(Commodity, pk=pk)
    if request.method == 'POST':
        commodity.delete()
        messages.success(request, 'Commodity deleted successfully.')
        return HttpResponseRedirect(reverse('commodity_list'))  # Redirect after deletion
    return render(request, 'stores/delete_commodity.html', {'commodity': commodity})

def update_logistics(request, pk):
    commodity = get_object_or_404(Commodity, pk=pk)
    if request.method == 'POST':
        form = UpdateLogisticsForm(request.POST, instance=commodity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Logistics updated successfully.')
            return redirect('commodity_list')
    else:
        form = UpdateLogisticsForm(instance=commodity)
    return render(request, 'stores/update_logistics.html/1/', {'form': form, 'commodity': commodity})

def filter_logistics(request):
    category = request.GET.get('category', 'all')
    status = request.GET.get('status', 'available')

    commodities = Commodity.objects.all()

    if category != 'all':
        commodities = commodities.filter(category=category)

    if status == 'low_stock':
        commodities = commodities.filter(quantity__lte=10)  # Example threshold
    elif status == 'out_of_stock':
        commodities = commodities.filter(quantity=0)

    return render(request, 'stores/dashboard.html', {'commodities': commodities})

def commodity_list(request):
    commodities = Commodity.objects.all()
    return render(request, 'stores/commodity_list.html', {'commodities': commodities})

# def dashboard_view(request):
    # Logic for the dashboard view
#   commodities = Commodity.objects.all()  # Example query
#    return render(request, 'stores/dashboard.html', {'commodities': commodities})
