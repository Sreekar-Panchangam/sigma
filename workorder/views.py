from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.db.models import Q
from .models import HoistWorkOrder
from .forms import HoistWorkOrderFilterForm
from .serializers import HoistWorkOrderSerializer

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
            return redirect('workorder:hwo_detail', hwo=wonumber)
        
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
    
class HoistWorkOrderDetailView(APIView):
    def get(self, request, hwo):
        workorder = HoistWorkOrder.objects.get(Work_Order_Number=hwo)
        context = {'hwo':workorder}
        return render(request, 'hwo_detail.html', context)