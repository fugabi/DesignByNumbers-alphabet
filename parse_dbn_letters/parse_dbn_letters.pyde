"""
s18018 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Converting some of Maeda's Design by Number
dbnletters.dbn code -> Processing
"""

dbn_letter = {}  # Dict of functions
 
def setup():
    parse_dbn_source("data/dbnletters.dbn")
    size(500, 280)
    strokeCap(SQUARE)
    noSmooth()
    noLoop()

def draw():
    strokeCap(ROUND);
    dbn_sample()
    scale(3,3)
    translate(80,0)
    dbn_sample()
    
def dbn_sample():
    for y in range(0, 5):
        for x in range(1, 6):
            dbn_letter[x + y * 5](x * 12, -20 - y * 12)
    dbn_letterZ(x * 12 + 12, -32 - y * 12)

def parse_dbn_source(file_path, color_mode = False):
    with open(file_path, "r") as f:
        dbn_source = f.readlines()
    inside_block = False
    command_name = ""
    command_block = []
    for ln in dbn_source:
        if ln.count("command"):
            command_name = ln[14:15]
        elif ln.count("{"):
            inside_block = True
        elif ln.count("}"):
            if command_name in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                def_dbn_letter(command_block, command_name)
            command_block = []  # empty block
            inside_block = False
        elif inside_block:
            command_block.append(ln.lstrip())


def def_dbn_letter(dbn_block, func_key):
    p_block = []
    for dbn_line in dbn_block:
        if dbn_line:
            p_block.append(dbn_line
                           .replace("line ", "line(")
                           .replace(" ", ",")
                           .replace("//", "#")
                           + ")")
    # println("def dbn_letter" + func_key)
    def func(h, v):
        with pushMatrix():
            scale(1, -1)
            for ln in p_block:
                # colorMode(HSB)
                # stroke(random(256), 200, 200)
                if ln[0] != "#":
                    eval(ln)

    dbn_letter[func_key] = func
    dbn_letter[ord(func_key) - 64] = func
    globals()["dbn_letter" + func_key] = func
