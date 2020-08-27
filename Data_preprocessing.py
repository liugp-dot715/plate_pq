# coding=utf-8

import xlrd
import untils
import jieba
import jieba.analyse

data = xlrd.open_workbook('./data/北京车牌.xlsx')
# ['小客车摇号问题及答案', '机动车上牌问题及答案', '附件_阶梯中签率对照表', '附件_机动车牌证申请表', '相关政策']
sentence_list = []
table = data.sheet_by_name('小客车摇号问题及答案')
sentence_list = table.col_values(3) + table.col_values(2)
table = data.sheet_by_name('机动车上牌问题及答案')
sentence_list = sentence_list + table.col_values(3) + table.col_values(2)

sentence = ''
for line in sentence_list:
    try:
        if '\n' in line:
            for line_one in line.split('\n'):
                line_seg = untils.seg_depart(line_one).replace(' ', '')
                sentence = sentence + line_seg
        else:
            ine_seg = untils.seg_depart(line).replace(' ', '')
            sentence = sentence + ' ' + line_seg
    except:
        pass

keywords = jieba.analyse.extract_tags(sentence,
                                      topK=200,
                                      withWeight=True,
                                      allowPOS=('n', 'nr', 'nz', 'PRE', 'ns', 'LOC', 'nt', 's', 'ORG', 'nw'))
for item in keywords:
    print(item[0], item[1])