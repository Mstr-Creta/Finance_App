import json

budget_limits = {
    "Groceries": 1000,
    "Travel": 500,
    "Dining": 800,
    "Shopping": 600
}

def load_categories(path):
    with open(path, "r") as f:
        return json.load(f)

def save_categories(categories, path):
    with open(path, "w") as f:
        json.dump(categories, f, indent=2)

def add_keyword_to_category(category, keyword, categories):
    keyword = keyword.strip()
    if keyword and keyword not in categories[category]:
        categories[category].append(keyword)

def check_budget_alert(category, amount):
    if category in budget_limits and amount > budget_limits[category]:
        return f"⚠️ You've exceeded your budget for **{category}** (Spent: {amount:.2f} AED)"
    return None