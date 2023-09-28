class character:
    
    def __init__(self,canvas,x, y, anc, img):
        self.canvas = canvas
        self.image = canvas.create_image(x,y, anchor=anc, image=img)
        
    def move(self, steps):
        coordinate = self.canvas.coords(self.image)
        self.canvas.move(self.image, steps,0)
        
class icon:
    def __init__(self,canvas,x1, y1,x2,y2, color, tag):
        self.canvas = canvas
        self.image = canvas.create_oval(x1, y1,x2,y2, fill=color,tags=tag)
        
    def move(self, steps):
        coordinate = self.canvas.coords(self.image)
        self.canvas.move(self.image, steps,0)
        
        
        
        