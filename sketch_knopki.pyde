penweight = 20
def setup():
    size(600,600)
    background(255)
    noStroke()
    
def draw():
    global penweight
    noStroke()
    fill(150)
    ellipse(200,500,20,20)
    ellipse(350,500,40,40)
    if mousePressed:
        strokeWeight(penweight)
        stroke(0)
        line(mouseX,mouseY,pmouseX,pmouseY)
        
        
def mouseClicked():
    global penweight
    if dist (mouseX,mouseY,200,500) <= 20:
        penweight = penweight - 5
    if dist (mouseX,mouseY,350,500) <= 40:
        penweight = penweight + 5
    if penweight <= 5:
        penweight = 5
    
