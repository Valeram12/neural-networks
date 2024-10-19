import os
import pandas as pd


def search_fonts(directory='fonts', threshold=5000):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        df = pd.read_csv(file_path)
        if len(df) > threshold:
            print(file.replace('.csv', ''), len(df))


def merge_fonts(font_list=None, directory='fonts', num_rows=10000):
    if font_list is None:
        font_list = ['ARIAL', 'TIMES', 'CALIBRI', 'MONEY', 'NUMERICS']

    data_combined = []

    for font_name in font_list:
        file_path = os.path.join(directory, f"{font_name}.csv")
        df = pd.read_csv(file_path)
        selected_data = df.iloc[:, 12:412]
        selected_data['font_family'] = font_name
        data_combined.append(selected_data.sample(frac=1, random_state=42).head(num_rows))

    final_data = pd.concat(data_combined, ignore_index=True)
    shuffled_data = final_data.sample(frac=1, random_state=42)
    
    return shuffled_data[['font_family'] + [col for col in shuffled_data.columns if col != 'font_family']]


font_data = merge_fonts()
font_data.to_csv('merged_fonts.csv', index=False)
