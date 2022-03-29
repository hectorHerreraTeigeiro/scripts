import base64
import datetime
import os
import time

from cfdiclient import (Autenticacion, DescargaMasiva, Fiel, SolicitaDescarga,
                        VerificaSolicitudDescarga)

# https://pypi.org/project/cfdiclient/
# https://www.sat.gob.mx/consultas/42968/consulta-y-recuperacion-de-comprobantes-(nuevo)

# Services
RFC = 'MTN040706LVA'
FIEL_CER = 'MTN040706LVA.cer'
FIEL_KEY = 'MTN040706LVA.key'
FIEL_PAS = 'Abcd#1234'

# Mexico
# RFC = 'SME1206076W2'
# FIEL_CER = 'SME1206076W2.cer'
# FIEL_KEY = 'SME1206076W2.key'
# FIEL_PAS = 'mtnetmexico'

FECHA_INICIAL = datetime.date(2022, 1, 1)
FECHA_FINAL = datetime.date(2022, 3, 29)
PATH = './'

cer_der = open(os.path.join(PATH, FIEL_CER), 'rb').read()
key_der = open(os.path.join(PATH, FIEL_KEY), 'rb').read()

fiel = Fiel(cer_der, key_der, FIEL_PAS)

auth = Autenticacion(fiel)

token = auth.obtener_token()

print('TOKEN: ', token)

descarga = SolicitaDescarga(fiel)

# tipo_solicitud='CFDI' o 'Metadata'
# EMITIDOS
# solicitud = descarga.solicitar_descarga(
#     token, RFC, FECHA_INICIAL, FECHA_FINAL, rfc_emisor=RFC, tipo_solicitud='CFDI'
# )

# RECIBIDOS
solicitud = descarga.solicitar_descarga(
    token, RFC, FECHA_INICIAL, FECHA_FINAL, rfc_receptor=RFC, tipo_solicitud='Metadata'
)

print('SOLICITUD:', solicitud)

while True:

    token = auth.obtener_token()

    print('TOKEN: ', token)

    verificacion = VerificaSolicitudDescarga(fiel)

    verificacion = verificacion.verificar_descarga(
        token, RFC, solicitud['id_solicitud'])

    print('SOLICITUD:', verificacion)

    estado_solicitud = int(verificacion['estado_solicitud'])

    # 0, Token invalido.
    # 1, Aceptada
    # 2, En proceso
    # 3, Terminada
    # 4, Error
    # 5, Rechazada
    # 6, Vencida

    if estado_solicitud <= 2:

        # Si el estado de solicitud esta Aceptado o en proceso el programa espera
        # 60 segundos y vuelve a tratar de verificar
        time.sleep(120)

        continue

    elif estado_solicitud >= 4:

        print('ERROR:', estado_solicitud)

        break

    else:
        # Si el estatus es 3 se trata de descargar los paquetes

        for paquete in verificacion['paquetes']:

            descarga = DescargaMasiva(fiel)

            descarga = descarga.descargar_paquete(token, RFC, paquete)

            print('PAQUETE: ', paquete)

            with open('{}.zip'.format(paquete), 'wb') as fp:

                fp.write(base64.b64decode(descarga['paquete_b64']))

        break
