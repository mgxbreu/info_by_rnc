DGII_URL = "https://www.dgii.gov.do/app/WebApps/ConsultasWeb/consultas/rnc.aspx"

CSV_HEADERS = "rnc,nombre_comercial,regimen_pago,estado,actividad_economica \n"


RNC_INPUT = "#ctl00_cphMain_txtRNCCedula"
SEARCH_BUTTON = "#ctl00_cphMain_btnBuscarPorRNC"
TRADE_NAME_VALUE = '''() => {
        const data = document.querySelector('#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(3) > td:nth-child(2)').innerText;
        return data;
    }'''
PAYMENT_REGIME_VALUE = '''() => {
        const data = document.querySelector('#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(5) > td:nth-child(2)').innerText;
        return data;
    }'''
STATUS_VALUE = '''() => {
        const data = document.querySelector('#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(6) > td:nth-child(2)').innerText;
        return data;
    }'''
ECONOMIC_ACTIVITY_VALUE = '''() => {
        const data = document.querySelector('#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(7) > td:nth-child(2)').innerText;
        return data;
    }'''
