import streamlit as st
import pandas as pd
import numpy as np
import psycopg
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource, Grid, LinearAxis, Plot, VBar
from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from bokeh.resources import CDN

@st.experimental_singleton
def init_connection():
    return psycopg.connect(**st.secrets["postgres"])

conn = init_connection()

# Perfom query.
# Uses st.experimental_memo to only rerun when the query changes of after 10 minutes
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


st.title("Hospitalizaciones debido a IRA en Bogotá D.C")
rows = run_query("SELECT * from hospi")



weeks = []
patients = []


for row in rows:
    weeks.append(row[0])
    patients.append(row[1])

numpy_array = np.array(patients)

if st.checkbox('Mostrar datos'):
    st.subheader('Hospitalizaciones en las semanas del año')
    
    df = pd.DataFrame(
        numpy_array,
        index=['Semana %d' % i for i in range(1, 53)],
        columns=['Pacientes'],
        ) 
    
    i = st.table(df)
    
p = figure(
     title='pacientes',
     x_axis_label='x',
     y_axis_label='y')

p.line(weeks, patients, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)

#st.bar_chart(patients)

plot = figure( plot_height=600, plot_width=600, title="pacientes",
       toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")
plot.title.text_font_size = '20pt'

#plot.xaxis.major_label_text_font_size = "14pt" 
plot.vbar(weeks, top=patients, width=.4, color= "firebrick", legend_label="Product Counts")
#plot.line(weeks, patients)
#plot.legend.label_text_font_size = '14pt'

st.bokeh_chart(plot, use_container_width=True)