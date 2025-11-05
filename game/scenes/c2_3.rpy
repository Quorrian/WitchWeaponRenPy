
label chapter2_3:
    $ chapter("CHAPTER 2\nPART 3: Another Mariru?")
    
    scene black with fastDissolve
    play music "audio/BGMusic/abnormal.wav"
    narrator "Escorted by the agents, Annie and I hopped into a jet-black sedan."

    scene car outside with fastDissolve
    pause
    narrator "The passenger compartment is suffocating."
    narrator "I wrap my arms around my knees,[pause] bewildered."
    narrator "Annie leans on me gently, which makes me feel somewhat relaxed."
    annie "So...[pause] what is SID?[pause]\nYou get edgy every time you hear it."
    player "Are you from outer space?[pause]\nSID is the intelligence department under the Senate."
    player "Some say SID plays a more important role than the Aegis defense system in keeping New"
    player "Opulentia neutral."
    player "But there're more urban legends about people taken by SID and never come back...[pause] It's just horrible."
    annie "Okay...[pause] But then, what's the Academy City?"
    player "(Wait...[pause] Does this girl have no common sense at all?)"
    narrator "Annie sees my surprised look...[pause] and she just gives me a relaxed smile."
    annie "Just relax, we won't have any problems!"
    annie "Because...[pause] you're special."
    player "..."
    narrator "It's weird that Annie's rambling has somehow calmed my agitated mind."
    narrator "It seems not that horrible to be taken away by SID..."
    narrator "(No.[pause] No.[pause] It is horrible!)"
    
    scene car inside with fade
    pause
    narrator "We arrive at the city's bustling business area and drive into an ordinary basement garage where"
    narrator "we get onto a car elevator."
    narrator "After the agent reports, the elevator starts to move."
    narrator "I can feel the swift movement of the elevator.[pause]\nThere's been a couple of long drops, and event"
    narrator "horizontal conveyor movements."
    player "(It's hard to imagine such an underground maze underneath the business area...)"
    narrator "Rumors about the SID headquarters abound.[pause]\nSome say it's located at the south suburbs of"
    narrator "New Opulentia, and the whole structure is coated with optical camouflage."
    narrator "Of course, for a building that doesn't officially exist in the system,"
    narrator "the media could make up anything as long as it attracts clicks."
    narrator "And where I'm stepping into is exactly the core area of this \"non-existent\" department."
    player "(I just hope that I won't be made \"non-existent\" here...)"

    scene black with fastDissolve
    narrator "We step off the car in front of a corridor wrapped with metal plates.[pause] It gives a sense of"
    narrator "technology and abstinence."
    narrator "The elevator door automatically shuts right after we get off.[pause] We hear it leaves as we continue"
    narrator "along the dark corridor.[pause] The air gets stiff and dreary."
    narrator "My heart is also sinking..."

    scene empty room with fastDissolve
    pause
    narrator "We follow the corridor and find ourselves end up in a well-lit, closed room."
    narrator "It looks like an interrogation room, although there wasn't any tables or chairs.[pause] It also has a glazed wall."
    narrator "Before I can turn to check on that wall--"
    show player3 fear with fastDissolve
    player "Whoooa--!"
    hide player3 with fastDissolve
    narrator "Someone forcefully reaches their arms around my waist."
    show player3 sad with fastDissolve
    player "Ouch... It hurts!"
    hide player3 with fastDissolve
    narrator "As I'm about to lose balance, I feel my head falls on something familiar, soft but firm."
    female "Well...[pause] Judging from your core strength, the spy stuff is not for you."
    female "I thought we got some body scan errors, so I wanted to personally confirm."
    female "Feels good though."
    narrator "The female voice from behind me sounds familiar."
    narrator "She loosens her arms.[pause] With lingering fright, I turn around."
    narrator "The woman in front of me--"
    show player3 blush with fastDissolve
    player "(Ah?[pause] That's... that's really huge!)"
    show player3 fear

    play music "audio/BGMusic/familiar.wav"
    player "Ms...[pause] Ms.[pause] Mariru!?"
    $ swap("player3", "annie confused")
    annie "You know her?"
    $ swap("annie", "mariru2 neutral")
    mariru "Huh?[pause] Could't wait to reveal your knowledge of an agent from another intelligence department?"
    mariru "You don't even care to hide your identity, do you?..."
    $ addSecond("mariru2", "player3 sad")
    player "(Gosh![pause] Silly me...)"
    $ tempHideBoth("mariru2", "player3")
    narrator "It's hard to believe, but this woman in uniform in front of me is the woman I met in my dream."
    narrator "The slim figure... the red hair... the sadist look..."
    $ tempShowBoth("mariru2", "player3")
    $ swapActive("player3", "mariru2 talk")
    mariru "You must answer my questions honestly now."
    show mariru2 smile
    mariru "Don't make any excuses or play any tricks."
    mariru "Interrogation is one of specialties, you know.[pause]\nI'll pull no punches."
    $ removeSecond("mariru2", "player3 worry")
    narrator "You're acting bossy and teasy.[pause] And you're now giving me this confident look with slight sneer."
    narrator "What's her full name again?[pause]\nRight, it's--"
    $ swap("player3", "mariru2 talk")
    mariru "Exactly.[pause] I'm the head of SID.[pause] My name is Mariru Von Braun."
    $ addSecond("mariru2", "player3 fear")
    narrator "Yes, it's her!"
    show player3 shock
    narrator "Wait... head of SID?[pause]\nI remembered she was the chief scientist?!"
    show player3 confused
    narrator "But having a close look at her clothes and shoulder marks, she's probably a big boss..."
    show player3 dissatisfied
    narrator "Her stockings and high heels are the same as yesterday though."
    $ swapActive("player3", "mariru2 neutral")
    mariru "Hey, girl, what are you looking at, huh?"
    $ swapActive("mariru2", "player3 sad")
    player "Oh![pause] Yeah...[pause] right![pause]\nSorry, Ma'am!"
    $ swapActive("player3", "mariru2 talk")
    mariru "You've got some guts, huh?[pause] Still got your head in the clouds."
    show mariru2 smile
    mariru "I've heard that you told many horrible stories about SID to this blue twin-tail."
    $ swapActive("mariru2", "player3 fear")
    narrator "Mariru twiddles her whip in her hands.[pause] I get nervous and swallow hard."
    $ swapActive("player3", "mariru2 neutral")
    mariru "Guess...[pause]\nHow many of them are true?"
    $ swapActive("mariru2", "player3 shadow")
    player "Uh![pause] I'm... so sorry!"
    hide mariru2
    hide player3
    with fastDissolve
    show annie shock with fastDissolve
    annie "B... blue twin-tail..."
    $ swap("annie", "mariru2 lecture")
    mariru "Now that you know fear, let's start with your identity."
    hide mariru2 with fastDissolve
    narrator "Mariru opens a hand-held device to project profiles on the wall."
    narrator "There're lots of photos of me captured by video surveillance from different angles."
    narrator "Nonetheless, the facial analysis results show--"
    narrator "[No matches found]"
    show mariru2 neutral with fastDissolve
    mariru "No arrival record...[pause] Aegis fails to identify."
    show mariru2 smile
    mariru "If it wasn't your poor physical fitness, you would be immediately dealt with as a spy or terrorist intruder."
    $ swap("mariru2", "player3 dissatisfied")
    narrator "I feel a bit embarrassed and rub my belly unconsciously."
    $ addSecond("player3", "annie shadow")
    annie "[playername], this girl looks tougher than the enemies we ran into earlier..."
    $ swapActive("annie", "player3 fakecheer")
    player "(Yeah... and she won't have any trouble seeing through my lies...)"
    $ removeSecond("annie", "player3 sad")
    player "(I'll confess![pause] Gosh![pause] Whatever!)"
    show player3 confused
    player "My name is [playername].[pause] Hmm, where should I begin..."
    player "It's a bit complicated, to be honest.[pause] I'm very confused too."
    player "You probably won't believe what I say..."
    $ swap("player3", "mariru2 lecture")
    mariru "Cut to the chase![pause] I'll have my own judgement!"

    play music "audio/BGMusic/come clean.wav"
    $ swap("mariru2", "player3 neutral")
    player "... Well... I had this dream."
    player "In the dream, I went to the Research Center to attend a lecture for my outdoor teaching"
    player "report... And I arrived right before the closing time."
    player "I met you there.[pause] And you said it has been captured..."
    hide player3 with fastDissolve
    narrator "Apparently, Mariru takes this as a joke or something."
    show player3 neutral with fastDissolve
    $ addSecond("player3", "mariru2 talk")
    mariru "You mean, you met me in a dream?"
    $ swapActive("mariru2", "player3 concerndrip")
    player "Yes, it was you.[pause]\nAnd you dragged me to a corner..."
    player "And you are an SS-level scientist recognized by the Senate..."
    player "Dr. Mariru Von Braun.[pause] Am I right?"
    $ swapActive("player3", "mariru2 neutral")
    mariru "...[pause] That's me."
    show mariru2 smile
    mariru "But this information is not secret--anybody familiar with New Opulentia knows it."
    mariru "... Forget it.[pause]\nSo, what happened next?"
    $ swapActive("mariru2", "player3 confused")
    player "You knocked down one of the intruders and got a pistol.[pause] You asked me to stay put and wait for"
    player "rescue, and you went to the hijack spot."
    $ swapActive("player3", "mariru2 smile")
    mariru "Hijack spot?[pause]\nWhere exactly?"
    $ swapActive("mariru2", "player3 casual")
    player "You said it was the Conference Hall."
    show player3 fear
    player "You were about to give a lecture there.[pause]\nYou were the lecturer."
    $ swapActive("player3", "mariru2 neutral")
    mariru "... Lecture... Lecturer."
    show mariru2 frown
    mariru "(Is she talking about the public lecture on Ross Goblet arranged by Wolfgang?)"
    mariru "(But it should have been canceled.[pause] How could she know about this?)"
    $ swapActive("mariru2", "player3 confused")
    player "Em... Ma'am?"
    $ swapActive("player3", "mariru2 neutral")
    mariru "Yeah... nothing.[pause] Go on."
    $ swapActive("mariru2", "player3 confused")
    player "And some masked gunmen came by.[pause] I ran downstairs and hid in the shadow of a slate..."
    player "Sorry but I can't remember what happened there..."
    player "I somehow fainted and when I woke up, I saw..."
    $ swapActive("player3", "mariru2 smile")
    mariru "What did you see?"
    $ removeSecond("mariru2", "player3 neutral")
    player "I saw smoke and flames all around."
    player "The Research Center and the surrounding buildings were all in ruins..."
    player "There was a pungent smell all around."
    show player3 concerndrip
    player "It had a heavy saline and bitter taste..."
    player "All people turned into stone figures."
    player "No, not exactly stone--it was salt."
    show player3 focus
    player "And I saw something shining in the air."
    player "It was like hell.[pause]\nBut somehow I can feel a kind of peculiar tranquility."
    player "Something is responding to me..."
    show player3 neutral
    player "And then my memory became vague...[pause] There might be a streak of light--"
    player "And... that's pretty much the end of the dream."
    show player3 confused
    player "When I woke up, I found myself on my bed in my room, and it was already morning."
    $ swap("player3", "mariru2 frown")
    mariru "Only... a dream...?"
    mariru "Your olfactory memory was so vivid as if you were actually there..."
    mariru "(What if this pungent smell is from brimstone...)"
    mariru "(It's like how Sodom and Gomorrah were detroyed mentioned in the Genesis)"

    jump chapter2_4