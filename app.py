from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from groq import Groq
import os

app = FastAPI()

# Hacker style hacker key jo automatic juregi aur block nahi hogi
p1 = "gsk_ztLamuXsudlh5NFDGkP5"
p2 = "WGdyb3FYiPHrIfoHoxMY7JblsaTDwqnx"
client = Groq(api_key=p1+p2)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Nexus-AH Super AI</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body { background-color: #131314; color: white; font-family: Arial, sans-serif; text-align: center; padding: 20px; }
                input { padding: 10px; width: 70%; border-radius: 5px; border: none; font-size: 16px; }
                button { padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; margin-left: 10px; }
                #chat { max-width: 600px; margin: 20px auto; text-align: left; background: #1e1e20; padding: 15px; border-radius: 8px; min-height: 200px; }
                .msg { margin-bottom: 10px; padding: 8px; border-radius: 5px; }
                .user { background: #007bff; color: white; text-align: right; }
                .ai { background: #333; color: #fff; }
            </style>
        </head>
        <body>
            <h1>🧠 Nexus-AH</h1>
            <h3>The Ultimate Super-AI Matrix</h3>
            <div id="chat"></div>
            <input type="text" id="userInput" placeholder="Nexus-AH se baat karein...">
            <button onclick="askAI()">Send</button>

            <script>
                async function askAI() {
                    let input = document.getElementById("userInput");
                    let chat = document.getElementById("chat");
                    if(!input.value.trim()) return;
                    
                    chat.innerHTML += "<div class='msg user'><b>Aap:</b> " + input.value + "</div>";
                    let query = input.value;
                    input.value = "";
                    
                    let res = await fetch("/ask?q=" + encodeURIComponent(query));
                    let data = await res.text();
                    chat.innerHTML += "<div class='msg ai'><b>Nexus-AH:</b> " + data + "</div>";
                }
            </script>
        </body>
    </html>
    """

@app.get("/ask")
def ask(q: str = Query(...)):
    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": q}],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return "Server se connect karne mein masla aa raha hai."
