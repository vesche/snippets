#!/usr/bin/env python

# False Planet
# https://github.com/vesche

import pyglet


window = pyglet.window.Window(caption='False Planet', width=800, height=600)
ball = pyglet.resource.image('images/ball.png')
# sound  = pyglet.resource.media('audio/weird.mp3', streaming=False)
label = pyglet.text.Label( 'False Planet',
                            font_name='Arial',
                            font_size=36,
                            # x=window.width//2, y=window.height//2,
                            # x=200, y=400,
                            x=window.width//2, y=window.height-30,
                            anchor_x='center', anchor_y='center' )
# Image Grid
# skel = pyglet.image.load('images/skeleton.png')
# skel_seq = pyglet.image.ImageGrid(skel, 6, 8)
# skel_tex_seq = pyglet.image.TextureGrid(skel_seq)

# Loading a gif
# animation = pyglet.image.load_animation('images/walk.gif')
# tex_bin = pyglet.image.atlas.TextureBin()
# animation.add_to_texture_bin(tex_bin)
# sprite = pyglet.sprite.Sprite(animation)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        ball.anchor_y, ball.anchor_x = -y+50, -x+50
        print 'M1 x:{} y:{}'.format(x, y)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.W:
        ball.anchor_y -= 10
    elif symbol == pyglet.window.key.A:
        ball.anchor_x += 10
    elif symbol == pyglet.window.key.S:
        ball.anchor_y += 10
    elif symbol == pyglet.window.key.D:
        ball.anchor_x -= 10
    # elif symbol == pyglet.window.key.SPACE:
    #     sound.play()
    print 'Image x:{} y:{}'.format(ball.anchor_x, ball.anchor_y)


@window.event
def on_draw():
    window.clear()
    ball.blit(0, 0)
    # sprite.draw(0,0)
    # skel_tex_seq.blit(100, 100)
    # skel_seq[0].blit(100,100)
    label.draw()


def main():
    pyglet.app.run()


if __name__ == '__main__':
    main()
