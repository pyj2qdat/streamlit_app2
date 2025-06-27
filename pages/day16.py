import streamlit as st
st.title("Customizing the theme of Streamlit apps")
st.write('이 앱의 `.strealit/config.toml`파일 내용')
st.code('''
        [theme]
        primaryColor='#A5AEFF'
        backgroundColor='#fff0d9'
        secondaryBackgroundColor="#FFDDEF"
        textColor="#FFFFFF"
        font="monospace"
""")
        
number = st.sidebar.slider('숫자를 선택하세요:',0,10,5)
st.write('슬라이더 위젯에서 선택된 숫자:',number)
        

        