import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid

st.set_page_config(page_title="DataFrame Demo", page_icon="")

st.markdown("# DataFrame Practice")
st.write(
    """Data courtesy of the [The Boston Housing Dataset](https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html)"""
)

df = pd.read_csv("Boston.csv")
row, col = df.shape
st.text(f"共 {col} 個變數 {row} 筆資料")
col_names = [df.columns[i] for i in range(col)]

# st.write(df)
colDefs = []
for i in range(int(col)):
    colDefs.append({
            "headerName": col_names[i], 
            "field": col_names[i], #"col"+str(i+1),
            "editable": False,
            "resizable": True,
            "sortable": True,
            "filter": True,
            "width":20,
        })
grid_options = {"columnDefs": colDefs}
grid_return1 = AgGrid(df, grid_options, height = 400, 
    theme = "blue") # ["streamlit", "light", "dark", "blue", "fresh", "material"]

# st.bar_chart(df[col_names[:]])
fig_pie = px.pie(df, names = 'hcol', title='類別型變數 hcol', hole = 0.3)
# st.write(pie_fig)
st.plotly_chart(fig_pie)

hist_var = st.selectbox('Which variable to select', col_names, 0)
fig_hist = px.histogram(df, x = hist_var, nbins = 50, opacity= 0.6,
    orientation ='v')
st.plotly_chart(fig_hist)

scatter_x = st.selectbox('Scatter plot: x', col_names, 0)
scatter_y = st.selectbox('Scatter plot: x', col_names, col-2)
fig_scatter = px.scatter(df, x = scatter_x, y = scatter_y, color = 'hcol')
st.plotly_chart(fig_scatter)

fig_scatter_all = px.scatter_matrix(df, width = 1200, height = 1200,
    color = 'hcol')
st.plotly_chart(fig_scatter_all)

boxplot_vars = st.multiselect('Select variables for boxplot(s):', col_names, ['medv'])
fig_box = px.box(df, y=boxplot_vars, points="all", notched=True)
fig_box.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default     
st.plotly_chart(fig_box)

fig_box2 = px.box(df, y=boxplot_vars, color = 'hcol')
fig_box2.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default     
st.plotly_chart(fig_box2)

fig_box3 = px.box(df, y=boxplot_vars, color = 'rad')
fig_box3.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default     
st.plotly_chart(fig_box3)

