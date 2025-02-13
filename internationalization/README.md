# 🌍 fEMR Internationalization (i18n) Guide

## 📖 Table of Contents

1. [🌎 Language List](#language-list)
2. [💻 Using the Script](#using-the-script)
3. [🌐 Adding a New Language](#adding-a-new-language)
4. [📝 Adding Text to the Main fEMR Repo](#adding-text-to-the-main-femr-repo)

---

## Language List

| Language    | Code | Language           | Code  |
| ----------- | ---- | ------------------ | ----- |
| English     | `en` | Italian            | `it`  |
| Spanish     | `es` | Japanese           | `ja`  |
| French      | `fr` | Korean             | `ko`  |
| Georgian    | `ka` | Polish             | `pl`  |
| Arabic      | `ar` | Portuguese         | `pt`  |
| Azerbaijani | `az` | Russian            | `ru`  |
| Bulgarian   | `bg` | Slovak             | `sk`  |
| Bengali     | `bn` | Swedish            | `sv`  |
| Bosnian     | `bs` | Turkish            | `tr`  |
| Czech       | `cs` | Vietnamese         | `vi`  |
| Danish      | `da` | Chinese            | `zh`  |
| German      | `de` | Tagalog (Filipino) | `fil` |
| Greek       | `el` | Hebrew             | `he`  |
| Estonian    | `et` | Hindi              | `hi`  |
| Persian     | `fa` | Croatian           | `hr`  |
| Finnish     | `fi` | Hungarian          | `hu`  |
| Indonesian  | `id` | -                  | -     |

---

## Using the Script

```bash
# 1️⃣ Copy the language files into the directory
cp /path/to/language-files .

# 2️⃣ Add your label and text data to `translator.py`
# Edit the `input_values` array inside `translator.py`

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the script
python3 translator.py

# Translations will populate the language files

# 5️⃣ Replace the main repo’s language-files with the new ones
mv language-files /path/to/femr-repo
```

---

## Adding a New Language

1. Add the new language’s code to the **Language List** in **translator.py**.
2. Run the script to generate the translations.
3. Verify the translations before adding them to the main repo.

---

## Adding Text to the Main fEMR Repo

Within the file you added text to, you will need to call an update function within the script block to load the translations.
Here is an example of that:

---

### Notes:

- Ensure that all translations are accurate before pushing changes.
- Maintain consistency with existing translation formats.
