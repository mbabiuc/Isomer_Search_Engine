import pandas as pd
import streamlit as st
import plotly_express as px
import numpy as np
import mpld3
import base64

# This is the general page setup info
st.set_page_config(page_title='Isomer Search Engine',
                   page_icon=':☢:',
                   layout='wide')

# This df function looks at where the Excel file and exact sheet that I want to use, then I specify the bounds of the dataset
# @st.cache_data                      # ---Unsure if it is needed---
# def get_data_from_excel():               #---Unsure if it is needed---
df = pd.read_excel(
    io="C:\\Users\\bigca\\Desktop\\SURE_research\\AAA Data Folder\\!Isomer Datasheet.xlsx",
    engine='openpyxl',
    sheet_name='Graph Data',
    skiprows=1,
    usecols='A:G',
    nrows=2860,
)
df0 = pd.read_excel(
    io="C:\\Users\\bigca\\Desktop\\SURE_research\\AAA Data Folder\\!Isomer Datasheet.xlsx",
    engine='openpyxl',
    sheet_name='Times',
    skiprows=1,
    usecols='A:E',
    nrows=1109,
)
df1 = pd.read_excel(
    io="C:\\Users\\bigca\\Desktop\\SURE_research\\AAA Data Folder\\!Isomer Datasheet.xlsx",
    engine='openpyxl',
    sheet_name='Times',
    skiprows=1,
    usecols='G:K',
    nrows=1373,
)
df2 = pd.read_excel(
    io="C:\\Users\\bigca\\Desktop\\SURE_research\\AAA Data Folder\\!Isomer Datasheet.xlsx",
    engine='openpyxl',
    sheet_name='Times',
    skiprows=1,
    usecols='M:Q',
    nrows=194,
)
df3 = pd.read_excel(
    io="C:\\Users\\bigca\\Desktop\\SURE_research\\AAA Data Folder\\!Isomer Datasheet.xlsx",
    engine='openpyxl',
    sheet_name='Times',
    skiprows=1,
    usecols='S:W',
    nrows=106,
)
df4 = pd.read_excel(
    io="C:\\Users\\bigca\\Desktop\\SURE_research\\AAA Data Folder\\!Isomer Datasheet.xlsx",
    engine='openpyxl',
    sheet_name='Times',
    skiprows=1,
    usecols='Y:AC',
    nrows=38,
)
df5 = pd.read_excel(
    io="C:\\Users\\bigca\\Desktop\\SURE_research\\AAA Data Folder\\!Isomer Datasheet.xlsx",
    engine='openpyxl',
    sheet_name='Times',
    skiprows=1,
    usecols='AE:AI',
    nrows=13,
)
df6 = pd.read_excel(
    io="C:\\Users\\bigca\\Desktop\\SURE_research\\AAA Data Folder\\!Isomer Datasheet.xlsx",
    engine='openpyxl',
    sheet_name='Times',
    skiprows=1,
    usecols='AK:AO',
    nrows=18,
)
df7 = pd.read_excel(
    io="C:\\Users\\bigca\\Desktop\\SURE_research\\AAA Data Folder\\!Isomer Datasheet.xlsx",
    engine='openpyxl',
    sheet_name='Times',
    skiprows=1,
    usecols='AQ:AU',
    nrows=6,
)
dfs = pd.read_excel(
    io="C:\\Users\\bigca\\Desktop\\SURE_research\\AAA Data Folder\\!Isomer Datasheet.xlsx",
    engine='openpyxl',
    sheet_name='Solar Abundance',
    skiprows=1,
    usecols='A:E',
    nrows=226,
)


def download_dataframe(dataframe):
    csv = dataframe.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    return b64
#        return df                   # ---Unsure if it is needed---
# df = get_data_from_excel()            #---Unsure if it is needed---


# This strips the extra whitespace from the Excel column headers to make it work cleaner
# df.columns = df.columns.str.strip()      #  ---Unsure if it is needed---

st.sidebar.header("Filter Your Dataset:")

plot_options = {
    "Nanoseconds": True,
    "Microseconds": True,
    "Milliseconds": True,
    "Seconds": True,
    "Minuets": True,
    "Hours": True,
    "Days": True,
    "Years": True
}
for plot_name, _ in plot_options.items():
    plot_options[plot_name] = st.sidebar.checkbox(plot_name, value=True)
#_______________________________Nanoseconds selection filters df0---------------------------
st.sidebar.subheader("Nanoseconds")
column_names0 = ['AMU', 'Half_Life', 'Gamma_(keV)']  # List of column names to filter
# This is the setup for how the slider works using the streamlit library
slider_range0 = {}
for column_name in column_names0:
    min_val = df0[column_name].min()
    max_val = df0[column_name].max()
    slider_range0[column_name] = (min_val, max_val)
# Each of these specify the range of which the slider will be selecting
options1 = np.sort(df0["AMU"].unique())
amu = st.sidebar.slider(
    'Select the Atomic Mass',
    min_value=float(options1[0]),
    max_value=float(options1[-1]),
    value=(float(options1[0]), float(options1[-1])),
    step=0.001
)
options2 = np.sort(df0["Half_Life"].unique())
hl = st.sidebar.slider(
    'Select the Half-Life',
    min_value=float(options2[0]),
    max_value=float(options2[-1]),
    value=(float(options2[0]), float(options2[-1])),
    step=0.001
)
options3 = np.sort(df0["Gamma_(keV)"].unique())
gre = st.sidebar.slider(
    'Select the Gamma Energy',
    min_value=float(options3[0]),
    max_value=float(options3[-1]),
    value=(float(options3[0]), float(options3[-1])),
    step=0.001
)

# This make the sliders interactable by choosing the df_selection as our new dataframe instead of the regular Excel file
df_selection0 = df0[
    (df0['AMU'].between(amu[0], amu[1], inclusive='both')) &
    (df0['Half_Life'].between(hl[0], hl[1], inclusive='both')) &
    (df0['Gamma_(keV)'].between(gre[0], gre[1], inclusive='both'))
    ]

#------------------------------Microseconds selection filters df1---------------------------
st.sidebar.subheader("Microseconds")
column_names1 = ['AMU.1', 'Half_Life.1', 'Gamma_(keV).1']  # List of column names to filter
# This is the setup for how the slider works using the streamlit library
slider_range1 = {}
for column_name in column_names1:
    min_val = df1[column_name].min()
    max_val = df1[column_name].max()
    slider_range1[column_name] = (min_val, max_val)
# Each of these specify the range of which the slider will be selecting
options1 = np.sort(df1["AMU.1"].unique())
amu = st.sidebar.slider(
    'Select the Atomic Mass',
    min_value=float(options1[0]),
    max_value=float(options1[-1]),
    value=(float(options1[0]), float(options1[-1])),
    step=0.001
)
options2 = np.sort(df1["Half_Life.1"].unique())
hl = st.sidebar.slider(
    'Select the Half-Life',
    min_value=float(options2[0]),
    max_value=float(options2[-1]),
    value=(float(options2[0]), float(options2[-1])),
    step=0.001
)
options3 = np.sort(df1["Gamma_(keV).1"].unique())
gre = st.sidebar.slider(
    'Select the Gamma Energy',
    min_value=float(options3[0]),
    max_value=float(options3[-1]),
    value=(float(options3[0]), float(options3[-1])),
    step=0.001
)
# This make the sliders interactable by choosing the df_selection as our new dataframe instead of the regular Excel file
df_selection1 = df1[
    (df1['AMU.1'].between(amu[0], amu[1], inclusive='both')) &
    (df1['Half_Life.1'].between(hl[0], hl[1], inclusive='both')) &
    (df1['Gamma_(keV).1'].between(gre[0], gre[1], inclusive='both'))
    ]

# -----------------------------Milliseconds selection filters df2---------------------------
st.sidebar.subheader("Milliseconds")
column_names2 = ['AMU.2', 'Half_Life.2', 'Gamma_(keV).2']  # List of column names to filter
# This is the setup for how the slider works using the streamlit library
slider_range2 = {}
for column_name in column_names2:
    min_val = df2[column_name].min()
    max_val = df2[column_name].max()
    slider_range2[column_name] = (min_val, max_val)
# Each of these specify the range of which the slider will be selecting
options1 = np.sort(df2["AMU.2"].unique())
amu = st.sidebar.slider(
    'Select the Atomic Mass',
    min_value=float(options1[0]),
    max_value=float(options1[-1]),
    value=(float(options1[0]), float(options1[-1])),
    step=0.001
)
options2 = np.sort(df2["Half_Life.2"].unique())
hl = st.sidebar.slider(
    'Select the Half-Life',
    min_value=float(options2[0]),
    max_value=float(options2[-1]),
    value=(float(options2[0]), float(options2[-1])),
    step=0.001
)
options3 = np.sort(df2["Gamma_(keV).2"].unique())
gre = st.sidebar.slider(
    'Select the Gamma Energy',
    min_value=float(options3[0]),
    max_value=float(options3[-1]),
    value=(float(options3[0]), float(options3[-1])),
    step=0.001
)
# This make the sliders interactable by choosing the df_selection as our new dataframe instead of the regular Excel file
df_selection2 = df2[
    (df2['AMU.2'].between(amu[0], amu[1], inclusive='both')) &
    (df2['Half_Life.2'].between(hl[0], hl[1], inclusive='both')) &
    (df2['Gamma_(keV).2'].between(gre[0], gre[1], inclusive='both'))
    ]

# -----------------------------Seconds selection filters df3___________________________
st.sidebar.subheader("Seconds")
column_names3 = ['AMU.3', 'Half_Life.3', 'Gamma_(keV).3']  # List of column names to filter
# This is the setup for how the slider works using the streamlit library
slider_range3 = {}
for column_name in column_names3:
    min_val = df3[column_name].min()
    max_val = df3[column_name].max()
    slider_range3[column_name] = (min_val, max_val)
# Each of these specify the range of which the slider will be selecting
options1 = np.sort(df3["AMU.3"].unique())
amu = st.sidebar.slider(
    'Select the Atomic Mass',
    min_value=float(options1[0]),
    max_value=float(options1[-1]),
    value=(float(options1[0]), float(options1[-1])),
    step=0.001
)
options2 = np.sort(df3["Half_Life.3"].unique())
hl = st.sidebar.slider(
    'Select the Half-Life',
    min_value=float(options2[0]),
    max_value=float(options2[-1]),
    value=(float(options2[0]), float(options2[-1])),
    step=0.001
)
options3 = np.sort(df3["Gamma_(keV).3"].unique())
gre = st.sidebar.slider(
    'Select the Gamma Energy',
    min_value=float(options3[0]),
    max_value=float(options3[-1]),
    value=(float(options3[0]), float(options3[-1])),
    step=0.001
)
# This make the sliders interactable by choosing the df_selection as our new dataframe instead of the regular Excel file
df_selection3 = df3[
    (df3['AMU.3'].between(amu[0], amu[1], inclusive='both')) &
    (df3['Half_Life.3'].between(hl[0], hl[1], inclusive='both')) &
    (df3['Gamma_(keV).3'].between(gre[0], gre[1], inclusive='both'))
    ]

# -----------------------------Minuets selection filters df4___________________________
st.sidebar.subheader("Minuets")
column_names4 = ['AMU.4', 'Half_Life.4', 'Gamma_(keV).4']  # List of column names to filter
# This is the setup for how the lsider works using the streamlit library
slider_range4 = {}
for column_name in column_names4:
    min_val = df4[column_name].min()
    max_val = df4[column_name].max()
    slider_range4[column_name] = (min_val, max_val)
# Each of these specify the range of which the slider will be selecting
options1 = np.sort(df4["AMU.4"].unique())
amu = st.sidebar.slider(
    'Select the Atomic Mass',
    min_value=float(options1[0]),
    max_value=float(options1[-1]),
    value=(float(options1[0]), float(options1[-1])),
    step=0.001
)
options2 = np.sort(df4["Half_Life.4"].unique())
hl = st.sidebar.slider(
    'Select the Half-Life',
    min_value=float(options2[0]),
    max_value=float(options2[-1]),
    value=(float(options2[0]), float(options2[-1])),
    step=0.001
)
options3 = np.sort(df4["Gamma_(keV).4"].unique())
gre = st.sidebar.slider(
    'Select the Gamma Energy',
    min_value=float(options3[0]),
    max_value=float(options3[-1]),
    value=(float(options3[0]), float(options3[-1])),
    step=0.001
)
# This make the sliders interactable by choosing the df_selection as our new dataframe instead of the regualer Excel file
df_selection4 = df4[
    (df4['AMU.4'].between(amu[0], amu[1], inclusive='both')) &
    (df4['Half_Life.4'].between(hl[0], hl[1], inclusive='both')) &
    (df4['Gamma_(keV).4'].between(gre[0], gre[1], inclusive='both'))
    ]

# -----------------------------Hours selection filters df5___________________________
st.sidebar.subheader("Hours")
column_names5 = ['AMU.5', 'Half_Life.5', 'Gamma_(keV).5']  # List of column names to filter
# This is the setup for how the lsider works using the streamlit library
slider_range5 = {}
for column_name in column_names5:
    min_val = df5[column_name].min()
    max_val = df5[column_name].max()
    slider_range5[column_name] = (min_val, max_val)
# Each of these specify the range of which the slider will be selecting
options1 = np.sort(df5["AMU.5"].unique())
amu = st.sidebar.slider(
    'Select the Atomic Mass',
    min_value=float(options1[0]),
    max_value=float(options1[-1]),
    value=(float(options1[0]), float(options1[-1])),
    step=0.001
)
options2 = np.sort(df5["Half_Life.5"].unique())
hl = st.sidebar.slider(
    'Select the Half-Life',
    min_value=float(options2[0]),
    max_value=float(options2[-1]),
    value=(float(options2[0]), float(options2[-1])),
    step=0.001
)
options3 = np.sort(df5["Gamma_(keV).5"].unique())
gre = st.sidebar.slider(
    'Select the Gamma Energy',
    min_value=float(options3[0]),
    max_value=float(options3[-1]),
    value=(float(options3[0]), float(options3[-1])),
    step=0.001
)
# This make the sliders interactable by choosing the df_selection as our new dataframe instead of the regualer Excel file
df_selection5 = df5[
    (df5['AMU.5'].between(amu[0], amu[1], inclusive='both')) &
    (df5['Half_Life.5'].between(hl[0], hl[1], inclusive='both')) &
    (df5['Gamma_(keV).5'].between(gre[0], gre[1], inclusive='both'))
    ]

# -----------------------------Days selection filters df6___________________________
st.sidebar.subheader("Days")
column_names6 = ['AMU.6', 'Half_Life.6', 'Gamma_(keV).6']  # List of column names to filter
# This is the setup for how the slider works using the streamlit library
slider_range6 = {}
for column_name in column_names6:
    min_val = df6[column_name].min()
    max_val = df6[column_name].max()
    slider_range6[column_name] = (min_val, max_val)
# Each of these specify the range of which the slider will be selecting
options1 = np.sort(df6["AMU.6"].unique())
amu = st.sidebar.slider(
    'Select the Atomic Mass',
    min_value=float(options1[0]),
    max_value=float(options1[-1]),
    value=(float(options1[0]), float(options1[-1])),
    step=0.001
)
options2 = np.sort(df6["Half_Life.6"].unique())
hl = st.sidebar.slider(
    'Select the Half-Life',
    min_value=float(options2[0]),
    max_value=float(options2[-1]),
    value=(float(options2[0]), float(options2[-1])),
    step=0.001
)
options3 = np.sort(df6["Gamma_(keV).6"].unique())
gre = st.sidebar.slider(
    'Select the Gamma Energy',
    min_value=float(options3[0]),
    max_value=float(options3[-1]),
    value=(float(options3[0]), float(options3[-1])),
    step=0.001
)
# This make the sliders interactable by choosing the df_selection as our new dataframe instead of the regualer Excel file
df_selection6 = df6[
    (df6['AMU.6'].between(amu[0], amu[1], inclusive='both')) &
    (df6['Half_Life.6'].between(hl[0], hl[1], inclusive='both')) &
    (df6['Gamma_(keV).6'].between(gre[0], gre[1], inclusive='both'))
    ]

# -----------------------------Years selection filters df7___________________________
st.sidebar.subheader("Years")
column_names7 = ['AMU.7', 'Half_Life.7', 'Gamma_(keV).7']  # List of column names to filter
# This is the setup for how the slider works using the streamlit library
slider_range7 = {}
for column_name in column_names7:
    min_val = df7[column_name].min()
    max_val = df7[column_name].max()
    slider_range7[column_name] = (min_val, max_val)
# Each of these specify the range of which the slider will be selecting
options1 = np.sort(df7["AMU.7"].unique())
amu = st.sidebar.slider(
    'Select the Atomic Mass',
    min_value=float(options1[0]),
    max_value=float(options1[-1]),
    value=(float(options1[0]), float(options1[-1])),
    step=0.001
)
options2 = np.sort(df7["Half_Life.7"].unique())
hl = st.sidebar.slider(
    'Select the Half-Life',
    min_value=float(options2[0]),
    max_value=float(options2[-1]),
    value=(float(options2[0]), float(options2[-1])),
    step=0.001
)
options3 = np.sort(df7["Gamma_(keV).7"].unique())
gre = st.sidebar.slider(
    'Select the Gamma Energy',
    min_value=float(options3[0]),
    max_value=float(options3[-1]),
    value=(float(options3[0]), float(options3[-1])),
    step=0.001
)
# This make the sliders interactable by choosing the df_selection as our new dataframe instead of the regualer Excel file
df_selection7 = df7[
    (df7['AMU.7'].between(amu[0], amu[1], inclusive='both')) &
    (df7['Half_Life.7'].between(hl[0], hl[1], inclusive='both')) &
    (df7['Gamma_(keV).7'].between(gre[0], gre[1], inclusive='both'))
    ]

# This is the formatting for the actual page itself. It still needs some work and I can use html to design it.
st.title("Isomer Search Engine")
st.subheader("An interactive website to search, filter, and find data on Isomeric Transition Nuclear Isomers")
st.markdown("#")


# ---Main Matplotlib Chart---
st.markdown("---")
intensities0 = np.ones(len(df_selection0))
intensities1 = np.ones(len(df_selection1))
intensities2 = np.ones(len(df_selection2))  # done
intensities3 = np.ones(len(df_selection3))  # done
intensities4 = np.ones(len(df_selection4))  # done
intensities5 = np.ones(len(df_selection5))  # done
intensities6 = np.ones(len(df_selection6))  # done
intensities7 = np.ones(len(df_selection7))  # done

numpoints = len(df_selection7)
x0_val = df_selection7["Gamma_(keV).7"].values
x1_val = df_selection7["Gamma_(keV).7"].values
y0_val = np.zeros(numpoints)
y1_val = np.ones(numpoints)
shape = [
    dict(type='line',
         x0=0,
         y0=0,
         x1=0,
         y1=0,
         line=dict(color='green',
                   width=1))
    for x0, y0, x1, y1 in zip(x0_val, y0_val, x1_val, y1_val)
]
shapes = shape

fig = px.scatter()
if plot_options["Nanoseconds"]:
    fig.add_scatter(
        x=df_selection0['Gamma_(keV)'],
        y=intensities0,
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection0['AMU'].astype(str) + '<br>' +
                'Element: ' + df_selection0['Element'].astype(str) + '<br>' +
                'Spin: ' + df_selection0['Spin'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection0['Half_Life'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection0['Gamma_(keV)'].astype(str)),
        mode='markers',
        name='Nanoseconds'
    )
    numpoints0 = len(df_selection0)
    x0_val = df_selection0["Gamma_(keV)"].values
    x1_val = df_selection0["Gamma_(keV)"].values
    y0_val = np.zeros(numpoints0)
    y1_val = np.ones(numpoints0)
    shapes0 = [
        dict(type='line',
             x0=x0,
             y0=y0,
             x1=x1,
             y1=y1,
             line=dict(color='green',
                       width=1))
        for x0, y0, x1, y1 in zip(x0_val, y0_val, x1_val, y1_val)
    ]
    shapes += shapes0
if plot_options["Microseconds"]:
    fig.add_scatter(
        x=df_selection1['Gamma_(keV).1'],
        y=intensities1,
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection1['AMU.1'].astype(str) + '<br>' +
                'Element: ' + df_selection1['Element.1'].astype(str) + '<br>' +
                'Spin: ' + df_selection1['Spin.1'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection1['Half_Life.1'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection1['Gamma_(keV).1'].astype(str)),
        mode='markers',
        name='Microseconds'
    )
    numpoints1 = len(df_selection1)
    x0_val = df_selection1["Gamma_(keV).1"].values
    x1_val = df_selection1["Gamma_(keV).1"].values
    y0_val = np.zeros(numpoints1)
    y1_val = np.ones(numpoints1)
    shapes1 = [
        dict(type='line',
             x0=x0,
             y0=y0,
             x1=x1,
             y1=y1,
             line=dict(color='green',
                       width=1))
        for x0, y0, x1, y1 in zip(x0_val, y0_val, x1_val, y1_val)
    ]
    shapes += shapes1
if plot_options["Milliseconds"]:
    fig.add_scatter(
        x=df_selection2['Gamma_(keV).2'],
        y=intensities2,
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection2['AMU.2'].astype(str) + '<br>' +
                'Element: ' + df_selection2['Element.2'].astype(str) + '<br>' +
                'Spin: ' + df_selection2['Spin.2'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection2['Half_Life.2'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection2['Gamma_(keV).2'].astype(str)),
        mode='markers',
        name='Milliseconds'
    )
    numpoints2 = len(df_selection2)
    x0_val = df_selection2["Gamma_(keV).2"].values
    x1_val = df_selection2["Gamma_(keV).2"].values
    y0_val = np.zeros(numpoints2)
    y1_val = np.ones(numpoints2)
    shapes2 = [
        dict(type='line',
             x0=x0,
             y0=y0,
             x1=x1,
             y1=y1,
             line=dict(color='green',
                       width=1))
        for x0, y0, x1, y1 in zip(x0_val, y0_val, x1_val, y1_val)
    ]
    shapes += shapes2

if plot_options["Seconds"]:
    fig.add_scatter(
        x=df_selection3['Gamma_(keV).3'],
        y=intensities3,
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection3['AMU.3'].astype(str) + '<br>' +
                'Element: ' + df_selection3['Element.3'].astype(str) + '<br>' +
                'Spin: ' + df_selection3['Spin.3'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection3['Half_Life.3'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection3['Gamma_(keV).3'].astype(str)),
        mode='markers',
        name='Seconds'
    )
    numpoints3 = len(df_selection3)
    x0_val = df_selection3["Gamma_(keV).3"].values
    x1_val = df_selection3["Gamma_(keV).3"].values
    y0_val = np.zeros(numpoints3)
    y1_val = np.ones(numpoints3)
    shapes3 = [
        dict(type='line',
             x0=x0,
             y0=y0,
             x1=x1,
             y1=y1,
             line=dict(color='green',
                       width=1))
        for x0, y0, x1, y1 in zip(x0_val, y0_val, x1_val, y1_val)
    ]
    shapes += shapes3

if plot_options["Minuets"]:
    fig.add_scatter(
        x=df_selection4['Gamma_(keV).4'],
        y=intensities4,
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection4['AMU.4'].astype(str) + '<br>' +
                'Element: ' + df_selection4['Element.4'].astype(str) + '<br>' +
                'Spin: ' + df_selection4['Spin.4'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection4['Half_Life.4'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection4['Gamma_(keV).4'].astype(str)),
        mode='markers',
        name='Minuets'
    )
    numpoints4 = len(df_selection4)
    x0_val = df_selection4["Gamma_(keV).4"].values
    x1_val = df_selection4["Gamma_(keV).4"].values
    y0_val = np.zeros(numpoints4)
    y1_val = np.ones(numpoints4)
    shapes4 = [
        dict(type='line',
             x0=x0,
             y0=y0,
             x1=x1,
             y1=y1,
             line=dict(color='green',
                       width=1))
        for x0, y0, x1, y1 in zip(x0_val, y0_val, x1_val, y1_val)
    ]
    shapes += shapes4

if plot_options["Hours"]:
    fig.add_scatter(
        x=df_selection5['Gamma_(keV).5'],
        y=intensities5,
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection5['AMU.5'].astype(str) + '<br>' +
                'Element: ' + df_selection5['Element.5'].astype(str) + '<br>' +
                'Spin: ' + df_selection5['Spin.5'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection5['Half_Life.5'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection5['Gamma_(keV).5'].astype(str)),
        mode='markers',
        name='Hours'
    )
    numpoints5 = len(df_selection5)
    x0_val = df_selection5["Gamma_(keV).5"].values
    x1_val = df_selection5["Gamma_(keV).5"].values
    y0_val = np.zeros(numpoints5)
    y1_val = np.ones(numpoints5)
    shapes5 = [
        dict(type='line',
             x0=x0,
             y0=y0,
             x1=x1,
             y1=y1,
             line=dict(color='green',
                       width=1))
        for x0, y0, x1, y1 in zip(x0_val, y0_val, x1_val, y1_val)
    ]
    shapes += shapes5

if plot_options["Days"]:
    fig.add_scatter(
        x=df_selection6['Gamma_(keV).6'],
        y=intensities6,
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection6['AMU.6'].astype(str) + '<br>' +
                'Element: ' + df_selection6['Element.6'].astype(str) + '<br>' +
                'Spin: ' + df_selection6['Spin.6'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection6['Half_Life.6'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection6['Gamma_(keV).6'].astype(str)),
        mode='markers',
        name='Days'
    )
    numpoints6 = len(df_selection6)
    x0_val = df_selection6["Gamma_(keV).6"].values
    x1_val = df_selection6["Gamma_(keV).6"].values
    y0_val = np.zeros(numpoints6)
    y1_val = np.ones(numpoints6)
    shapes6 = [
        dict(type='line',
             x0=x0,
             y0=y0,
             x1=x1,
             y1=y1,
             line=dict(color='green',
                       width=1))
        for x0, y0, x1, y1 in zip(x0_val, y0_val, x1_val, y1_val)
    ]
    shapes += shapes6

if plot_options["Years"]:
    fig.add_scatter(
        x=df_selection7['Gamma_(keV).7'],
        y=intensities7,
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection7['AMU.7'].astype(str) + '<br>' +
                'Element: ' + df_selection7['Element.7'].astype(str) + '<br>' +
                'Spin: ' + df_selection7['Spin.7'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection7['Half_Life.7'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection7['Gamma_(keV).7'].astype(str)),
        mode='markers',
        name='Years'
    )
    numpoints7 = len(df_selection7)
    x0_val = df_selection7["Gamma_(keV).7"].values
    x1_val = df_selection7["Gamma_(keV).7"].values
    y0_val = np.zeros(numpoints7)
    y1_val = np.ones(numpoints7)
    shapes7 = [
        dict(type='line',
             x0=x0,
             y0=y0,
             x1=x1,
             y1=y1,
             line=dict(color='green',
                       width=1))
        for x0, y0, x1, y1 in zip(x0_val, y0_val, x1_val, y1_val)
    ]
    shapes += shapes7

fig.update_layout(shapes=shapes)

fig.update_layout(title='Isomeric Transition Gamma Ray Spectrogram', showlegend=True, legend_title='Half-Life Set')
fig.update_yaxes(visible=False)
st.plotly_chart(fig, use_container_width=True)

#-------------- Scatter Plot -------------------

fig2 = px.scatter()
if plot_options["Nanoseconds"]:
    fig2.add_scatter(
        x=df_selection0['AMU'],
        y=df_selection0['Gamma_(keV)'],
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection0['AMU'].astype(str) + '<br>' +
                'Element: ' + df_selection0['Element'].astype(str) + '<br>' +
                'Spin: ' + df_selection0['Spin'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection0['Half_Life'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection0['Gamma_(keV)'].astype(str)),
        mode='markers',
        name='Nanoseconds'
    )

if plot_options["Microseconds"]:
    fig2.add_scatter(
        x=df_selection1['AMU.1'],
        y=df_selection1['Gamma_(keV).1'],
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection1['AMU.1'].astype(str) + '<br>' +
                'Element: ' + df_selection1['Element.1'].astype(str) + '<br>' +
                'Spin: ' + df_selection1['Spin.1'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection1['Half_Life.1'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection1['Gamma_(keV).1'].astype(str)),
        mode='markers',
        name='Microseconds'
    )

if plot_options["Milliseconds"]:
    fig2.add_scatter(
        x=df_selection2['AMU.2'],
        y=df_selection2['Gamma_(keV).2'],
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection2['AMU.2'].astype(str) + '<br>' +
                'Element: ' + df_selection2['Element.2'].astype(str) + '<br>' +
                'Spin: ' + df_selection2['Spin.2'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection2['Half_Life.2'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection2['Gamma_(keV).2'].astype(str)),
        mode='markers',
        name='Milliseconds'
    )

if plot_options["Seconds"]:
    fig2.add_scatter(
        x=df_selection3['AMU.3'],
        y=df_selection3['Gamma_(keV).3'],
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection3['AMU.3'].astype(str) + '<br>' +
                'Element: ' + df_selection3['Element.3'].astype(str) + '<br>' +
                'Spin: ' + df_selection3['Spin.3'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection3['Half_Life.3'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection3['Gamma_(keV).3'].astype(str)),
        mode='markers',
        name='Seconds'
    )

if plot_options["Minuets"]:
    fig2.add_scatter(
        x=df_selection4['AMU.4'],
        y=df_selection4['Gamma_(keV).4'],
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection4['AMU.4'].astype(str) + '<br>' +
                'Element: ' + df_selection4['Element.4'].astype(str) + '<br>' +
                'Spin: ' + df_selection4['Spin.4'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection4['Half_Life.4'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection4['Gamma_(keV).4'].astype(str)),
        mode='markers',
        name='Minuets'
    )


if plot_options["Hours"]:
    fig2.add_scatter(
        x=df_selection5['AMU.5'],
        y=df_selection5['Gamma_(keV).5'],
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection5['AMU.5'].astype(str) + '<br>' +
                'Element: ' + df_selection5['Element.5'].astype(str) + '<br>' +
                'Spin: ' + df_selection5['Spin.5'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection5['Half_Life.5'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection5['Gamma_(keV).5'].astype(str)),
        mode='markers',
        name='Hours'
    )

if plot_options["Days"]:
    fig2.add_scatter(
        x=df_selection6['AMU.6'],
        y=df_selection6['Gamma_(keV).6'],
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection6['AMU.6'].astype(str) + '<br>' +
                'Element: ' + df_selection6['Element.6'].astype(str) + '<br>' +
                'Spin: ' + df_selection6['Spin.6'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection6['Half_Life.6'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection6['Gamma_(keV).6'].astype(str)),
        mode='markers',
        name='Days'
    )

if plot_options["Years"]:
    fig2.add_scatter(
        x=df_selection7['AMU.7'],
        y=df_selection7['Gamma_(keV).7'],
        hoverinfo='text',
        hovertext=(
                'AMU: ' + df_selection7['AMU.7'].astype(str) + '<br>' +
                'Element: ' + df_selection7['Element.7'].astype(str) + '<br>' +
                'Spin: ' + df_selection7['Spin.7'].astype(str) + '<br>' +
                'Half-Life: ' + df_selection7['Half_Life.7'].astype(str) + '<br>' +
                'Gamma Ray Energy: ' + df_selection7['Gamma_(keV).7'].astype(str)),
        mode='markers',
        name='Years'
    )
fig2.update_layout(title='Isomer Gamma Ray Energies', showlegend=True, legend_title='Half-Life Set')
st.plotly_chart(fig2, use_container_width=True)

if plot_options["Nanoseconds"]:
    st.subheader("Dataframe for Isomers with Nanosecond Half-Lives")
    st.dataframe(df_selection0)
    csv_data0 = download_dataframe(df_selection0)
    b64_data0 = base64.b64decode(csv_data0)
    st.download_button(label="Download Isomer Nanosecond Data", data=b64_data0, file_name='isomers_nano.csv',
                       mime='text/csv')

if plot_options["Microseconds"]:
    st.subheader("Dataframe for Isomers with Microsecond Half-Lives")
    st.dataframe(df_selection1)
    csv_data1 = download_dataframe(df_selection1)
    b64_data1 = base64.b64decode(csv_data1)
    st.download_button(label="Download Isomer Microsecond Data", data=b64_data1, file_name='isomers_mic.csv',
                       mime='text/csv')

if plot_options["Milliseconds"]:
    st.subheader("Dataframe for Isomers with Millisecond Half-Lives")
    st.dataframe(df_selection2)
    csv_data2 = download_dataframe(df_selection2)
    b64_data2 = base64.b64decode(csv_data2)
    st.download_button(label="Download Isomer Millisecond Data", data=b64_data2, file_name='isomers_mil.csv',
                       mime='text/csv')

if plot_options["Seconds"]:
    st.subheader("Dataframe for Isomers with Second Half-Lives")
    st.dataframe(df_selection3)
    csv_data3 = download_dataframe(df_selection3)
    b64_data3 = base64.b64decode(csv_data3)
    st.download_button(label="Download Isomer Second Data", data=b64_data3, file_name='isomers_sec.csv',
                       mime='text/csv')

if plot_options["Minuets"]:
    st.subheader("Dataframe for Isomers with Minuet Half-Lives")
    st.dataframe(df_selection4)
    csv_data4 = download_dataframe(df_selection4)
    b64_data4 = base64.b64decode(csv_data4)
    st.download_button(label="Download Isomer Minuet Data", data=b64_data4, file_name='isomers_min.csv',
                       mime='text/csv')

if plot_options["Hours"]:
    st.subheader("Dataframe for Isomers with Hour Half-Lives")
    st.dataframe(df_selection5)
    csv_data5 = download_dataframe(df_selection5)
    b64_data5 = base64.b64decode(csv_data5)
    st.download_button(label="Download Isomer Hour Data", data=b64_data5, file_name='isomers_hour.csv',
                       mime='text/csv')

if plot_options["Days"]:
    st.subheader("Dataframe for Isomers with Day Half-Lives")
    st.dataframe(df_selection6)
    csv_data6 = download_dataframe(df_selection6)
    b64_data6 = base64.b64decode(csv_data6)
    st.download_button(label="Download Isomer Day Data", data=b64_data6, file_name='isomers_day.csv',
                       mime='text/csv')

if plot_options["Years"]:
    st.subheader("Dataframe for Isomers with Year Half-Lives")
    st.dataframe(df_selection7)
    csv_data7 = download_dataframe(df_selection7)
    b64_data7 = base64.b64decode(csv_data7)
    st.download_button(label="Download Isomer Year Data", data=b64_data7, file_name='isomers_year.csv',
                       mime='text/csv')

fig3 = px.bar(
    dfs,
    x='Element',
    y='Amount',
    color='atom%',
    title='Solar Abundance',
    log_y=True,
    color_continuous_scale='algae'
)
st.plotly_chart(fig3, use_container_width=True)



# This hides the streamlit library watermarks
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
