import time
import os

frames = {
    "frame1": [  # лапка вверх + Luck
        "   /\\_/\\     ",
        "  ( o.o )  /",
        "   > ^ <       ",
        "    Luck       "
    ],
    "frame2": [  # лапка вниз + lUck
        "   /\\_/\\     ",
        "  ( o.o )",
        "   > ^ <  \\",
        "    lUck       "
    ],
    "frame3": [  # лапка вверх + luCk
        "   /\\_/\\     ",
        "  ( o.o )  /",
        "   > ^ <       ",
        "    luCk       "
    ],
    "frame4": [  # лапка вниз + lucK
        "   /\\_/\\     ",
        "  ( o.o )",
        "   > ^ <  \\",
        "    lucK       "
    ]
}

# сортировка кадров по ключам
keys = sorted(frames.keys())

# цикл анимации
for i in range(6):  # сколько раз повторить
    for key in keys:
        os.system("cls" if os.name == "nt" else "clear")  # очистка консоли
        for line in frames[key]:
            print(line)
        time.sleep(0.5)
