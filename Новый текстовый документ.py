from pygame import*
window = display.set_mode((700, 500))
display.set_caption('Ping-Pon')
window.fill((0, 255, 255))

game =True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    b.draw()
    b.update()
    display.update()