import stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
import shop.models as md
import shop.models.report as report


@login_required()
def create_report(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
    xlsx_data = report.write_excel(md.Product.objects.all(), request.user.profile.get_profile())
    response.write(xlsx_data)
    return response


@login_required()
def create_admin_report(request):
    if not request.user.profile.user.is_superuser:
        return HttpResponseRedirect('http://google.com')
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
    xlsx_data = report.admin_report()
    response.write(xlsx_data)
    return response
