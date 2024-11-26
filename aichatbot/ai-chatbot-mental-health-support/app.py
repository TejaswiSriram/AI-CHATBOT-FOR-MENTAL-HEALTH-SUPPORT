from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load training data
data = pd.read_csv('training_data.csv')
responses = dict(zip(data['input'], data['response']))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message', '').strip().lower()
    
    # Find matching response
    response = responses.get(user_input, 
                              "I'm sorry, I don't have a response for that. Can you tell me more?")
    
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
