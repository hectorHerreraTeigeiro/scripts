# csv open file
import csv, requests

url = 'http://omawww.sat.gob.mx/cifras_sat/Documents/Listado_Completo_69-B.csv'
list_file = requests.get(url)
for pos,line in enumerate(list_file.iter_lines(delimiter='\r\n')):
    # if pos>11921 and pos<11929:
        print('***p***', pos,'***bol', line, '***eol')
