import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import copy
st.markdown('## Linear Convolution using DFT and IDFT')
st.markdown('#### Determines the Linear convolution b/w x(n) & h(n) using DFT and IDFT')
x=st.text_input('Enter the i/p sequence x(n)')
x1=[int(i) for i in x.split()]
h=st.text_input('Enter the i/p sequence h(n)')
h1=[int(i) for i in h.split()]
if x1 and h1:
    N=len(h1)+len(x1)-1
    x2=copy.copy(x1)
    h2=copy.copy(h1)
    x2=x2+[0]*(N-len(x2))
    h2=h2+[0]*(N-len(h2))
    X2=np.fft.fft(x2)
    H2=np.fft.fft(h2)
    Y=np.array(X2)*np.array(H2)
    y=np.fft.ifft(Y)
    y=np.real(y)
    st.write('FFT of x=',X2)
    st.write('FFT of h=',H2)
    st.write('Linear convolution using DFT and IDFT y=',y)
    fig=plt.figure()
    plt.subplot(3,1,1)
    plt.stem(range(len(x1)),x1)
    plt.xlabel('n-->')
    plt.ylabel('x(n)-->')
    plt.title('x(n)')
    plt.subplot(3,1,2)
    plt.stem(range(len(h1)),h1)
    plt.xlabel('n-->')
    plt.ylabel('h(n)-->')
    plt.title('h(n)')
    plt.subplot(3,1,3)
    plt.stem(range(len(y)),y)
    plt.xlabel('n-->')
    plt.ylabel('y(n)-->')
    plt.title('Linear convolution y(n) using DFT and IDFT')
    plt.tight_layout()
    st.pyplot(fig) 