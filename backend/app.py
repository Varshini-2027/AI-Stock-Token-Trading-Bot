from flask import Flask, request, jsonify
from services.prediction_service import get_stock_prediction
from services.stock_service import fetch_stock_data

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    stock_symbol = request.args.get('symbol')
    stock_data = fetch_stock_data(stock_symbol)
    prediction = get_stock_prediction(stock_data)
    return jsonify({'symbol': stock_symbol, 'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)