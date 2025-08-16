import os
from flask import Flask, render_template, request
import google.generativeai as genai
import markdown  # pip install markdown

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    response_html = None
    user_prompt = None

    if request.method == "POST":
        user_prompt = request.form.get("prompt")
        if user_prompt:
            try:
                response = model.generate_content(user_prompt)
                # Convert Markdown to HTML for clean rendering
                response_html = markdown.markdown(response.text)
            except Exception as e:
                response_html = f"<p style='color:red;'>Error: {e}</p>"

    return render_template("index3.html", response=response_html, prompt=user_prompt)

if __name__ == "__main__":
    app.run(debug=True)
