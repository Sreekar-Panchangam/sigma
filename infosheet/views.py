from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from django.db.models import Q
from .models import HoistInformationSheet
from workorder.models import HoistWorkOrder
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
class InformationSheetListView(APIView):
    def get(self, request):
        return render(request, 'his_search_list.html')

    def post(self, request):
        slnumber = request.data.get('slnumber')
        customer = request.data.get('customer')
        city = request.data.get('city')
        engineer = request.data.get('engineer')
        sales_rep = request.data.get('sales_rep')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        query = Q()
        if slnumber:
            return redirect('infosheet:his_detail', his=slnumber)
        if customer:
            query &= Q(work_order__customer__name__icontains=customer)
        if city:
            query &= Q(work_order__customer__city__icontains=city)
        if engineer:
            query &= Q(engineer_in_charge__icontains=engineer)
        if sales_rep:
            query &= Q(work_order__sales_rep=sales_rep)
        if start_date:
            query &= Q(dispatch_date__gte=start_date)
        if end_date:
            query &= Q(dispatch_date__lte=end_date)
        if query:
            hiss = HoistInformationSheet.objects.filter(query)
            print(hiss)
        else:
            hiss = HoistInformationSheet.objects.all()
            print(hiss)

        context = {
            'hiss': hiss,
        }
        return render(request, 'his_search_results.html', context)
    
class InformationSheetDetailView(APIView):
    def get(self, request, his):
        infosheet = HoistInformationSheet.objects.get(serial_number=his)
        context = {'his':infosheet}
        return render(request, 'his_detail.html', context)
    
    def post(self, request, his):
        infosheet = HoistInformationSheet.objects.get(serial_number=his)
        slnum = infosheet.serial_number
        context = {'his':infosheet}
        template_path = 'download_his.html'
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{slnum}.pdf"'
        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(
        html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response