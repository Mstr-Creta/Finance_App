from style_utils import apply_custom_styles, render_title, render_header, alert_box, success_box
apply_custom_styles()

import streamlit as st
from data_processing import load_transactions, categorize_transactions
from helpers import save_categories, add_keyword_to_category, load_categories, check_budget_alert
import plotly.express as px
import os


st.set_page_config(page_title="Your Daily Finance App", page_icon="🤑", layout="wide")
category_file = "categories.json"

if "categories" not in st.session_state:
    st.session_state.categories = {"Uncategorized": []}

if os.path.exists(category_file):
    st.session_state.categories = load_categories(category_file)

def main():
    render_title("💸 Your Beautiful Finance Dashboard")

    uploaded_file = st.file_uploader("Upload your transaction CSV file", type=["csv"])
    if uploaded_file:
        df = load_transactions(uploaded_file)
        if df is not None:
            df = categorize_transactions(df, st.session_state.categories)
            debits_df = df[df["Debit/Credit"] == "Debit"].copy()
            credits_df = df[df["Debit/Credit"] == "Credit"].copy()
            st.session_state.debits_df = debits_df.copy()

            tab1, tab2 = st.tabs(["💸 Expenses", "💰 Payments"])
            with tab1:
                new_category = st.text_input("New Category Name")
                if st.button("Add Category") and new_category:
                    if new_category not in st.session_state.categories:
                        st.session_state.categories[new_category] = []
                        save_categories(st.session_state.categories, category_file)
                        st.rerun()

                st.subheader("Your Expenses")
                edited_df = st.data_editor(
                    debits_df[["Date", "Details", "Amount", "Category"]],
                    column_config={
                        "Date": st.column_config.DateColumn("Date", format="DD/MM/YYYY"),
                        "Amount": st.column_config.NumberColumn("Amount", format="₹%.2f INR"),
                        "Details": st.column_config.TextColumn("Details"),
                        "Category": st.column_config.SelectboxColumn(
                            "Category", options=list(st.session_state.categories.keys())
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor"
                )

                if st.button("Apply Changes", type="primary"):
                    for idx, row in edited_df.iterrows():
                        new_cat = row["Category"]
                        old_cat = debits_df.at[idx, "Category"]
                        if new_cat != old_cat:
                            details = row["Details"]
                            debits_df.at[idx, "Category"] = new_cat
                            add_keyword_to_category(new_cat, details, st.session_state.categories)
                    save_categories(st.session_state.categories, category_file)

                render_header("📊 Expense Summary")
                category_totals = debits_df.groupby("Category")["Amount"].sum().reset_index()
                category_totals = category_totals.sort_values("Amount", ascending=False)
                st.dataframe(category_totals, use_container_width=True, hide_index=True)

                #Budget Alerts
                for _, row in category_totals.iterrows():
                    alert_msg = check_budget_alert(row["Category"], row["Amount"])
                    if alert_msg:
                        alert_box(alert_msg)

                fig = px.pie(
                    category_totals,
                    values="Amount",
                    names="Category",
                    title="Expenses by Category"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # 📅 Monthly Expense Trend
                monthly_trend = debits_df.copy()
                monthly_trend["Month"] = monthly_trend["Date"].dt.to_period("M").astype(str)
                monthly_summary = monthly_trend.groupby("Month")["Amount"].sum().reset_index()

                fig_line = px.line(
                monthly_summary, 
                x="Month", 
                y="Amount", 
                markers=True,
                title="🕒 Monthly Spending Trend"
                )
                st.plotly_chart(fig_line, use_container_width=True)

                # 🔁 Top Spending Categories (Bar Chart)
                fig_bar = px.bar(
                category_totals, 
                x="Category", 
                y="Amount", 
                title="🏷️ Top Spending Categories",
                color="Amount", 
                color_continuous_scale="Reds"
                )
                st.plotly_chart(fig_bar, use_container_width=True)

                # 📈 Category-Wise Monthly Spending
                category_monthly = debits_df.copy()
                category_monthly["Month"] = category_monthly["Date"].dt.to_period("M").astype(str)
                grouped = category_monthly.groupby(["Month", "Category"])["Amount"].sum().reset_index()

                fig_multi_line = px.line(
                grouped, 
                x="Month", 
                y="Amount", 
                color="Category",
                title="📈 Category-Wise Monthly Spending"
                )
                st.plotly_chart(fig_multi_line, use_container_width=True)


            with tab2:
                st.subheader("Payments Summary")
                total_credits = credits_df["Amount"].sum()
                st.metric("Total Payments", f"₹{total_credits:,.2f} INR")
                st.dataframe(credits_df, use_container_width=True)

main()