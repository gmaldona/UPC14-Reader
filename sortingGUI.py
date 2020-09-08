from tkinter import *
import assignment1

print('***+++ To run assignment without the GUI, enter the interactive python shell +++***')
print('***+++ python3 -i assignment1.py +++***')
        
class Method:
    method = ''
    
    def setCurrent(self, method):
        self.method = method
        
    def getCurrent(self):
        return self.method
        
method = Method()

def eventlistener_process():
    assignment1.sort(method.getCurrent(), False, 0)
    
def eventlistener_quicksort(button_quicksort, button_radixsort, button_heapsort):
    tag = 'QUICKSORT'
    method.setCurrent(tag)
    updateButton(tag, button_quicksort, button_radixsort, button_heapsort)

def eventlistener_radixsort(button_quicksort, button_radixsort, button_heapsort):
    tag = 'RADIXSORT'
    method.setCurrent(tag)
    updateButton(tag, button_quicksort, button_radixsort, button_heapsort)

def eventlistener_heapsort(button_quicksort, button_radixsort, button_heapsort):
    tag = 'HEAPSORT'
    method.setCurrent(tag)
    updateButton(tag, button_quicksort, button_radixsort, button_heapsort)
    
def run():
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

    button_quicksort = Button(frame, text='QUICKSORT', height=3, width=10)
    button_quicksort.pack(side=LEFT)

    button_radixsort = Button(frame, text='RADIXSORT', height=3, width=10, command=eventlistener_radixsort)
    button_radixsort.pack(side=LEFT)

    button_heapsort = Button(frame, text='HEAPSORT', height=3, width=10, command=eventlistener_heapsort)
    button_heapsort.pack(side=LEFT)
                              
    button_quicksort['command'] = (lambda 
                                   
                            button_qs=button_quicksort,
                            button_rs=button_radixsort,
                            button_hs=button_heapsort
                              
                            : eventlistener_quicksort(button_qs, button_rs, button_hs)  
                                   
                                   )
    
    button_radixsort['command'] = (lambda 
                                   
                            button_qs=button_quicksort,
                            button_rs=button_radixsort,
                            button_hs=button_heapsort
                              
                            : eventlistener_radixsort(button_qs, button_rs, button_hs)  
                                   
                                   )
    
    button_heapsort['command'] = (lambda 
                                   
                            button_qs=button_quicksort,
                            button_rs=button_radixsort,
                            button_hs=button_heapsort
                              
                            : eventlistener_heapsort(button_qs, button_rs, button_hs)  
                                   
                                   )
    
    root.mainloop()

def updateButton(method, button_quicksort, button_radixsort, button_heapsort):  
    if method == 'QUICKSORT':
        button_quicksort['fg'] = '#33FF39'
        button_radixsort['fg'] = '#000000'
        button_heapsort['fg'] =  '#000000'
    elif method == 'HEAPSORT':
        button_quicksort['fg'] = '#000000'
        button_radixsort['fg'] = '#000000'
        button_heapsort['fg'] =  '#33FF39'
    elif method == 'RADIXSORT':
        button_quicksort['fg'] = '#000000'
        button_radixsort['fg'] = '#33FF39'
        button_heapsort['fg'] =  '#000000'
        
        
    #button_heapsort = Button(frame, text="Blue", fg="blue")

if __name__  == '__main__':
    run()