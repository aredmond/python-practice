from datetime import datetime, timedelta
import time
import sys
import pyglet



if len(sys.argv) > 1:
    seconds_to_countdown = int(sys.argv[1])
else:
    seconds_to_countdown = 300

window = pyglet.window.Window(400,300)
window.set_location(900, 700)
current_time = datetime.now()
future_time = current_time + timedelta(seconds=seconds_to_countdown)
time_left = future_time - current_time

label = pyglet.text.Label(f'4:56',
                          font_name='Font Awesome 5 Brands Regular',
                          font_size=70,
                          x=(window.width//2 - 100), y=window.height//2,
                          anchor_x='left', anchor_y='center')

def seconds_to_time_stamp(s):
    mins = s // 60
    secs_left = s % 60
    tens_secs_left = secs_left // 10
    ones_secs_left = secs_left % 10
    return f'{mins}:{tens_secs_left}{ones_secs_left}'

def update(secs_left):
    current_time = datetime.now()
    # if time_left > 0:
    time_left = future_time - current_time

    label.text = seconds_to_time_stamp(time_left.seconds)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.clock.schedule_interval(update, 1/10.0)
pyglet.app.run()