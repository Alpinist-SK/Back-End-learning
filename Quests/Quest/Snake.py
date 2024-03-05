#Змейка
import random, time, copy, os
clear = lambda: os.system('cls')
clear()

class Map:
    def __init__(self, n = 40, speed = 0.02):
        self.map_size = n
        self.snake_speed = speed

    def map_add(self):                                #Метод для создания карты
        MAP = [["__" for i in range(self.map_size)], ]
        MAP_line = [["|", ] + ["  " for i in range(self.map_size - 1)] + ["|", ]]
        
        for i in range(self.map_size // 2):
            MAP += copy.deepcopy(MAP_line)        
        
        MAP += [["‾‾" for i in range(self.map_size)], ]
        return MAP
    
    def map_view(self, MAP):           #Метод для отображения карты
        for i in range(len(MAP)):
            for j in range(len(MAP[i])):
                print(MAP[i][j], end = "")
            print()


        
class Snake(Map):
   
    def snake_add(self):
        n = self.map_size
        MAP = self.map_add()
        MAP[n // 4][1] = "__"
        Map().map_view(MAP)
        return MAP
    
    def snake_move(self):
        n = self.map_size
        speed = self.snake_speed
        Map.__init__(self)
        MAP = self.snake_add()

        x, y = 1, n // 4
        while x < n + 1:
            time.sleep(speed)
            if x == n - 1:
                MAP[y][n - 1] = "  "
                MAP[y][1] = "__"
                x = 1
            else:
                MAP[y][x] = "  "
                MAP[y][x + 1] = "__"
                x += 1
            clear()
            Map().map_view(MAP)


        


    

Snake1 = Snake()
Snake1.snake_move()



