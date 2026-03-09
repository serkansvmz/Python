import turtle

def draw_heart():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Simetrik Kalp Çizimi")

    heart = turtle.Turtle()
    heart.color("red")
    heart.fillcolor("red")
    heart.pensize(3)
    heart.speed(5) # Çizimi izlemek için biraz yavaşlattık

    # Kalp çizimi animasyonu
    heart.penup()
    heart.goto(0, -150) # Başlangıç noktası
    heart.pendown()
    
    heart.begin_fill()
    heart.left(120)  # Sol kenarın açısı
    heart.forward(224)
    
    # Sol lob (kulakçık)
    for _ in range(200):
        heart.right(1)
        heart.forward(1)
    
    heart.left(163) # Tam tepe noktası dönüşü
    
    # Sağ lob (kulakçık)
    for _ in range(200):
        heart.right(1)
        heart.forward(1)
        
    heart.forward(224) # Başlangıç noktasına dönüş
    heart.end_fill()

    # Yazı ekleme
    heart.penup()
    heart.goto(0, 50)
    heart.color("white")
    heart.write("Seni Seviyorum", align="center", font=("Arial", 20, "bold"))

    heart.hideturtle()
    screen.exitonclick()

draw_heart()