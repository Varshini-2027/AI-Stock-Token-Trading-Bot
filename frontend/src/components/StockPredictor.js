import React, { useState } from 'react';

function StockPredictor() {
    const [symbol, setSymbol] = useState('');
    const [prediction, setPrediction] = useState('');

    const fetchPrediction = async () => {
        const response = await fetch(`http://localhost:5000/predict?symbol=${symbol}`);
        const data = await response.json();
        setPrediction(`Prediction for ${symbol}: ${data.prediction}`);
    };

    return (
        <div>
            <input 
                type="text" 
                placeholder="Enter stock symbol" 
                value={symbol}
                onChange={(e) => setSymbol(e.target.value)}
            />
            <button onClick={fetchPrediction}>Get Prediction</button>
            <p>{prediction}</p>
        </div>
    );
}

export default StockPredictor;