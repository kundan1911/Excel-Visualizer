import pandas as pd
import plotly_express as px
import streamlit as st
import math

def plot_bar_graph(colume_val,Title):
    # st.subheader('Average Rating')
    # st.subheader(f"{give_mean(colume_val)}")
    df_for_plot=pd.DataFrame(columns=['values','count'])
    df_for_plot=pd.DataFrame(columns=['values','count'])
    df_for_plot['values']=colume_val.unique();
    # give_mean(colume_val)
    for i in range(0,len(df_for_plot['values']-1)):
        df_for_plot['count'][i]=colume_val.value_counts()[df_for_plot['values'][i]]

    df_for_plot=df_for_plot.sort_values(by=['values'])
    # print(df_reason_1)
    # st.dataframe(df_for_plot)
    st.subheader('Average Rating')
    st.subheader(f"{give_mean(df_for_plot)}")
    fig2= px.bar(df_for_plot, x='values', y='count',orientation='v',width=700,color_discrete_sequence =['green']*len(df_for_plot),
             title=Title,
             labels={'x': 'Some X', 'y':'Some Y'})

    fig2.update_layout(
    xaxis_title="X Axis Title",
    yaxis_title="No of people",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=25,
        color="orange"
    )
    )
    # for data in fig2.data:
    #     data["width"] = 0.15
    # fig2.update_layout(width=0.15, bargap=0.05)
    st.write(fig2)
    
    
def give_mean(df):
    mean=0;
    noofresp=0
    
    for i in range(0,len(df['count'])):
        x = float(df['count'][i])
        if not math.isnan(x):
            mean=mean+df['values'][i]*df['count'][i];
            noofresp=noofresp+df['count'][i];
    if  noofresp:
        return round(mean/noofresp,2);


st.set_page_config(
    page_title="Data Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

df=pd.read_excel(
    io='data.xlsx',
    engine='openpyxl',
    skiprows=0,
    usecols='B:W',
    nrows=250
)
# st.dataframe(df)


st.sidebar.header('Use the following filters:')
age=st.sidebar.multiselect(
    "Select Age :",
    options=df['Age'].unique(),
    default=df['Age'].unique()
)
gender=st.sidebar.multiselect(
    "Select Gender :",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)
marriage=st.sidebar.multiselect(
    "Select Marital Status :",
    options=df['Marital_Status'].unique(),
    default=df['Marital_Status'].unique()
)
religion=st.sidebar.multiselect(
    "Select Religion :",
    options=df['Religion'].unique(),
    default=df['Religion'].unique()
)
education=st.sidebar.multiselect(
    "Select Education :",
    options=df['Education'].unique(),
    default=df['Education'].unique()
)
occupation=st.sidebar.multiselect(
    "Select Occupation :",
    options=df['Occupation'].unique(),
    default=df['Occupation'].unique()
)
df_selection=df.query(
    'Age == @age & Gender == @gender & Marital_Status == @marriage & Religion == @religion & Education == @education & Occupation == @occupation'
)

# reason_1=df_selection['Reason_1'];
# if len(reason_1):
#    plot_bar_graph(reason_1,"Increase in women literacy rate")
# st.dataframe(df_selection)

# Front - Page

st.title("People responses");
# average_rating=round(df_selection["Reason_1"].mean(),1)
# left_column,middlecol,right_col=st.columns(3)

# with left_column:
#     st.subheader('Average Rating')
#     st.subheader(f"{average_rating}")

st.markdown("---")
st.title("Government’s reason for increasing woman minimum marriage age are:-");
left_column,right_col=st.columns(2)
with left_column:
    reason_1=df_selection['Reason_1'];
    if len(reason_1):
        plot_bar_graph(reason_1,"Increase in women literacy rate")
with right_col:
    reason_2=df_selection['Reason_2'];
    if len(reason_2):
        plot_bar_graph(reason_2,"Domestic violence will reduce and Gender equality will be maintained")

st.markdown("---")

left_column,right_col=st.columns(2)
with left_column:
    reason_3=df_selection['Reason_3'];
    if len(reason_3):
        plot_bar_graph(reason_3,"Child health would be better")
with right_col:
    reason_4=df_selection['Reason_4'];
    if len(reason_4):
        plot_bar_graph(reason_4,"Will reduce women death after childbirth as they would be more mature")

st.markdown("---")

left_column,right_col=st.columns(2)
with left_column:
    reason_5=df_selection['Reason_5'];
    if len(reason_5):
        plot_bar_graph(reason_5,"Population Control")
with right_col:
    reason_6=df_selection['Reason_6'];
    if len(reason_6):
        plot_bar_graph(reason_6,"Women empowerment")


st.markdown("---")
st.title("Measures that the government can take");
left_column,right_col=st.columns(2)
with left_column:
    m1=df_selection['Measures_1'];
    if len(m1):
        plot_bar_graph(m1,"Awareness drives ,media campaigns and Organize outreach programmes")
with right_col:
    m2=df_selection['Measures_2'];
    if len(m2):
        plot_bar_graph(m2,"Government officials should visit, inspect and interact with the children as well as the community. Release an helpline number.")
    st.markdown("---")

left_column,right_col=st.columns(2)
with left_column:
    m3=df_selection['Measures_3'];
    if len(m3):
        plot_bar_graph(m3,"Heavy fine of 10 lakh and 5 year imprisonment must be imposed on Parents of both sides")
with right_col:
    m4=df_selection['Measures_4'];
    if len(m4):
        plot_bar_graph(m4,"Strict verification of documents of woman by both police in charge as well as by marriage court.")

st.markdown("---")
st.title("Why Indian parents are keen to marry their Daughter’s early");
left_column,right_col=st.columns(2)
with left_column:
    m1=df_selection['Parent_reason_1'];
    if len(m1):
        plot_bar_graph(m1,"As woman age increases more dowry is demanded by the groom side So the parents want to get rid of this burden")
with right_col:
    m2=df_selection['Parent_reason_2'];
    if len(m2):
        plot_bar_graph(m2,"They consider their daughter’s as paraya dhan")
    st.markdown("---")

left_column,right_col=st.columns(2)
with left_column:
    m3=df_selection['Parent_reason_3'];
    if len(m3):
        plot_bar_graph(m3,"They feel that ‘marriage market’ needs only young brides")
with right_col:
    m4=df_selection['Parent_reason_4'];
    if len(m4):
        plot_bar_graph(m4,"In their Old age Parents think that only a boy would be able to take care of them not a girl.")
