import serial

def connect() -> serial.Serial | str:
    """Conecta con el arduino por el puerto serial

    Returns:
        serial.Serial | str: Objeto serial.Serial si se conectó correctamente, str si no se pudo conectar
    """
    try:
        arduino: serial.Serial = serial.Serial(
            port='/dev/ttyACM0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0)
        return arduino
    except serial.SerialException:
        return "No se pudo conectar con el arduino. Verifique que el arduino esté conectado y que el puerto sea el correcto."
mensaje: str = ""

def sendData(dato: str) -> dict:
    """Envía un dato al arduino por el puerto serial
    
    Args:
        dato (str): Dato a enviar al arduino
        
    Returns:
        dict: {"status": "Dato enviado correctamente"} si el dato se envió correctamente, {"error": str} si no se pudo conectar con el arduino
    """
    arduino = connect()
    if type(arduino) == str:
        return {"error": arduino}
    arduino.write(f'<{dato}>'.encode())
    return {"status": "Dato enviado correctamente"}

def receiveData() -> dict:
    """Recibe un dato del arduino por el puerto serial

    Returns:
        dict: {"data": {<dato1>: <valor1>, <dato2>: <valor2>, ...}} si se recibió algún dato, {"warning": "No se recibió ningún dato"} si no se recibió ningún dato, {"error": str} si no se pudo conectar con el arduino
    """
    arduino = connect()
    if type(arduino) == str:
        return {"error": arduino}
    # Leer el dato con la sintaxis <dato>. 
    # Ignorando todo lo que este fuera de los caracteres < y >.
    # Ejemplo: ncein;'fanc<dato>cnio574w:en -> dato
    data, caracter = "", ""
    marcadorInicio, marcadorFin = "<", ">"
    lecturaEnProceso: bool = False
    while arduino.in_waiting > 0:
        caracter = arduino.read().decode()
        if (lecturaEnProceso):
            if caracter != marcadorFin:
                data += caracter
            else:
                lecturaEnProceso = False
                data += "\0"
        elif caracter == marcadorInicio:
            lecturaEnProceso = True
    # Verificar si se recibió algún dato
    if data == "":
        return {"warning": "No se recibió ningún dato"}
    # Dar formato a los datos recibidos como diccionario
    # Ejemplo: "dato1\0valor1\0dato2\0valor2\0" -> {"dato1": "valor1", "dato2": "valor2"}
    data = data.split("\0")
    data = {data[i]: data[i+1] for i in range(0, len(data), 2)}
    return {"data": data}