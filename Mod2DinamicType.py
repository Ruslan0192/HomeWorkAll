import simple_draw as sd
sd.resolution = (1200, 600)

def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius, width=2)

# for y in range(100,301,100):
#    for x in range(100, 1001, 100):
for _ in range(100):
    point = sd.random_point()
    bubble(point, 5)

sd.pause()
