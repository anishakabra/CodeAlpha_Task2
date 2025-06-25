import tkinter as tk
from tkinter import messagebox

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3300,
    "MSFT": 320
}

portfolio = {}

def add_stock():
    stock = stock_entry.get().upper()
    try:
        qty = int(qty_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Quantity must be a number.")
        return

    if stock in stock_prices:
        if stock in portfolio:
            portfolio[stock] += qty
        else:
            portfolio[stock] = qty
        result_text.insert(tk.END, f"Added: {stock} x{qty}\n")
        stock_entry.delete(0, tk.END)
        qty_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Stock Not Found", f"{stock} is not in the price list.")

def calculate_total():
    total = 0
    result_text.insert(tk.END, "\n--- Investment Summary ---\n")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        result_text.insert(tk.END, f"{stock} ({qty} shares) = ${value}\n")
        total += value
    result_text.insert(tk.END, f"\nTotal Investment: ${total}\n")

def save_to_file():
    try:
        with open("portfolio.txt", "w") as f:
            f.write("--- Investment Summary ---\n")
            total = 0
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                f.write(f"{stock} ({qty} shares) = ${value}\n")
                total += value
            f.write(f"\nTotal Investment: ${total}\n")
        messagebox.showinfo("Saved", "Portfolio saved to portfolio.txt")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Stock Portfolio Tracker")
root.geometry("400x500")
root.config(bg="lightblue")

tk.Label(root, text="Stock Symbol:", bg="lightblue").pack()
stock_entry = tk.Entry(root)
stock_entry.pack(pady=5)

tk.Label(root, text="Quantity:", bg="lightblue").pack()
qty_entry = tk.Entry(root)
qty_entry.pack(pady=5)

tk.Button(root, text="Add Stock", command=add_stock, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Calculate Total", command=calculate_total, bg="orange").pack(pady=5)
tk.Button(root, text="Save to File", command=save_to_file, bg="lightgray").pack(pady=5)

result_text = tk.Text(root, height=15, width=50)
result_text.pack(pady=10)

root.mainloop()
