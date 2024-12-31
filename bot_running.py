# from flask import Flask
# from threading import Thread

# app = Flask('')

# @app.route('/')
# def home():
#     return "Hello. The bot is running 🏃!"

# def run():
#   app.run(host='0.0.0.0',port=8080)

# def keep_alive():
#     t = Thread(target=run)
#     t.start()


from fastapi import FastAPI
import uvicorn
from threading import Thread

app = FastAPI()

@app.get('/')
async def home():
    return "Hello. The bot is running 🏃!"

def run():
    uvicorn.run(app, host='0.0.0.0', port=8080)

def run_bot():
    t = Thread(target=run)
    t.start()