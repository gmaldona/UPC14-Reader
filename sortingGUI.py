from tkinter import *
import assignment1

currentSortingMethod = 'QUICKSORT'

def eventlistener_process():
    assignment1.sort(currentSortingMethod)
    
def eventlistener_quicksort():
    tag = 'QUICKSORT'
    currentSortingMethod = tag
    print(currentSortingMethod)
    updateButton(tag)

def eventlistener_radixsort():
    tag = 'RADIXSORT'
    currentSortingMethod = tag
    updateButton(tag)

def eventlistener_heapsort():
    tag = 'HEAPSORT'
    currentSortingMethod = tag
    updateButton(tag)

root = Tk()
root.title('UPC Sorter')
root.geometry('300x400')
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

label_main = Label(frame, text='Pick a Sorting Algorithm:', pady=50)
label_main.pack(side=TOP)

button_quit = Button(frame, text='QUIT', height=2, width=10, command=root.destroy, fg='#d11f1f')
button_quit.pack(side=BOTTOM)

button_process = Button(frame, text='PROCESS', height=2, width=10, command=eventlistener_process)
button_process.pack(side=BOTTOM)

padding = Label(frame, text='', pady=50)
padding.pack(side=BOTTOM)

button_quicksort = Button(frame, text='QUICKSORT', height=3, width=10, command=eventlistener_quicksort)
button_quicksort.pack(side=LEFT)

button_radixsort = Button(frame, text='RADIXSORT', height=3, width=10, command=eventlistener_radixsort)
button_radixsort.pack(side=LEFT)

button_heapsort = Button(frame, text='HEAPSORT', height=3, width=10, command=eventlistener_heapsort)
button_heapsort.pack(side=LEFT)

def updateButton(button):
    if button == 'QUICKSORT':
        button_quicksort['fg'] = '#006400'
        button_radixsort['fg'] = '#000000'
        button_heapsort['fg'] =  '#000000'
    elif button == 'HEAPSORT':
        button_quicksort['fg'] = '#000000'
        button_radixsort['fg'] = '#000000'
        button_heapsort['fg'] =  '#006400'
    elif button == 'RADIXSORT':
        button_quicksort['fg'] = '#000000'
        button_radixsort['fg'] = '#006400'
        button_heapsort['fg'] =  '#000000'
    
    
#button_heapsort = Button(frame, text="Blue", fg="blue")

root.mainloop()