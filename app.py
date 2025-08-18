"#Archivo con el codigo para la API" 

from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route ('/')
def home():
    return jsonify({'message:''Bienvenidos a la API de microservicio Base - Tratamiento de datos Paralelo A '})


@app.route ('/api/sumar', methods=['POST'])
def sumar ():
    data = request.get_json()
    a= data.get('a')
    b= data.get('b')

    if a is None or b is  None:
        return jsonify({'error:''faltan datos'}), 400
    
    return jsonify({'resultado':a+b})

@app.route('/api/info',methods=["GET"])
def info():
    return jsonify({'nombre': 'Microservicio Base Tratamiento de datos Paralelo A', 
                    
            'version': '1.0.0.',
            'descripcion': 'Esta api se encarga de sumar dos numeros ',
            'Autor': 'RP',})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port= 8080)





