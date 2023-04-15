import datetime


class Helper:

    def validar_fecha(fecha):
        # Convertir la fecha de string a datetime
        fecha_dt = datetime.datetime.strptime(fecha, '%d-%m-%Y')

        # Obtener la fecha actual
        hoy = datetime.datetime.today().date()
        # Obtener la fecha de mañana
        maniana = hoy + datetime.timedelta(days=1)

        # Comparar la fecha con la de hoy o mañana
        if fecha_dt.date() == hoy or fecha_dt.date() == maniana:
            return True
        else:
            return False

    def parse_string(str):
        str = str.replace('\xa0', '')
        # Remover el símbolo de USD
        str = str.replace("USD", "")
        # Convertir a int
        amount_int = int(str)
        return amount_int
