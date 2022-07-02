# from tkinter import YView
import numpy as np
import streamlit as st
import matplotlib.pylab as plt
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

#-------------------------------------------
st.markdown("### st.line_chart")
n = 100
y = np.random.randn(n, 2)
# print(np.reshape(x, (-1,1)))
# print(y.shape)
st.line_chart(y)

code = '''
n = 100
y = np.random.randn(n, 2)
st.line_chart(y)
'''
st.code(code, language='python')
st.write('---')
# ----------------------------------------
st.markdown("### matplotlib + st.pyplot")

x = np.linspace(-3*np.pi, 3*np.pi,200)
y = 0
fig = plt.figure()

for i in range(10):
    y += np.sin((2*i+1) * x) / (2*i+1)
    plt.plot(x, 4 / np.pi * y, color = 'b')
    plt.ylim([-3, 3])

col1, col2, col3= st.columns((1,4,1))
with col2:
    st.pyplot(fig)

with st.expander("See python codes"):
    code = '''
x = np.linspace(-3*np.pi, 3*np.pi,200)
y = 0
fig = plt.figure()
for i in range(10):
    y += np.sin((2*i+1) * x) / (2*i+1)
    plt.plot(x, 4 / np.pi * y, color = 'b')
    plt.ylim([-3, 3])
    
st.pyplot(fig)
'''
    st.code(code, language='python')
st.write('---')
# ----------------------------------------
st.markdown("### plotly graph_objects+ st.plotly_chart")
st.latex(r'f(x) = \frac{4}{\pi}\left(\sin x+\frac{\sin 3x}{3}+\frac{\sin 5x}{5}+\frac{\sin 7x}{7}+\cdots\right)')

x = np.linspace(-3*np.pi, 3*np.pi,200)
xm = np.min(x) - 1.5
xM = np.max(x) + 1.5
ym = -2.5
yM = 2.5
y = 0
N = np.arange(0, 20)
fig4 = go.Figure()

for k in N:
    y += 4/np.pi*(np.sin((2*k+1) * x) / (2*k+1))
    fig4.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=1),
            name="k = " + str(k),
            x=x,
            y=y))

fig4.add_trace(go.Scatter(x=x, y=4/np.pi*np.sin(x),
                    mode='lines',
                    name='sin(x)',
                    line=dict(color='firebrick', width=4)))
# Make 10th trace visible
# fig4.data[10].visible = True

# Create and add slider
steps = [] # for slider's attributes
for i in range(len(fig4.data)-1):
    k =str(N[i]) 
    step = dict(
        method="update",
        # method="animate",
        args=[{"visible": [False] * len(fig4.data)},
              {"title": "Slider switched to k: " + k}],  # layout attribute
        label = str(i) # change the label under the slider
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    step["args"][0]["visible"][-1] = True # the last trace always be visible
    steps.append(step)

# check layout.sliders in plotly for attributes
sliders = [dict(
    active=0,
    currentvalue={"prefix": "Number of terms added: ", "suffix":" terms"},
    # minorticklen = 10,
    # pad={"t": 100},
    steps=steps
)]
fig4.update_xaxes(range=(xm,xM))
fig4.update_yaxes(range=(ym,yM))
fig4.update_layout(
    sliders=sliders,
    # showlegend=False
)

st.plotly_chart(fig4)
st.write('---')
# -----------------------------------------
st.markdown("### plotly express + st.plotly_chart")
st.latex(r'f(x) = \frac{4}{\pi}\left(\sin x+\frac{\sin 3x}{3}+\frac{\sin 5x}{5}+\frac{\sin 7x}{7}+\cdots\right)')
terms = st.number_input('How many terms ?', min_value=1, max_value=100, value=20)
n = 200
x = np.linspace(-3*np.pi, 3*np.pi,n)
y = 0
df = pd.DataFrame()
for i in range(int(terms)):
    y += 4/np.pi*np.sin((2*i+1)*x)/(2*i+1)
    df = pd.concat([df, pd.DataFrame([x, y, i*np.ones(n)]).T])

df.columns= ['x', 'y', 'k']
# st.write(df)
fig = px.line(df, x='x', y = 'y', animation_frame= 'k',
    range_x = [np.min(x) - 1.5, np.max(x) + 1.5], 
    range_y = [-2.5, 2.5])
# st.write(fig)
fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='LightPink')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_layout(title_text="f(x)")
fig.update_layout()
st.plotly_chart(fig)
st.write('---')
# -----------------------------------------
st.markdown("### st.camera_input + st.image")
st.write('暫時關閉')
# picture = st.camera_input("Take a picture")

# if picture:
#      st.image(picture)
st.write('---')
# -----------------------------------------
st.markdown("### st.video")
st.video("https://www.youtube.com/watch?v=WIQJUlE7DNo")
# -----------------------------------------
st.markdown("### st.file_uploader + st.audio")
uploaded_file = st.file_uploader("Choose an audio file")
if uploaded_file:
        # st.write("File name:", uploaded_file.name)
    audio_file = open(uploaded_file.name,'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)    
