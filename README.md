# C++ Helper API

A Flask-based API using OpenAI's GPT to assist with C++ programming. This tool provides:
- C++ query resolutions
- Code improvement suggestions
- Function generation based on descriptions

## Features
1. **C++ Query Helper**: Ask questions about C++ programming.
2. **Code Improvement**: Get suggestions to improve your C++ code.
3. **Function Generator**: Generate C++ functions from descriptions.

## Requirements
- Python 3.10+
- OpenAI API Key

## Setup

### Step 1: Clone the Repository

git clone https://github.com/BlackDok7/CppHelper.git
cd cpp-helper-api

### Step 2: Install Dependencies

pip install -r requirements.txt

### Step 3: Set Environment Variables

Fill the .env with your OpenAI Key

### Step 4: Run the application

python app.py

#The API will run on http://127.0.0.1:5000

### Additional: Docker setup

docker build -t cpp-helper-api .
docker run -p 5000:5000 cpp-helper-api

