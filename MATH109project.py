'''
MATH-109 project , proving the law of reflection
Requires: pip install matplotlib numpy
about: 
WHAT IS THE LAW OF REFLECTION?
The law of reflection states that when a ray of light reflects off a surface, the angle of reflection (𝜃𝑟)
is equal to the angle of incidence (𝜃𝑖)
relation to CALCULUS?
The law of reflection (𝜃𝑖=𝜃𝑟) is proven using calculus by applying Fermat's Principle, which
states that light takes the path of least time (or distance, in a uniform medium). 
By expressing the total path distance as a function of the reflection point, setting its derivative to zero,
and solving, the angle of incidence is shown to equal the angle of reflection.
'''




import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.patches import Arc
import numpy as np



# 
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.2)

current_step = 0 #To count where the user is right now..
final_steps = 27 #The maximum amount of steps 
angle_A_deg = np.degrees(np.arctan2(7 - 1, 0 - 5))  # Angle from mirror to source (0,7)
angle_B_deg = np.degrees(np.arctan2(7 - 1, 10 - 5)) # Angle from mirror to target (10,7)
def draw_steps():
     ax.clear()
     ax.set_xlim(-12, 12) #drawing the X axis
     ax.set_ylim(-12, 12) #drawing the Y axis


     ax.axhline(0, color='black', linewidth=2) 
     ax.plot([0, 0], [0, 12], color='black', linewidth=2) 

     # where the angle should be
     arc_A = Arc((5,1), width=4, height=4, angle=0, theta1=147, theta2=180, color='black', linewidth=1.5)
     arc_B = Arc((0, 1), width=4, height=4, angle=0, theta1=0, theta2=33, color='black', linewidth=1.5)
     # Base: Mirror
     ax.plot([0, 10], [1, 1], color='grey', linewidth=4, label="Mirror") #Plots the mirror

     if current_step >= 1: ax.plot(0, 7, marker='o', color='blue', markersize=10, label="Source") #Plots the source of the laser ray

     if current_step >= 2: ax.text(-2, 7, '(0,C)', fontsize=14, color='blue') # showing where is the source of the laser

     if current_step >= 3: ax.plot([0, 5], [7, 1], color='blue', linestyle='-', label="Laser ray") #plotting the laser

     if current_step >= 4: ax.text(4,0.25 , '(X,1)' ,fontsize=14, color='black')  # showing where did the laser hit

     if current_step >= 5: ax.plot([5, 10], [1, 7], color='green', linestyle='-', label="incidence Laser ray") # the reflection of the laser

     if current_step >= 6: ax.plot(10, 7, marker='o', color='green', markersize=10, label="incidence")

     if current_step >= 7: ax.text(9,8 , '(D,C)' ,fontsize=14, color='green')

     if current_step >= 8: ax.plot([0,5],[7,7],color='red', linestyle='-', label="X") #plotting the distance between the source and the reflection point

     if current_step >= 9: ax.text(2.5,7.5,"X",fontsize=14,color="red") #naming it X

     if current_step >= 10: ax.plot([5,10],[7,7],color='pink', linestyle='-', label="D-X") #plotting the distance between the reflection point to incidence

     if current_step >= 11: ax.text(7.5,7.5,"D-X",fontsize=14,color="pink") #naming it

     if current_step >= 12: ax.plot([5,5],[1,7],color='brown', linestyle='-', label="C") 

     if current_step >= 13: ax.text(4.5,3.5,"C",fontsize=14,color="brown")

     if current_step >= 14: #drawing the angle A
        arc_A = Arc((5, 1), width=3, height=3, angle=0, theta1=angle_A_deg, theta2=180, color='black', linewidth=1.5)
        ax.add_patch(arc_A)
        ax.text(2.8, 1.5, "A", fontsize=14, color='black', fontweight='bold')  

     if current_step >= 15:#drawing the angle B
        arc_B = Arc((5, 1), width=3, height=3, angle=0, theta1=0, theta2=angle_B_deg, color='black', linewidth=1.5)
        ax.add_patch(arc_B)
        ax.text(6.8, 1.5, "B", fontsize=14, color='black', fontweight='bold')

     if current_step >= 16: #finding where should the hyp values go
         rot_left = np.degrees(np.arctan2(1 - 7, 5 - 0)) 
         rot_right = np.degrees(np.arctan2(7 - 1, 10 - 5)) 
        
         ax.text(1.5, 1.5, r'$\sqrt{X^2 + C^2}$', fontsize=14, color="blue", 
         rotation=rot_left, ha='center', va='bottom')
        
         ax.text(9, 1.25, r'$\sqrt{(D-X)^2 + C^2}$', fontsize=14, color="green", 
         rotation=rot_right, ha='center', va='bottom')

     #proving the law of reflection
     if current_step >= 17: ax.text(-12, 10, r'$s = \sqrt{X^2 + C^2} + \sqrt{(D-X)^2 + C^2}$', fontsize=14)

     if current_step >= 18: ax.text(-12, 9, r"$s=vt \Rightarrow t= \frac{s}{v}$", fontsize=14) 

     if current_step >= 19: ax.text(-12, 8, r"$t'(X) = (\frac{1}{v}) (\frac{X}{\sqrt{X^2 + C^2}} - \frac{D-X}{\sqrt{(D-X)^2 + C^2}}) $", fontsize=14)

     if current_step >= 20: ax.text(-12,7,'t\'(X) = 0',fontsize=14)

     if current_step >= 21: ax.text(-12,6,r"$(\frac{1}{v}) (\frac{X}{\sqrt{X^2 + C^2}} - \frac{D-X}{\sqrt{(D-X)^2 + C^2}}) = 0 $", fontsize=14)

     if current_step >= 22: ax.text(-12,4,r"$\frac{X}{\sqrt{X^2 + C^2}} - \frac{D-X}{\sqrt{(D-X)^2 + C^2}} = 0 $", fontsize=14)

     if current_step >= 23: ax.text(-12,2,r"$\frac{X}{\sqrt{X^2 + C^2}} = \frac{D-X}{\sqrt{(D-X)^2 + C^2}}$", fontsize=14)

     if current_step >= 24: ax.text(-12,-2,r"$cos(A) = \frac{X}{\sqrt{X^2 + C^2}}$", fontsize=14)

     if current_step >= 25: ax.text(-12,-4,r"$cos(B) = \frac{D-X}{\sqrt{(D-X)^2 + C^2}}$", fontsize=14)

     if current_step >= 26:
         ax.text(-12,-6,"therefore", fontsize=14,fontweight='bold')
         ax.text(-12,-7,"cos(A) - cos(B) = 0", fontsize=14)

     if current_step >= 27:
         ax.text(-12,-8,"then", fontsize=14,fontweight='bold')
         ax.text(-12,-9," A = B", fontsize=14)


         




     ax.set_xlabel("X")
     ax.set_ylabel("Y")
     ax.set_title("Proving the Law of Reflection")
     ax.grid(True, linestyle='--', alpha=0.6)
     if current_step >= 0:
        ax.legend(loc='lower right', fontsize='small')
     plt.draw()

# Callback functions
def next_step(event):
    global current_step
    if current_step < final_steps:
        current_step += 1
        draw_steps()

def prev_step(event):
    global current_step
    if current_step > 0:
        current_step -= 1
        draw_steps()

# Button placement
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(next_step)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(prev_step)

draw_steps()
plt.show()