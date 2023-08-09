from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from django.db.models import Q
import pdfkit
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import HoistWorkOrder
from .forms import HoistWorkOrderFilterForm
from .serializers import HoistWorkOrderSerializer
from sigma import settings
from sigma.settings import WKHTMLTOPDF_CMD

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

    # def post(self, request, hwo):
    #     # Fetch the work order details again (similar to the get method)
    #     workorder = HoistWorkOrder.objects.get(Work_Order_Number=hwo)
    #     context = {'hwo': workorder}
    #
    #     # Render the template to HTML
    #     template = get_template('download_hwo.html')
    #     rendered_html = template.render(context)
    #
    #     # Convert HTML to PDF using WeasyPrint
    #     pdf_file = HTML(string=rendered_html).write_pdf()
    #
    #     # Create an HTTP response with PDF content
    #     response = HttpResponse(pdf_file, content_type='application/pdf')
    #     response['Content-Disposition'] = f'filename="{hwo}_workorder.pdf"'
    #     return response

    def post(self, request, hwo):
        workorder = HoistWorkOrder.objects.get(Work_Order_Number=hwo)
        wonum = workorder.Work_Order_Number
        context = {'hwo': workorder}
        template_path = 'download_hwo.html'
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{wonum}.pdf"'
        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(
        html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

    # def post(self, request, hwo):
    #     workorder = HoistWorkOrder.objects.get(Work_Order_Number=hwo)
    #     context = {'hwo': workorder}

    #     html = render(request, 'download_hwo.html', context).content

    #     options = {
    #         'quiet': '',
    #         'load-error-handling': 'ignore',
    #         'enable-local-file-access': True,
    #     }

    #     pdf = pdfkit.from_string(html.decode(), False, options=options)

    #     response = HttpResponse(pdf, content_type='application/pdf')
    #     response['Content-Disposition'] = f'filename="{workorder.Work_Order_Number}.pdf"'
    #     return response
