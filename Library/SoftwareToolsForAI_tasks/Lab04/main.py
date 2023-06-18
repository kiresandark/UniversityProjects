import time
import antClass as aC

if __name__ == "__main__":
    start_time = time.time() # сохранение времени начала выполнения
    aC.main() # выполнение кода
    print("time of execution: %s seconds" %abs (time.time() - start_time)) # вычисление времени выполнения
