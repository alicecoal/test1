from datetime import date
from io import BytesIO
import xlsxwriter
from shop.models.goods import Exterior
from shop.models.order import Inspector


def admin_report():
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    inspector = Inspector()
    print(inspector.__dict__)
    today = str(date.today())
    counter = str(inspector.counter)
    value = str(inspector.value)
    worksheet.write_string(1, 1, today)
    worksheet.write_string(2, 1, counter)
    worksheet.write_string(3, 1, value)
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data


def write_excel(data, user):
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    print(data.count())
    print(data[0].__dict__)
    print(data[0].__str__())
    print(data[0].class_name())
    for i in range(data.count()):
        if isinstance(data[i], Exterior):
            temp = Exterior(data[i])
            print(temp.__dict__)
        value = (data[i]).get_value()
        for j in range(data[i].count_value()):
            field = str(value[j])
            worksheet.write_string(i, j, field)
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data
