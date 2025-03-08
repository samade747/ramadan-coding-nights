from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelancing - start offering your skills online",
    "Dropshipping - sell without handling inventory",
    "Stock market - live the life of a day trader",
    "Affiliate marketing - earn commission by promoting other people's products",
    "Social media influencer - become a brand ambassador",
    "Blogging - start a blog and monetize it",
    "YouTube - create videos and earn money through ads",
    "Podcasting - start a podcast and earn money through sponsorships",
    "E-commerce - start an online store",
    "Online courses - create and sell online courses",
    "App development - create and sell apps",
    "Web development - create and sell websites",
    "Graphic design - create and sell graphics",
    "Photography - sell your photos online",
    "Writing - write and sell books",
    "Consulting - offer consulting services",
    "Virtual assistant - offer virtual assistant services",
    "SEO - offer SEO services",
    "Copywriting - offer copywriting services",
    "Translation - offer translation services"
]

money_quotes = [
    "Money is a terrible thing. If you have it, you can afford anything.",
    "Formal education is the most expensive thing in the world.",
    "Education is the most powerful weapon which you can use to change the world.",
    "The more you learn, the more you earn."
]

# Correct API response format
@app.get("/side_hustles")
def get_side_hustles():
    return {"side_hustle": random.choice(side_hustles)}  # Returns a dictionary

@app.get("/money_quotes")  # Fixed endpoint name
def get_money_quotes():
    return {"money_quote": random.choice(money_quotes)}  # Returns a dictionary
