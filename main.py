from tkinter import *

class Window():
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.block_size = 20
        self.IN_GAME = True
        self.root = Tk()
        self.c = Canvas(self.root, width=self.WIDTH, height=self.HEIGHT, bg="#819ca3")

    def create_window(self):
        self.root.title("The best snake")
        self.c.grid()
        self.c.focus_set()
        self.root.mainloop()
    
class Block(Window):
    def __init__(self):
        Window.__init__(self)
        self.access = True
        self.block_size = 20
        self.block = self.c.create_rectangle(2*self.block_size, 0, 3*self.block_size, self.block_size, fill='#eba80e')
        self.root.bind('<Up>', lambda event, dir1 = 0, dir2 = -1 : self.bind_move(event, dir1, dir2))
        self.root.bind('<Down>', lambda event, dir1 = 0, dir2 = 1 : self.bind_move(event, dir1, dir2))
        self.root.bind('<Right>', lambda event, dir1 = 1, dir2 = 0 : self.bind_move(event, dir1, dir2))
        self.root.bind('<Left>', lambda event, dir1 = -1, dir2 = 0 : self.bind_move(event, dir1, dir2))
        self.run = self.root.after(500, lambda dir1 = 1, dir2 = 0 : self.moving(dir1, dir2))
        self.block1 = self.c.create_rectangle(self.block_size, 0, 2*self.block_size, self.block_size, fill='#eba80e')
        self.block2 = self.c.create_rectangle(0, 0, self.block_size, self.block_size, fill='#eba80e')
        self.block_list = [self.block, self.block1, self.block2]

    def moving(self, dir1, dir2):
        # змея двигается до тех пор, пока доступ разрешён
        if self.access == True:
            # перебираем все сегменты змеи с конца до головы (не включительно)
            for i in range(len(self.block_list)-1, 0, -1):
                # запоминаем координаты следующего блока
                x1 = self.c.coords(self.block_list[i-1])[0]
                y1 = self.c.coords(self.block_list[i-1])[1]
                # создаем новый блокт на том месте, координаты которого мы уже получили
                new_block = self.c.create_rectangle(x1, y1, x1 + self.block_size, y1 + self.block_size, fill='#eba80e')
                # удаляем старый блок
                self.c.delete(self.block_list[i])
                # обновляем координаты блока в листе сегментов змеи
                self.block_list[i] = new_block
            # c.move двигает блок головы в заданном направлении
            self.c.move(self.block, dir1 * self.block_size, dir2 * self.block_size)
            # заставляет повторить функцию передвижения змеи
            self.run = self.root.after(250, lambda dir1 = dir1, dir2 = dir2 : self.moving(dir1, dir2))

    def bind_move(self, event, dir1, dir2):
        self.root.after_cancel(self.run)
        self.moving(dir1, dir2)

def main():
    snake = Block()
    snake.create_window()

if __name__ == "__main__":
    main()