# -*- coding:utf-8 -*-
import sys
from imp import reload

reload(sys)
import random
import jieba


def autotxt():
    # file = open(fname1)
    # string=file.read()
    # dataset_file=string.split()

    dataset_file = [
        '''在卷积神经网络广泛应用后，人们开始尝试使用它对图像的诱发情感进行研究。''',
        '''然而，虽然神经网络有很多优秀的模型可用于图像处理识别，但其本身并不具备高层语义以及先验知识，这决定了直接使用这些模型分析情感所带来的局限性。''',
        '''本文探讨了一种在神经网络的基础上利用语义知识的图像情感分析方式，对于图像的低层信息，本文使用迁移学习训练神经网络实现情感分布预测。''',
        '''对于图像的高层语义信息，我们使用神经词向量对网络文本进行提取形成知识库，并在图像目标检测的基础上分析可能的语义联想，实现了对先验知识的利用。''',
        '''最后，本文对网络图像包含的上下文信息、低层图像特征和高层语义信息进行多模态融合与分析，最终实现对图像的诱发情感分布的预测。''',
    ]
    print("\n分词前：", dataset_file)
    for i, each_sentence in enumerate(dataset_file):
        dataset_file[i] = " ".join(jieba.cut(each_sentence))
        print("\n分词后：", dataset_file)
    model = {}

    for line in dataset_file:
        line = line.lower().split()
        for i, word in enumerate(line):
            if i == len(line) - 1:
                model['END'] = model.get('END', []) + [word]
            else:
                if i == 0:
                    model['START'] = model.get('START', []) + [word]
                model[word] = model.get(word, []) + [line[i + 1]]
    print("\n模型：", model)
    generated = []
    while True:
        if not generated:
            words = model['START']
        elif generated[-1] in model['END']:
            break
        else:
            words = model[generated[-1]]
        generated.append(random.choice(words))
    print("\n生成的一个结果：" + "".join(generated))
    # file.close()


#########################
autotxt()
