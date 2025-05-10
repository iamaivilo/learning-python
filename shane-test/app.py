from flask import Flask, render_template, request, jsonify
from datetime import datetime
import openai

app = Flask(__name__)

# Initialize OpenAI client - you'll need to set this with your API key
openai.api_key = 'Fill in your own API key'  # Replace this with your actual API key

# Store chat history in memory (in a real app, you'd use a database)
chat_history = []

@app.route('/')
def home():
    return render_template('index.html', chat_history=chat_history)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message', '')
    timestamp = datetime.now().strftime("%H:%M")
    
    try:
        # Call ChatGPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150
        )
        
        # Extract the bot's response from the API response
        bot_response = response.choices[0].message.content
        
    except Exception as e:
        bot_response = "Sorry, I'm having trouble connecting to my brain right now. Please try again later."
        print(f"Error calling OpenAI API: {str(e)}")
    
    # Add messages to chat history
    chat_history.append({
        'message': user_message,
        'sender': 'user',
        'time': timestamp
    })
    chat_history.append({
        'message': bot_response,
        'sender': 'bot',
        'time': timestamp
    })
    
    return jsonify({'response': bot_response, 'time': timestamp})

if __name__ == '__main__':
    app.run(debug=True) 