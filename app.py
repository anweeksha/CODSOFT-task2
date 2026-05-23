from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ──────────────────────────────────────────
#  GAME LOGIC
# ──────────────────────────────────────────

def check_winner(board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    for combo in wins:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return board[a], combo
    return None, None

def is_full(board):
    return all(cell != '' for cell in board)

def minimax(board, depth, is_maximizing, alpha, beta):
    winner, _ = check_winner(board)
    if winner == 'O': return 10 - depth   # AI wins
    if winner == 'X': return depth - 10   # Human wins
    if is_full(board): return 0            # Draw

    if is_maximizing:
        best = -1000
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ''
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break  # Beta cutoff
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ''
                best = min(best, score)
                beta = min(beta, best)
                if beta <= alpha:
                    break  # Alpha cutoff
        return best

def best_move(board):
    best_score = -1000
    move = -1
    for i in range(9):
        if board[i] == '':
            board[i] = 'O'
            score = minimax(board, 0, False, -1000, 1000)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i
    return move

# ──────────────────────────────────────────
#  ROUTES
# ──────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ai_move', methods=['POST'])
def ai_move():
    data = request.get_json()
    board = data.get('board')  # list of 9: 'X', 'O', or ''

    winner, combo = check_winner(board)
    if winner or is_full(board):
        return jsonify({'move': -1})

    move = best_move(board)
    board[move] = 'O'

    winner, combo = check_winner(board)
    draw = is_full(board) and not winner

    return jsonify({
        'move': move,
        'winner': winner,
        'combo': combo,
        'draw': draw
    })

if __name__ == '__main__':
    app.run(debug=True)
