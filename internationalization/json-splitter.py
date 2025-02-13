import json
import os

# If at some point you want to split the languages.json file into separate files for each language, you can use the following script.

def split_languages(input_file):
    output_dir = "language-files"
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    num_languages = 0
    for lang_code, translations in data.items():
        output_file = os.path.join(output_dir, f"{lang_code}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({lang_code: translations}, f, ensure_ascii=False, indent=4)
            num_languages += 1
        print(f"Created {output_file}")
    print(f"Created {num_languages} language files.")

if __name__ == "__main__":
    input_filename = "languages.json"  
    split_languages(input_filename)