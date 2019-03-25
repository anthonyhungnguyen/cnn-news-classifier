import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open('cnn.json', encoding="utf8") as json_data:
    articles = json.load(json_data)
    print(len(articles), "Articles loaded succesfully")
    statistic = {}
    for article in articles:
        title = article['title']
        cate = article['cate']
        content = article['content']
        if cate != None:
            newpath = dir_path + '\\tf-idf\\' + cate

            if cate not in statistic:
                count = 0
                statistic[cate] = 0
            else:
                statistic[cate] += 1
            count = statistic[cate]

            if not os.path.exists(newpath):
                os.makedirs(newpath)
            file_name = str(count)+'.txt'
            complete_path = os.path.join(newpath, file_name)
            f = open(complete_path, 'w', encoding="utf-8")
            f.write('{}\n{}\n{}\n'.format(title, cate, content))
            f.close()
