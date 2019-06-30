# services/orders/project/__init__.py

from flask import Flask, jsonify  # <-- nuevo

# instanciando la app
app = Flask(__name__)

# establelciendo configuracion
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/orders/ping', methods=['GET'])
def ping_pong():
   return jsonify({
       'status':'success',
       'message': 'ṕong'
   })   