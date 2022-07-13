import numpy as np
import pandas as pd

# ~ Функция с вызовом numpy
def my_numpy():
    arr=np.array([2033, 300.5, 1550, 2703, 5110, 2146, 4733, 7114, 1614,
     3105])
    print(arr)
    print(type(arr))
    
# ~ Функция с вызовом pandas
def my_pandas():
    a=[2033, 300.5, 1550, 2703, 5110, 2146, 4733, 7114, 1614, 3105]
    myvar=pd.Series(a)
    print(myvar)
    print("")
    print("{:.1f}".format(myvar[1]))    

# ~ Точка входа в программу
def main():
    my_numpy()
    print("")
    my_pandas()
    return 0

if __name__ == '__main__':
    main()
