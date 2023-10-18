
import tkinter as tk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import math
import numpy as np


sigma_x = 5000
sigma_y = 20000
tau_xy = 2000

tau_r = math.sqrt(pow((sigma_x-sigma_y)/2,2)+pow(tau_xy,2))

sigma_a  = ((sigma_x+sigma_y)/2) - tau_r
sigma_b  = ((sigma_x+sigma_y)/2) + tau_r    


  
# plot function is created for  
# plotting the graph in  
# tkinter window 
def validate_input(P):
    # This function is called whenever a key is pressed in the Entry widget.
    if P.isdigit() or P == "":
        return True
    else:
        print("invalid input detected")
        return False

def plot(): 
  
    sigma_x = int(E1.get()) # this should be int
    sigma_y = int(E2.get()) 
    tau_xy = int(E3.get())

    tau_r = math.sqrt(pow((sigma_x-sigma_y)/2,2)+pow(tau_xy,2))

    sigma_a  = ((sigma_x+sigma_y)/2) - tau_r
    sigma_b  = ((sigma_x+sigma_y)/2) + tau_r    
    
    f_tau_r = f"{tau_r:.2f}"
    f_sigma_a = f"{sigma_a:.2f}"
    f_sigma_b = f"{sigma_b:.2f}"

    print(f_tau_r) 
    print(f_sigma_a)
    print(f_sigma_b)

    # the figure that will contain the plot 
    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
    plot1 = fig.add_subplot(111) 




  
    # Generate data for a circle
    theta = np.linspace(0, 2 * np.pi, 100)
    radius = 1.0  # You can adjust the radius as needed
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # plotting the graph 
    plot1.plot(x,y)   


    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().grid(row = 5, column = 0) 
  
            # # creating the Matplotlib toolbar 
            # toolbar = NavigationToolbar2Tk(canvas, 
            #                                window) 
            # toolbar.update() 
        
            # # placing the toolbar on the Tkinter window 
            # canvas.get_tk_widget().grid(row = 6, column = 0) 
        
# the main Tkinter window 
window = tk.Tk() 
  
# setting the title  
window.title('Mohrs Cirle') 
  
# dimensions of the main window 
window.geometry("500x500") 
  
# button that displays the plot 
plot_button = tk.Button(master = window,  
                     command = plot, 
                     height = 2,  
                     width = 10, 
                     text = "Plot") 


validate_input_cmd = window.register(validate_input)

L1 = tk.Label(master = window, text="sigma_x")
E1 = tk.Entry(master = window, bd =5, validate = "key", validatecommand=(validate_input_cmd, "%P"))

L2 = tk.Label(master = window, text="sigma_y")
E2 = tk.Entry(master = window, bd =5, validate = "key", validatecommand=(validate_input_cmd, "%P"))

L3 = tk.Label(master = window, text="Tau_xy")
E3 = tk.Entry(master = window, bd =5, validate = "key", validatecommand=(validate_input_cmd, "%P"))

# place the entries in the main window 
plot_button.grid(row = 3, column = 0) 

L1.grid( row = 0, column = 0, sticky = tk.W, pady = 2)
E1.grid( row = 0, column = 2, sticky = tk.E, pady = 2)
E1.insert(0,"5000")
  
L2.grid( row = 1, column = 0, sticky = tk.W , pady = 2)
E2.grid( row = 1, column = 2, sticky = tk.E , pady = 2)
E2.insert(0,"20000")

L3.grid( row = 2, column = 0, sticky = tk.W, pady = 2)
E3.grid( row = 2, column = 2, sticky = tk.E, pady = 2)
E3.insert(0,"2000")

# run the gui 
window.mainloop() 