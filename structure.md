# Project Structure

## Classes

### Board
- Contains all the logic needed for moving pieces around the board
- Finds the moves that a piece can do for a given position
- Determines if the king is in check
- Determines if game is in checkmate
- Has as list matrix representing the actual squares on a chess board filled with Piece objects

### Piece
- Represents an actual chess piece
- Has attributes for the type of piece that it is, eg Queen, Bishop etc, along which colour it is (white or black)
- Each type of Piece has its own subclass, makes it easy for coding. These all override the type property. 
- Has an attribute for if it has been captured or not.

### Game
- Represents the state of the game
- Starts the game
- Method to return a dictionary of the current state of the game, ie the current scores of each player, to be parsed by 
the command line ui
- Method to find the scores of each player

### Player
- Represents a player in the chess game
- Has string attribute for the colour of their pieces
- Owns a list pieces
- Should keep track of which pieces are currently active
- Should keep track of their score

### CommandLineUI
- Class for code relating to the command line interface with players
- Should print a welcome message, should then ask players to enter their names
- Should print out a grid of the game to the command line

## Playing the game
- White player starts
- At the start of each turn, a player chooses the position of the piece that they would like to move. 
- When they select this position, they are then presented with the options of positions that they can move this piece to
- At the start of each turn, the current score of the game should be displayed
- When one player checkmates another, a message should be displayed declaring victory for one of the players, along with the
final score

### Niche features
- Must support en passant capturing
- Must support castling
- Must support pawn promotion, when this is done, the score for a player is refunded back based on the piece that the pawn is promoted to