# Tic-Tac-Toe AI
### CodSoft AI Internship | Task 2

## 📌 About
An unbeatable Tic-Tac-Toe AI built with Python (Flask) using the **Minimax algorithm with Alpha-Beta Pruning**.

## 🧠 How the AI Works
- **Minimax:** Recursively explores all possible game states, maximizing AI's score and minimizing human's score.
- **Alpha-Beta Pruning:** Prunes branches that can't affect the final decision, making the algorithm significantly faster.
- The AI is **unbeatable** — the best a human can do is draw.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Algorithm:** Minimax + Alpha-Beta Pruning

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install flask
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
```
http://127.0.0.1:5000
```

## 📁 Project Structure
```
tictactoe/
├── app.py               # Flask backend + Minimax AI
├── requirements.txt
├── README.md
└── templates/
    └── index.html       # Game UI
```

## 🎮 Features
- Unbeatable AI using Minimax + Alpha-Beta Pruning
- Score tracking across games
- Choose who goes first (You or AI)
- Win highlighting animation
- Clean dark-themed UI
