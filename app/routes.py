from flask import Blueprint, jsonify, request
from .services import songs, update_song, delete_song

# Agrupar endpoints
main = Blueprint("main", __name__)

# Función para validar datos requeridos
REQUIRED_FIELDS = ["title", "artist"]
def validate_song(data):
    if not data:
        return "Request body is required"
    for field in REQUIRED_FIELDS:
        if field not in data:
            return f"{field} is required"
    return None

# GET
@main.route("/songs", methods=["GET"])
def get_songs():
    return jsonify(songs)

# POST
@main.route("/songs", methods=["POST"])
def create_song():
    data = request.json
    error = validate_song(data)
    if error:
        return{"Error": error}, 400
    songs.append(data)

    return{"message": "Song added"}, 201

# PUT
@main.route("/songs/<int:index>", methods=["PUT"])
def edit_song(index):
    data = request.json
    error = validate_song(data)
    if error:
        return {"error": error}, 400
    
    success = update_song(index, data)

    if not success:
        return {"error": "Song not found"}, 404
    
    return {"message": "Song updated"}

# DELETE
@main.route("/songs/<int:index>", methods=["DELETE"])
def remove_song(index):
    success = delete_song(index)

    if not success:
        return {"error": "Song not found"}, 404

    return {"message": "Song deleted"}
