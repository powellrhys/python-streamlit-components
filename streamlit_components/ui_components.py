from typing import Literal
import streamlit as st
import warnings

def configure_page_config(
    repository_name: str,
    initial_sidebar_state: Literal["expanded", "collapsed", "auto"] = "expanded",
    layout: Literal["wide", "centered"] = "wide",
    page_icon: str = ":streamlit:",
    authentication_enabled: bool = True
) -> None:
    """
    Configures the Streamlit page settings, including the sidebar state, layout, page icon,
    and menu items. It also supports enabling or disabling authentication components.

    Args:
        repository_name (str): The name of the repository used to generate the "Report a Bug" menu link.
        initial_sidebar_state (Literal["expanded", "collapsed", "auto"], optional): The initial state of the sidebar.
            Can be "expanded", "collapsed", or "auto" (default is "expanded").
        layout (Literal["wide", "centered"], optional): The layout of the Streamlit page. Can be either "wide" or
            "centered" (default is "wide").
        page_icon (str, optional): The icon for the page. Can be any valid emoji or image URL
            (default is ":streamlit:").
        authentication_enabled (bool, optional): Flag to enable/disable authentication components in the sidebar.
            If True, shows user details and a log out button (default is True).

    Raises:
        ValueError: If `initial_sidebar_state` or `layout` contains an invalid value.

    Returns:
        None
    """
    # Ensure acceptable value used for initial_sidebar_state
    if initial_sidebar_state not in ['expanded', 'collapsed', 'auto']:
        raise ValueError(f"{initial_sidebar_state} not acceptable value for layout. "
                         "Acceptable values include 'expanded', 'collapsed' or 'auto'")

    # Ensure acceptable value used for layout
    if layout not in ['wide', 'centered']:
        raise ValueError(f"{layout} not acceptable value for layout. Acceptable values include "
                         "'wide' or 'centered'")

    # Set page config
    st.set_page_config(
        initial_sidebar_state=initial_sidebar_state,
        layout=layout,
        page_icon=page_icon,
        menu_items={
            "Report a Bug": f"https://github.com/powellrhys/{repository_name}/issues"
        }
    )

    # Disable page warnings
    warnings.filterwarnings("ignore")

    if authentication_enabled:

        # Render account login component on sidebar
        st.sidebar.markdown(f"👤 **Logged in as:** {st.experimental_user.name}")

        # Render logout button on sidebar
        if st.sidebar.button('Log Out'):
            st.logout()
