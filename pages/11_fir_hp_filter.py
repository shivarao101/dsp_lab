import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from cmath import exp
st.markdown('## High pass FIR filter design using Hamming window')
st.markdown('#### Design High Pass FIR filter')
N=st.text_input('Enter the order')
wc=st.text_input('Enter the cut off freq ')
if N and wc:
    N=int(N)
    wc=float(wc)
    hd=np.zeros((N))
    wh=np.zeros((N))
    h=np.zeros((N))
    alp=(N-1)/2
    for n in range(N):
        if n==alp:
            hd[n]=(np.pi-wc)/np.pi
            wh[n]=1
        else:
            hd[n]=-(np.sin(wc*(n-alp)))/(np.pi*(n-alp))
            wh[n]=0.54- 0.46*np.cos((2*np.pi*n)/(N-1))
    h=hd*wh
    w1=[i for i in np.arange(0,np.pi,0.01)]
    H=np.zeros(len(w1),'complex')
    w2=0
    for w in range(len(w1)):
        for n in range(N):
            H[w]+=h[n]*exp(-1j*w2*n)
        w2+=0.01
    fig=plt.figure()
    plt.subplot(2,1,1)
    plt.stem(range(N),h)
    plt.xlabel('time n-->')
    plt.ylabel('Amplitude h(n)-->')
    plt.title('Impulse response of FIR HP filter using Hamming window')
    plt.subplot(2,1,2)
    plt.plot(w1,np.abs(H))
    plt.xlabel('frequency w-->')
    plt.ylabel('Amplitude |H(w)|-->')
    plt.title('Frequency response of FIR HP filter using Hamming window')
    plt.tight_layout()
    st.pyplot(fig)


