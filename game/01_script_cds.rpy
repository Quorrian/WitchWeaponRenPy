python early:
    def parse_smartSay(lexer):
        line = lexer.rest()
        quoteIndex = line.index("\"")
        meta = line[0:quoteIndex]
        what = line[quoteIndex+1:-1].replace('\\"', '"').replace("\\n", "[nl]")
        renpy.log(what)
        splitIndex = meta.index(" ")
        who = meta[0:splitIndex]
        how = meta[splitIndex:]
        return (who, how, what)

    def parse_smartSayDrop(lexer):
        line = lexer.rest()
        quoteIndex = line.index("\"")
        meta = line[0:quoteIndex]
        what = line[quoteIndex+1:-1].replace('\\"', '"').replace("\\n", "[nl]")
        renpy.log(what)
        splitIndex = meta.index(" ")
        splitIndex2 = meta.index(" ", splitIndex+1)
        whodrop = meta[0:splitIndex]
        who = meta[splitIndex+1:splitIndex2]
        how = meta[splitIndex2:]
        return (whodrop, who, how, what)

    def execute_sayswap(parsed_object):
        who, how, what = parsed_object
        renpy.call("smartSwapSay", eval(who), how, what)

    def execute_sayadd(parsed_object):
        who, how, what = parsed_object
        renpy.call("smartAddSay", eval(who), how, what)

    def execute_saydrop(parsed_object):
        whodrop, who, how, what = parsed_object
        renpy.call("smartDropSay", eval(whodrop), eval(who), how, what)

    def lint_smartSay(parsed_object):
        who, how, what = parsed_object
        try:
            eval(who)
        except Exception:
            renpy.error("Character not defined: {}".format(who))

        tte = renpy.check_text_tags(what)
        if tte:
            renpy.error(tte)

    def lint_smartSayDrop(parsed_object):
        whoDrop, who, how, what = parsed_object
        try:
            eval(whodrop)
        except Exception:
            renpy.error("Character (drop) not defined: {}".format(whodrop))
        try:
            eval(whodrop)
        except Exception:
            renpy.error("Character (say) not defined: {}".format(who))

        tte = renpy.check_text_tags(what)
        if tte:
            renpy.error(tte)

    renpy.register_statement(
        "sayswap",
        parse=parse_smartSay,
        execute=execute_sayswap,
        lint=lint_smartSay,
    )

    renpy.register_statement(
        "sayadd",
        parse=parse_smartSay,
        execute=execute_sayadd,
        lint=lint_smartSay,
    )

    renpy.register_statement(
        "saydrop",
        parse=parse_smartSayDrop,
        execute=execute_saydrop,
        lint=lint_smartSayDrop,
    )