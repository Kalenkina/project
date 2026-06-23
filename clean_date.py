import pandas as pd
import re

VALID_ACTIONS = ['like', 'comment', 'share', 'view']

df = pd.read_json('file.jsonl', lines=True)

df = df[df['action_type'].isin(VALID_ACTIONS)]

def clean_comment(text):
    if pd.isna(text):
        return ""
    text = re.sub(r'[^A-Za-zА-Яа-я0-9\s]', '', str(text))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['comment_text'] = df['comment_text'].apply(clean_comment)

df['post_id'] = df['post_id'].fillna(0)

df.to_csv('cleaned_activities.csv', index=False)

print("Деректер тазартылды")