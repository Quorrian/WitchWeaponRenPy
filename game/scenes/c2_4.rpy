
label chapter2_4:
    $ chapter("CHAPTER 2\nPART 4: Identity Check")
    
    scene empty room with fastDissolve
    play music "audio/BGMusic/come clean.wav"
    show player3 neutral with fastDissolve
    player "Yeah... I'm also confused because it felt so real--unlike any dream."
    show player3 confused
    player "I've searched for news of fire or building damages, but there's nothing."
    player "The city looks just as peaceful as it used to be."
    show player3 neutral
    player "Except for one thing..."
    $ swap("player3", "mariru2 neutral")
    mariru "Hmm?"
    $ swap("mariru2", "annie neutral")
    annie "Except for what?"
    $ swap("annie", "player3 shameleft")
    player "When I woke up..."

    play music "audio/BGMusic/chill jazz piano.wav"
    player "I found my body changed to a girl's body..."
    $ swap("player3", "mariru2 neutral")
    mariru "..."
    $ addSecond("mariru2", "annie neutral")
    annie "..."
    $ removeSecond("mariru2", "annie")
    hide annie with fastDissolve
    show player3 dissatisfied with fastDissolve
    player "Well..."
    $ addSecond("player3", "mariru2 talk")
    mariru "Huh?[pause] Did you say... it changed?"
    $ swapActive("mariru2", "player3 dissatisfied")
    player "I'm not... I didn't look like this before..."
    player "I... I am actually a boy!"
    $ removeSecond("player3", "mariru2 talk")
    mariru "Ewwwww... a boy?"
    $ swap("mariru2", "annie shock")
    annie "Okay... wait, what?"
    $ swap("annie", "mariru2 smile")
    mariru "You mean you're a boy cross-dressing?[pause] (leans close)"
    $ addSecond("mariru2", "player3 fear")
    player "No, no... That's not what I mean.[pause]\nDon't get this close!"
    show player3 shameleft
    player "But... in some sense...[pause]\nMaybe you're right..."
    show player3 dissatisfied
    player "Oh god... how can I explain this!"
    $ removeSecond("player3", "mariru2 neutral")
    mariru "Anyway... you've got a great boob job.[pause] (Touches)"
    show mariru2 smile
    mariru "So bouncy... Where did you get it done?[pause]\nSuch a natural touch... (Pinches)"
    $ addSecond("mariru2", "annie happy")
    annie "Woo... I want to find out too!"
    hide mariru2
    hide annie
    with fastDissolve
    show player3 fear with fastDissolve
    player "Ouch![pause] No... it's not... wait...\nStop that!"
    $ swap("player3", "mariru2 neutral")
    mariru "Let me check... slender arms, curvy waistline, perfect."
    mariru "What materials did you use?[pause] Especially here...."
    $ swap("mariru2", "player3 fear")
    player "Ahhhhh![pause] That's itchy...!"
    show player3 shock
    player "Ms.[pause] Mariru![pause] Don't touch it here!"
    show player3 fear
    player "No...!"
    hide player3 with fastDissolve
    narrator "..."
    show player3 sad with fastDissolve
    player "Boohoo..."
    player "Believe it or not![pause] I was a boy until yesterday!"
    player "There was no surgery..."
    $ addSecond("player3", "mariru2 neutral")
    mariru "Yeah, no doubt about this."
    mariru "Such a complete gender change is impossible with current technologies."
    mariru "You cannot do this unless you replace every bone in your body."
    mariru "Which means, you are, and have been, a girl."
    $ swapActive("mariru2", "player3 sad")
    player "What![pause] I've told you![pause]\nI woke up as a girl."
    $ swapActive("player3", "mariru2 smile")
    mariru "Do you have proof?[pause]\nAnything to prove that you used to be a boy?"
    $ swapActive("mariru2", "player3 confused")
    player "Well... proof...\nYeah right![pause] My student ID card!"
    $ tempHideBoth("player3", "mariru2")
    narrator "We handed in all my belongings when entering here, including my clothes and ID card."
    narrator "Mariru taps on her hand-held device, which brings up my student card."
    $ tempShowBoth("player3", "mariru2")
    $ swapActive("mariru2", "player3 disbelief2")
    player "Yeah![pause] That's it![pause]\nLook![pause] That's the proof."
    $ swapActive("player3", "mariru2 neutral")
    mariru "The facial features do look a bit like you, but this is hardly any proof..."
    mariru "Let me retrieve all footages of [playername] for the last month in the metropolis surveillance system..."
    $ tempHideBoth("player3", "mariru2")
    narrator "Mariru taps on her tablet, looking a bit excited."
    $ tempShowBoth("player3", "mariru2")
    $ swapActive("mariru2", "player3 confused")
    player "I thought it was only a dream when I saw those ruins, and I thought everything will go back to"
    player "normal after waking up."
    player "But now, I become a girl..."
    $ swapActive("player3", "mariru2 smile")
    mariru "Apply bone change corrections.[pause] Activate gait analyses on your footage at the corridor just now..."
    $ tempHideBoth("player3", "mariru2")
    narrator "Mariru ignores my murmur and focuses on her tablet."
    $ tempShowBoth("player3", "mariru2")
    $ swapActive("mariru2", "player3 disbelief2")
    player "Maybe it's not a dream.[pause] But now, everything looks just fine.[pause] No fire, no destruction."
    show player3 fakecheer
    player "Ughh... I'm totally confused...!"
    player "I can't get things straight..."
    $ swapActive("player3", "mariru2 smile")
    mariru "... Gait pattern matches."
    $ swapActive("mariru2", "player3 confused")
    player "What does that mean?"
    $ swapActive("player3", "mariru2 neutral")
    mariru "Gait pattern is the signature control pattern of a person's muscles when walking.[pause] Even the best"
    mariru "agents can't disguise it."
    show mariru2 frown
    mariru "Although scientifically unexplainable...\nYou are [playername], no doubt."
    $ addThird("player3", "mariru2", "annie shock")
    annie "A... are you sure...?"
    $ removeThird("annie", "player3", "mariru2")
    $ removeSecond("mariru2", "player3 confused")
    player "Finally... I thought you guys knew something about this..."
    $ addSecond("player3", "mariru2 neutral")
    mariru "So, have you heard of the Ross Goblet?"
    $ swapActive("mariru2", "player3 fakecheer")
    player "Ross Goblet?[pause] A Substance H that suddenly disappeared under video surveillance, according"
    player "to the news this morning... But I haven't seen it in person yet."
    $ swapActive("player3", "mariru2 smile")
    mariru "Well, if you're telling the truth..."
    mariru "It will probably be the only reason that I would agree to give this boring lecture for free."
    show mariru neutral
    mariru "It is a Substance H found on the Ross Islands.[pause] Four gems with remarkable purity are mounted"
    mariru "on the exterior."
    $ swapActive("mariru2", "player3 worry")
    player "I did see something that looks like a shining goblet flying in the sky after I climbed out of the ruins."
    show player3 neutral
    player " It floated in the sky, emitting a faint red light..."
    $ removeSecond("player3", "mariru2 frown")
    mariru "Faint red?"
    mariru "(The faint red liquid in the goblet has been a mystery...)"
    mariru "(This is confidential information, and has never been made public even though the risk rating of"
    mariru "the goblet was lowered to \"Safe\" lately.)"
    mariru "(No one could give such details without having seen it before...)"
    show mariru2 neutral
    mariru "Regardless of whether it was a dream, I'm afraid we need to confirm more information with you."

    jump chapter2_5