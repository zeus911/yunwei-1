# -*- coding: utf-8 -*-
import sys
import logging

from mmpy_bot import bot, settings


def main():
    logging.basicConfig(**{
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%m/%d/%Y %H:%M:%S',
        'level': logging.DEBUG if settings.DEBUG else logging.INFO,
        'stream': sys.stdout,
    })

    try:
        b = bot.Bot()
        b.run()
        print('运行结束')
    except KeyboardInterrupt:
        print('异常结束')
        pass


if __name__ == "__main__":
    # execute only if run as a script
    main()