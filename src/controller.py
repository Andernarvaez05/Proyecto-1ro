from flask import Flask, request, jsonify
from bson import ObjectId
from services import AvesService

app = Flask(__name__)
aves_service = AvesService()

# Ruta para obtener todos los pollos
@app.route('/pollos', methods=['GET'])
def get_pollos():
    pollos = aves_service.get_pollos()
    for pollo in pollos:
        pollo['_id'] = str(pollo['_id'])
    return jsonify(pollos)

# Ruta para obtener un pollo por su ID
@app.route('/pollos/<pollo_id>', methods=['GET'])
def get_pollo(pollo_id):
    pollo = aves_service.get_pollo_by_id(pollo_id)
    if pollo:
        pollo['_id'] = str(pollo['_id'])
        return jsonify(pollo)
    else:
        return jsonify({"error": "Pollo no encontrado"}), 404

# Ruta para crear un nuevo pollo
@app.route('/pollos', methods=['POST'])
def create_pollo():
    pollo_data = request.json
    pollo_id = aves_service.create_pollo(pollo_data)
    return jsonify({"_id": pollo_id}), 201

# Ruta para actualizar un pollo existente
@app.route('/pollos/<pollo_id>', methods=['PUT'])
def update_pollo(pollo_id):
    update_data = request.json
    success = aves_service.update_pollo(pollo_id, update_data)
    if success:
        return jsonify({"message": "Pollo actualizado correctamente"})
    else:
        return jsonify({"error": "Pollo no encontrado"}), 404

# Ruta para eliminar un pollo
@app.route('/pollos/<pollo_id>', methods=['DELETE'])
def delete_pollo(pollo_id):
    success = aves_service.delete_pollo(pollo_id)
    if success:
        return jsonify({"message": "Pollo eliminado correctamente"})
    else:
        return jsonify({"error": "Pollo no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
