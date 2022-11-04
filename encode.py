#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/11/4 11:23
# @Author : DongHao

class Encode:
    def __init__(self, s):
        self.text = s
        self.res_encode = ''
        self.res_decode = ''
        self.dic_uni_to_code = dict()
        self.dic_code_to_uni = dict()
        self.arr_n = [
            '峥老师',
            '董浩叔叔',
            '薛屌',
            '小刘',
            '帕克王',
            '狗西',
            '玩蛇',
            '子峰',
            '坤坤',
            '科比',
            '开黑啦',
            'bilibili',
            '斗鱼',
            'tweet',
            'ph',
            'dota2',
            'csgo',
            'TI',
            'Professional',
            '西班牙老板',
            '人声鼎沸的直播间',
            '烟花',
            '丁真',
            '俊豪',
            '小强',
            'kaka',
            '海南',
            '赛博丁真',
            '女拳',
        ]

        self.arr_v = [
            'Hello',
            '惜败',
            '碾压',
            '乱杀',
            '吐了',
            '健身',
            '登dua郎',
            '让他了解',
            '失声痛哭在',
            '单防',
            '踢走',
            '送走',
        ]
        self.arr_punctuation = [
            '= =',
            '.',
            '?',
            '!',
            '~',
            '...',
            '。',
            '——',
        ]
        self.words = self.generate_words()
        self.generate_dic()

    def decode(self):
        src = self.text.split('†')
        res = ''
        for s in src:
            unicode = self.dic_code_to_uni[s]
            res += chr(unicode)
        self.res_decode = res

    def encode(self):
        tmp = ""
        for c in self.text:
            tmp += self.encode_char(c)
            tmp += '†'
        self.res_encode = tmp.rstrip('†')

    def encode_char(self, c):
        unicode = ord(c)
        return self.dic_uni_to_code[unicode]

    def generate_words(self):
        res = []
        for i in self.arr_n:
            for j in self.arr_v:
                for k in self.arr_n:
                    for l in self.arr_punctuation:
                        if i != k:
                            res.append(i + j + k + l)
        return res

    def generate_dic(self):
        for i in range(0, 65536):
            self.dic_uni_to_code[i] = self.words[i]
            self.dic_code_to_uni[self.words[i]] = i




