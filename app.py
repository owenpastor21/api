from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

def add_numbers(a: float, b: float) -> float:
    return a + b

def multiply_numbers(a: float, b: float) -> float:
    return a * b

def get_raw_result(a: float, b: float) -> str:
    return f"The numbers are {a} and {b}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/<function>')
def api_function(function):
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        
        if function == "add":
            result = add_numbers(a, b)
            return jsonify({"result": result})
        elif function == "multiply":
            result = multiply_numbers(a, b)
            return jsonify({"result": result})
        elif function == "raw":
            result = get_raw_result(a, b)
            return result
        else:
            return jsonify({"error": "Unknown function"}), 400
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400

if __name__ == '__main__':
    app.run(debug=True)
