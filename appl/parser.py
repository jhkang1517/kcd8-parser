import json

import pandas as pd
import unicodedata


class Parser:

    def __init__(self):
        self.dct_data = {'concept': list()}

    def read_file(self):
        file_path = "C:/Users/jhkan/Desktop/20220620/제8차 한국표준질병ㆍ사인(死因)분류 DB master_5차.csv"
        df = pd.read_csv(file_path, encoding="utf-8")
        df = df.loc[:, ["분류\n기준", "질병분류\n코드", "한글명칭", "영문명칭"]]

        condition = df["분류\n기준"] == "소"
        condition2 = df["분류\n기준"] == "세"
        df = df.loc[condition | condition2, :]
        df = df.applymap(lambda x: x.replace('\xa0', '').replace('\xa9', '').replace('\xa6', '').replace('\xf6', '')
                         .replace('\u216a', '').replace('\xf3', '').replace('\xe9', '').replace('\xe8', '')
                         .replace('\xe7', '').replace('\u75ff', '').replace('\u970d', ''))

        # df.to_csv("C:/Users/jhkan/Desktop/20220620/test.csv", encoding="euc-kr", sep="|")

        for i in df.index:
            temp_dct = dict()
            # val1 = df._get_value(i, "분류\n기준")
            val2 = df._get_value(i, "질병분류\n코드")
            val3 = df._get_value(i, "한글명칭")
            val4 = df._get_value(i, "영문명칭")

            temp_dct['code'] = val2
            temp_dct['display'] = val3
            temp_dct['definition'] = val3
            temp_dct['designation'] = [{'language': 'en', 'value': val4}]

            self.dct_data['concept'].append(temp_dct)

            # json_val = json.dumps(temp_dct, ensure_ascii=False)
            # print(json_val)

            # clean_text_val1 = unicodedata.normalize("NFKD", val1)
            # clean_text_val2 = unicodedata.normalize("NFKD", val2)
            # clean_text_val3 = unicodedata.normalize("NFKD", val3)
            # clean_text_val4 = unicodedata.normalize("NFKD", val4)

            # print(clean_text_val1 + '|' + clean_text_val2 + '|' + clean_text_val3 + '|' + clean_text_val4)
            # print(val1 + '|' + val2 + '|' + val3 + '|' + val4)

        with open("C:/Users/jhkan/Desktop/20220620/sample.json", 'w') as outfile:
            json.dump(self.dct_data, outfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    a = Parser()
    a.read_file()
