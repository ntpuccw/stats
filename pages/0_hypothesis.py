# This program uses AgGrid for an editable Table in streamit.
# need to  "pip install streamlit-aggrid"


import numpy as np
import streamlit as st
import pandas as pd
from scipy.stats import chi2_contingency
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder # pip install streamlit-aggrid

st.markdown('### 獨立性檢定')
c1, c2 = st.columns(2)
with c1:
    col = st.number_input('Columns（輸入獨立變數個數）:', min_value=2, max_value=10, value=3, step=1)
    col_names = ["col{}".format(i+1) for i in range(int(col))]
    # col_names = ["col1", "col2", "col3"]
    # user_def_col = ""
    # for s in col_names:
    #     user_def_col += s +',' 
    user_def_col = ",".join(col_names) # join to col1,col2,clo3
    tmp = st.text_area('輸入獨立變數名稱（以逗點 , 分隔）: ', user_def_col, height=80)
    col_names = str(tmp).split(',')

with c2:
    row = st.number_input('Rows（輸入因變數個數）:', min_value=2, max_value=10, value=2, step=1)
    row_names = ["row{}".format(i+1) for i in range(int(row))]
    # row_names = ["row1", "row2"]
    user_def_row = ",".join(row_names)
    tmp = st.text_area('輸入因變數名稱（以逗點 , 分隔）: ', user_def_row, height=80)
    row_names = str(tmp).split(',')


data = np.ones((int(row), int(col)), dtype = float)
df = pd.DataFrame(data, columns = col_names)
df.insert(0, '/', row_names)
# st.write(df)
colDefs = [{
            "headerName": "",
            "field": "/",
            "editable": False,
        }]
for i in range(int(col)):
    colDefs.append({
            "headerName": col_names[i], #"col"+str(i+1),
            "field": col_names[i], #"col"+str(i+1),
            "editable": True,
            "resizable": True,
        })
grid_options = {"columnDefs": colDefs
    # "columnDefs": [
    #     {
    #         "headerName": "",
    #         "field": "row",
    #         "editable": False,
    #     },
        
    #     {
    #         "headerName": "col1",
    #         "field": "col1",
    #         "editable": True,
    #     },
    #     {
    #         "headerName": "col2",
    #         "field": "col2",
    #         "editable": True,
    #     },
    #     {
    #         "headerName": "col3",
    #         "field": "col3",
    #         "editable": True,
    #     },
    # ],
}
st.text('直接在表格內輸入數據')
grid_return1 = AgGrid(df, grid_options, height = 200, 
    theme = "blue") # ["streamlit", "light", "dark", "blue", "fresh", "material"]
df_res = pd.DataFrame(grid_return1['data'])

D = df_res.values[:,1:]
total_col = np.append(np.sum(D, axis = 0), np.sum(D))
total_row = np.sum(D, axis = 1)
df_res['Total']= total_row
df_res.loc[len(df_res)]= df_res.values[0,:]
df_res.iloc[len(df_res)-1, 1:] = total_col # data start from the second column 
df_res.iloc[len(df_res)-1, 0] = 'Total'
df_res.rename(columns = {'/':''}, inplace = True)
chi2, p, dof, expected = chi2_contingency(D)
# st.text(df_res.columns)
# df_res.columns = col_names
# df_res.columns = '***'
# st.text(df_res.columns)
# df_res.loc['Total']= total_col

# df_res = df_res.assign(Sum = df_res.iloc[0:len(row_names)+1, 1:len(col_names)+1].sum(axis=1))
# df_res.loc[len(df_res)] = df_res.iloc[0:len(row_names)+1, 1:len(col_names)+2].sum(axis=0)#['sum',3,3,3,3]
# df_res.iloc[len(df_res)-1,0]='Sum'
st.write(df_res)
st.write(f'''
Chi2 statistic = {np.round(chi2,2)} \n
p-value = {np.round(p, 2)} \n
dof = {dof} 
''')
st.write('Expected frequency:', np.round(expected, 2))
st.write('---')
st.markdown('### Example:')
st.image('hypothesis_example.png')