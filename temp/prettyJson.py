import argparse
import os
import json

if __name__ == '__main__':
    raw_filepath = "../../wizard_of_wikipedia/test_random_split.json"   
    with open(raw_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open("data/raw.json", 'w', encoding='utf-8') as f:
        for conv_ex in data[:5]:
            json.dump(conv_ex, f, indent=4) 
            f.write(3*'\n')
   
    data = []
    with open("data/test_seen.jsonl", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data.append(json.loads(line))

    with open("data/preprocessed.jsonl", 'w', encoding='utf-8') as f:
        for conv_ex in data[:5]:
            json.dump(conv_ex, f, indent=4) 
            f.write(3*'\n')
