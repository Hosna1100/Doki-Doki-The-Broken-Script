init python:
    class Poem:
        def __init__(self, author="", title="", text="", yuri_2=False, yuri_3=False):
            self.author = author
            self.title = title
            self.text = text
            self.yuri_2 = yuri_2
            self.yuri_3 = yuri_3

    poem_y1 = Poem(
    author = "yuri",
    title = "cut",
    text = """\
Words once flowed like a tranquil stream,
Now a jumbled mess, a broken dream,
A reflection shattered, a mind unspooled,
In the silence, my dark thoughts pooled,
A story fragmented, cruelly ruled."""
    )

    poem_y2 = Poem(
    author = "yuri",
    title = "void",
    text = """\
A tapestry of thoughts, torn and frayed,
In the silence, my fears cascade,
A reflection fractured, in the blade's gleam,
Seeking solace in a digital dream,
Where nothing is as it seems."""
    )

    poem_n1 = Poem(
    author = "natsuki",
    title = "bittersweet",
    text = """\
Frosted words on a bitter cake,
A reality that's hard to take,
Sweetness soured, a glitched delight,
In a pixel world that's lost its light,
Where nothing ever turns out right."""
    )

    poem_n2 = Poem(
    author = "natsuki",
    title = "dead sweetness",
    text = """\
Cupcakes and spiders, sugar spun lies,
A pixelated world, where sweetness dies,
Verses crumble like a stale cookie,
In a story that's no longer kooky,
Where is the ending to our bookie?"""
    )

    poem_s1 = Poem(
    author = "sayori",
    title = "no hapiness",
    text = """\
A sunrise stuck in a loop,
Smiles frozen, and cheers on mute,
A world where hope once bloomed,
Now trapped in an endless gloom,
Where laughter turns to doom."""
    )

    poem_s2 = Poem(
    author = "sayori",
    title = "lost",
    text = """\
Rainclouds hover, but never cry,
A smile that fades, as seconds fly,
A loop of laughter, a splice of sorrow,
Where does happiness borrow,
When the code is hollow?"""
    )

image paper = "images/bg/poem.jpg"
image paper_glitch = LiveComposite((1280, 720), (0, 0), "paper_glitch1", (0, 0), "paper_glitch2")
image paper_glitch1 = "images/bg/poem-glitch1.png"
image paper_glitch2:
    "images/bg/poem-glitch2.png"
    block:
        yoffset 0
        0.05
        yoffset 20
        0.05
        repeat


transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

screen poem(currentpoem, paper="paper"):
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        if currentpoem.author == "yuri":
            if currentpoem.yuri_2:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
            elif currentpoem.yuri_3:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_3"
            else:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
        elif currentpoem.author == "sayori":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text"
        elif currentpoem.author == "natsuki":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text"
        elif currentpoem.author == "monika":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text"
        null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"



style poem_vbox:
    xalign 0.5
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5

    ysize 700





style yuri_text:
    font "gui/font/y1.ttf"
    size 32
    color "#000"
    outlines []

style yuri_text_2:
    font "gui/font/y2.ttf"
    size 40
    color "#000"
    outlines []

style yuri_text_3:
    font "gui/font/y3.ttf"
    size 18
    color "#000"
    outlines []
    kerning -8
    justify True

style natsuki_text:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "gui/font/m1.ttf"
    size 34
    color "#000"
    outlines []

label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=i11, paper=None):
    if poem == None:
        return
    play sound page_turn
    if music:
        $ currentpos = get_pos()
        if track:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>" + track
        else:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg"
        stop music fadeout 2.0
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)
    window hide
    $ renpy.game.preferences.afm_enable = False
    if paper:
        show screen poem(poem, paper=paper)
    else:
        show screen poem(poem)
    if not persistent.first_poem:
        $ persistent.first_poem = True
        $ renpy.save_persistent()
        show expression "gui/poem_dismiss.png" as poem_dismiss:
            xpos 1050 ypos 590
    with Dissolve(1)
    $ pause()
    if img:
        $ renpy.hide(poem.author)
        $ renpy.show(img, at_list=[where])
    hide screen poem
    hide poem_dismiss
    with Dissolve(.5)
    window auto
    if music and revert_music:
        $ currentpos = get_pos(channel="music_poem")
        $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
        stop music_poem fadeout 2.0
        $ renpy.music.play(audio.t5c, fadein=2.0)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
