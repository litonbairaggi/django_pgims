from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill


class HomeView(View):
    template_name = "home.html"
    paginate_by = 5
    def get(self, request):        
        labels = []
        data = []    
        bills = SaleBill.objects.all().order_by('-time')  
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)


            
        context = {
            'labels': labels,
            'data': data,
            'bills': bills
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"