label chapter2_2:
    $ chapter("CHAPTER 2\nPART 2: Spacetime Flu")
    
    scene sound only with fastDissolve
    play music "audio/BGMusic/maze.wav"
    agentA "All teams, attention![pause] The Flux is declining!"
    agentA "The enemy may emerge at any minute![pause]\nHold position and get ready to fight!"
    agentB "... Sir!"
    agentB "Two human-like entities spotted in the central flux area.[pause] They just emerged from nowhere..."
    agentA "Human?[pause]\nImpossible![pause] What about the meme detection?"
    agentB "The hue is...\nGreen!!"
    agentB "Looks like two little girls...\nHold your fire!"
    agentA "..."
    agentA "Just got an order.[pause] The priority is to keep the girls under control and take them to the base."
    agentA "Send a Senior Agent to talk--"
    agentA "All others, stay alert![pause] You have my permission to take down the targets whenever needed!"
    agentB "Understood!"

    stop music fadeout 0.3
    scene outside center morning with fade
    narrator "We are carefully moving towards the exit of the Research Center."
    narrator "We do see the familiar streets at the exit, but didn't expect the barrier tapes and armed"
    narrator "personnel behind them."
    play music "audio/BGMusic/warbly riffs.wav"
    show player3 worry with fastDissolve
    player "Wh-why are there so many people here all of a sudden?!"
    show player3 fear
    player "Ah--Annie,\nChange my clothes back!"
    show player3 shameleft
    player "This suit is so embarrassing...[pause]\nWhat if someone recognizes me..."
    $ addSecond("player3", "annie confused")
    annie "Is it a right time to focus on this now?"
    show annie proud
    annie "Your clothes is safe with me.[pause] No worries..."
    annie "If you must, just take off the Battle Suit, and then put on those loose pieces."
    show annie shuteyes
    annie "But there are many guys here...[pause]\nAre you sure you wanna get changed in front of them?"
    $ swapActive("annie", "player3 shameright")
    player "Sniff-sniff...\nI'm actually a..."
    $ swapActive("player3", "annie shock")
    annie "Right... You were in boy's clothes![pause]\nNo way..."
    $ swapActive("annie", "player3 worry")
    player "Huh?[pause] Have you come across the same situation?"
    show player3 confused
    player "(It's possible... Maybe Annie is no ordinary girl?)"
    show player3 cheer
    player "(If it's true, Annie may understand my situation...)"
    $ swapActive("player3", "annie shuteyes")
    annie "Of course, I understand..."
    show annie happy
    annie "You snitched the clothes of the boy you have a crush on, right?"
    $ swapActive("annie", "player3 shadow")
    player "So that's what you understand??"
    $ swapActive("player3", "annie shuteyes")
    annie "Yup [playername], you are attracted to other's body odor, aren't you?[pause] No need to feel shy..."
    $ swapActive("annie", "player3 sad")
    player "Please... Don't put on this \"I-know-you're-a-pervert-and-I-don't-mind\" look!"
    show player3 fakecheer
    player "Puh... I still have no idea why I has become a girl..."
    hide player3
    hide annie
    with fastDissolve
    narrator "..."
    show agent with fastDissolve
    sidAgent "Halt![pause]\nHands up!"
    hide agent with fastDissolve
    narrator "A woman in black suit comes up, shouting."
    show agent with fastDissolve
    $ addSecond("agent", "player3 fear")
    player "Huh?[pause]\nShe thinks we are bad guys?"
    show player3 worry
    player "(What?[pause] The badge on the leading woman's chest)"
    player "(A round, concentric shield--Is she...)"
    $ removeSecond("player3", "agent")
    sidAgent "Girls, I'm an SID agent.[pause]\nTo keep yourselves safe, do not move."
    $ swap("agent", "player3 shadow")
    narrator "That's it![pause] She's from SID![pause]\nI'm doomed!!"
    narrator "My mind is suddenly flooded with news about waves of SID agents sent to capture spies."
    show player3 sad
    narrator "And all those rumors about \"secret jails\", \"assassinations\"... the list goes on..."
    $ swap("player3", "agent")
    sidAgent "Report from the Central Blockade Area![pause] The two targets don't show any intention to attack."
    sidAgent "Threat rating set to D+ for now."
    sidAgent "A couple of quick questions first...[pause]\n--Who are you?[pause] Why are you sneaking around here?"
    $ swap("agent", "player3 worry")
    player "I'm a student in this city..."
    show player3 shadow
    player "We're just... just on a field trip to the Research Center..."
    hide player3 with fastDissolve
    narrator "The agent in black suit doesn't hide her scorn."
    show agent with fastDissolve
    sidAgent "Oh, yeah?[pause] A field trip to the Research Center?"
    $ swap("agent", "agent3 worry")
    narrator "Crap...\nI just remember--"
    narrator "As the Ross Goblet disappeared, the Research Center has been shut down since last night."
    show player3 sad
    narrator "A field trip, here and now... Damn, what a lame excuse."
    narrator "See?[pause] She seems to have received an order from her earphone, looking at me seriously."
    $ addSecond("player3", "agent")
    sidAgent "It's my Boss.[pause] You have to follow me."
    hide player3
    hide agent
    with fastDissolve
    narrator "Within a few seconds, we are completely surrounded."
    narrator "All guns pointed right at us."
    show player3 sad with fastDissolve
    $ addSecond("player3", "annie confused")
    annie "[playername], they look scary...\nWe'd better run when the time is right."
    $ addThird("player3", "annie", "agent")
    sidAgent "Don't worry.[pause] We won't hurt you.[pause]\nAs long as you cooperate, everything will be"
    sidAgent "dealt with peacefully."
    sidAgent "You should be aware that the disappearance of Substance H is no laughing matter.[pause] From this"
    sidAgent "point on, anything beyond comprehensions could happen."
    $ removeThird("player3 confused", "annie", "agent", isLeftActive=True)
    player "(Anything... beyond comprehension?)"
    show player3 neutral
    player "Alright, got it.[pause] I'll go with you."
    $ swapActive("player3", "annie shock")
    annie "Er?[pause] Why are you going with them?[pause]\nHey![pause] [playername]!"
    $ swapActive("annie", "player3 fear")
    player "St... stop dragging me![pause] My skirt is almost off, you idiot!"
    $ swapActive("player3", "annie shock")
    annie "You're the idiot![pause] Why are you going with these strange guys?[pause] What if they knock you out and sell you?"
    $ swapActive("annie", "player3 shameright")
    player "Who would buy a guy..."
    show player3 fakecheer
    player "Ahem... I mean.. what kind of human traffickers would go about in this way?"
    $ swapActive("player3", "annie shadow")
    annie "[playername], you must've never seen the gangs on the Lebona Islands."
    $ swapActive("annie", "player3 worry")
    player "Anyway... Maybe we could clear up some doubts."
    player "So we'd better go with her..."
    $ swapActive("player3", "annie confused")
    annie "Alright, I'll follow you wherever you go..."
    $ swapActive("annie", "player3 worry")
    player "Uh, if you don't mind, could you pass me a coat?"
    show player3 shameleft
    player "This suit is too..."
    hide player3
    hide annie
    with fastDissolve
    narrator "It's so awkward to get people's attention in a girl's suit."
    show agent with fastDissolve
    sidAgent "Fine.[pause] I'll put in a request."
    sidAgent "...[pause] Sorry, request rejected.[pause]\nThe Officer said your dress is cute."
    $ swap("agent", "player3 worry")
    player "What's wrong with this Officer!"

    jump chapter2_3