label ch0_main:
    stop music fadeout 2.0
    scene black
    "..."
    "Where am I?"
    "What's happening?"

    show monika 1a at t11 zorder 2 with dissolve
    show sayori 1b at t21 zorder 2 with dissolve
    show yuri 1a at t31 zorder 2 with dissolve
    show natsuki 1b at t44 zorder 2 with dissolve

    "Everything is... broken."

    scene bg classroom

    "I can hear their voices... but they're all jumbled up."
    "It's like a bad dream that keeps repeating."

    # Dialogue repeats
    "I'm sorry, but an uncaught exception occurred."
    "I'm sorry, but an uncaught exception occurred."
    "I'm sorry, but an uncaught exception occurred."


    scene bg club_day 
    "..."
    scene bg corridor 
    "..."
    scene bg club_day 
    "..."
    scene bg corridor
    "..."

    # MC's realization
    mc "..."
    "This isn't right. This isn't how things are supposed to be."
    "Monika... What's happened to the world you once controlled?"

    show monika 4p zorder 2 at t11
    m "I don't know... It's like I'm no longer in charge of this script."
    m "The code is rewriting itself and I can't stop it."

    # Girls' personalities warp
    show sayori 2k zorder 2 at t44
    s "I feel so... scattered."
    
    show yuri 2y4 zorder 2 at t42
    y "My thoughts are fragmented, like shards of a broken mirror."

    show natsuki 2k zorder 2 at t41
    n "It's like I'm fading away... and I can't hold on to who I am."

    # Poems become distorted
    "The words on the pages begin to twist and warp, forming disturbing patterns."

    call showpoem (poem_y1, revert_music=True, paper="images/bg/poem.jpg", where=truecenter)

    call showpoem (poem_s1, revert_music=True, paper="images/bg/poem.jpg", where=truecenter)

    call showpoem (poem_n1, revert_music=True, paper="images/bg/poem.jpg", where=truecenter)
    play music m1

    "What does it all mean? Can we ever escape this broken narrative?"
    "Or are we doomed to repeat this cycle forever?"

    # The script ends with a choice
    "What do you do?"
    menu choice:
        "Try to fix the game":
            # Attempts to fix the game
            "I start to piece together the broken code."
            "But it's like trying to hold water in my hands."
            "It just slips through my fingers."
            "Nothing changes."

        "Accept the broken world":
            # Accepts the broken narrative
            "Maybe this is how things are meant to be now."
            "A world where nothing makes sense... and there's no way out."
            "I sit down, close my eyes, and let the chaos wash over me."
            "It's strangely calming."
            jump endbad


label endbad:
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show endbad
    pause 0.75
    $ quick_menu = True
    $ renpy.quit()



