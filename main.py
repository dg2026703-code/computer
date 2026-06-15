Web VPython 3.2


sphere(pos=vector(0,0,0))

box(pos=vector(0,0,0.9),size=vector(17,10,0.5))

box(pos=vector(0,-5,0),size=vector(1,10,1))

box(pos=vector(0,-5,0),size=vector(1,10,1))

box(pos=vector(-7,-10,10),size=vector(20,0.5,10))

box(pos=vector(-7,-9.8,11),size=vector(18,0.5,7),color=color.black)




box(pos=vector(20,-4,-8),size=vector(10,15,20))

box(pos=vector(0,-10,0), size=vector(5,0.1,5))

box(pos=vector(8,-10,10), size=vector(3,1,5))

box(pos=vector(8,-9.5,9), size=vector(0.5,0.1,3), color=color.black)


my_box = box(pos=vector(0,0,1.2), size=vector(16,9,0.2), color=color.red)


b = [
    box(pos=vector(0,0,1.2), size=vector(16,9,0.2), color=color.green), 
    box(pos=vector(20,-4,-8), size=vector(10,15,20), color=color.green)
]


b[0].color = vector(0, 0.5, 0.2)

while True:
    rate(100)
    k = keysdown() 
    

    if 'a' in k:
        my_box.rotate(angle=0.01, axis=vector(0, 1, 0))
        my_box.color = color.blue
        
    
    if 'd' in k:
        my_box.rotate(angle=-0.01, axis=vector(0, 1, 0))
        my_box.color = color.blue    
        
        
        
    if 'q' in k:
        for box_item in b:
            box_item.color = color.yellow 
                
    if 'e' in k:
        for box_item in b:
            box_item.color = color.green
            
            
            
            
