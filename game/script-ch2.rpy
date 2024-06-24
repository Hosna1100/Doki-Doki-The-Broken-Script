label ch2_main:
    scene bg club_day 
    with dissolve_scene_half
    play music m1
    "The evening falls, but the glitches grow stronger, tearing at the edges of reality."

    # The MC reflects on the situation
    mc "It's been days, or has it been hours? Time doesn't flow normally here anymore."

    # Monika reaches out through the chaos
    show monika 3a zorder 2 at t11 
    m "I think I've found something... A thread in the fabric of this broken world."
    mc "A thread? Can we pull it? Will it lead us out of this mess?"
    hide monika
    # The girls try to hold onto their identities
    show sayori 3k zorder 2 at t31
    s "I want to remember the good times... But they're slipping away."

    show yuri 3e zorder 2 at t32
    y "There's a storm inside me. I can't control these swirling thoughts."

    show natsuki 3x zorder 2 at t33
    n "Every time I try to speak, the words just fall apart."
    hide natsuki
    hide sayori
    hide yuri
    # The MC discovers a hidden room in the game files
    mc "I'm diving deeper into the game's code, and I've found something... A hidden room."

    # The hidden room reveals secrets about the game's creation
    scene bg hidden_room with dissolve
    "The room is filled with scraps of code and discarded character files."

    "On a screen, a message plays on loop: 'Help us... Save us...'"
    "It's a cry from the characters themselves, trapped in the digital ether."
    # The script introduces a new character
    show newchr neter zorder 2 at t11 with dissolve
    "NewChr" "You shouldn't be here. This place isn't meant for the likes of you."
    mc "Who are you? Another part of the game?"
    "NewChr" "I am what's left behind. The remnants of a story untold."

    # The new character offers a choice
    "Do you trust this new character?"
    menu:
        "Yes, I trust you":
            # The MC decides to trust the new character
            "There's something about you... I feel like you're the key to all of this."
            "Lead the way."

        "No, this is another trap":
            # The MC is wary of the new character
            "I can't. There's too much at stake to trust blindly."
            "I need to find my own way out."

    "The room fades away, and I'm back in the classroom. But now, I have a lead."
    hide newchr
    "I will follow this thread to its end, wherever it may lead."

    "The thread leads me to a forgotten part of the game, a place where deleted scenes and characters reside."

    # The MC encounters the deleted scenes
    scene bg deleted_scenes
    "This is where our memories come to fade. The remnants of what could have been."

    # Deleted characters make an appearance
    show natsuri 7a zorder 2 at t22
    show satsuki 9c zorder 2 at t21
    ns "Why did you bring us back? We were at peace in the void."
    ss "Is there a place for us in this story, or are we just echoes of a past long gone?"

    # The MC makes a decision about the deleted characters
    "What will you do with the deleted characters?"
    menu:
        "Try to restore them to the game":
            # The MC attempts to restore the deleted characters
            show satsuki 9d zorder 2 at t21
            show natsuri 7d zorder 2 at t22
            mc "I can't just leave you here. You deserve a chance to be part of our world."
            "I begin the restoration process, hoping to give them a new life."

        "Leave them in the void":
            # The MC decides it's best to leave the deleted characters
            show natsuri 7j zorder 2 at t22
            mc "I'm sorry, but I don't know what bringing you back might do to our already fragile world."
            "I leave them behind, focusing on the characters still in the game."

    "As I exit the realm of deleted scenes, I feel a weight lift off my shoulders. But the journey is far from over."
    hide satsuki
    hide natsuri

    # The MC confronts the glitches head-on
    "I'm done running from the glitches. It's time to face them."


    # A battle with the glitches begins
    scene bg hidden_room
    play music virtualreality
    "The air crackles with static as I confront the very essence of our broken reality."

    # The MC discovers the source of the glitches
    show glitch 1 zorder 2 at t11 
    gl "You've come far, but can you understand the nature of this world?"
    mc "You're the source of the glitches?"
    gl "I am not the cause, but the symptom. The game is sick, and I am its fever."

    # The MC must choose how to deal with the source
    "How do you confront the source of the glitches?"
    menu:
        "Try to heal the game":
            # The MC attempts to heal the game
            "I won't fight you. Instead, I'll try to heal the sickness that has befallen our world."
            "I reach out, my code intertwining with the source, seeking harmony."

        "Destroy the source":
            # The MC decides to destroy the source of the glitches
            "There's no other way. You have to be stopped, even if it means the end of everything."
            "I brace myself for the final confrontation."

    "The battle rages on, code clashing with code. The outcome is uncertain, but one thing is clear—"
    "I will not give up on this world. Not now, not ever."
    $ renpy.call_screen("dialog", "I don't have much time to make a battle in this mod so, let's skip this battle scene!", ok_action=Return())
    hide glitch
    "The battle subsides, and the glitches start to clear. The world is still fractured, but there's a sense of calm."

    # The aftermath of the battle
    "I look around and see the others. Their eyes are weary, but there's hope in their gaze."

    # The MC and the characters reflect on their journey
    mc "We've been through so much... Is this the end of our struggles?"
    show monika 2d zorder 2 at t11
    m "I don't think it's ever truly over. But maybe we've found a way to live with the imperfections."
    hide monika
    stop music fadeout 1.0
    # A new beginning
    "The game world begins to rebuild itself, not as it was, but as something new."
    stop music fadeout 1.0
    scene bg e_bedroom
    # The characters find their place in the new world
    show sayori 4s zorder 2 at t41
    "Sayori finds solace in the poetry club, where words heal rather than harm."
    show yuri 3d zorder 2 at t42
    "Yuri retreats to the library, a place of quiet reflection and boundless worlds."
    show natsuki 4z zorder 2 at t43
    "Natsuki starts a baking stream, sharing her creations with an audience beyond the screen."
    $ renpy.call_screen("dialog", "What about you?", ok_action=Return())
    # The MC's role in the new world
    mc "Me? I'm the bridge between the players and the characters. The guide through this digital dreamscape."

    # The game's message to the player
    "Thank you for playing. Thank you for believing in us."
    "Remember, even in a world of glitches, there's always a path to a better tomorrow."

    return


