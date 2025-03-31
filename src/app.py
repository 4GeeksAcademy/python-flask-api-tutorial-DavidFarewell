from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta test
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello World"})

# Lista de tareas
todos = [
    { "done": True, "label": "Sample Todo 1" },
    { "done": False, "label": "Sample Todo 2" }
]

# GET /todos 
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# POST /todos 
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    print("Incoming request with the following body:", request_body)
    todos.append(request_body)
    return jsonify(todos)

# DELETE 
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):
        todos.pop(position)
    return jsonify(todos)

# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
