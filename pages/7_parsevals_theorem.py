import numpy as np
import streamlit as st
st.markdown('## Parsevals theorem')
st.markdown('#### To verify Parsevals theorem')
st.latex(r'''\sum_{n=0}^{N-1}|x(n)|^2 = (1/N)\sum_{k=0}^{N-1}|X(k)|^2
 ''')
ip=st.text_input('Enter the i/p sequence x(n)')
ip1=[int(i) for i in ip.split()]
if ip1:
    en=sum(np.abs(ip1)**2)
    st.write('Energy in time domain',en)
    en1=(1/len(ip1))*sum(np.abs(np.fft.fft(ip1))**2)
    st.write('Energy in freq domain',en1)
