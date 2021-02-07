from django.shortcuts import render
from .resources import AddressResource
from tablib import Dataset
from django.contrib import messages
from .models import Address
import xlwt
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def home(request):
    if request.method == 'POST':
        address_resource = AddressResource()
        dataset = Dataset()
        new_address = request.FILES['myfile']
        if not new_address.name.endswith('xlsx' or 'xl'):
            messages.info(request, 'Wrong format! please choose Exel file to upload')
            return render(request, 'home.html')
        imported_data = dataset.load(new_address.read(), format=('xlsx' or 'xl'))
        for data in imported_data:
            value = Address(
                data[0], data[1], data[2], data[3], data[4], data[5],
                data[6], data[7], data[8], data[9], data[10], data[11]
            )
            value.save()
    return render(request, 'home.html')


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Address')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name', 'Job', 'Address1', 'Address2', 'Area', 'City', 'State', 'Country', 'Pincode', 'location',
               ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Address.objects.all().values_list('Name', 'Job', 'Address1', 'Address2', 'Area', 'City', 'State', 'Country',
                                             'Pincode', 'latitude', 'longitude')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return HttpResponse(response, home(request))
