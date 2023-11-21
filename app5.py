import streamlit as st
import pandas as ad

# 이미지 / 동영상을 화면에 보여주기

from PIL import Image

def main():
    
    img = Image.open('./data/image_03.jpg')

    print(img)

    st.image(img)

    st.image(img, use_column_width= True)

    img_url = 'https://i.namu.wiki/i/7Qa1HFI80Lly0neWoiclvQA8z2qrQfVdPcwKK5PW4-XmlZSTJQbFJcw0sdxbrHccwzNCzRCuIl0JnqKmHuL4Sg.webp'

    st.image(img_url)

    # 동영상

    video_file = open('./data/video1.mp4', 'rb')

    st.video( video_file )


if __name__ == '__main__' :
    main()