# specification/views.py

from django.shortcuts import get_object_or_404, redirect

# specification/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView

from .models import StandardChangeMst, SalesMst, ItemMst
from .forms import StandardChangeMstForm

from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from datetime import datetime

class StandardChangeMstCreateView(CreateView):
    model = StandardChangeMst
    form_class = StandardChangeMstForm
    template_name = 'specification/standardchange_form.html'
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
    fields = ['update_date', 'item_id', 'change_details', 'attachment']
    template_name = 'specification/standardchange_form.html'
    success_url = reverse_lazy('standardchange_list')

@require_POST
def send_email_to_customer(request, item_id):
    update_date = datetime.strptime(request.POST['update_date'], "%Y年%m月%d日").strftime("%Y-%m-%d") 

    standard_change = StandardChangeMst.objects.filter(item_id=item_id ,update_date=update_date)[0]
    customer_details = get_customer_details_for_standard_change(item_id)
    subject = '商品規格情報変更のご連絡'
    from_email = settings.DEFAULT_FROM_EMAIL

    try:
        for customer_email, customer_name in customer_details:
            
            message = render_to_string('emails/standard_change_email.txt', {
                'customer_name': customer_name,
                'standard_change': standard_change,
            })
            email = EmailMessage(subject, message, from_email, [customer_email])
            
            if standard_change.attachment:
                email.attach_file(standard_change.attachment.path)
            email.send()
        
        standard_change.send_mail_flg = 1
        standard_change.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        print(f"Failed to send email: {e}")
        return JsonResponse({'status': 'error'}, status=500)

def get_customer_details_for_standard_change(item_id):
    sales_mst_list = SalesMst.objects.filter(item_id=item_id)
    customer_details = []
    for sales_instance in sales_mst_list:
        customer_address = sales_instance.customer.customer_address
        customer_name = sales_instance.customer.customer_name
        customer_details.append((customer_address, customer_name))
    return customer_details

def check_item_id(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        item_id = request.POST.get('item_id')

        if ItemMst.objects.filter(item_id=item_id).exists():
            return JsonResponse({'exists': True})
        else:
            return JsonResponse({'exists': False})

    return JsonResponse({'error': 'Invalid request method or not ajax'})


@require_POST
def standardchange_delete(request, pk):
    # pkに対応するStandardChangeオブジェクトを取得する
    standard_change = get_object_or_404(StandardChangeMst, pk=pk)
    
    # 削除処理
    standard_change.delete()
    
    # 削除後にリダイレクトする
    return redirect('standardchange_list')  # 削除後にリダイレクトするURLを適宜変更する