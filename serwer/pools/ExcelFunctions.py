import xlsxwriter
import xlrd
from .models import DetailedMetric, Sample, ExternalFactor, Result

def generate_empty_xlsx(output,experiment_data, supplement_name, percentage_of_supplement, metrices):
    # experiment_data [nazwa,opis,link autor,data utworzenia]
    # metrices list of lists of elements ['name','num_series', 'num_repeats', 'id_próbki', 'num_of_values_external_factor', 'list_of_values_external_factor', 'metrice_id']
    xlsx_name = supplement_name + "_" + str(percentage_of_supplement) + "%" + ".xlsx"
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})

    locked = workbook.add_format()
    locked.set_locked(True)
    unlocked = workbook.add_format()
    unlocked.set_locked(False)
    unlocked.set_bg_color('#FFFFCC')
    unlocked.set_border()
    cell_formatBlue = workbook.add_format()
    cell_formatBlue.set_bg_color('#CCE5FF')
    cell_formatBlue.set_border()

    worksheet = workbook.add_worksheet("opis_eksperymentu")
    worksheet.protect()
    worksheet.set_column('A:B', 60)
    worksheet.write('A1', experiment_data[0], cell_formatBlue)
    worksheet.write('A2', experiment_data[1], cell_formatBlue)
    worksheet.write('A3', experiment_data[2], cell_formatBlue)
    worksheet.write('A4', experiment_data[3], cell_formatBlue)
    worksheet.write('A5', experiment_data[4], cell_formatBlue)

    for data in metrices:
        worksheet_name = str(data[3]) + "," + str(data[0]) + "," + str(data[6])
        worksheet = workbook.add_worksheet(worksheet_name)
        worksheet.protect()
        how_wide = 1 + int(data[4])
        how_many_lines = 1 + 1 + int(data[1]) + int(data[2])
        where_title = 'A1:' + str(chr(ord('A') + how_wide - 1)) + '1'
        worksheet.merge_range(where_title, data[0], cell_formatBlue)
        counter = ord('B')
        for val in data[5]:
            cell = str(chr(counter)) + str(2)
            worksheet.write(cell, val, cell_formatBlue)
            counter = counter + 1
            row_counter = 3
        for i in [k for k in range(1, int(data[4]) + 1)]:
            seria = "SERIA " + str(i)
            cell = 'B' + str(row_counter) + ":" + str(chr(ord('B') + data[4] - 1)) + str(row_counter)
            if data[4] - 1:
                worksheet.merge_range(cell, seria, cell_formatBlue)
            else:
                worksheet.write(cell, seria, cell_formatBlue)
            row_counter = row_counter + int(data[2])
            for j in range(1, data[2]):
                cellPomiar = 'A' + str(row_counter - j)
                to_write = "pomiar " + str(data[2] - j)
                worksheet.write(cellPomiar, to_write, cell_formatBlue)
                for b in range(0, len(data[5])):
                    cell = str(chr(ord('B') + b)) + str(row_counter - j)
                    worksheet.write(cell, "", unlocked)
    workbook.close()

    return workbook


def read_experiment_data(path):
    # res to [[id_metryki_szczegółowej, [[pomiar1seria1, pomiar2seria1],[pomiar1seria2, pomiar2seria2]]], [id_metryki_szczegółowej, [[pomiar1seria1, pomiar2seria1],[pomiar1seria2, pomiar2seria2]]]]
    # gdy pomiary dla róznych wartości czynnika zew to po średniku wpisane do tego samego wiersza tabeli wyniku
    loc = (path)
    wb = xlrd.open_workbook(loc)
    result = []
    for sheet in wb.sheets():
        data = str(sheet.name).split(",")
        if len(data) > 1:
            res = []
            res.append(data[2])
            infos = DetailedMetric.objects.get(id=data[2])
            series = []
            sample = Sample.objects.get(id=data[0])
            external_factor = ExternalFactor.objects.get(name=sample.externalFactor)
            rowcounter = 3
            colcounter = 1
            for i in range(0, infos.number_of_series):
                serie = []
                for j in range(0, infos.number_of_repeat):
                    measure = ""
                    rowcounter = rowcounter + j
                    for k in range(0, external_factor.number_of_values):
                        if measure == "":
                            measure = measure + sheet.cell_value(rowx=rowcounter, colx=colcounter + k)
                        else:
                            measure = measure + "," + sheet.cell_value(rowx=rowcounter, colx=colcounter + k)
                serie.append(measure)
                rowcounter = rowcounter + 2
                series.append(serie)
            res.append(series)
            result.append(res)

    # wstawienie wyników do bazy
    for res in result:
        for i in range(0, len(res[1])):
            for j in range(0, len(res[1][i])):
                r = Result(value=res[1][i][j], number_of_measure=j, number_of_serie=i, detailed_metric__id=res[0])
                r.save()