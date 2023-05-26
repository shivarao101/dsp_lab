import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.markdown('## Discrete Fourier Transform(DFT)')
st.markdown('#### To determine magnitude and phase response')
x=st.text_input('Enter the i/p sequence x(n)')
x1=[int(i) for i in x.split()]
if x1:
    X=np.fft.fft(x1)
    fig=plt.figure()
    plt.subplot(2,1,1)
    plt.stem(range(len(X)),np.abs(X))
    plt.xlabel('k-->')
    plt.ylabel('|X(k)|-->')
    plt.title('Magnitude response')
    plt.subplot(2,1,2)
    plt.stem(range(len(X)),np.angle(X))
    plt.xlabel('k-->')
    plt.ylabel('<X(k)-->')
    plt.title('Phase response')
    plt.tight_layout()
    st.pyplot(fig) 
   
