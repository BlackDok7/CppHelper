from flask import Flask, request, jsonify
import openai

# Initialize Flask App
app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = "your_openai_api_key_here"

# API Endpoint to Handle C++ Coding Queries
@app.route('/cpp-helper', methods=['POST'])
def cpp_helper():
    try:
        # Parse the request JSON
        data = request.json
        if not data or 'query' not in data:
            return jsonify({'error': 'Invalid input. Please provide a "query".'}), 400

        # User's C++ related query
        user_query = data['query']

        # OpenAI API call
        response = openai.Completion.create(
            model="text-davinci-003",  # Change model if needed
            prompt=f"You are an expert C++ programmer. Help with the following task:\n\n{user_query}",
            max_tokens=1500,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        # Extract and return the response
        answer = response.choices[0].text.strip()
        return jsonify({'response': answer})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Example Endpoint to Suggest C++ Code Improvements
@app.route('/cpp-code-improvement', methods=['POST'])
def cpp_code_improvement():
    try:
        # Parse the request JSON
        data = request.json
        if not data or 'code' not in data:
            return jsonify({'error': 'Invalid input. Please provide C++ "code".'}), 400

        # User's C++ code
        user_code = data['code']

        # OpenAI API call
        response = openai.Completion.create(
            model="text-davinci-003",  # Change model if needed
            prompt=f"Analyze and suggest improvements for the following C++ code:\n\n{user_code}\n\nSuggestions:",
            max_tokens=1500,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        # Extract and return the response
        suggestions = response.choices[0].text.strip()
        return jsonify({'improvements': suggestions})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Example Endpoint to Generate a C++ Function
@app.route('/cpp-function-generator', methods=['POST'])
def cpp_function_generator():
    try:
        # Parse the request JSON
        data = request.json
        if not data or 'description' not in data:
            return jsonify({'error': 'Invalid input. Please provide a "description" of the function.'}), 400

        # User's function description
        function_description = data['description']

        # OpenAI API call
        response = openai.Completion.create(
            model="text-davinci-003",  # Change model if needed
            prompt=f"Write a C++ function based on the following description:\n\n{function_description}\n\nFunction:",
            max_tokens=1500,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        # Extract and return the response
        function_code = response.choices[0].text.strip()
        return jsonify({'function': function_code})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
