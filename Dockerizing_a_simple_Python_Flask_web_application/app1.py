from google import genai
from flask import Flask, request, jsonify, render_template

# Initialize the Flask application
app = Flask(__name__)

# Initialize the GenAI client with your API key
client = genai.Client(api_key="AIzaSyBantpebwUuopIEm2fTCLgF3h50vcb6t-k")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    print(request.json)
    user_input = request.json.get('message')

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        prompt = f"கொடுக்கப்பட்ட வார்த்தையிலிருந்து approximately 20 வரி தனித்துவமான காதல் தமிழ் கவிதையை உருவாக்கவும் : '{user_input}' தற்காலத் தமிழில்."

   
        response = client.models.generate_content(
          model="gemini-2.0-flash",  
         contents=prompt
         )   
        # Use the GenerativeModel to generate content
        # model = genai.GenerativeModel("gemini-2.0-flash")

        # # Generate response using the user input
        # response = model.generate_content(
        #     f"கொடு வார்த்தையைப் பயன்படுத்தி ஒரு ஆக்கபூர்வமான கவர்ச்சிகரமான காதல் தமிழ் கவிதையை உருவாக்குங்கள் : {user_input}. ஆங்கில வார்த்தைகள் எதுவும் வேண்டாம்."
        # )

        if response and response.text:
            return jsonify({"response": response.text})
        else:
            return jsonify({"error": "Gemini API returned an empty response."}), 500

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)