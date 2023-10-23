
import tkinter as tk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import math
import numpy as np


sigma_x = 5000
sigma_y = 20000
tau_xy = 2000

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
  
    #---------------------MATH--------------------------------------------
    sigma_x = int(E1.get()) # this should be int
    sigma_y = int(E2.get()) 
    tau_xy = int(E3.get())

    C_mohr = (sigma_x+sigma_y)/2
    tau_r = math.sqrt(pow((sigma_x-sigma_y)/2,2)+pow(tau_xy,2))
    
    sigma_a  = ((sigma_x+sigma_y)/2) - tau_r
    sigma_b  = ((sigma_x+sigma_y)/2) + tau_r    
    
    f_tau_r = f"{tau_r:.2f}"
    f_sigma_a = f"{sigma_a:.2f}"
    f_sigma_b = f"{sigma_b:.2f}"

    phi = math.atan(sigma_x/tau_xy)/2 # angle 
    
    
    
    # Generate data for the circle
    theta = np.linspace(0, 2 * np.pi, 100)
    radius = tau_r  # You can adjust the radius as needed
    x = C_mohr + radius * np.cos(theta)
    y = radius * np.sin(theta)



    #---------------------PLOTTING  --------------------------------------
    # the figure that will contain the plot 
    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
    plot1 = fig.add_subplot(111) 

    # plotting the graph 
    plot1.plot(x,y)   #Circle, Mohrs


    # point out important graphical points on the graph
    #max shear 
    arrowprops = dict(arrowstyle = "->", relpos=(0, .5),connectionstyle = "angle, angleA = 0, angleB = 90, rad= 10") 

    gap = 1 * radius # how long is this arrow fella - probs good to do a ratio thing, like in overlord 
    
    plot1.annotate('Max Shear: %.2f'%(radius), xy=(C_mohr,radius), xytext=((C_mohr - radius), 1.1 * radius ),
            arrowprops=arrowprops)

    plot1.annotate('Min Shear: %.2f'%(radius), xy=(C_mohr,-1 * radius), xytext=((C_mohr - .7 * radius), -1.2 * radius ),
            arrowprops=arrowprops)  

    plot1.text(C_mohr,.1*radius,"(%.2f, 0.0)" % C_mohr)

    # Set custom axis limits
    gp = 1.3 * radius # gap to the limits , in radians
    plot1.set_xlim(C_mohr - gp, C_mohr + gp)  # Set x-axis limits
    plot1.set_ylim(-gp, gp)  # Set y-axis limits

    # Make the axis lines visible
    plot1.spines['left'].set_visible(True)
    plot1.spines['right'].set_visible(True)
    plot1.spines['top'].set_visible(True)
    plot1.spines['bottom'].set_visible(True)

    plot1.axhline(0,color='red') # x = 0
    plot1.axvline(0,color='red') # y = 0

    #dots, at the end so they are in the front layer
    plot1.plot([sigma_y,sigma_x],[tau_xy,-tau_xy],linestyle = 'dotted') #Line for start state
    plot1.plot([sigma_y,sigma_y],[tau_xy,0],linestyle = 'dotted')
    plot1.plot([sigma_x,sigma_x],[-tau_xy,0],linestyle = 'dotted')

    plot1.scatter([C_mohr,C_mohr], [tau_r,-tau_r], c ="blue") #taumax dots
    plot1.scatter([sigma_a,sigma_b,C_mohr], [0, 0, 0], c = "black") #principle stresses and center

    # Add grid lines
    plot1.grid(True)  # note - does this even do anything? 

    #change Calculated values beloW
    L4.config(text = "Principal stress 1: %.2f" %sigma_a )
    L5.config(text = "Principal stress 2: %.2f" %sigma_b )
    L6.config(text = "Inplane shear stress: %.2f" %tau_r )


    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().grid(row = 5, column = 0, rowspan = 2, columnspan = 2) 
  
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
window.geometry("600x800") 
  
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

L4 = tk.Label(master = window, text="Principal stress 1: ")
L5 = tk.Label(master = window, text="Principal stress 2: ")
L6 = tk.Label(master = window, text="Inplane shear stress: ")
#NOTE: it would be fun to add the yield strengths. perhaps something with a dropdown? 

# place the entries in the main window 
plot_button.grid(row = 3, column = 0, rowspan = 2) 

L1.grid( row = 0, column = 0, sticky = tk.W, pady = 2)
E1.grid( row = 0, column = 1, sticky = tk.E, pady = 2)
E1.insert(0,str(sigma_x))

L2.grid( row = 1, column = 0, sticky = tk.W , pady = 2)
E2.grid( row = 1, column = 1, sticky = tk.E , pady = 2)
E2.insert(0,str(sigma_y))

L3.grid( row = 2, column = 0, sticky = tk.W, pady = 2)
E3.grid( row = 2, column = 1, sticky = tk.E, pady = 2)
E3.insert(0,str(tau_xy))

L4.grid( row = 7,  column = 0, sticky = tk.W, pady = 2)
L5.grid( row = 8,  column = 0, sticky = tk.W, pady = 2)
L6.grid( row = 9,  column = 0, sticky = tk.W, pady = 2)


plot() # initial graph 

# run the gui 
window.mainloop() 