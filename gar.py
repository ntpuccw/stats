# import numpy as np
# import plotly.express as px
# import pandas as pd

# terms = 20
# n = 200
# x = np.linspace(-3*np.pi, 3*np.pi,n)
# y = 0
# df = pd.DataFrame()
# for i in range(int(terms)):
#     y += 4/np.pi*np.sin((2*i+1)*x)/(2*i+1)
#     df = pd.concat([df, pd.DataFrame([x, y, i*np.ones(n)]).T])

# df.columns= ['x', 'y', 'k']
# # st.write(df)
# fig = px.line(df, x='x', y = 'y', animation_frame= 'k',
#     range_x = [np.min(x) - 1.5, np.max(x) + 1.5], 
#     range_y = [-2.5, 2.5])
# # st.write(fig)
# fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='LightPink')
# fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
# fig.update_layout(title_text="f(x)")
# fig.update_layout()

# fig.show()
# 
a=[1,2,3,4,5,6]

print(a>3)