import numpy as np
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder # pip install streamlit-aggrid


# ------------------------------------------
st.markdown("#### Python list and indexing")

number_list = [0, 1, 1, 2, 3, 5, 8]
st.text('number_list = ' + str(number_list))
st.text('number_list[0:3] ==> ' + str(number_list[0:3]))
st.text('number_list[-3:] ==> ' + str(number_list[-3:]))

list_list = [[1, 2, 3], [4, 5, 6]]
st.text('list_list = ' + str(list_list))
st.text('list_list[0] ==> ' + str(list_list[0]))
st.text('list_list[1][2] ==> ' + str(list_list[1][2]))
# st.text(list_list[0:2])
# ------------------------------------------------
st.write('---')
st.markdown("#### numpy array and indexing")
a = np.array([1, 2, 3])
st.text('a = np.array([1, 2, 3])')
st.text('a.shape ==> ' + str(a.shape))
# st.text('a = np.array([1, 2, 3]) ==> ' + str(np.array([1, 2, 3])))

A = np.array([[1, 2, 3]])
st.text('A = np.array([[1, 2, 3]])')
st.text('A.shape ==>' + str(A.shape))
st.text('A.reshape(-1, 1) ==> ' + str(A.reshape(-1, 1)))

A = np.array([[1, 2, 3],[4, 5, 6]])
st.text('A = np.array([[1, 2, 3],[4, 5, 6]])')
st.text('A ==> ' + str(A))
st.text('A[1] ==> ' + str(A[1]))
st.text('A[1, :] ==> ' + str(A[1, :]))
st.text('A[:, 1] ==> ' + str(A[:, 1]))
st.text('A[:, 0:-1] ==> ' + str(A[:, 0:-1]))
st.text('A[:, 1:] ==> ' + str(A[:, 1:]))
st.text('A[:, -2:] ==> ' + str(A[:, -2:]))
st.write('---')
# ----------------------------------------
st.markdown("#### vector and matrix concatenation")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
st.text('a = np.array([1, 2, 3])')
st.text('b = np.array([4, 5, 6])')
st.text('np.concatenate((a, b)) ==> ' + str(np.concatenate((a, b))))
st.text('np.append(a, b) ==> ' + str(np.append(a, b)))
st.text('np.hstack((a, b)) ==> ' + str(np.hstack((a, b))))
st.text(' np.r_[a, b] == > ' + str( np.r_[a, b]))
st.text('np.vstack((a, b)) ==> ' + str(np.vstack((a, b))))
st.text('np.c_[a, b] ==> ' + str(np.c_[a, b]))
st.text('-----------------')
a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])
st.text('a = np.array([[1, 2, 3]])')
st.text('b = np.array([[4, 5, 6]])')
st.text('np.concatenate((a, b), axis = 1) ==> ' + str(np.concatenate((a, b), axis = 1)))
st.text('np.concatenate((a, b), axis = 0) ==> ' + str(np.concatenate((a, b), axis = 0)))
st.text(' np.r_[a, b] == > ' + str( np.r_[a, b]))
st.text('np.c_[a, b] ==> ' + str(np.c_[a, b]))
st.text('np.concatenate((a.T, b.T), axis =1) ==> ' + str(np.concatenate((a.T, b.T), axis =1)))
st.text('np.hstack((a.T, b.T)) ==> ' + str(np.hstack((a.T, b.T))))
st.text('np.c_[a.T, b.T] ==> ' + str(np.c_[a.T, b.T]))
# st.text([a,b, np.ones(3)])
st.write('---')
st.markdown("#### Pandas dataframe basics")
A = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
st.text('A = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]')
df = pd.DataFrame(A)
st.text('df = pd.DataFrame(A)')
st.write(df)
df.columns = ["col1", "col2", "col3", "col4"]
st.text('df.columns = ["col1", "col2", "col3", "col4"]')
st.write(df)
c1 = [91, 92, 93]
c2 = [71, 72, 73]
c3 = [51, 52, 53]
c4 = [31, 32, 33]
st.text('''
c1 = [91, 92, 93]
c2 = [71, 72, 73]
c3 = [51, 52, 53]
c4 = [31, 32, 33]''')
df = df.assign(col5 = c1)
df.insert(2, 'new', c2)
df['col6'] = c3
st.text('''
df = df.assign(col5 = c1)
df.insert(2, 'new', c2)
df['col6'] = c3''')
st.write("Add a column", df)
r1 = [81, 82, 83, 84, 85, 86, 87]
df.loc[len(df)] = r1
r2 = [61, 62, 63, 64, 65, 66, 67]
df.loc[-0.5] = r2 # move to top
df = df.sort_index().reset_index(drop=True)
df.loc[1.5] = r2 
df = df.sort_index().reset_index(drop=True)
st.text('''
r1 = [81, 82, 83, 84, 85, 86, 87]
df.loc[len(df)] = r1
r2 = [61, 62, 63, 64, 65, 66, 67]
df.loc[-0.5] = r2 # move to top
df = df.sort_index().reset_index(drop=True)
df.loc[1.5] = r2 
df = df.sort_index().reset_index(drop=True)''')
st.write("Add a row", df)
# st.table(df)
# st.dataframe(df)
df.drop(['new', 'col6'], axis=1, inplace=True)
# df.drop(['row3'], axis=0, inplace=True)
df.drop(df.index[2], inplace=True)
df = df.sort_index().reset_index(drop=True)
st.text('''
df.drop(['new', 'col6'], axis=1, inplace=True)
df.drop(df.index[2], inplace=True)
df = df.sort_index().reset_index(drop=True)''')
st.write("Delete columns & rows", df)
df.loc[0:3]
st.write('df.loc[0:3]', df.loc[0:3])
st.write('df[["col2", "col3"]].loc[0:2]', df[["col2", "col3"]].loc[0:2])
st.write('df.iloc[0:3, 0:4]', df.iloc[0:3, 0:4])
st.write('---')

st.subheader("Editable Grids")
c1, c2 = st.columns(2)
with c1:
    grid_return1 = AgGrid(df, key='grid1', editable=True)
    st.text("Grid 1 Return")
    st.write(grid_return1['data'])

with c2:
    grid_return2 = AgGrid(df,  key='grid2', editable=True)
    st.text("Grid 2 Return")
    st.write(grid_return2['data'])