from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Q
from .models import HoistWorkOrder
from .forms import HoistWorkOrderFilterForm

# class HoistWorkOrderListView(ListView):
#     model = HoistWorkOrder
#     template_name = 'hoistworkorder_list.html'
#     context_object_name = 'workorders'
#     paginate_by = 10

#     def get_queryset(self):
#         form = HoistWorkOrderFilterForm(self.request.GET)

#         if form.is_valid():
#             wonumber = form.cleaned_data.get('wonumber')
#             customer = form.cleaned_data.get('customer')
#             city = form.cleaned_data.get('city')
#             capacity = form.cleaned_data.get('capacity')
#             sales_rep = form.cleaned_data.get('sales_rep')
#             start_date = form.cleaned_data.get('start_date')
#             end_date = form.cleaned_data.get('end_date')

#             query = Q()

#             if wonumber:
#                 query &= Q(Work_Order_Number=wonumber)

#             if customer:
#                 query &= Q(customer__name__icontains=customer)

#             if city:
#                 query &= Q(customer__city__icontains=city)

#             if capacity:
#                 query &= Q(capacity=capacity)

#             if sales_rep:
#                 query &= Q(sales_rep=sales_rep)

#             if start_date:
#                 query &= Q(date__gte=start_date)

#             if end_date:
#                 query &= Q(date__lte=end_date)

#             if query:
#                 return HoistWorkOrder.objects.filter(query)
#             else:
#                 return HoistWorkOrder.objects.all()
#         else:
#             return HoistWorkOrder.objects.all()
        
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = HoistWorkOrderFilterForm(self.request.GET)
#         return context

class HoistWorkOrderListView(APIView):
    def get(self, request):
        return render(request, 'hwo_search_list.html')

    def post(self, request):
        wonumber = request.data.get('wonumber')
        customer = request.data.get('customer')
        city = request.data.get('city')
        capacity = request.data.get('capacity')
        sales_rep = request.data.get('sales_rep')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        query = Q()

        if wonumber:
            query &= Q(Work_Order_Number=wonumber)
        
        if customer:
            query &= Q(customer__name__icontains=customer)

        if city:
            query &= Q(customer__city__icontains=city)

        if capacity:
            query &= Q(capacity=capacity)

        if sales_rep:
            query &= Q(sales_rep=sales_rep)

        if start_date:
            query &= Q(date__gte=start_date)

        if end_date:
            query &= Q(date__lte=end_date)

        if query:
            hwos = HoistWorkOrder.objects.filter(query)
            print(hwos)
        else:
            hwos = HoistWorkOrder.objects.all()
            print(hwos)
        
        context = {
            'hwos': hwos,
        }
        return render(request, 'hwo_search_results.html', context)