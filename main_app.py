
import streamlit as st
from modules.sponsorship import partner_ecosystem_builder

TOOLS = {
    "Partner Ecosystem Builder": {
        "function": partner_ecosystem_builder.run,
        "role": ["Admin", "Board", "Sponsorship Manager"],
        "category": "Sponsorship Tools"
    }
}

def run_app(user_role="Admin"):
    st.set_page_config(page_title="SportAI Dashboard", layout="wide")
    st.sidebar.title("SportAI Modules")

    # Filter tools based on role
    visible_tools = {name: config for name, config in TOOLS.items() if user_role in config["role"]}
    categories = sorted(set(config["category"] for config in visible_tools.values()))
    selected_category = st.sidebar.selectbox("Select Tool Category", categories)

    tools_in_category = [name for name, config in visible_tools.items() if config["category"] == selected_category]
    selected_tool = st.sidebar.selectbox("Select Tool", tools_in_category)

    # Run selected tool
    tool_config = visible_tools[selected_tool]
    tool_config["function"]()

if __name__ == "__main__":
    run_app()
