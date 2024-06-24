label ch1_main:
    stop music fadeout 1.0
    with dissolve_scene_half
    play music virtualreality
    scene bg classroom
    "The classroom is different... It's as if reality is crumbling around us."

    # The MC tries to make sense of the situation
    mc "I need to understand what's happening. Maybe there's a pattern to this madness."

    # Monika tries to communicate through the glitches
    show monika 1g zorder 2 at t11
    m "Can you hear me? Please, tell me you can hear me."
    mc "Monika? Is that you? Your voice is all broken up."
    m "It's... not just my voice. It's everything. The game, our world—it's falling apart!"
    show monika zorder 2 at t41
    # The girls appear, each with their own distorted presence
    show sayori 2f zorder 2 at t42
    s "I feel so lost... Why does happiness keep slipping away from me?"

    show yuri 2w zorder 2 at t43 
    y "My mind is a labyrinth of sharp edges, and I can't find my way out."

    show natsuki 2u zorder 2 at t44
    n "I don't want to be here anymore. This isn't the story I wanted to be a part of."
    hide natsuki
    hide yuri
    hide sayori
    # The MC decides to take action
    mc "We can't just wait for things to fix themselves. We need to find a way out."
    show monika zorder 2 at t22
    # A mysterious figure appears
    show mysteriousfigure zorder 2 at t21 with dissolve
    "..."
    mc "Who are you?"
    mf "I am the echo of what once was. The remnant of a deleted future."

    # The figure offers cryptic advice
    mf "To escape this loop, you must look beyond the code. Find the truth hidden in the poetry."

    # The MC examines the girls' poems for clues
    "I take a closer look at the poems. The words seem to dance and shift before my eyes."

    call showpoem (poem_s2, revert_music=True, paper="images/bg/poem.jpg", where=truecenter)

    call showpoem (poem_y2, revert_music=True, paper="images/bg/poem.jpg", where=truecenter)

    call showpoem (poem_n2, revert_music=True, paper="images/bg/poem.jpg", where=truecenter)
    stop music fadeout 1.0
    play music virtualreality
    # The MC finds a hidden message
    mc "There's a message here... A plea for help woven into the verses."

    # The script leads to a pivotal choice
    "How do you respond to the hidden message?"
    menu:
        "Reach out to the voice within the poems":
            # The MC attempts to communicate with the voice
            "I call out to the voice, offering my help."
            "The words on the page shimmer, and I feel a connection."

        "Ignore the message and search for another way":
            # The MC looks for other solutions
            "I can't focus on cryptic messages. There has to be another way to fix this."
            "I start to look through the game files, searching for anything out of place."

    "The path forward is uncertain, but I know I can't give up. Not now, not ever."

    return

