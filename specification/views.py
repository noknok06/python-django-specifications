# specification/views.py

from django.shortcuts import get_object_or_404, redirect

# specification/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView

from .models import StandardChangeMst, SalesMst
from .forms import StandardChangeMstForm

from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_POST

class StandardChangeMstCreateView(CreateView):
    model = StandardChangeMst
    form_class = StandardChangeMstForm
    template_name = 'specification/standardchange_create.html'
    success_url = reverse_lazy('standardchange_list') 

class StandardChangeMstListView(ListView):
    model = StandardChangeMst
    template_name = 'specification/standardchange_list.html'
    context_object_name = 'standard_changes'

class StandardChangeMstDetailView(DetailView):
    model = StandardChangeMst
    template_name = 'specification/standardchange_detail.html'
    context_object_name = 'standard_change'

class StandardChangeMstUpdateView(UpdateView):
    model = StandardChangeMst
    fields = ['update_date', 'item_id', 'change_details']
    template_name = 'specification/standardchange_form.html'
    success_url = reverse_lazy('standardchange_list')



@require_POST
def send_email_to_customer(request, item_id):
    # Get the StandardChangeMst instance
    standard_change = get_object_or_404(StandardChangeMst, item_id=item_id)
    
    # Get customer addresses for the item_id
    customer_addresses = get_customer_addresses_for_standard_change(item_id)
    
    if customer_addresses:
        subject = 'Regarding Standard Change'
        message = f"Dear Customers,\n\nWe want to inform you about the recent standard change:\n\n{standard_change.change_details}\n\nBest regards,\nYour Company"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = customer_addresses
        
        try:
            # Send email
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            # Handle email sending failure
            # Log the error or take appropriate action
            print(f"Failed to send email: {e}")
    
    return redirect('standardchange_detail', pk=standard_change.pk)

def get_customer_addresses_for_standard_change(item_id):
    try:
        sales_mst_list = SalesMst.objects.filter(item_id=item_id)
        customer_addresses = [sales_instance.customer.customer_address for sales_instance in sales_mst_list]
        return customer_addresses
    except SalesMst.DoesNotExist:
        return []