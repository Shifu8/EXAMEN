from flask import Blueprint, abort , request, render_template, redirect, url_for, jsonify
from flask import flash
from flask import Flask
from controls.expresionesDaoControl import ExpresionesDaoControl
from controls.expresionesControl import ExpresionesControl
from models.expresiones import Expresiones
from flask_cors import CORS
import json


app = Flask(__name__)
app.secret_key = '1234'

cors = CORS(app)

router = Blueprint('router', __name__)

import secrets

app.secret_key = secrets.token_hex(16)  # Genera una cadena hexadecimal de 16 bytes



#CORS(api)
cors = CORS(router, resource={
    r"/*":{
        "origins":"*"
    }
})

@router.route('/') #SON GETS
def home():
    return render_template('templateexpresiones.html')


@router.route('/expresiones')
def lista_expresiones():
    e = ExpresionesDaoControl()
    return render_template('expresiones/listaexpresiones.html', lista = e.to_dict())


@router.route('/expresiones/ver')
def ver_expresiones():
   return render_template('expresiones/guardarexpresiones.html')

@router.route('/expresiones/guardar', methods=["POST"])
def guardar_expresiones():
    e = ExpresionesDaoControl()
    data = request.form
    
    # Imprimir los datos recibidos para depuración
    print("Datos recibidos:", data)
    
    # Validar si los datos mínimos están presentes
    if not all(key in data for key in ["expresionObtenida", "numero1", "numero2", "operando1", "operando2", "resultado"]):
        abort(400, "Faltan datos necesarios")

    nueva_expresion = Expresiones()
    nueva_expresion._expresionObtenida = str(data["expresionObtenida"]) 
    nueva_expresion._numero1 = str(data["numero1"]) 
    nueva_expresion._numero2 = str(data["numero2"]) 
    nueva_expresion._operando1 = str(data["operando1"])
    nueva_expresion._operando2 = str(data["operando2"])
    nueva_expresion._resultado = str(data["resultado"])
    lista_expresiones = e._list()
    nuevo_id = lista_expresiones._lenght + 1  # ID único basado en la longitud de la lista más 1
    nueva_expresion._id = nuevo_id
    
    e._save(nueva_expresion)

    return redirect("/expresiones", code=302)


@router.route('/expresiones/eliminar/<int:expresion_id>', methods=["POST"])
def eliminar_expresion(expresion_id):
    e = ExpresionesControl()
    try:
        e.eliminar(expresion_id)
        
        # Eliminar la persona del JSON
        with open('data/expresiones.json', 'r') as file:
            expresiones = json.load(file)
        expresiones = [expresion for expresion in expresiones if expresion['id'] != expresion_id]
        with open('data/expresiones.json', 'w') as file:
            json.dump(expresiones, file, indent=4)

        return jsonify({"message": "Expresion eliminada correctamente.", "expresion_id": expresion_id}), 200
    except Exception as e:
        return jsonify({"error": f"No se pudo eliminar la expresion: {str(e)}"}), 500
 