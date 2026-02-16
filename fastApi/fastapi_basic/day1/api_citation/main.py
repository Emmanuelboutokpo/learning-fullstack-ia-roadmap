from fastapi import FastAPI
import random

app = FastAPI()

quotes = [
    {
        "author": "Albert Einstein",
        "quote": "Life is like riding a bicycle. To keep your balance you must keep moving."
    },
    {
        "author": "Oscar Wilde",
        "quote": "Be yourself; everyone else is already taken."
    },
    {
        "author": "Marilyn Monroe",
        "quote": "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best."
    },
    {
        "author": "Nelson Mandela",
        "quote": "The greatest glory in living lies not in never falling, but in rising every time we fall."
    },
    {
        "author": "Mahatma Gandhi",
        "quote": "Be the change that you wish to see in the world."
    },
    {
        "author": "Martin Luther King Jr.",
        "quote": "Darkness cannot drive out darkness; only light can do that."
    },
    {
        "author": "Mother Teresa",
        "quote": "Spread love everywhere you go. Let no one ever come to you without leaving happier."
    },
    {
        "author": "Mark Twain",
        "quote": "The secret of getting ahead is getting started."
    },
    {
        "author": "Confucius",
        "quote": "It does not matter how slowly you go as long as you do not stop."
    },
    {
        "author": "Winston Churchill",
        "quote": "Success is not final, failure is not fatal: it is the courage to continue that counts."
    }
]


@app.get("/quote/random")
async def get_random_quote() :
    return random.choice(quotes)