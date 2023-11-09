# Attempt at making a Chessbot

This is my attemt at building a ChessBot from scratch. I am first trying to come up with my own way of doing this before looking up existing methods. After which I will look up online how they make ChessBots. Here are the steps I believe I will need to take:

1) Board Representation
2) Piece Representation and Legal Moves
3) Move Generation - Making a move
4) Way to represent past data
5) Framework for making the model learn
6) To be decided after 5

# Step 1: Board Representation

After some thinking I have come to realise that I can represent the board as a 8 x 8 matrix. So each square on the board is a space in the matrix representing the piece it is. Each of the even x even square is a black square and each of the odd x odd square is a white square. The chess board is traditionally represented with letters and numbers, with a1 being the bottom left square and h8 being the top left. In my representation of the Board the the bottom left is a (0,0) square, and the top right is a (7,7) square. So for a position in the array (x,y), x represents the rank(1,2,...,8) and y represents the file(a,b,...,h). To do this I representing a board as a simple numpy array.

# Step 2: Piece Representation and Legal Moves
