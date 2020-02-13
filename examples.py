import arcade
import random

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200
SCREEN_TITLE = "Lick me in the calcium"

CIRCLE_RADIUS = 5
	
GRAVITY_CONSTANT = 0.69
BOUNCINESS = 0.999

def function():
	pass

def draw(_delta_time) :
	arcade.start_render()

	arcade.draw_circle_filled(draw.x, draw.y, CIRCLE_RADIUS, arcade.color.PINK)
	draw.x += draw.delta_x
	draw.y += draw.delta_y 

	draw.delta_y -= GRAVITY_CONSTANT

	if draw.x <	CIRCLE_RADIUS and draw.delta_x < 0:
		draw.delta_x *= - BOUNCINESS
		arcade.set_background_color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
	elif draw.x > SCREEN_WIDTH - CIRCLE_RADIUS and draw.delta_x > 0:
		draw.delta_x *= - BOUNCINESS
		arcade.set_background_color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

	if draw.y < CIRCLE_RADIUS and draw.delta_y < 0:
		if draw.delta_y * -1 > GRAVITY_CONSTANT * 16:
			draw.delta_y *= -BOUNCINESS
			arcade.set_background_color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
		else:
			draw.delta_y *= -BOUNCINESS / 2
			arcade.set_background_color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

draw.x = CIRCLE_RADIUS
draw.y = SCREEN_HEIGHT - CIRCLE_RADIUS
draw.delta_x = 2
draw.delta_y = 0

def main():
	arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
	arcade.set_background_color(arcade.color.BLUE)

	arcade.schedule(draw,1 / 69)

	arcade.run()

	arcde.close_window()

if __name__ == "__main__":   
    main()
