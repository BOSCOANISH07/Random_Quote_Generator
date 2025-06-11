import tkinter as tk 
from tkinter import messagebox 
from transformers import pipeline 
import random 
import time 
generator = pipeline("text-generation", model="gpt2") 
themes = ["inspiration", "love", "life", "success", "happiness"] 
example_quotes = { 
    "inspiration": [ 
        "The best way to predict the future is to invent it.", 
        "Act as if what you do makes a difference. It does.", 
        "The only way to do great work is to love what you do.", 
        "Success is not the key to happiness. Happiness is the key to success.", 
        "The future belongs to those who believe in the beauty of their dreams.", 
        "It always seems impossible until it's done.", 
        "Don't watch the clock; do what it does. Keep going.", 
        "The only limit to our realization of tomorrow is our doubts of today.", 
        "The journey of a thousand miles begins with one step.", 
        "You miss 100% of the shots you don't take.", 
        "What lies behind us and what lies before us are tiny matters compared to what lies within us.", 
        "Success is not how high you have climbed, but how you make a positive difference to the world.", 
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", 
        "Everything you can imagine is real.", 
        "Your time is limited, don't waste it living someone else's life." 
    ], 
    "love": [ 
        "Love all, trust a few, do wrong to none.", 
        "Love is not about possession. Love is about appreciation.", 
        "The best thing to hold onto in life is each other.", 
        "You don’t have to be rich to love, but you have to be patient to make love last.", 
        "Love isn’t something you find. Love is something that finds you.", 
        "There is no remedy for love but to love more.", 
        "To love and be loved is to feel the sun from both sides.", 
        "In the end, love is not about what you say, but about what you do.", 
        "The greatest thing you'll ever learn is just to love and be loved in return.", 
        "Love is composed of a single soul inhabiting two bodies.", 
        "True love cannot be found where it does not exist, nor can it be denied where it does.", 
        "Love is the only reality, and it is not a mere sentiment. It is the ultimate truth that lies at the heart of creation.", 
        "Love is the flower you’ve got to let grow.", 
        "We are most alive when we're in love.", 
        "Love is a promise, love is a souvenir, once given never forgotten, never let it disappear." 
    ], 
    "life": [ 
        "Life is what happens when you're busy making other plans.", 
        "In the middle of every difficulty lies opportunity.", 
        "It is never too late to be what you might have been.", 
        "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well.", 
        "Don’t count the days, make the days count.", 
        "Life is really simple, but we insist on making it complicated.", 
        "The only impossible journey is the one you never begin.", 
        "The biggest adventure you can take is to live the life of your dreams.", 
        "Life is 10% what happens to us and 90% how we react to it.", 
        "Live life as if everything is rigged in your favor.", 
        "You only live once, but if you do it right, once is enough.", 
        "The purpose of life is to live it, to taste experience to the utmost, to reach out eagerly and without fear for newer and richer experience.", 
        "Life is short, and it is up to you to make it sweet.", 
        "A life spent making mistakes is not only more honorable but more useful than a life spent doing nothing.", 
        "Your life does not get better by chance, it gets better by change." 
    ], 
    "success": [ 

        "Success usually comes to those who are too busy to be looking for it.", 
        "Success is not final, failure is not fatal: It is the courage to continue that counts.", 
        "The road to success and the road to failure are almost exactly the same.", 
        "Don’t be afraid to give up the good to go for the great.", 
        "Success is walking from failure to failure with no loss of enthusiasm.", 
        "The only place where success comes before work is in the dictionary.", 
        "I find that the harder I work, the more luck I seem to have.", 
        "Success is the sum of small efforts, repeated day in and day out.", 
        "The key to success is to focus on goals, not obstacles.", 
        "Opportunities don't happen, you create them.", 
        "Success is not the key to happiness. Happiness is the key to success.", 
        "There is no elevator to success — you have to take the stairs.", 
        "Your success will be determined by your own confidence and fortitude.", 
        "Success is not in what you have, but who you are.", 
        "Success is the result of preparation, hard work, and learning from failure." 
    ], 
    "happiness": [ 
        "Happiness is not something ready-made. It comes from your own actions.", 
        "Happiness depends upon ourselves.", 
        "The purpose of life is to live it, to taste experience to the utmost, to reach out eagerly and without fear for newer and richer experience.", 
        "Happiness is when what you think, what you say, and what you do are in harmony.", 
        "For every minute you are angry, you lose sixty seconds of happiness.", 
        "Happiness is a choice, not a result. Nothing will make you happy until you choose to be happy.", 
        "Happiness is not the absence of problems, it's the ability to deal with them.", 
        "The more that you read, the more things you will know. The more that you learn, the more places you'll go.", 
        "Do more of what makes you happy.", 
        "Happiness is not having what you want. It is appreciating what you have.", 
        "There is no path to happiness: happiness is the path.", 
        "Happiness is not by chance, but by choice.", 
        "If you want to be happy, be.", 
        "To be happy, we must not be too concerned with others.", 
        "Happiness is the highest good." 
    ] 
} 
 
used_quotes = set() 
def generate_quote(theme): 
    """Generates a quote based on the theme or randomly selects one.""" 
    global used_quotes    
    if theme not in themes: 
        theme = random.choice(themes) 
    unused_quotes = [quote for quote in example_quotes[theme] if quote not in used_quotes] 
    if unused_quotes: 
        quote = random.choice(unused_quotes) 
        used_quotes.add(quote) 
    else: 
        prompt = f"Write a motivational quote about {theme}:" 
        try: 
            result = generator(prompt, max_length=50, num_return_sequences=1) 
            quote = result[0]["generated_text"] 
        except Exception as e: 
            quote = f"Error generating quote: {e}" 
        used_quotes.add(quote)   
    return quote 
def reset_quotes(): 
    """Clear the used quotes set to allow reuse and clear the display.""" 
    global used_quotes 
    used_quotes.clear() 
    quote_display.delete("1.0", tk.END) 
def display_quote(): 
    """Display the generated quote in the GUI with fade-in animation effect.""" 
    theme = theme_entry.get().strip().lower() 
    if not theme: 
        theme = random.choice(themes) 
    if theme not in themes: 
        messagebox.showerror("Invalid Theme", "Please enter a valid theme (e.g., inspiration,love, life, success, happiness).") 
        return 
    quote = generate_quote(theme) 
    quote_display.delete("1.0", tk.END) 
    for i in range(0, len(quote), 2): 
        quote_display.insert(tk.END, quote[i:i+2]) 
root.update() 
time.sleep(0.05) 
quote_display.insert(tk.END, f"\n\nTheme: {theme.capitalize()}\n") 
root = tk.Tk() 
root.title("Random Quote Generator with Machine Learning") 
root.geometry("600x500") 
root.configure(bg="#2C3E50") 
title_label = tk.Label(root, text="Random Quote Generator", font=("Orbitron", 18, "bold"), 
fg="#E74C3C", bg="#2C3E50") 
title_label.pack(pady=20) 
theme_label = tk.Label(root, text="Enter a theme (optional):", font=("Arial", 12), 
fg="#ECF0F1", bg="#2C3E50") 
theme_label.pack(pady=5) 
theme_entry = tk.Entry(root, font=("Arial", 12), width=30, relief="solid", bd=2, 
fg="#1ABC9C") 
theme_entry.pack(pady=5) 
def on_enter_generate(event): 
generate_button.config(bg="#3498DB", fg="white") 
def on_leave_generate(event): 
generate_button.config(bg="#2980B9", fg="white") 
generate_button = tk.Button(root, text="Generate Quote", font=("Arial", 14), bg="#2980B9", 
fg="white", command=display_quote) 
generate_button.pack(pady=20) 
generate_button.bind("<Enter>", on_enter_generate) 
generate_button.bind("<Leave>", on_leave_generate) 
def on_enter_reset(event): 
reset_button.config(bg="#E74C3C", fg="white") 
def on_leave_reset(event): 
reset_button.config(bg="#C0392B", fg="white") 
reset_button = tk.Button(root, text="Reset Quotes", font=("Arial", 14), bg="#C0392B", 
fg="white", command=reset_quotes) 
reset_button.pack(pady=5) 
reset_button.bind("<Enter>", on_enter_reset) 
reset_button.bind("<Leave>", on_leave_reset) 
quote_display = tk.Text(root, font=("Orbitron", 12), wrap="word", height=10, width=50, 
bg="#34495E", fg="#ECF0F1", bd=2, relief="solid") 
quote_display.pack(pady=10) 
root.mainloop()