# visualised Sorting
import random

#bar charts
num = 100
bars = []
barW = 0
maxBarH = 0
c = 0
sortedI = 0

def setup():
    global bars, barW, maxBarH
    size(500,300)
    background(0,0,0)
    
    for i in range(num):
        bars.append(i+1)
    barW = width/len(bars)
    maxBarH = height/len(bars)
    random.shuffle(bars)

def selectionSort(nums,c):
    sI = 0
    smallest = 999999999
    drawBar(c,color(0,0,255))
    if c >= len(nums):
        return True
    for i in range(c,len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            sI = i
    drawBar(sI)
    nums[c], nums[sI] = nums[sI], nums[c]
    c += 1
    
def bubbleSort(nums,c):
    drawBar(c,color(0,0,255))
    if nums[c] > nums[c+1]:
        drawBar(c)
        nums[c], nums[c+1] = nums[c+1], nums[c]

def insertionSort(nums,c):
    global sortedI
    for i in range(sortedI):
        drawBar(i,color(0,255,0))
    drawBar(sortedI,color(0,0,255))
    drawBar(c)
    for i in range(sortedI)[::-1]:
        if nums[c] < nums[i]:
            nums[c], nums[i] = nums[i], nums[c]
            c -= 1
        else:
            break
        sortedI += 1
    
def mergeSort(nums, c):
    #compare items from two lists
    # TODO: figure this out!
    if nums[c] > nums[c+1]:
        drawBar(c)
        nums[c], nums[c+1] = nums[c+1], nums[c]

def quickSort(nums,c):
    #choose a midpoint
    mid = int(round(len(nums)/2))
    #for all values move left or right
    if c < mid:
        if nums[c] < nums[mid]:
            pass
        else:
            pass
        
            
def drawBar(i,col = color(255,0,0)):
    fill(col)
    rect(barW*i,height,barW,-bars[i]*maxBarH)

def drawBars():
    clear()
    for i in range(len(bars)):
        rect(barW*i,height,barW,-bars[i]*maxBarH)

def draw():
    global bars,c
    sorted = False
    if not sorted:
        if c+1 >= len(bars):
            c = 0
        fill(color(255,255,255))
        drawBars()
        #sorted = selectionSort(bars,c)
        sorted = bubbleSort(bars,c)
        #sorted = insertionSort(bars,c)
        #sorted = mergeSort(bars,c)
        #sorted = quickSort(bars,c)
        #delay(100)
        c+=1
    
    