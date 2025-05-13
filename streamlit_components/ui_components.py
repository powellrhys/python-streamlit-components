# Import python dependencies
from typing import Literal
import streamlit as st
import warnings

# Import project dependencies
from streamlit_components.data_functions import (
    list_blob_files
)

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


def data_source_badge(
    blob_connection_string: str,
    file_name: str,
    additional_comments: str = ''
) -> None:
    """
    Function to render data source metadata badge.

    Args:
        blob_connection_string (str): azure blob storage connection string
        file_name (str): blob storage file name
        additional_comments (str = ''): Additional notes to render on badge

    Raise:
        TypeError: If blob_connection_string or file_name not a string

    Return: None
    """
    # Ensure input variables are strings
    for arg_name, arg_value in locals().items():
        if not isinstance(arg_value, str):
            raise TypeError(f"{arg_name} must be a string, but got {type(arg_value).__name__}")

    # Collect list of blob files
    _, blob_files = list_blob_files(connection_string=blob_connection_string,
                                    container_name='play-cricket')

    # Filter blob files list to retrieve file of interest and when file was last modified
    last_modified = [file for file in blob_files if file['name'] == file_name][0]['last_modified']

    # Configure additional notes string
    if additional_comments:
        additional_note = f' **| Note:** {additional_comments}'
    else:
        additional_note = ''

    # Define Badge message
    badge_message = f'**Data Source:** {file_name} **| Data Updated:** ' + \
        f'{last_modified.strftime("%d/%m/%Y %H:%M:%S")} {additional_note}'

    # Render badge on streamlit page
    st.badge(label=badge_message,
             color='primary')
