import sys; args = sys.argv[1:]
cols = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}

def display2D(board, canMove):
   if canMove:
      for m in canMove:
         board = board[0:m] + "*" + board[m+1:]
   for i in range(0,64,8):
      print(board[i:i+8])

def getMoves(board, toMove):
   toCheck = ""
   if toMove == "o": toCheck = "x"
   else: toCheck = "o"
   moves = set()
   for i in range(64):
      if board[i] == toMove:
         canPlace = False
         dotI = -1
         for j in range(i, 64, 8):
            if board[j] == toCheck: canPlace = True
            if (board[j] == toMove or board[j] == "*") and j != i: canPlace = False; break
            if board[j] == '.': dotI = j; break
         if canPlace: moves.add(dotI); canPlace = False
         dotI = -1
         for j in range(i, -1, -8):  
            if board[j] == toCheck: canPlace = True
            if (board[j] == toMove or board[j] == "*") and j != i: canPlace = False; break
            if board[j] == '.': dotI = j; break
         if canPlace: moves.add(dotI); canPlace = False
         dotI = -1
         for j in range(i, i + (8 - i % 8)):  
            if board[j] == toCheck: canPlace = True
            if (board[j] == toMove or board[j] == "*") and j != i: canPlace = False; break
            if board[j] == '.': dotI = j; break
         if canPlace: moves.add(dotI); canPlace = False
         dotI = -1
         for j in range(i , i + (8 - i % 8) - 9, -1):  
            if board[j] == toCheck: canPlace = True
            if (board[j] == toMove or board[j] == "*") and j != i: canPlace = False; break
            if board[j] == '.': dotI = j; break
         if canPlace: moves.add(dotI); canPlace = False
         dotI = -1
         for j in range(i , 64, 9):  
            if board[j] == '.': dotI = j; break
            if (j+(8-j%8)-1) == j: canPlace = False; break
            if board[j] == toCheck: canPlace = True
            if (board[j] == toMove or board[j] == "*") and j != i: canPlace = False; break
         if canPlace: moves.add(dotI); canPlace = False
         dotI = -1
         for j in range(i , 64, 7):  
            if board[j] == '.': dotI = j; break
            if (j+(8-j%8)-8) == j: canPlace = False; break
            if board[j] == toCheck: canPlace = True
            if (board[j] == toMove or board[j] == "*") and j != i: canPlace = False; break
         if canPlace: moves.add(dotI); canPlace = False
         dotI = -1
         for j in range(i, -1, -9):
            if board[j] == '.': dotI = j; break
            if (j+(8-j%8)-8) == j: canPlace = False; break
            if (board[j] == toMove or board[j] == "*") and j != i: canPlace = False; break
            if board[j] == toCheck: canPlace = True
         if canPlace: moves.add(dotI); canPlace = False
         dotI = -1
         for j in range(i , -1, -7):  
            if board[j] == '.': dotI = j; break
            if (j+(8-j%8)-1) == j: canPlace = False; break
            if board[j] == toCheck: canPlace = True
            if (board[j] == toMove or board[j] == "*") and j != i: canPlace = False; break
         if canPlace: moves.add(dotI); canPlace = False
         dotI = -1
   if -1 in moves: moves.remove(-1)
   return moves

def makeMove(moveIndex, toPlay):
   toCheck = ""
   if toPlay == "o": toCheck = "x"
   else: toCheck = "o"

   newBoard = board[0:moveIndex] + toPlay + board[moveIndex+1:]

   change = []
   toChange = False

   temp = []
   for j in range(moveIndex, moveIndex + (8 - moveIndex % 8)):
      if j == moveIndex: continue
      if board[j] == toPlay: toChange = True; break
      if board[j] != toCheck: toChange = False; break
      temp.append(j)
   if toChange: change += temp
   temp = []; toChange = False
   for j in range(moveIndex, 64, 8):
      if j == moveIndex: continue
      if board[j] == toPlay: toChange = True; break
      if board[j] != toCheck: toChange = False; break
      temp.append(j)
   if toChange: change += temp
   temp = []; toChange = False
   for j in range(moveIndex, -1, -8):
      if j == moveIndex: continue
      if board[j] == toPlay: toChange = True; break
      if board[j] != toCheck: toChange = False; break
      temp.append(j)
   if toChange: change += temp
   temp = []; toChange = False
   for j in range(moveIndex, moveIndex + (8 - moveIndex % 8) - 9, -1):
      if j == moveIndex: continue
      if board[j] == toPlay: toChange = True; break
      if board[j] != toCheck: toChange = False; break
      temp.append(j)
   if toChange: change += temp
   temp = []; toChange = False
   for j in range(moveIndex, 64, 9):
      if board[j] == toPlay: toChange = True; break
      if (j+(8-j%8)-1) == j: toChange = False; break
      if j == moveIndex: continue
      if board[j] != toCheck: toChange = False; break
      temp.append(j)
   if toChange: change += temp
   temp = []; toChange = False
   for j in range(moveIndex, 64, 7):
      if board[j] == toPlay: toChange = True; break
      if (j+(8-j%8)-8) == j: toChange = False; break
      if j == moveIndex: continue
      if board[j] != toCheck: toChange = False; break
      temp.append(j)
   if toChange: change += temp
   temp = []; toChange = False
   for j in range(moveIndex, -1, -9):
      if board[j] == toPlay: toChange = True; break
      if (j+(8-j%8)-8) == j: toChange = False; break
      if j == moveIndex: continue
      if board[j] != toCheck: toChange = False; break
      temp.append(j)
   if toChange: change += temp
   temp = []; toChange = False
   for j in range(moveIndex, -1, -7):
      if board[j] == toPlay: toChange = True; break
      if (j+(8-j%8)-1) == j: toChange = False; break
      if j == moveIndex: continue
      if board[j] != toCheck: toChange = False; break
      temp.append(j)
   if toChange: change += temp
   temp = []; toChange = False

   for c in change:
      newBoard = newBoard[0:c] + toPlay + newBoard[c+1:]

   if toPlay == "x": toPlay = "o"
   else: toPlay = "x"
   return newBoard, toPlay

def quickMove(brd, tkn):
   posMoves = getMoves(brd, tkn)
   return [*posMoves][0]

def main():
   global board; global toPlay; global moves
   board = '.'*27+'ox......xo'+'.'*27
   toPlay = "X"
   moves = []
   for arg in args:
      if arg.isnumeric(): moves.append(arg)
      elif len(arg) == 1: toPlay = arg.lower()
      elif len(arg) == 64: board = arg.lower()
      elif len(arg) == 2:
         temp = arg[0].upper()
         if temp == "-": moves.append(arg)
         else:
            index = 0
            index += cols[temp]
            index += (int(arg[1]) - 1) * 8
            moves.append(index)
      board = board.lower()
   if toPlay == "X":
      if ((64-board.count(".")) % 2) != 0: toPlay = "o"
      else: toPlay = "x"
   canMove = getMoves(board, toPlay)
   if moves:
      if int(moves[0]) in canMove:
         display2D(board, canMove)
         print("")
         print(f"{board} {board.count('x')}/{board.count('o')}")
         if canMove:
            print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
         else:
            print("No moves possible")
      else:
         if toPlay == "x": toPlay = "o"
         else: toPlay = "x"
         canMove = getMoves(board, toPlay)
         display2D(board, canMove)
         print("")
         print(f"{board} {board.count('x')}/{board.count('o')}")
         if canMove:
            print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
         else:
            print("No moves possible")
   else:
      display2D(board, canMove)
      print("")
      print(f"{board} {board.count('x')}/{board.count('o')}")
      if len(canMove) == 0:
         if toPlay == "x": toPlay = "o"
         else: toPlay = "x"
      canMove = getMoves(board, toPlay)
      if canMove:
         print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
      else:
         print("No moves possible")
   for i, move in enumerate(moves):
      if move == "-2": continue
      if move == "-1":
         if i != 0:
            if toPlay == "x": toPlay = "o"
            else: toPlay = "x"
         continue
      else:
         print("")
         print(f"{toPlay} plays to {move}")
         made = makeMove(int(move), toPlay)
         board = made[0]
         toPlay = made[1]
         canMove = getMoves(board, toPlay) 
         display2D(board, canMove)
         print("")
         print(f"{board} {board.count('x')}/{board.count('o')}")
         if canMove:
            print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
         else:
            if i == len(moves) - 1:
               if toPlay == "x": toPlay = "o"
               else: toPlay = "x"
               canMove = getMoves(board, toPlay) 
               if canMove:
                  print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
               else:
                  print("No moves possible")
            elif moves[i+1] != "-1":
               if toPlay == "x": toPlay = "o"
               else: toPlay = "x"
               canMove = getMoves(board, toPlay) 
               print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
            else:
               temp = ""
               if toPlay == "x": temp = "o"
               else: temp = "x"
               canMove = getMoves(board, temp) 
               print(f"Possible moves for {temp}: {', '.join(str(move) for move in canMove)}")
   if len(getMoves(board, toPlay)) != 0:
      mypref = quickMove(board, toPlay)
      print(f"The preferred move is: {mypref}")

if __name__ == '__main__': main()

# Zachary Baker, Pd. 4, 2024