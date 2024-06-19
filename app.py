import streamlit as st
from PIL import Image

st.sidebar.title('Side Bar')
st.sidebar.header('텍스트 입력 사용 예')
user_id = st.sidebar.text_input('아이디(ID)입력', value='streamlit', max_chars=15)
user_password = st.sidebar.text_input('패스워드(Password)입력', value='abcd', type='password')

st.sidebar.header('셀렉트박스 사용 예')
selectbox_options = ['진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하장인']
your_option = st.sidebar.selectbox('좋아하는 작품은?', selectbox_options, index=3)
st.sidebar.write('**당신의 선택** :', your_option)
folder = './data/'
image_files = [
    'https://github.com/wbwhdrhadl/streamlit/blob/main/data/Vermeer.png?raw=true', 
    'https://github.com/wbwhdrhadl/streamlit/blob/main/data/Gogh.png?raw=true',
    'https://github.com/wbwhdrhadl/streamlit/blob/main/data/Munch.png?raw=true', 
    'https://github.com/wbwhdrhadl/streamlit/blob/main/data/ShinYoonbok.png?raw=true'
    ]

selectbox_options_index = selectbox_options.index(your_option)
image_file = image_files[selectbox_options_index]
image_local = Image.open(folder + image_file)
st.image(image_file, caption=your_option)