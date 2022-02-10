import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
button.config(text= 'Turn light on')
window['bg'] = 'black'
def clickButton(event):
    if button.config('text')[-1] == 'Turn light on':
        button.config(text= 'Turn light off')
        window['bg'] = 'yellow'
        print('Light is on')
    else:
        button.config(text= 'Turn light on')
        window['bg'] = 'black'
        print('Light is off')

button.bind('<Button-1>', clickButton)
# schijf hier tussen je code

window.mainloop()