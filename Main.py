import pygame as pg
from Settings import arr
import BubbleSort
import QuickSort
import MergeSort

def main():
    pg.init()
    BubbleSort.bubbleSort(arr)
    #QuickSort.quickSort(arr, 0, len(arr) - 1)
    #MergeSort.mergeSort(arr, 0, len(arr) - 1)
    pg.quit()
    exit()

if __name__ == '__main__':
    main()
