# Python OOP Coin System

This project implements a small **Object-Oriented Python system** that simulates coins, euro coins, a wallet, a piggy bank, a stack, and a queue.

It demonstrates OOP principles such as **classes**, **inheritance**, **encapsulation**, and data structure manipulation.

---

## 🔧 Features

### 🪙 `Coin` & `Eurocoin` classes
- `Coin` represents a generic coin with a value and a year.
- `Eurocoin` inherits from `Coin` and adds a `country` field and a simple euro-to-USD conversion method.
- Each coin can be "flipped" to randomly return **Head** or **Tail**.

---

### 👛 `Wallet`
- Stores a list of `Coin` objects.
- Add and remove coins.
- Sort coins by year.
- Compute the total sum of coin values.

---

### 🐷 `PiggyBank`
- Stores coins in a Python dictionary with:
  - **key** = coin value  
  - **value** = last year seen for that value
- Computes the sum of all coin values inside the piggy bank.

---

### 📚 `CoinStack` (LIFO)
- Classic stack implementation for `Coin` objects.
- `push_item()` to push a coin.
- `pop_item()` to pop the last coin.
- `top_of_stack()` to see the top coin on the stack.

---

### 📬 `CoinQueue` (FIFO)
- Simple queue implementation for `Coin` objects.
- `enqueue()` to add a coin to the queue.
- `dequeue()` to remove a coin from the front.

---

## 📁 File Included

- `coin_system.py`

---

## ▶️ How to Run

```bash
python coin_system.py
```
You will see:

Information about different euro coins.

Random coin flip results.

Wallet operations (add, sort, sum, remove).

Piggy bank aggregation.

Stack and queue operations.

🎓 What This Project Demonstrates
Object-Oriented Programming in Python

Inheritance (Eurocoin extends Coin)

Working with lists and dictionaries

Implementing stack (LIFO) and queue (FIFO) behavior

Clean and structured console-based logic
