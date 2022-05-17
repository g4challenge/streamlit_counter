mkdir -p ~/.streamlit/

echo "\n
[server] \n
headless = true\n
enableCORS=false\n
port = $PORT\n
[theme] \n
primaryColor='##0b8f6a' \n
backgroundColor='#FFFFFF' \n
secondaryBackgroundColor='#F0F2F6' \n
textColor='#0b8f6a' \n
font='sans serif' \n
" > ~/.streamlit/config.toml

echo  "\n
[server] 
headless = true
enableCORS=false
port = $PORT
[theme]
primaryColor='#F63366'
primaryColor='#F63366'
backgroundColor='#FFFFFF'
secondaryBackgroundColor='#F0F2F6'
textColor='#262730'
font='sans serif'
"