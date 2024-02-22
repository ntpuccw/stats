# Description: This program uses AgGrid for an editable Table in streamit.
# need to  "pip install streamlit-aggrid"
''' 
Objective: This program is to create an app to 
    perform hypothesis testing for independence of 
    two categorical variables.
'''

from matplotlib import container
import numpy as np
import streamlit as st
import pandas as pd
from scipy.stats import chi2_contingency
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder # pip install streamlit-aggrid

st.markdown('''
### 獨立性檢定
###### [下載示範 EXCEL 檔](https://github.com/ntpuccw/stats/blob/master/data/hypothesis_excel.xlsx)
先下載示範檔案並觀察格式，再上傳自己的 EXCEL 檔案進行獨立性檢定。
            ''')

uploaded_file = st.file_uploader("Choose an Excel file（檔案格式必須與示範的 EXCEL 檔相同）")
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    # st.write(df)
    row, col = df.shape
    df.rename(columns = {'Unnamed: 0':'/'}, inplace = True)
    col_names = [df.columns[i+1] for i in range(col-1)]
    row_names = [df['/'][i] for i in range(row)]
    data = df.values[:,1:]
    
# create a two-column layout
c1, c2 = st.columns(2)
with c1:
    col_init = col-1 if 'col' in locals() else 3 # if col is defined, then col_init = col-1, else col_init = 3
    # if 'col' in locals():
    #     col_init = col-1
    # else:
    #     col_init = 3
    col = st.number_input('Columns（輸入解釋變數個數 >=2, <=10）:', min_value=2, max_value=10, value=col_init , step=1)
    if not uploaded_file: # if uploaded_file is not defined
        col_names = ["col{}".format(i+1) for i in range(int(col))]
    # col_names = ["col1", "col2", "col3"]
    # user_def_col = ""
    # for s in col_names:
    #     user_def_col += s +',' 
    user_def_col = ",".join(col_names) # join to col1,col2,clo3
    tmp = st.text_area('輸入解釋變數名稱（以逗點 , 分隔）: ', user_def_col, height=80)
    col_names = str(tmp).split(',')

with c2:
    row_init = row if 'row' in locals() else 2
    row = st.number_input('Rows（輸入反應變數個數 >=2, <=10）:', min_value=2, max_value=10, value=row_init, step=1)
    if not uploaded_file:
        row_names = ["row{}".format(i+1) for i in range(int(row))]
    # row_names = ["row1", "row2"]
    user_def_row = ",".join(row_names)
    tmp = st.text_area('輸入反應變數名稱（以逗點 , 分隔）: ', user_def_row, height=80)
    row_names = str(tmp).split(',')


if not uploaded_file:
    data = np.ones((int(row), int(col)), dtype = float) # create a 2D array with all elements = 1
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
    theme = "streamlit") # ["streamlit", "light", "dark", "blue", "fresh", "material"]
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
st.markdown('#### Test Results:')
c1, c2 = st.columns(2)
with c1:
        st.write(f'''
        Chi2 statistic = {np.round(chi2,2)} \n
        p-value = {np.round(p, 2)} \n
        dof = {dof} 
        ''')
with c2:
        st.write('Expected frequency:', np.round(expected, 2))

if st.button('Save the results to an EXCEL file'):
     st.write(df_res)
     # write the result to an EXCEL file 
    #  df_new = df_res.copy()        
     df_new = df_res.iloc[0:len(row_names), 0:len(col_names)]
     df_new.to_excel('hypothesis_test_new.xlsx', index = False)
     st.write('The results are saved as hypothesis_test_new.xlsx')

st.write('---')
st.markdown('### Example: EXCEL 檔格式')
st.image('hypothesis_example.png')