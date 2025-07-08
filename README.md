---

## 🤑 Daily Finance Dashboard

A sleek and interactive personal finance tracker powered by **Streamlit**, **Plotly**, and **Pandas**—perfect for visualizing expenditures, managing budgets, and showcasing your Python portfolio.

---

### 🚀 Features

- 🔍 **Smart Categorization**: Auto-tags transactions by keywords
- 🧠 **Keyword Learning**: Improves over time as users update categories
- 📊 **Multi-Chart Visualizations**:
  - Pie Chart by Category
  - Monthly Expense Trend (Line Chart)
  - Top Categories (Bar Chart)
  - Spending by Weekday
  - Category-Wise Monthly Breakdown
- 💸 **Currency Conversion**: Choose your base and target currency; updated via live exchange rates
- 🔔 **Budget Alerts**: Set spending limits for each category
- ✨ **Custom Styled UI**: Beautiful typography, headers, and warning badges

---

### 🧱 Project Structure

```
finance_dashboard/
├── app.py                  # Main Streamlit app
├── data_processing.py      # CSV loading & categorization logic
├── helpers.py              # Category management and budgeting
├── currency_utils.py       # Conversion logic with API call
├── style_utils.py          # Text styling and custom CSS
├── categories.json         # Saved category-keyword mapping
├── requirements.txt        # App dependencies
```

---

### 📦 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

### 🔄 Currency Conversion (Next Update)

Powered by [ExchangeRate.host](https://exchangerate.host). Choose base and target currencies from dropdowns to instantly convert all values.

---

### 🌟 Visualizations

| Chart Type                          | Purpose                                      |
|------------------------------------|----------------------------------------------|
| 🥧 Pie Chart                        | Expense breakdown by category                |
| 📈 Line Chart                       | Monthly spending trend                       |
| 📊 Bar Chart                        | Compare top categories                       |
| 🗓️ Bar Chart (by weekday)          | Spot spending habits by day                  |
| 📉 Multi-line Chart                 | Category-wise monthly trends                 |

---

### 🔐 Budgeting

Set limits in `helpers.py`:
```python
budget_limits = {
    "Groceries": 1000,
    "Travel": 500,
    ...
}
```

App auto-detects overspending and displays styled warnings.

---

### 🧰 Tech Stack

- Streamlit  
- Pandas  
- Plotly  
- requests  
- HTML & CSS for styling  
- JSON for persistent data

---

### 📄 License

MIT License — feel free to fork, improve, and share!

---

### 🙌 About Me

Made with care by **Creta** — a passionate cloud security and data engineering explorer with a focus on automation, modular design, and scalable tools.

---


