from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__, template_folder='../views', static_folder='../views/public')


@app.route('/add', methods=['GET'])
def add_numbers():
    # Get 'a' and 'b' from the request's arguments
    a = request.args.get('a', default=0, type=int)
    b = request.args.get('b', default=0, type=int)
    
    # Calculate the sum
    result = a + b
    
    # Return the result as JSON
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
