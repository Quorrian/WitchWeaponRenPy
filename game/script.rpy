# The script of the game goes in this file.

# TODO: change the size of the videos to match the game resolution to take up less space for web
# TODO: change default volume settings because good lord is that loud on web

init -10:
    define cOrange = "{color=#D08F27}"
    define cEnd = "{/color}"
    default playername = "Ren"
    define pause = "{w=0.5}"
    define nl = "\n"
    define fastDissolveSpeed = 0.2
    define fastDissolve = Dissolve(fastDissolveSpeed)
    define activeFadeTime = 0.3

    image black = Solid("#000")
    image white = Solid("#fff")
    image red = Solid("#f00")
    image darkorange = Solid((238,110,68))

    default activeSpeaker = ""
    default cleanSpeakers = []
    default speakers = []
    default isHiding = False


init -10 python:
    def shrink(s):
        return Transform(s, zoom=0.62)
    def slightRight(s):
        return Transform(s, pos=(0.6, 1.0), anchor=(0.5, 1.0))

    config.displayable_prefix["std"] = shrink
    config.displayable_prefix["sr"] = slightRight

# basic transforms
init -3:
    transform leftish:
        pos(0.32, 1.0)
        anchor(0.5, 1.0)

    transform leftisher:
        pos(0.28, 1.0)
        anchor(0.5, 1.0)

    transform rightish:
        pos(0.68, 1.0)
        anchor(0.5, 1.0)

    transform rightisher:
        pos(0.72, 1.0)
        anchor(0.5, 1.0)

    transform inactive:
        matrixcolor TintMatrix("#555555") * SaturationMatrix(0.75)

    transform active:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    transform fadeWait:
        pause activeFadeTime

    transform fadeToLeft:
        parallel:
            linear activeFadeTime leftish
        parallel:
            active
            linear activeFadeTime inactive

    transform fadeToRight:
        parallel:
            linear activeFadeTime rightish
        parallel:
            active
            linear activeFadeTime inactive

    transform fadeToLefter:
        parallel:
            linear activeFadeTime leftisher
        parallel:
            linear activeFadeTime inactive

    transform fadeToCenter:
        parallel:
            linear activeFadeTime center
        parallel:
            linear activeFadeTime inactive

    transform fadeToRighter:
        parallel:
            linear activeFadeTime center
        parallel:
            linear activeFadeTime inactive

    transform returnToLeft(state=active):
        parallel:
            linear activeFadeTime leftish
        parallel:
            linear activeFadeTime state

    transform returnToCenter:
        parallel:
            linear activeFadeTime center
        parallel:
            linear activeFadeTime active

    transform returnToRight(state=active):
        parallel:
            linear activeFadeTime rightish
        parallel:
            linear activeFadeTime state

    transform fadeActive:
        linear activeFadeTime active

    transform fadeInactive:
        active
        linear activeFadeTime inactive

    transform tempHide:
        mesh True
        linear activeFadeTime alpha 0.0

    transform tempShow:
        linear activeFadeTime alpha 1.0

    transform wait_show(child, before=0, after=1):
        Null()
        pause before
        child
        pause after
        Null()

init -1 python:
    def p(duration, jump_target):
        result = renpy.pause(duration)
        if result:
            renpy.jump(jump_target)

    def beepy_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/SFX/beeps.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def chapter(title):
        renpy.call("smartClear")
        renpy.music.stop(fadeout=1.0)
        _window_hide(auto=False)
        renpy.scene()
        renpy.show("black")
        renpy.with_statement(dissolve)
        renpy.say(titlecard, title)

    # OLD MULTI SPRITE MANAGEMENT SYSTEM
    def swap(toRemove, toActive):
        renpy.hide(toRemove)
        renpy.with_statement(fastDissolve)
        renpy.show(toActive)
        renpy.with_statement(fastDissolve)

    def swapActive(toRemove, toActive):
        renpy.show(toRemove, at_list=[fadeInactive])
        renpy.show(toActive, at_list=[fadeActive])
        renpy.pause(activeFadeTime)

    def addSecond(toRemove, toActive):
        renpy.show(toRemove, at_list=[fadeToLeft])
        renpy.pause(activeFadeTime)
        renpy.show(toActive, at_list=[rightish])
        renpy.with_statement(fastDissolve)

    def addThird(toLeft, toCenter, toActive):
        renpy.show(toLeft, at_list=[fadeToLefter])
        renpy.show(toCenter, at_list=[fadeToCenter])
        renpy.pause(activeFadeTime)
        renpy.show(toActive, at_list=[rightisher])
        renpy.with_statement(fastDissolve)

    def removeSecond(toRemove, toActive):
        renpy.hide(toRemove)
        renpy.with_statement(fastDissolve)
        renpy.show(toActive, at_list=[returnToCenter])
        renpy.pause(activeFadeTime)

    def removeThird(toActive, toLeft, toRight, isLeftActive=True):
        renpy.hide(toRemove)
        renpy.with_statement(fastDissolve)
        if (isLeftActive):
            renpy.show(toLeft, at_list=[returnToLeft(active)])
            renpy.show(toRight, at_list=[returnToRight(inactive)])
        else:
            renpy.show(toLeft, at_list=[returnToLeft(inactive)])
            renpy.show(toRight, at_list=[returnToRight(active)])
        renpy.pause(activeFadeTime)

    # NEW MULTI SPRITE MANAGEMENT SYSTEM
    def cleanName(name):
        return name.split(" ")[0]

    def updateSpeaker(name):
        index = cleanSpeakers.index(cleanName(name))
        speakers[index] = name

    def removeSpeaker(name):
        index = cleanSpeakers.index(cleanName(name))
        del cleanSpeakers[index]
        del speakers[index]

    def addSpeaker(name):
        speakers.append(name)
        cleanSpeakers.append(cleanName(name))

    def pauseDialogBox():
        #renpy.say(None, "{w=[activeFadeTime]}{nw}")
        renpy.pause(activeFadeTime)

    def sneak():
        _window_show(trans=None)
        for speaker in speakers:
            renpy.show(speaker, at_list=[tempHide])
        pauseDialogBox()

    def unsneak():
        _window_show(trans=None)
        for speaker in speakers:
            renpy.show(speaker, at_list=[tempShow])
        pauseDialogBox()

    def smartSwapSayPy(who, how, what):
        if (who.image_tag is None):
            # switching to a no-image character. hide all images but don't change active speaker
            sneak()
            renpy.say(who, what)
            return (True, activeSpeaker)

        imageTag = who.image_tag + how
        cleanActive = cleanName(activeSpeaker)
        # the only case where we do not unhide: Doing a replace while hidden
        if (len(speakers) == 1 and who.image_tag != cleanActive and isHiding):
            removeSpeaker(activeSpeaker)
            addSpeaker(imageTag)
            renpy.show(imageTag)
            renpy.with_statement(fastDissolve)
            renpy.say(who, what)
            renpy.hide(cleanActive)
            return (False, imageTag)

        if (isHiding):
            unsneak()
        if (activeSpeaker == imageTag or (how == "" and who.image_tag == cleanActive)):
            renpy.say(who, what)
            return (False, activeSpeaker)
        if (who.image_tag == cleanActive):
            updateSpeaker(imageTag)
            renpy.show(imageTag)
            renpy.say(who, what)
            return (False, imageTag)

        if (len(speakers) == 1):
            toHide = cleanActive
            removeSpeaker(activeSpeaker)
            addSpeaker(imageTag)
            renpy.show(cleanActive, at_list=[tempHide])
            renpy.pause(activeFadeTime)
            renpy.show(imageTag)
            renpy.with_statement(fastDissolve)
            renpy.say(who, what)
            renpy.hide(cleanActive)
            return (False, imageTag)

        updateSpeaker(imageTag)
        renpy.show(cleanActive, at_list=[fadeInactive])
        renpy.show(imageTag, at_list=[fadeActive])
        renpy.say(who, what)
        return (False, imageTag)

    def smartAddSayPy(who, how, what):
        imageTag = who.image_tag + how
        if (isHiding):
            unsneak()
        if (len(speakers) == 0):
            renpy.show(imageTag, at_list=[center])
            renpy.with_statement(fastDissolve)
        if (len(speakers) == 1):
            renpy.show(activeSpeaker, at_list=[fadeToLeft])
            pauseDialogBox()
            renpy.show(imageTag, at_list=[rightish])
            renpy.with_statement(fastDissolve)
        elif (len(speakers) == 2):
            renpy.show(speakers[0], at_list=[fadeToLefter])
            renpy.show(speakers[1], at_list=[fadeToCenter])
            pauseDialogBox()
            renpy.show(imageTag, at_list=[rightisher])
            renpy.with_statement(fastDissolve)
        addSpeaker(imageTag)
        renpy.say(who, what)
        return (False, imageTag)

    def smartDropSayPy(whodrop, who, how, what):
        noImage = who.image_tag is None
        dropImageTag = whodrop.image_tag
        newActive = ""
        if (isHiding):
            unsneak()
        removeSpeaker(dropImageTag)
        renpy.hide(dropImageTag)
        renpy.with_statement(fastDissolve)
        #if (len(speakers) == 0):
        if (len(speakers) == 1):
            if (noImage):
                newActive = speakers[0]
            else:
                newActive = cleanSpeakers[0] + how
            renpy.show(newActive, at_list=[returnToCenter])
            pauseDialogBox()
        elif (len(speakers) == 2):
            if (noImage):
                renpy.show(speakers[0], at_list=[returnToLeft(inactive)])
                renpy.show(speakers[1], at_list=[returnToRight(active)])
                newActive = speakers[1]
            elif (cleanSpeakers[0] == who.image_tag):
                renpy.show(cleanSpeakers[0] + how, at_list=[returnToLeft(active)])
                renpy.show(speakers[1], at_list=[returnToRight(inactive)])
                newActive = cleanSpeakers[0] + how
            else:
                renpy.show(speakers[0], at_list=[returnToLeft(inactive)])
                renpy.show(cleanSpeakers[1] + how, at_list=[returnToRight(active)])
                newActive = cleanSpeakers[1] + how
            pauseDialogBox()

        if (noImage):
            # switching to a no-image character. hide all images but don't change active speaker
            sneak()
            renpy.say(who, what)
            return (True, newActive)

        renpy.say(who, what)
        return (False, newActive)




init:
    define titlecard = Character(None, what_style="centered_text", window_style="centered_window", what_font="arial-mt-black.ttf", what_size=34, what_suffix="{fast}")
    define narrator = Character(None, callback=beepy_voice)
    define record = Character("Record", callback=beepy_voice)
    define sys = Character("System Voice", callback=beepy_voice)
    define player = Character("[playername]", callback=beepy_voice)
    define labWoman = Character("Woman in Lab Coat", callback=beepy_voice)
    define mariru = Character("Mariru", callback=beepy_voice)
    define maleA = Character("Male Voice A", callback=beepy_voice)
    define maleB = Character("Male Voice B", callback=beepy_voice)
    define balaA = Character("Balaclava A", callback=beepy_voice)
    define balaB = Character("Balaclava B", callback=beepy_voice)
    define balaBoss = Character("Balaclava Boss", callback=beepy_voice)
    define news = Character("News", callback=beepy_voice)
    define guard = Character("Guard", callback=beepy_voice)
    define funnyFace = Character("Funny Face", callback=beepy_voice)
    define blueGirl = Character("Blue-Haired Girl", callback=beepy_voice)
    define defMin = Character("Defense Ministry Officer", callback=beepy_voice)
    define milOff = Character("Military Officer", callback=beepy_voice)
    define female = Character("Female Voice", callback=beepy_voice)
    define milCom = Character("Military Communication", callback=beepy_voice)
    define agentA = Character("Agent A", callback=beepy_voice)
    define agentB = Character("Agent B", callback=beepy_voice)
    define sidAgent = Character("SID Agent", callback=beepy_voice)

    define playerboy = Character("[playername]", image="player", callback=beepy_voice)
    define playergirl = Character("[playername]", image="player2", callback=beepy_voice)
    define playerbat = Character("[playername]", image="player3", callback=beepy_voice)
    define marirulab = Character("Mariru", image="mariru", callback=beepy_voice)
    define marirusid = Character("Mariru", image="mariru2", callback=beepy_voice)
    define annie = Character("Annie", image="annie", callback=beepy_voice)
    define kirs = Character("Kirs", image="ikirs", callback=beepy_voice)
    define bright = Character("Bright", image="ibright", callback=beepy_voice)
    define sharpc = Character("#C", image="isharpc", callback=beepy_voice)

    image movieGrailBoom = Movie(play="images/video/endoftheworld.webm", loop=False, size=(1024,576))
    image movieGrailBoy = Movie(play="images/video/gobletgothim.webm", loop=False, size=(1024,576))
    image movieSeeWreckage = Movie(play="images/video/lookatwreckage.webm", loop=False, size=(1024,576))
    image movieDream = Movie(play="images/video/wasadream.webm", loop=False, size=(1024,576))


    image gunmanA = "std:gunman a"
    image gunmanB = "std:gunman b"
    image gunmanBoss = "std:gunman boss"
    image gobletNews = "std:goblet news"
    image twisted = "std:sr:twisted gal"
    image agent = "std:sid agent"
    image ikirs = "std:kirs"
    image ibright = "std:bright"
    image isharpc = "std:sharpc"

    layeredimage player1:
        zoom 0.62
        always:
            "player1_base"
        group face auto:
            pos (140, 127)
            attribute neutral default

    layeredimage player2:
        zoom 0.62
        always:
            "player2_base"
        group face auto:
            pos (175, 134)
            attribute neutral default

    layeredimage player3:
        zoom 0.62
        always:
            "player3_base"
        group face auto:
            pos (168, 98)
            attribute neutral default

    layeredimage mariru:
        zoom 0.62
        always:
            "mariru_base"
        group face auto:
            pos (116, 134)
            attribute neutral default

    layeredimage mariru2:
        zoom 0.62
        always:
            "mariru2_base"
        group face auto:
            pos (307, 200)
            attribute neutral default

    layeredimage guard:
        zoom 0.62
        always:
            "guard_base"
        group face auto:
            pos (192, 121)
            attribute neutral default

    layeredimage annie:
        zoom 0.62
        always:
            "annie_base"
        group face auto:
            pos (262, 140)
            attribute neutral default


label show_sub(text, wait_before=0, wait_after=1):
    $ textImage = Text(text, size=23, slow=False, xalign=0.5, yalign=0.90, color="#FFF", outlines=[(2, "#000")], textalign=0.5)
    show expression textImage at wait_show(before=wait_before, after=wait_after)
    return

label smartSwapSay(who, how, what):
    $ (out_isHiding, out_activeSpeaker) = smartSwapSayPy(who, how, what)
    $ isHiding = out_isHiding
    $ activeSpeaker = out_activeSpeaker
    return

label smartAddSay(who, how, what):
    $ (out_isHiding, out_activeSpeaker) = smartAddSayPy(who, how, what)
    $ isHiding = out_isHiding
    $ activeSpeaker = out_activeSpeaker
    return

label smartDropSay(whodrop, who, how, what):
    $ (out_isHiding, out_activeSpeaker) = smartDropSayPy(whodrop, who, how, what)
    $ isHiding = out_isHiding
    $ activeSpeaker = out_activeSpeaker
    return


label smartClear():
    $ activeSpeaker = ""
    $ speakers = []
    $ cleanSpeakers = []
    $ isHiding = False
    return

# https://www.lezcave.com/name-input/
label nameInput(prompt, length):
    # Create an endless loop
    while True:
        # Let player type in
        $ typedIn = renpy.input(prompt, length=length).strip()

        # If something was typed in, return it
        # This will store it in the _return variable and break the loop.
        if typedIn != "":
            return typedIn

# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ chapter("CHAPTER 1\nPART 1: Substance H")
label chapter1_1:

    scene good age with fastDissolve
    play music "audio/BGMusic/WW_BGM_04.wav"

    record "This is a booming era in which technology and supernatural power progress hand in hand."
    record "The most amazing supernatural power is controlled by the six major nations:"
    record "[cOrange]Substance H[cEnd], [pause]a.k.a. The Divine Touch by common people."

    scene relic city with fastDissolve

    record "As the research on Substance H progresses, \"the Divine Touch\" itself becomes more and more powerful."

    scene politics with fastDissolve

    record "As all six nations had Substance H, and no one wanted to risk a war that could end the world,"
    record "they signed a peace treaty."
    record "As a result, all capitals of the six nations were renamed [cOrange]Academy City[cEnd], and they only focused on research."

    scene witch with fastDissolve

    record "Modern science suggests that certain individuals can resonance with Substance H and control its"
    record "power when provided with [cOrange]specific mediums[cEnd]."
    record "[cOrange]Witches[cEnd] are the widely known example."
    record "Their mysterious power came from Substance H.[pause]\nAlthough, it was called [cOrange]Catalyst[cEnd] back in the days."

    $ chapter("CHAPTER 1\nPART 2: Kidnap?")
label chapter1_2:

    scene aegis with fastDissolve
    play music "audio/BGMusic/chill jazz piano.wav"

    call nameInput("Enter your name:", 13)
    $ playername = _return
    sys "Login Successful!"
    sys "ID: 2519G1911\nName: [playername]"
    sys "Age: 15\nGender: Male"
    sys "Welcome to the Steele Monte Collection and Research Center in the Fifth Academy City,"
    sys "The largest Substance H collection and research center in New Opulentia."
    sys "Substance H, [pause]a.k.a. the Divine Touch, is a general term for items and tools that activate"
    sys "supernatural phenomena at certain conditions."
    sys "On this Open Day, The Collection and Research Center is open to the public and other Academy Cities."
    sys "As an important public awareness initiative, We will present some Divine Touches and research results..."

    scene passage night
    show player1 neutral with fastDissolve
    player "Lucky![pause] Finally here before the closing time!"
    player "Why are all elevators in the lobby out of service?[pause]\nLuckily this freight elevator is still running."
    show player1 happy
    player "Anyway, just need a stamp on the lecture paper to get school credits."
    show player1 confused
    player "Wait... why is there no one on this floor?"
    hide player1 with fastDissolve
    narrator "I walk along the corridor on the second floor and look around."
    narrator "Generally, there are not many visitors here, but it shouldn't be this empty..."
    narrator "And the smell of disinfectant... feels like a deep cleaning is taking place."
    show player1 disbelief with fastDissolve
    player "Is the lecture over already?"
    hide player1 with fastDissolve
    narrator "I turn around the corner of the spiral staircase to look for the Conference Hall."
    show player1 confused with fastDissolve
    player "It sucks.[pause] Shouldn't play the video game..."
    show player1 disbelief
    player "The \"Continue\" button is really addictive--[pause]\nAhhh Ummm!?"

    scene black with dissolve
    play music "audio/BGMusic/escalation.wav"

    narrator "Suddenly my neck feels like being clutched by something and pulled backwards."
    narrator "As I'm about to lose balance, I feel my head falls on something soft but firm."
    narrator "When I come back to myself, I find myself dragged into a dark, narrow aisle at the corner of the staircase."
    player "Oops--![pause]\nUmm--!"

    scene hiding passage with dissolve

    narrator "Before I can make a sound, someone muzzles me tightly."
    narrator "Out of the corner of my eye, I see a lady in a lab coat--"
    narrator "She leans against the wall, one hand over my mouth."
    narrator "My cheek pressed into her chest...[pause] I smell the fragrance on her."
    player "(What?[pause] I...[pause] I can't breathe!)"
    player "(What's up?![pause] Who is she!?)"
    labWoman "Hush![pause] Keep quiet!"
    narrator "She keeps her voice down, but there's still a sense of authority in it."
    narrator "I can't think straight.[pause] I'm suffocating.[pause]\nI can only nod slightly to show my obedience..."
    narrator "Although my mouth is still smothered, my neck feels a little bit better."
    narrator "Now my eyes turn to her chest... I can vaguely see a name tag on her lab coat... Chief Scientist..."
    player "(Scientist?[pause] So she works at this Center?)"
    narrator "Now I find that she's not looking at me.[pause] Head turned, she is looking at the corridor attentively."
    narrator "Loud and hasty footsteps sounded down the corridor."
    maleA "Sir, no one's here."
    maleA "But there is an independent freight elevator.[pause] Let me shut it down."
    player "(Seems like... that guy has his face covered, and is holding... a gun?)"
    labWoman "This place has been captured.[pause] Be quiet if you want to save your life."
    player "(Cap...[pause] captured?[pause] What happened?[pause] And you're the one who looks more dangerous!)"

    scene stairs with fastDissolve
    narrator "She suddenly rushes out before I know it."
    narrator "A few seconds later, I hear a thump and snap of bone."
    narrator "She catches the masked man from behind--saving a crash, drags him into the aisle and seizes his pistol."
    player "He is...?!"
    narrator "Without a word, she swings open the Switchgear Cabinet on the wall,"
    narrator "and kicks the limp brawny man into it."
    narrator "She is agile and energetic even in her white shirt and slim-fit skirt."
    show mariru neutral with fastDissolve
    labWoman "Whew.[pause] All clear, for the moment."
    hide mariru with fastDissolve
    narrator "As if having just dumped an oversized trash she dusts off her hands and turns to me with relief."
    narrator "My brain stops working, eyes fixated on her."
    show player1 blush with fastDissolve
    player "(This young lady looks beautiful!)\n(And look at her figure![pause] Like a model...)"
    show player1 neutral
    player "(But her name tag clearly reads \"scientist\")"
    show player1 disbelief
    player "(It must have been a hallucination...[pause]\nScientist-turned martial artist or something.)"
    hide player1 with fastDissolve
    narrator "I have imagined a brawny guy locked in Switchgear Cabinet."

    scene legs with fastDissolve
    narrator "Such a conclusion makes me feel secure.[pause] My eyes turn to her legs..."
    narrator "(Wouldn't it be great to work with her...)[pause]\n(Substance H researcher can be an exciting job)"

    scene stairs
    show mariru neutral with dissolve
    show mariru talk
    labWoman "Hey boy, what are you looking at?"
    hide mariru with fastDissolve
    narrator "She unloads the gun and checks the bullets as she speaks."
    show player1 sad with fastDissolve
    player "(Can't fool myself anymore!)"
    show player1 neutral
    player "Who... who are you?"
    $ swap("player1", "mariru")
    labWoman "Well...[pause] Just call me Mariru.[pause]\nI was supposed to give a boring lecture today."
    hide mariru with fastDissolve
    narrator "She loads the gun skillfully and puts it into her pocket."
    show mariru grin with fastDissolve
    labWoman "But these gangsters hijacked the Conference Hall just now."
    labWoman "So the lecture was cancelled, thank goodness."
    $ addSecond("mariru grin", "player1 shock")
    player "Mariru... Mariru Von Braun?"
    player "You... You're the lecturer to stamp on my paper![pause]\nAnd you're an SS-level scientist conferred by the Senate!"
    $ swapActive("player1 shock", "mariru neutral")
    mariru "Hum, SS level... Those old fools are gullible..."
    mariru "You're here just for school credits, aren't you?"
    $ swapActive("mariru neutral", "player1 confused")
    player "Yeah... I'm sorry!"
    $ removeSecond("player1", "mariru talk")
    mariru "I don't know if it's bad luck or stupidity... finding the only elevator upstairs in lockdown mode!"
    mariru "But for me, I'm sure you would've ended up in the Conference Hall."
    hide mariru with fastDissolve
    narrator "Lockdown mode...?[pause]\nI check my phone.[pause] There's really no signal."
    narrator "Now I see why all the elevators in the front hall were out of service... The Center is not really closed!"
    show mariru neutral with fastDissolve
    mariru "Now the freight elevator is also shut down.[pause] Stay here and wait for rescue by the Defense Ministry."
    mariru "I have to go and check the Conference Hall.[pause] If anyone comes, you know how to hide."
    $ swap("mariru", "player1 shock")
    player "But... you... alone?"
    $ swap("player1", "mariru mad")
    mariru "Understand?"
    $ swap("mariru", "player1 shock")
    player "Yes, ma'am!"

    $ chapter("CHAPTER 1\nPART 3: Failed Gamble")
label chapter1_3:

    scene stairs with fastDissolve
    play music "audio/BGMusic/fight.wav"
    show gunmanA with fastDissolve
    maleA "It's been a while since their last reply.[pause] Go check on them--"
    $ swap("gunmanA", "gunmanB")
    maleB "Yes!"
    $ swap("gunmanB", "gunmanA")
    maleA "I'm gonna get a heartbeat detector.[pause] Stay vigilant!"
    $ swap("gunmanA", "player1 confused")
    player "Crap![pause] There's nowhere to hide..."
    player "It's impossible to sneak away right under their noses.[pause] I have no choice but to take down one of"
    player "them when they separate."
    player "Perhaps I can make it...[pause]\nAs that woman just did it with bare hands..."
    show player1 neutral
    player "I need a weapon..."
    hide player1 with fastDissolve
    narrator "On the wall of the hallway hangs a baseball bat.\nUnder it is a plate saying \"Lebona's Light of Freedom\"..."
    show player1 happy with fastDissolve
    player "Looks like an exhibit...\nOops, I have to borrow it.[pause] Uh, just for a while..."
    player "...\n..."
    show player1 brave
    player "Now... Go![pause]\nAhh--!"
    hide player1
    show white
    with fastDissolve
    show white:
        alpha 0.5
        linear 0.2 alpha 1.0
    narrator "Bang!{fast}{nw}"
    show white:
        alpha 0.5
        linear 0.1 alpha 1.0
    show darkorange:
        alpha 0.0
        pause 0.1
        alpha 0.1
        linear 0.5 alpha 1.0
        linear 0.01 alpha 0.0
    show red:
        alpha 0.0
        pause 0.6
        linear 0.2 alpha 1.0
    show black:
        alpha 0.0
        pause 0.8
        linear 0.2 alpha 1.0
    narrator "Bang!{fast}{w=1}{nw}"
    hide white
    hide darkorange
    hide red
    narrator "With all my strength, I hit the masked man on the back of his head, and hear a loud bang."
    narrator "Damn... This is too loud!"

    scene stairs with fastDissolve
    narrator "But he doesn't collapse as I expect.[pause] Instead, he turns around, and stares at me with fiery eyes."
    show player1 shock with fastDissolve
    player "Why doesn't this go like the plot in games?"
    $ swap("player1", "gunmanA")
    balaA "Who the hell are you?"

    hide gunmanA with fastDissolve
    show red:
        alpha 0.0
        linear 0.1 alpha 0.5
        pause 0.5
        alpha 0.0
        linear 0.1 alpha 0.5
        pause 0.1
        alpha 0.25
        linear 0.3 alpha 0.9
        linear 0.2 alpha 0.0
    narrator "The masked man throws his pistol grip towards me.[pause] I hastily parry his attack with my bat."
    hide red

    show player1 shock with fastDissolve
    player "Damn--"
    hide player1 with fastDissolve

    show black:
        alpha 0.0
        linear 1 alpha 1.0
        pause 2
        linear 0.5 alpha 0.0
    show darkorange:
        alpha 0.0
        pause 2.7
        linear 0.3 alpha 0.2
        linear 0.5 alpha 0.0
    narrator "His mighty strength is pouring through the bat down to my hands and shoulders."
    narrator "Just as I'm gritting my teeth and getting on with it, he suddenly kicks me."

    show black:
        alpha 0.0
        linear 0.5 alpha 1.0
    show red:
        alpha 0.0
        pause 1.0
        linear 0.15 alpha 0.5
        linear 0.15 alpha 0.0
    narrator "He brutally slams his foot against my unp{nw}"
    show white:
        alpha 0.0
        linear 1.5 alpha 1.0
    narrator "He brutally slams his foot against my u{nw}"
    show white:
        alpha 0.0
        linear 0.15 alpha 1.0
        alpha 0.0
    show red:
        alpha 0.0
        pause 0.15
        alpha 1.0
        linear 1.2 alpha 0.0
    narrator "He brutally slams his foot against my unprotected stomach."
    hide white
    hide red
    hide darkorange

    show gunmanA with fastDissolve
    balaA "Damn![pause] The little skunk ambushing me fell downstairs."
    balaA "I'm gonna finish him!"

    $ swap("gunmanA", "player1 hurt")
    player "... I have to flee...\n... I must hide... in the... shadow of that exhibit..."

    scene stairs
    show gunmanB
    with fastDissolve
    balaB "Hang on... Boss just sent a message.[pause] He said the self-destruct anti-theft system was deactivated."
    balaB "Don't waste time on a kid.[pause] Fall in at the Conference Hall, now!"
    balaB "We'll be long gone when he comes round."

    $ swap("gunmanB", "gunmanA")
    balaA "Yes!"

    stop music fadeout 0.3
    scene black with dissolve
    show player1 hurt with fastDissolve
    player "I'm... falling... unconscious...\nMariru..."

    scene black with fastDissolve
    play music "audio/BGMusic/maze.wav"
    narrator "Meanwhile, at the Conference Hall"

    scene hiding conference with dissolve
    mariru "It looks like these guys have sneaked in with optic disguises..."
    mariru "They knew the anti-optic detectors in the Collection Center were partially shut down for"
    mariru "maintenance.[pause] Looks like a mole is planted among us."
    mariru "But I can't figure out who they are... For now, I can only wait."

    scene conference with fade
    show gunmanBoss with fastDissolve
    balaBoss "Aha![pause] Bravo!"
    balaBoss "Finally back in our hands..."

    scene hiding conference with fastDissolve
    mariru "The Ross Goblet!?"

    scene grail with dissolve
    narrator "The Ross Goblet is a Substance H discovered by an expedition on the Ross Islands that suddenly"
    narrator "emerged in the center of the Pacific Ocean.[pause] It is embedded with four gemstones."
    narrator "Inside the Goblet is a red liquid that cannot be poured or touched.[pause] It seems to be an illusion,"
    narrator "rather than any physical stuff."
    narrator "The old geeks at the Research Center had tried every possible means, but didn't figure out what the liquid is..."
    narrator "In time the risk rating of the Goblet was lowered to \"Safe\"."
    narrator "Now it's available for public research..."
    mariru "Haw, only the gems seem valuable."
    mariru "But the gems and the Goblet body are actually uniform at the molecular level.[pause] So, it's impossible to..."
    show gunmanBoss with fastDissolve
    balaBoss "To split this filthy thing into parts.[pause] I shall do it!"
    hide gunmanBoss with fastDissolve
    mariru "Split?[pause] How can it be possible--"

    $ chapter("CHAPTER 1\nPART 4: The End of the World")
label chapter1_4:

    show movieGrailBoom
    call show_sub("Mariru: Is that thing...", 0, 2.1)
    call show_sub("Mariru: The fourth Nail...", 2.1, 2)
    call show_sub("Mariru: That got stolen from the Hovering Palace Museum not long ago?", 4.1, 2)
    call show_sub("Mariru: Dammit!", 7, 1.5)
    call show_sub("Is that... the prophet's holy relic?", 8.6, 3.5)
    call show_sub("Huh? The liquid in the glass...", 13.4, 2.3)
    call show_sub("Mariru: You idiot!", 16.3, 1.2)
    $ p(28.4, "post_movieGrailBoom")

label post_movieGrailBoom:
    scene black
    narrator "..."

    play music "audio/BGMusic/ominous magic.wav"
    show player1 hurt with dissolve
    player "(Uh, what just happened to me?)"
    player "Ouch..."
    player "(Ah, I was attacked...)\n(And I crawled to the shadow of an exhibit near me...)"
    player "I'm surrounded by slates\n(There are weird paintings and inscriptions on them...)"
    player "The plate of the exhibit says \"Miskatonic...\"\n(The following words are obscured)"
    player "I'm suddenly aware that it's too quiet here..."
    player "Have those masked guys been gone?"
    player "Le... let me check around.[pause]\nThe Conference Hall... Mariru..."

    stop music fadeout 1.0
    scene black with dissolve
    show movieGrailBoy
    call show_sub("!!!!!!!!!!!!!!", 2.6, 1)
    call show_sub("The air reeks of sulphur.\nSmells salty, too. Makes one feel thirsty.", 3.6, 3)
    call show_sub("Something's floating in the air, radiating blinding light.\nI can't tell what it's shaped like...", 6.6, 3.5)
    call show_sub("And right in front of me, the world has gone to hell...", 10.1, 2)
    call show_sub("I'm dreaming, right?", 13.1, 2.6)
    call show_sub("Just... what's going on?", 16.1, 2.5)
    $ p(22.033, "post_movieGrailBoy")

label post_movieGrailBoy:
    scene black

    scene salt fire with dissolve
    play music "audio/BGMusic/ominous magic.wav"
    player "This must be a dream... I suppose?[pause]\nWhat the heck is this all about?"
    narrator "In a sea of fire, people are standing still like sculptures."
    narrator "Their postures are lively and expressions vivid..."
    narrator "But they don't show the normal colors of human, and are all ghostly pale."
    player "H... how could this... be possible..."
    player "No...\nWhat happened... to these people?"
    player "And Ms. Mariru... Where is she?"
    player "Please... someone tell me!"
    narrator "I try to touch the frozen face of a woman, but her neck just breaks without a sound."
    narrator "Her head falls onto the floor and crushes into parts."
    player "It's... salt?"
    player "Uh... No...\nWaaaah!"
    player "Waaaah![pause]\nNoooo!"

    $ chapter("CHAPTER 1\nPART 5: It's Gone!")
label chapter1_5:

    scene black
    show movieSeeWreckage
    call show_sub("If, you know, if...", 4, 2.6)
    call show_sub("God really exists...", 7.9, 2.7)
    call show_sub("Then I wish...", 12.1, 2.4)
    call show_sub("I wish all this were just a dream.", 17, 3)
    $ p(21.5, "post_movieSeeWreckage")

label post_movieSeeWreckage:
    hide movieSeeWreckage

    $ renpy.movie_cutscene("images/video/becomevessel.webm")

    show movieDream

    call show_sub("!!!!!!!!!!!!!!!!!!!", 8, 2.5)
    call show_sub("... What was that?", 18, 3)
    call show_sub("A dream?", 21, 2)
    call show_sub("I open my eyes to meet the familiar sight of my bedroom ceiling.", 24, 1.8)
    call show_sub("Normally I'd have just gone back to sleep...", 25.8, 3)
    call show_sub("But that nightmare was way too real. My heart is still hammering madly in my chest...", 28.8, 4.2)
    call show_sub("Wait, my chest...", 35, 2)
    call show_sub("Huh?", 37, 1.5)
    call show_sub("Why does my body feel so... soft?", 38.5, 2)
    call show_sub("Did I sprout more flab out of nowhere while I was asleep?", 40.5, 2)
    call show_sub("Hey, what's this...", 43.5, 2)
    call show_sub("Is this... is this really...", 46, 2)
    call show_sub("Hmm...", 48, 1)
    call show_sub("Am I still dreaming?", 49.5, 2)
    call show_sub("Ha, what a weird dream...", 51.5, 3)
    call show_sub("Hm, feels pretty good!", 54.5, 2.5)
    call show_sub("Haha... (squeezing)", 57, 2)
    call show_sub("I do have dreams like this from time to time.", 59, 3)
    call show_sub("It... still feels weird though... (squeezing)", 62, 3)
    call show_sub("Wait! At least save it for me...", 68, 2.5)
    call show_sub("...", 71.5, 4)
    call show_sub("What?", 75.5, 1.5)
    call show_sub("WHAT?", 77, 1)
    call show_sub("That thing, you know, [playername] Junior...", 78, 1.5)
    call show_sub("It's gone!", 80.1, 1.9)
    call show_sub("So... those things I've been squeezing...", 83, 1.5)
    call show_sub("Were they...", 84.5, 2.5)
    call show_sub("I...", 87, 1.2)
    call show_sub("I've turned into a girl!", 88.2, 2.8)
    $ p(97.033, "post_movieDream")
    

label post_movieDream:
    scene black

    play music "audio/BGMusic/EverythingisgonabeOK.wav"
    scene home bedroom
    show player2
    with fastDissolve
    player "(Checked once and again in the washroom...)\n(Couldn't think properly now...)"
    player "(Pinched myself really hard)\n(It's not a dream!)"
    show player2 blush
    player "(My body is much softer)\n(Feels... not bad...)"
    show player2 shock
    player "Damn![pause]\nNo, what's on my mind!"
    show player2 blush
    player "Damn it... This T-shirt fitted me well yesterday.[pause]\nNow it's oversized..."
    player "Fact is, my body becomes much smaller..."
    hide player2 with fastDissolve
    narrator "The little girl in the mirror is wearing an oversized T-shirt."
    narrator "Looks like in her boyfriend's clothes... That's how it goes in movies..."
    show player2 shock with fastDissolve
    player "... What am I blushing for..."
    show player2 neutral
    player "Indeed...\nBecoming a girl overnight... is hard to swallow..."
    player "I've checked my room carefully.[pause]\nEverything is the same as it was, except for the extra"
    player "metal baseball bat at the bedside."
    show player2 confused
    player "I dreamed of an attack in the Collection and Research Center last night."
    player "I used this bat in the battle..."
    show player2 neutral
    player "If it can be called a battle..."
    player "And then, the whole city... was in ruins..."
    show player2 confused
    player "Right, check the cellphone![pause]\nIf there was a battle yesterday, it should be"
    player "made the headlines!"
    show player2 neutral
    player "No news about terrorist attacks..."
    player "Great, it was really a dream..."
    show player2 confused
    player "Wait, what's this..."
    $ swap("player2", "gobletNews")
    news "Ross Goblet Vanished under Close Surveillance."
    news "The Ross Goblet disappeared from its site last night under the watchful eyes of a dozen surveillance devices."
    news "Strictly managed and monitored... unlikely to steal anything..."
    $ swap("gobletNews", "player2 confused")
    player "Well... I have to go and find out what happened!"
    show player2 neutral
    player "The dream last night, and my body...\nI have a feeling that maybe they have"
    player "something to do with the Center."
    player "OK![pause] Let's go!"

    scene street day
    show player2 blush
    with fade
    player "But wait...\nI look clearly suspicious in these clothes..."
    hide player2 with fastDissolve
    narrator "I come to regret it when I see my reflection in the glass of the entrance hall."
    narrator "The shirt is obviously oversized.[pause] And the jeans are dragging on the ground."
    narrator "More weirdly, I have a metal bat with me...\nYet, this is the only evidence I have..."

    scene outside center morning
    show player2
    with fastDissolve
    player "Well... like it or not, here I am... What next?"
    player "A terrorist attack is just unlikely to happen with so many security guards standing watch."
    player "Of course--a collectable just disappeared..."
    $ swap("player2", "guard talk")
    guard "... Wait, girl!"
    $ swap("guard", "player2")
    player "..."
    $ swap("player2", "guard talk")
    guard "Little girl over there, stop!"
    narrator "A man with buzz-cut shouts behind me.[pause] I see from his cuffs the powerful muscles of his brawny arms."
    narrator "A well-trained body plus a dazzling smile... He looks just like a wrestler in the movie."
    $ addSecond("guard talk", "player2 shock")
    player "What!?"
    $ swapActive("player2 shock", "guard smile")
    guard "Yeah, you girl."
    $ swapActive("guard smile", "player2 blush")
    player "Girl?[pause] No, you idiot![pause]\nI am... I... am..."
    $ swapActive("player2 blush", "guard smile")
    guard "Hmm?[pause] Anyway, something important went missing yesterday."
    guard "We are sent here to blockade this place."
    $ swapActive("guard smile", "player2 shock")
    narrator "I've got something important missing too![pause]\nVery important, missing since I woke up this morning!"
    $ swapActive("player2 shock", "guard smile")
    guard "The public is no longer allowed to enter.[pause] Come back some other time, girl."
    show guard neutral
    guard "And..."
    $ swapActive("guard neutral", "player2 shock")
    player "What![pause] Anything else...?"
    $ swapActive("player2 shock", "guard smile")
    guard "Girl, you'd better stop loitering with a baseball bat in your hand![pause] Put on more clothes or else"
    guard "you'll catch a cold.[pause]\nTake care!"
    hide guard
    hide player2
    with fastDissolve
    narrator "The security guard gives me a thumb up and again, a warm smile."
    show player2 neutral with fastDissolve
    player "O... ok, goodbye!"
    show player2 blush
    player "(Haven't got used to being called a girl...)"
    show player2 neutral
    player "Ugh--there must be some clues in the Center.[pause]\nBut I can't get in..."
    player "... Seems the only thing to do now is go home."


    play music "audio/BGMusic/escalation.wav" fadeout 1.0 fadein 1.0
    scene outside center weird
    show player2
    with fade
    player "Huh?[pause] I think I'm walking towards the station.[pause] But it seems to be a wrong way?"
    show player2 confused
    player "Uh...\nWhat's wrong?"
    show player2 neutral
    player "Am I lost?"
    $ swap("player2", "twisted")
    funnyFace "Chirp--![pause]... Věta... hrích...!"
    $ swap("twisted", "player2")
    player "These guys look fishy...\nWhat are they talking about?"
    show player2 shock
    player "Whoaaaaa!"
    player "What![pause] They are after me!?"
    $ swap("player2", "twisted")
    funnyFace "... Mors...!"
    $ swap("twisted", "player2 shock")
    player "So damn weird![pause] I've got to run!"
    show player2 blush
    player "... Whirr...![pause] It's impossible to run away...[pause]\nCan't move fast enough in these baggy clothes"
    player "and shoes...!"
    $ swap("player2", "twisted")
    funnyFace "Ahhhh!"
    $ swap("twisted", "player2 shock")
    player "They're catching up...\nI'm finished!!"
    player "Eh?[pause] The baseball bat...?"
    hide player2 with fastDissolve
    narrator "The pattern on the baseball bat is glowing eery lights."
    narrator "What... What's this...!"

    scene white
    $ renpy.music.set_volume(0.0)
    $ renpy.movie_cutscene("images/video/activatebat.webm", stop_music=False)
    $ renpy.music.set_volume(1.0)

    scene outside center blue
    show annie
    with fastDissolve
    blueGirl "Hoo... Finally... Hey, this is Annie.[pause] You're holding my bat?[pause] So you know I'm a witch?"
    show annie shock
    annie "Ugh, who are these fierce-looking guys?[pause] Seems you are in trouble!"
    $ addSecond("annie shock", "player2 shock")
    player "Annie... witch?[pause]\nI am definitely in big trouble today."
    $ swapActive("player2 shock", "annie shuteyes")
    annie "I have loads of questions for you,\nBut let's solve the immediate problem first!"
    show annie confused
    annie "What are you wearing?[pause] So baggy...\nUnsuitable for a battle, huh?"
    show annie proud
    annie "I'll give you a fitted suit...[pause]\nReady for battle?"
    $ swapActive("annie proud", "player2 shock")
    player "Ba... Battle?"

    $ chapter("CHAPTER 1\nPART 6: A New Wardrobe")
label chapter1_6:

    scene outside center morning with fastDissolve
    play music "audio/BGMusic/WW_BGM_02.wav"
    show player3 with fastDissolve
    player "... Phew, hah... I don't know what's going on.[pause]\nBut, did we just win?"
    $ addSecond("player3 neutral", "annie neutral")
    annie "... Looks like so."
    $ swapActive("annie neutral", "player3 fear")
    player "Who... who are you?[pause]\nWhere are you from?"
    player "Who are those guys attacking me?[pause]\nWhat is this bat?"
    player "And what's going on here?"
    $ swapActive("player3 fear", "annie shock")
    annie "Take it easy![pause]\nI'll answer your questions one by one, as much"
    annie "as I know."
    show annie confused
    annie "But I'm just as confused as you are.[pause]\nWho are you, by the way?"
    $ swapActive("annie confused", "player3 neutral")
    player "Sorry, I panicked..."
    $ swapActive("player3 neutral", "annie shuteyes")
    annie "Never mind.[pause]\nAnd we haven't introduced ourselves yet."
    show annie neutral
    annie "My name is Annie Bass.[pause]\nJust call me Annie."
    $ swapActive("annie neutral", "player3 concern")
    player "... I'm [playername].[pause] Good to see you."
    $ swapActive("player3 concern", "annie neutral")
    annie "[playername], good to see you, too."
    show annie happy
    annie "Your name sounds like a boy's name.[pause] So cool!"
    $ swapActive("annie happy", "player3 fear")
    player "!?"
    $ swapActive("player3 fear", "annie neutral")
    annie "What?[pause] Why do you look terrified?"
    $ swapActive("annie neutral", "player3 dissatisfied")
    player "Ahh, I'm now...\nA girl..."
    $ swapActive("player3 dissatisfied", "annie neutral")
    annie "Er?[pause] You're a girl![pause]\nLook at the costume I created for you!"
    annie "It suits you, right?"
    show annie proud
    annie "It's so cute...[pause]\nTake this Battle Suit as a gift from me!"
    $ swapActive("annie proud", "player3 neutral")
    player "... Battle Suit?"
    show player3 fear
    player "Oh my--Aaaah!!"

    scene shy girl with fade
    narrator "I just notice that\nI've been wearing girl's clothes!!"
    narrator "A sailor dress...\nAnd the skirt is awkwardly short!"
    narrator "The stockings... feel so strange!"
    player "And the feel of tightness around my chest... No way... (Touching)"
    player "Aaaah!"

    scene outside center morning with fastDissolve
    show annie with fastDissolve
    annie "The suit is a perfect match for your hair-tone.[pause]\nAnd it's ideal for workouts."
    show annie confused
    annie "Huh?[pause] Something wrong?"
    $ addSecond("annie", "player3 dissatisfied")
    player "It's...\nIt's just..."

    jump chapter2_1








    # This ends the game.

    return
