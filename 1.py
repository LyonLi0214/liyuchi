import xml.etree.ElementTree as ET
import os
import pandas as pd

# 文件夹路径列表
folders = {
    'ja': 'C:\\Users\\Lyon\\Desktop\\1\\jp',  # 日文文件夹
    'zh': 'C:\\Users\\Lyon\\Desktop\\1\\zh',    # 中文文件夹
    'en': 'C:\\Users\\Lyon\\Desktop\\1\\en',  # 英文文件夹
    'ko': 'C:\\Users\\Lyon\\Desktop\\1\\kr',      # 韩语文件夹
    'fr': 'C:\\Users\\Lyon\\Desktop\\1\\fr',      # 法语文件夹
    'de': 'C:\\Users\\Lyon\\Desktop\\1\\de'       # 德语文件夹
}

data = {}

# 遍历每个语言文件夹
for lang, folder in folders.items():
    for filename in os.listdir(folder):
        if filename.endswith('.xml'):
            tree = ET.parse(os.path.join(folder, filename))
            root = tree.getroot()
            
            for text in root.findall('entries/text'):
                text_id = text.get('id')
                text_value = text.text
                
                if text_id not in data:
                    data[text_id] = {}
                data[text_id][lang] = text_value

# 创建DataFrame
df = pd.DataFrame.from_dict(data, orient='index').fillna('')

# 导出为CSV，列名为 id-日文-中文-日文-韩语-法语-德语
df.reset_index(inplace=True)
df.columns = ['ID', '日文', '中文', '英文', '韩语', '法语', '德语']
df.to_csv('aligned_corpus.csv', index=False, encoding='utf-8-sig')
