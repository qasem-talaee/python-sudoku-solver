
class Solver:

    def __init__(self, table):
        self.table = table
        self.moves = []
        self.area = [[], [], [], [], [], [], [], [], []]
        self.find_empty()
        self.init_area()
    
    def init_area(self):
        my_rows = [0, 1, 2]
        my_cols = [0, 1, 2]
        area_counter = 0
        for _ in range(3):
            my_cols = [0, 1, 2]
            for _ in range(3):
                for i in my_rows:
                    for j in my_cols:
                        self.area[area_counter].append([i, j])
                my_cols = [x+3 for x in my_cols]
                area_counter += 1
            my_rows = [x+3 for x in my_rows]
    
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.table[i][j] == 0:
                    self.moves.append([i, j, []])
    
    def check(self, j, move):
        row = self.moves[move][0]
        col = self.moves[move][1]
        numbers = []
        for i in range(len(self.moves)):
            if self.moves[i][0] == row:
                if len(self.moves[i][2]) != 0:
                    numbers.append(self.moves[i][2][-1])
        for i in range(len(self.moves)):
            if self.moves[i][1] == col:
                if len(self.moves[i][2]) != 0:
                    numbers.append(self.moves[i][2][-1])
        if j not in numbers:
            return True
        else:
            return False
    
    def check_area(self, j, move):
        row = self.moves[move][0]
        col = self.moves[move][1]
        area = 0
        for i in range(9):
            if [row, col] in self.area[i]:
                area = i
                break
        for i in range(9):
            my_row = self.area[area][i][0]
            my_col = self.area[area][i][1]
            if self.table[my_row][my_col] != 0:
                if self.table[my_row][my_col] == j:
                    return False
            else:
                move = 0
                for q in range(len(self.moves)):
                    if self.moves[q][0] == my_row and self.moves[q][1] == my_col:
                        move = q
                        break
                if len(self.moves[move][2]) != 0:
                    if self.moves[move][2][-1] == j:
                        return False
        return True
    
    def find_not_used(self, move):
        row = self.moves[move][0]
        col = self.moves[move][1]
        rows_num = []
        cols_num = []
        for i in range(9):
            if self.table[row][i] != 0:
                rows_num.append(self.table[row][i])
        for i in range(9):
            if self.table[i][col] != 0:
                cols_num.append(self.table[i][col])
        for i in range(1, 10):
            if i not in rows_num:
                if i not in cols_num:
                    if i not in self.moves[move][2]:
                        if self.check(i, move):
                            if self.check_area(i, move):
                                self.moves[move][2].append(i)
                                return True
        return False

    def result(self):
        for i in range(len(self.moves)):
            row = self.moves[i][0]
            col = self.moves[i][1]
            out = self.moves[i][2][-1]
            self.table[row][col] = out
        print('Your solved sudoku : \n')
        for i in range(9):
            for j in range(9):
                print(str(self.table[i][j]), end='  ')
            print()

        
    def del_after(self, i):
        for j in range(i, len(self.moves)):
            self.moves[j][2] = []
    
    def run(self):
        print('Solving...Please wait\n')
        i = 0
        step = 0
        while i != len(self.moves):
            if not self.find_not_used(i):
                self.del_after(i)
                i -= 1
            else:
                i += 1
            step += 1
        print('Your sudoku sloved in {step} step(s).'.format(step=step))
        self.result()