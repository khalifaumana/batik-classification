mkdir -p ~/.streamlit/

echo "\
[general]
email = \"khalifaumana@gmail.com\"
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
enableCORS=false
port = $PORT
" > ~/.streamlit/config.toml
