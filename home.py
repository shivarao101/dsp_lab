from pathlib import Path
import streamlit as st
from PIL import Image
hide_menu='''
<style>
#Mainmenu
footer{
   visibility:hidden;
}
footer:after{
content:'Designed by Prof. Shivapasad VCET, Puttur';
display:block;
}
</style>
'''
st.set_page_config(page_title='DSP Lab',page_icon='📻')
current_dir= Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
college_pic = current_dir / "assets" / "college.png"
NAME = "Vivekananda College of Engineering and Technology, Puttur"
DESCRIPTION = "Department of Electronics and Communication Engineering"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
college_pic=Image.open(college_pic)
col1, col2 = st.columns((0.3,0.7),gap="large")
with col1:
    st.image(college_pic, width=150)
with col2:
    st.markdown(f"### {NAME}")
    st.write(f"##### {DESCRIPTION}")
st.markdown(hide_menu,unsafe_allow_html=True)

st.markdown('## DSP lab experiments')
st.sidebar.success('Select pages above')
st.write('1. Computation of N point DFT of a given sequence and to plot magnitude and phase spectrum.')
st.write('''2. Computation of circular convolution of two given sequences and verification of commutative,
distributive and associative property of convolution.''')
st.write('3. Computation of linear convolution of two sequences using DFT and IDFT.')
st.write('4. Computation of circular convolution of two given sequences using DFT and IDFT')
st.write('''5. Verification of Linearity property, circular time shift property & circular frequency shift property
of DFT.''')
st.write('6. Verification of Parseval’s theorem')
st.write('7. Design and implementation of IIR (Butterworth) low pass filter to meet given specifications.')
st.write('8. Design and implementation of IIR (Butterworth) high pass filter to meet given specifications.')
st.write('9. Design and implementation of low pass FIR filter to meet given specifications.')
st.write('10. Design and implementation of high pass FIR filter to meet given specifications.')
st.markdown(hide_menu,unsafe_allow_html=True)