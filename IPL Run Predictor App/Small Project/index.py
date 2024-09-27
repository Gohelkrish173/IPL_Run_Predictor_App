import joblib
from flask import Flask, request, jsonify 
from flask_cors import CORS

# Load the model and encoders
ipl_model = joblib.load('ipl_delivery_model.pkl')
le_batter = joblib.load('le_batter.pkl')
le_bowler = joblib.load('le_bowler.pkl')
le_batting_team = joblib.load('le_batting_team.pkl')
le_bowling_team = joblib.load('le_bowling_team.pkl')
le_over = joblib.load('le_over.pkl')
le_inning = joblib.load('le_inning.pkl')
le_ball = joblib.load('le_ball.pkl')

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})

@app.route('/predict', methods=['POST'])
def predict():
     # Get JSON data from request
    data = request.json
    
    batter = data['batter']
    bowler = data['bowler']
    batting_team = data['batting_team']
    bowling_team = data['bowling_team']
    over = data['over']
    inning = data['inning']
    ball = data['ball']

    # Encode the input data
    batter_encoded = le_batter.transform([batter])[0]
    bowler_encoded = le_bowler.transform([bowler])[0]
    batting_team_encoded = le_batting_team.transform([batting_team])[0]
    bowling_team_encoded = le_bowling_team.transform([bowling_team])[0]
    over_encoded = le_over.transform([over])[0]
    inning_encoded = le_inning.transform([inning])[0]
    ball_encoded = le_ball.transform([ball])[0]
    
     # Prepare input for prediction
    input_data = [[batter_encoded, bowler_encoded, batting_team_encoded, bowling_team_encoded,over_encoded,inning_encoded,ball_encoded]]

    # Predict the outcome (e.g., runs)
    prediction = ipl_model.predict(input_data)
    
    # Return the prediction as JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
