import streamlit as st
import requests
import os

def main():
    st.title("Name Greeting App")
    
    # Get server URL from environment variable or use default
    server_url = os.getenv('SERVER_URL', 'http://localhost:5000')
    
    # Create input field for name
    name = st.text_input("Enter your name:")
    
    # Create send button
    if st.button("Send"):
        if name:
            # Make API call to backend
            response = requests.get(f"{server_url}/api/{name}")
            if response.status_code == 200:
                # Display the response message
                message = response.json()["message"]
                st.success(message)
            else:
                st.error("Error connecting to the server")
        else:
            st.warning("Please enter a name")

if __name__ == "__main__":
    main()
