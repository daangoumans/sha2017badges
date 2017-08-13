import ugfx, badge, random, os

interval = 300000

swearing = [
    "Fuck off",
    "Piss off",
    "Bugger off",
    "Sod off",
    "Go away",
    "Arsehole",
    "Twat",
    "Cockwomble",
    "Arse",
    "Screw you",
    "Fuck you",
    "Wanker",
    "Lamer",
    "N00b",
    "Oxygen thief",
    "Cunt",
    "Turd",
    "Asshat",
    "Douche",
    "Douchebag",
    "Bastard",
    "Bitch",
    "Fucknugget",
    "Fucktard",
    "Cocksucker",
    "Shitbag",
    "Shitstain",
    "Idiot",
    "Tool",
    "Fartbreath",
    "Fart",
    "Bellend",
    "Jabroni",
    "Motherfucker",
    "Unclefucker",
    "Wankstain",
    "Cuntscab",
    "Douchecanoe",
    "Asswipe",
    "Arsewipe",
    "Moron",
    "Halfwit",
    "Twerp",
]

seeded = False
message = ""

def setup():
    pass

def loop():
    global interval, seeded, message, swearing
    enabled = badge.nvs_get_u8("sweary","enable", 0)
    if enabled:
	if not seeded:
	    seed = sum(c << (i*8) for i, c in enumerate(os.urandom(4)))
	    random.seed(seed)
	    seeded = True
	# Do this here so that we don't choose a new message as soon as we redraw for sleep
	message = random.choice(swearing);
        return interval

    return 9999999999

def draw(y, sleep=2):
    global message
    enabled = badge.nvs_get_u8("sweary","enable", 0)
    if enabled and seeded and sleep:
        nick = badge.nvs_get_str("owner", "name", 'Offensive Owner')

	ugfx.clear(ugfx.BLACK)
	ugfx.flush()
	ugfx.clear(ugfx.WHITE)
	ugfx.flush()

	ugfx.string_box(0,10,296,26, nick + " says:", "Roboto_BlackItalic24", ugfx.BLACK, ugfx.justifyLeft)
	ugfx.string_box(0,45,296,38, message, "PermanentMarker36", ugfx.BLACK, ugfx.justifyCenter)

	return [interval, 0]

    return [9999999999, 0]
