import sys; args = sys.argv[1:]

cols = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
global NEGACACHE, MOVECACHE, MAKECACHE, MIDCACHE

NEGACACHE = dict()
MOVECACHE = dict()
MAKECACHE = dict()
MIDCACHE = dict()

global HOLELIMIT
HOLELIMIT = [8]

def display2D(board, canMove, move=-1):
   if canMove:
      for m in canMove:
         board = board[0:m] + "*" + board[m+1:]
   if move != -1: board = board[0:int(move)] + board[int(move)].upper() + board[int(move)+1:]
   for i in range(0,64,8):
      print(board[i:i+8])

def getNeighbors(index):
   neighbors = [index+1, index-1, index+8, index-8, index+7, index-7, index+9, index-9]
   if index == (index + (8 - index % 8)) - 1: neighbors.remove(index+1); neighbors.remove(index-7); neighbors.remove(index+9)
   if index == (index + (8 - index % 8) - 8): neighbors.remove(index-1); neighbors.remove(index-9); neighbors.remove(index+7)
   if index < 8: 
      neighbors.remove(index-8); 
      if index-9 in neighbors: neighbors.remove(index-9)
      if index-7 in neighbors: neighbors.remove(index-7)
   if index > 55: 
      neighbors.remove(index+8)
      if index+9 in neighbors: neighbors.remove(index+9)
      if index+7 in neighbors: neighbors.remove(index+7)
   return neighbors

def findMoves(board, toMove):
   if (board, toMove) in MOVECACHE: return MOVECACHE[(board, toMove)]
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
   MOVECACHE[(board, toMove)] = moves
   moves = sorted(moves, key=lambda x: x not in [0, 7, 56, 63])
   return moves

def makeMove(board, toPlay, moveIndex):
   if (board, toPlay, moveIndex) in MOVECACHE: return MOVECACHE[(board, toPlay, moveIndex)]
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
   MAKECACHE[(board, toPlay, moveIndex)] = (newBoard, toPlay)
   return newBoard, toPlay

def evaluateBoard(board, tkn):
   etkn = "x"
   if tkn == "x": etkn = "o"
   score = 0

   mstability = 0
   

   # check how many secure tokens are on the board. every token has 8 possible directions to go. the 8 directions are divided into 4 pairs. up and down, right and left, etc. every pair needs to have one direction that is filled with tokens up until a wall.
   for i in range(0, 64):
      tkns = [tkn, etkn]
      for token in tkns:
         otherTkn = "x"
         if token == "x": otherTkn = "o"
         if board[i] == token:
            # iterate down
            isSecure1 = True
            isSecure2 = True
            ultraSecure = True
            for j in range(i, 64, 8):
               if board[j] == otherTkn: isSecure1 = False; break
               if board[j] == ".": isSecure1 = False; ultraSecure = False; break
            for j in range(i, -1, -8):
               if board[j] == otherTkn: isSecure2 = False; break
               if board[j] == ".": isSecure2 = False; ultraSecure = False; break
            if isSecure1 or isSecure2:
               isSecure1 = True
               isSecure2 = True
               for j in range(i, i + (8 - i % 8)):
                  if board[j] == otherTkn: isSecure1 = False; break
                  if board[j] == ".": isSecure1 = False; ultraSecure = False; break
               for j in range(i, i + (8 - i % 8) - 9, -1):
                  if board[j] == ".": isSecure2 = False; ultraSecure = False; break
                  if board[j] == otherTkn: isSecure2 = False; break
               if isSecure1 or isSecure2:
                  isSecure1 = True
                  isSecure2 = True
                  for j in range(i, 64, 9):
                     if board[j] == ".": isSecure1 = False; ultraSecure = False; break
                     if board[j] == otherTkn: isSecure1 = False; break
                  for j in range(i, 64, -9):
                     if board[j] == ".": isSecure2 = False; ultraSecure = False; break
                     if board[j] == otherTkn: isSecure2 = False; break
                  if isSecure1 or isSecure2:
                     isSecure1 = True
                     isSecure2 = True
                     for j in range(i, 64, 7):
                        if board[j] == ".": isSecure1 = False; ultraSecure = False; break
                        if board[j] == otherTkn: isSecure1 = False; break
                     for j in range(i, -1, -7):
                        if board[j] == ".": isSecure2 = False; ultraSecure = False; break
                        if board[j] == etkn: isSecure2 = False; break
                     if isSecure1 or isSecure2:
                        if token == tkn: score += 1
                        else: score -= 1
                     else: 
                        if ultraSecure:
                           if token == tkn: score += 1
                           else: score -= 1

   if board[0] == tkn: score += 5
   if board[7] == tkn: score += 5
   if board[56] == tkn: score += 5
   if board[63] == tkn: score += 5
   if board[0] == etkn: score -= 5
   if board[7] == etkn: score -= 5
   if board[56] == etkn: score -= 5
   if board[63] == etkn: score -= 5

   score += len(findMoves(board, tkn)); score -= len(findMoves(board, etkn))

   # check if tokens are next to corners. if so, that is bad for that player
   # ntc1 = [0, 1, 8, 9]; ntc2 = [7, 6, 14, 15]; ntc3 = [56, 48, 49, 57]; ntc4 = [63, 62, 55, 54]
   # for c in [ntc1, ntc2, ntc3, ntc4]:
   #    for j in c[1:]:
   #       if board[j] == tkn and board[c[0]] == ".": score -= 1
   #       if board[j] == etkn and board[c[0]] == ".": score += 1 

   score += (board.count(tkn)-board.count(etkn))/(board.count(tkn)+board.count(etkn))

   # ea = [2, 3, 4, 5, 58, 59, 60, 61]; ed = [16, 24, 32, 40, 23, 31, 39, 47]
   # for i in ea:
   #    if board[i] == tkn:
   #       opponentMoves = findMoves(board, etkn)
   #       if not ((i-1) in opponentMoves) and not ((i+1) in opponentMoves): score += 1
   #    if board[i] == etkn:
   #       opponentMoves = findMoves(board, tkn)
   #       if not ((i-1) in opponentMoves) and not ((i+1) in opponentMoves): score -= 1
   # for i in ed:
   #    if board[i] == tkn:
   #       opponentMoves = findMoves(board, etkn)
   #       if not ((i-8) in opponentMoves) and not ((i+8) in opponentMoves): score += 1
   #    if board[i] == etkn:
   #       opponentMoves = findMoves(board, tkn)
   #       if not ((i-8) in opponentMoves) and not ((i+8) in opponentMoves): score -= 1

   return score

def alphabeta(brd, tkn, alpha, beta):
   global NEGACACHE
   if (brd, tkn, alpha, beta) in NEGACACHE: return NEGACACHE[(brd, tkn, alpha, beta)]

   etkn = ""
   if tkn == "x": etkn = "o"
   else: etkn = "x"
   if not findMoves(brd, tkn):
      if not findMoves(brd, etkn):
         return [brd.count(tkn)-brd.count(etkn)]
      ab = alphabeta(brd, etkn, -beta, -alpha)
      NEGACACHE[(brd, tkn, -beta, -alpha)] = ab
      return [-ab[0]] + ab[1:] + [-1]

   best = [alpha-1]
   for mv in findMoves(brd,tkn):
      ab = alphabeta(makeMove(brd, tkn, mv)[0], etkn, -beta, -alpha)
      NEGACACHE[(makeMove(brd, tkn, mv)[0], etkn, -beta, -alpha)] = ab
      if -ab[0] <= alpha: continue
      if -ab[0] > beta: return [-ab[0]]
      if -ab[0] > best[0]: best = [-ab[0]] + ab[1:] + [mv]
      alpha = -ab[0]+1
   NEGACACHE[(brd, tkn, alpha, beta)] = best
   return best

def midalphabeta(brd, tkn, alpha, beta, depth): 
   global MIDCACHE
   #if (brd, tkn, alpha, beta) in MIDCACHE: return MIDCACHE[(brd, tkn, alpha, beta)]

   etkn = ""
   if tkn == "x": etkn = "o"
   else: etkn = "x"

   if depth >= 4: return [evaluateBoard(brd, tkn)]

   if not findMoves(brd, tkn):
      if not findMoves(brd, etkn):
        return [evaluateBoard(brd, tkn)]
      ab = midalphabeta(brd, etkn, -beta, -alpha, depth+1)
      MIDCACHE[(brd, tkn, -beta, -alpha)] = ab
      return [-ab[0]] + ab[1:] + [-1]

   best = [alpha-1]
   for mv in findMoves(brd,tkn):
      ab = midalphabeta(makeMove(brd, tkn, mv)[0], etkn, -beta, -alpha, depth+1)
      MIDCACHE[(makeMove(brd, tkn, mv)[0], etkn, -beta, -alpha)] = ab
      if -ab[0] <= alpha: continue
      if -ab[0] > beta: return [-ab[0]]
      if -ab[0] > best[0]: best = [-ab[0]] + ab[1:] + [mv]
      alpha = -ab[0]+1
   MIDCACHE[(brd, tkn, alpha, beta)] = best
   return best

def quickMove(brd, tkn):
   if not brd: HOLELIMIT[0] = int(tkn); return

   posMoves = [*findMoves(brd, tkn)]

   if brd.count(".") < HOLELIMIT[0]:
      nm = alphabeta(brd, tkn, -100, 100)
      return nm[-1]
   else:
      nm = midalphabeta(brd, tkn, -1000, 1000, 0)
      return nm[-1]

def main():
   global board; global toPlay; global moves
   board = '.'*27+'ox......xo'+'.'*27
   toPlay = "X"
   moves = []
   for arg in args:
      if arg.isnumeric() and len(arg) < 3: moves.append(arg)
      elif arg[0:2] == "HL": HOLELIMIT[0] = int(arg[2:]);
      elif len(arg) == 1: toPlay = arg.lower()
      elif len(arg) == 64 and "." in arg: board = arg.lower()
      elif len(arg) == 2:
         temp = arg[0].upper()
         if temp == "-": moves.append(arg)
         else:
            index = 0
            index += cols[temp]
            index += (int(arg[1]) - 1) * 8
            moves.append(index)
      else:
         for i in range(0,len(arg),2):
            if arg[i] == "_": moves.append(arg[i+1])
            else: moves.append(arg[i:i+2])
      board = board.lower()
   if toPlay == "X":
      if ((64-board.count(".")) % 2) != 0: toPlay = "o"
      else: toPlay = "x"
   canMove = findMoves(board, toPlay)
   if moves:
      if int(moves[0]) in canMove:
         display2D(board, canMove)
         print("")
         print(f"{board} {board.count('x')}/{board.count('o')}")
         if canMove:
            print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
         # else:
         #    print("No moves possible")
      else:
         if toPlay == "x": toPlay = "o"
         else: toPlay = "x"
         canMove = findMoves(board, toPlay)
         display2D(board, canMove)
         print("")
         print(f"{board} {board.count('x')}/{board.count('o')}")
         if canMove:
            print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
         # else:
         #    print("No moves possible")
   else:
      canMove = findMoves(board, toPlay)
      if len(canMove) == 0:
         if toPlay == "x": toPlay = "o"
         else: toPlay = "x"
         canMove = findMoves(board, toPlay)
      display2D(board, canMove)
      print("")
      print(f"{board} {board.count('x')}/{board.count('o')}")
      if len(canMove) == 0:
         if toPlay == "x": toPlay = "o"
         else: toPlay = "x"
      canMove = findMoves(board, toPlay)
      if canMove:
         print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
      # else:
      #    print("No moves possible")
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
         made = makeMove(board, toPlay, int(move))
         board = made[0]
         toPlay = made[1]
         canMove = findMoves(board, toPlay) 
         display2D(board, canMove, move)
         print("")
         print(f"{board} {board.count('x')}/{board.count('o')}")
         if canMove:
            print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
         else:
            if i == len(moves) - 1:
               if toPlay == "x": toPlay = "o"
               else: toPlay = "x"
               canMove = findMoves(board, toPlay) 
               if canMove:
                  print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
               # else:
               #    print("No moves possible")
            elif moves[i+1] != "-1":
               if toPlay == "x": toPlay = "o"
               else: toPlay = "x"
               canMove = findMoves(board, toPlay) 
               print(f"Possible moves for {toPlay}: {', '.join(str(move) for move in canMove)}")
            else:
               temp = ""
               if toPlay == "x": temp = "o"
               else: temp = "x"
               canMove = findMoves(board, temp) 
               print(f"Possible moves for {temp}: {', '.join(str(move) for move in canMove)}")
   if len(findMoves(board, toPlay)) != 0:
      mypref = quickMove(board, toPlay)
      print(f"The preferred move is: {mypref}")
      if board.count(".") < HOLELIMIT[0]:
         nm = alphabeta(board, toPlay, -100, 100)
         print(f"Min score: {nm[0]}; move sequence: {nm[1:]}")

if __name__ == '__main__': main()

# Zachary Baker, Pd. 4, 2024