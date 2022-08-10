#!/usr/bin/env python

import argparse
from config import audio_codecs, video_codecs
from factory import Factory
from adapter_cls import AdapterCls


def main():
    parser = argparse.ArgumentParser(description='Codec choice')

    parser.add_argument('--codec', type=str, choices=[*audio_codecs, *video_codecs],
                        help='set codec')

    parser.add_argument('--open-file-name', type=str,
                        help='path to a file (dummy)')

    parser.add_argument('--save-file-name', type=str,
                        help='path to a file (dummy)')

    args = parser.parse_args()
    if not args.codec:
        print(f'''Варианты кодеков:
        Аудио: {" ".join(audio_codecs)}
        Видео: {" ".join(video_codecs)}''')

    factory = Factory(args.codec)
    factory.decode(AdapterCls)
    factory.save(AdapterCls)


if __name__ == '__main__':
    main()
