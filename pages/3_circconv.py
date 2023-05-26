import streamlit as st
import copy
import matplotlib.pyplot as plt
def circ_conv(x,h):
    x1=copy.copy(x)
    h1=copy.copy(h)
    if len(x)>len(h):
        N=len(x)
        for i in range(len(h),len(x)):
            h1.append(0)
    elif len(x)<len(h):
        N=len(h)
        for i in range(len(x),len(h)):
            x1.append(0)
    else:
        N=len(x)
    y=[0]*N
    for n in range(N):
        for k in range(N):
            y[n]+=x1[k]*h1[mod((n-k),N)]
    return y


from operator import mod
st.markdown('## Circular convolution')
st.markdown('#### Determines N point circular conv b/w x(n) & h(n)')
x=st.text_input('Enter the i/p sequence x(n)')
x1=[int(i) for i in x.split()]
h=st.text_input('Enter the i/p sequence h(n)')
h1=[int(i) for i in h.split()]
if x1 and h1:
    y=circ_conv(x1,h1)
    st.write('circular convolution y=',y)
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
    plt.title('Circular convolution y(n)')
    plt.tight_layout()
    st.pyplot(fig) 
    
