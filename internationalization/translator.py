import ssl
import argostranslate.package
import argostranslate.translate
from googletrans import Translator
import json

ssl._create_default_https_context = ssl._create_unverified_context

# Define input values as a list of tuples (label, input_text)
input_values = [
    ("bruh", "Should be greater than:"),
    ("brig", "and should be less than:"),
]

from_code = "en"
languages = ["en", "es", "fr", "ka", "ar", "az", "bg", "bn", "bs", "cs", "da", "de", "el", "et", "fa", "fi", "tl", "he", "hi", "hr", "hu", "id", "it", "ja", "ko", "pl", "pt", "ru", "sk", "sv", "tr", "vi", "zh"]

# Initialize Google Translator
translator = Translator()

# Install the packages
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()

# Store installed languages
installed_languages = []

for to_code in languages:
    # Find the package to install
    package_to_install = next(
        (pkg for pkg in available_packages if pkg.from_code == from_code and pkg.to_code == to_code), 
        None
    )
    
    if package_to_install is not None:
        argostranslate.package.install_from_path(package_to_install.download())
        installed_languages.append(to_code)  # Track installed languages
    else:
        print(f"No translation model found for {from_code} to {to_code}. Will use google translate instead.")

# Open the file in write mode
translations = {}
for language in languages:
    lang_code = "fil" if language == "tl" else language
    translations[lang_code] = {}
    for label, input_text in input_values:
        if language in installed_languages:
            # Argos Translate
            translated_text = argostranslate.translate.translate(input_text, from_code, language)
        else:
            # Google Translate fallback
            print(f"Using Google Translate for {language}...")
            translated_text = translator.translate(input_text, src=from_code, dest=language).text
        
        translations[lang_code][label] = translated_text

    lang_file = f'language-files/{lang_code}.json'
    try:
        with open(lang_file, 'r+', encoding='utf-8') as file:
            lang_data = json.load(file)
    except FileNotFoundError:
        lang_data = {}
        
    lang_data[lang_code].update(translations[lang_code])

    with open(lang_file, 'w', encoding='utf-8') as file:
        json.dump(lang_data, file, ensure_ascii=False, indent=4)
        print(f"Translation for {lang_code} completed.")
        
print("Translation completed. Check translated.txt")