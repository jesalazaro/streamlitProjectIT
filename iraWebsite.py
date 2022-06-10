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
from bokeh.layouts import row , gridplot


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
co2018 = run_query("SELECT * from co2018")
co2019 = run_query("SELECT * from co2019")
co2021 = run_query("SELECT * from co2021")
co2018adj = run_query("SELECT * from co2018adj")
co2019adj = run_query("SELECT * from co2019adj")
co2021adj = run_query("SELECT * from co2021adj")
weekMeans = run_query("SELECT * from weekmeans")

patients2018 = []
patients2019 = []
patients2020 = []
patients2021 = []

carvajal2018 = []
carvajal2019 = []
carvajal2021 = []
centro2018 = []
centro2019 = []
centro2021 = []
kennedy2018 = []
kennedy2019 = []
kennedy2021 = []
lasFerias2018 = []
lasFerias2019 = []
lasFerias2021 = []
puenteA2018 = []
puenteA2019 = []
puenteA2021 = []
tunal2018 = []
tunal2019 = []
tunal2021 = []
usaquen2018 = []
usaquen2019 = []
usaquen2021 = []


carvajal2018adj = []
carvajal2019adj = []
carvajal2021adj = []
centro2018adj = []
centro2019adj = []
centro2021adj = []
kennedy2018adj = []
kennedy2019adj = []
kennedy2021adj = []
lasFerias2018adj = []
lasFerias2019adj = []
lasFerias2021adj = []
puenteA2018adj = []
puenteA2019adj = []
puenteA2021adj = []
tunal2018adj = []
tunal2019adj = []
tunal2021adj = []
usaquen2018adj = []
usaquen2019adj = []
usaquen2021adj = []


carvajal2018mean = []
carvajal2019mean = []
carvajal2021mean = []
centro2018mean = []
centro2019mean = []
centro2021mean = []
kennedy2018mean = []
kennedy2019mean = []
kennedy2021mean = []
lasFerias2018mean = []
lasFerias2019mean = []
lasFerias2021mean = []
puenteA2018mean = []
puenteA2019mean = []
puenteA2021mean = []
tunal2018mean = []
tunal2019mean = []
tunal2021mean = []
usaquen2018mean = []
usaquen2019mean = []
usaquen2021mean = []

x = []
n = 0
z = []
m = 0
weeks2018 = []
weeks2019 = []
weeks2020 = []
weeks2021 = []
c2018 = 0
c2019 = 0
c2020 = 0
c2021 = 0

for row in rows:
    patients2018.append(row[1])
    weeks2018.append(c2018)
    c2018 += 1


for row in rows:
    patients2019.append(row[2])
    weeks2019.append(c2019)
    c2019 += 1

for row in rows:
    patients2020.append(row[3])
    weeks2020.append(c2020)
    c2020 += 1


for row in rows:
    patients2021.append(row[4])
    weeks2021.append(c2021)
    c2021 += 1

for i in co2018:
    carvajal2018.append(i[1])
    centro2018.append(i[2])
    kennedy2018.append(i[3])
    lasFerias2018.append(i[4])
    puenteA2018.append(i[5])
    tunal2018.append(i[6])
    usaquen2018.append(i[7])
    x.append(n)
    n += 1

for i in co2019:
    carvajal2019.append(i[1])
    centro2019.append(i[2])
    kennedy2019.append(i[3])
    lasFerias2019.append(i[4])
    puenteA2019.append(i[5])
    tunal2019.append(i[6])
    usaquen2019.append(i[7])
    
for i in co2021:
    carvajal2021.append(i[1])
    centro2021.append(i[2])
    kennedy2021.append(i[3])
    lasFerias2021.append(i[4])
    puenteA2021.append(i[5])
    tunal2021.append(i[6])
    usaquen2021.append(i[7])


for i in co2018adj:
    carvajal2018adj.append(i[0])
    centro2018adj.append(i[1])
    kennedy2018adj.append(i[2])
    lasFerias2018adj.append(i[3])
    puenteA2018adj.append(i[4])
    tunal2018adj.append(i[5])
    usaquen2018adj.append(i[6])
    z.append(m)
    m += 1

for i in co2019adj:
    carvajal2019adj.append(i[0])
    centro2019adj.append(i[1])
    kennedy2019adj.append(i[2])
    lasFerias2019adj.append(i[3])
    puenteA2019adj.append(i[4])
    tunal2019adj.append(i[5])
    usaquen2019adj.append(i[6])
    
for i in co2021adj:
    carvajal2021adj.append(i[0])
    centro2021adj.append(i[1])
    kennedy2021adj.append(i[2])
    lasFerias2021adj.append(i[3])
    puenteA2021adj.append(i[4])
    tunal2021adj.append(i[5])
    usaquen2021adj.append(i[6])

n = 0
for i in weekMeans:
    carvajal2018mean.append(i[1])
    carvajal2019mean.append(i[2])
    carvajal2021mean.append(i[3])
    centro2018mean.append(i[4])
    centro2019mean.append(i[5])
    centro2021mean.append(i[6])
    kennedy2018mean.append(i[7])
    kennedy2019mean.append(i[8])
    kennedy2021mean.append(i[9])
    lasFerias2018mean.append(i[10])
    lasFerias2019mean.append(i[11])
    lasFerias2021mean.append(i[12])
    puenteA2018mean.append(i[13])
    puenteA2019mean.append(i[14])
    puenteA2021mean.append(i[15])
    tunal2018mean.append(i[16])
    tunal2019mean.append(i[17])
    tunal2021mean.append(i[18])
    usaquen2018mean.append(i[19])
    usaquen2019mean.append(i[20])
    usaquen2021mean.append(i[21])
    x.append(n)
    n += 1

numpy_a_patients = np.array(patients2018)

if st.checkbox('Mostrar datos'):
    st.subheader('Hospitalizaciones en las semanas del año')
    
    df = pd.DataFrame(
        numpy_a_patients,
        index=['Semana %d' % i for i in range(1, 54)],
        columns=['Pacientes'],
        ) 
    
    i = st.table(df)

p = figure(title="Pacientes por año", x_axis_label='semanas', y_axis_label='N. de pacientes', plot_width=800, plot_height=400)
# add multiple renderers
p.line(weeks2021, patients2018, legend_label="2018", color="blue", line_width=2)
p.line(weeks2021, patients2019, legend_label="2019", color="red", line_width=2)
p.line(weeks2021, patients2020, legend_label="2020", color="green", line_width=2)
p.line(weeks2021, patients2021, legend_label="2021", color="yellow", line_width=2)

st.bokeh_chart(p)

p2018 = figure(title='pacientes',x_axis_label='semanas', y_axis_label='N. de pacientes')
p2018.line(weeks2018, patients2018, legend_label='Tre', line_width=2)

pl2018 = figure( plot_height=600, plot_width=600, title="pacientes",x_axis_label='semanas', y_axis_label='N. de pacientes',
       toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")
pl2018.vbar(weeks2018, top=patients2018, width=.4, color= "firebrick", legend_label="Product Counts")


p2019 = figure(title='pacientes',x_axis_label='semanas', y_axis_label='N. de pacientes')
p2019.line(weeks2019, patients2019, legend_label='Tre', line_width=2)

pl2019 = figure( plot_height=600, plot_width=600, title="pacientes",x_axis_label='semanas', y_axis_label='N. de pacientes',
       toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")
pl2019.vbar(weeks2019, top=patients2019, width=.4, color= "firebrick", legend_label="Product Counts")


p2020 = figure(title='pacientes',x_axis_label='semanas', y_axis_label='N. de pacientes')
p2020.line(weeks2020, patients2020, legend_label='Tre', line_width=2)

pl2020 = figure( plot_height=600, plot_width=600, title="pacientes",x_axis_label='semanas', y_axis_label='N. de pacientes',
       toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")
pl2020.vbar(weeks2020, top=patients2020, width=.4, color= "firebrick", legend_label="Product Counts")


p2021 = figure(title='pacientes',x_axis_label='semanas', y_axis_label='N. de pacientes')
p2021.line(weeks2021, patients2021, legend_label='Tre', line_width=2)

pl2021 = figure( plot_height=600, plot_width=600, title="pacientes",x_axis_label='semanas', y_axis_label='N. de pacientes',
       toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")
pl2021.vbar(weeks2021, top=patients2021, width=.4, color= "firebrick", legend_label="Product Counts")


patientsgrid = gridplot([
 [p2018,pl2018]
,[p2019,pl2019] 
,[p2020,pl2020] 
,[p2021,pl2021] 
], width=400, height=400)

st.bokeh_chart(patientsgrid)

pYear2018Carvajal = figure(title='carvajal2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Carvajal.line(x, carvajal2018, line_width=2)
pYear2019Carvajal = figure(title='carvajal2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Carvajal.line(x, carvajal2019, line_width=2)
pYear2021Carvajal = figure(title='carvajal2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Carvajal.line(x, carvajal2021, line_width=2)


pYear2018Carvajaladj = figure(title='carvajal2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Carvajaladj.line(x, carvajal2018adj, line_width=2)
pYear2019Carvajaladj = figure(title='carvajal2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Carvajaladj.line(x, carvajal2019adj, line_width=2)
pYear2021Carvajaladj = figure(title='carvajal2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Carvajaladj.line(x, carvajal2021adj, line_width=2)


pYear2018Centro = figure(title='Centro 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Centro.line(x, centro2018, line_width=2)
pYear2019Centro = figure(title='Centro 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Centro.line(x, centro2019, line_width=2)
pYear2021Centro = figure(title='Centro 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Centro.line(x, centro2021, line_width=2)

pYear2018Centroadj = figure(title='Centro 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Centroadj.line(x, centro2018adj, line_width=2)
pYear2019Centroadj = figure(title='Centro 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Centroadj.line(x, centro2019adj, line_width=2)
pYear2021Centroadj = figure(title='Centro 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Centroadj.line(x, centro2021adj, line_width=2)


pYear2018Kennedy = figure(title='Kennedy 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Kennedy.line(x, kennedy2018, line_width=2)
pYear2019Kennedy = figure(title='Kennedy 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Kennedy.line(x, kennedy2019, line_width=2)
pYear2021Kennedy = figure(title='Kennedy 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Kennedy.line(x, kennedy2021, line_width=2)


pYear2018Kennedyadj = figure(title='Kennedy 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Kennedyadj.line(x, kennedy2018adj, line_width=2)
pYear2019Kennedyadj = figure(title='Kennedy 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Kennedyadj.line(x, kennedy2019adj, line_width=2)
pYear2021Kennedyadj = figure(title='Kennedy 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Kennedyadj.line(x, kennedy2021adj, line_width=2)


pYear2018Las_Ferias = figure(title='Las Ferias 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Las_Ferias.line(x, lasFerias2018, line_width=2)
pYear2019Las_Ferias = figure(title='Las Ferias 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Las_Ferias.line(x, lasFerias2019, line_width=2)
pYear2021Las_Ferias = figure(title='Las Ferias 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Las_Ferias.line(x, lasFerias2021, line_width=2)


pYear2018Las_Feriasadj = figure(title='Las Ferias 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Las_Feriasadj.line(x, lasFerias2018adj, line_width=2)
pYear2019Las_Feriasadj = figure(title='Las Ferias 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Las_Feriasadj.line(x, lasFerias2019adj, line_width=2)
pYear2021Las_Feriasadj = figure(title='Las Ferias 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Las_Feriasadj.line(x, lasFerias2021adj, line_width=2)


pYear2018Puente_Aranda = figure(title='Puente Aranda 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Puente_Aranda.line(x, puenteA2018, line_width=2)
pYear2019Puente_Aranda = figure(title='Puente Aranda 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Puente_Aranda.line(x, puenteA2019, line_width=2)
pYear2021Puente_Aranda = figure(title='Puente Aranda 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Puente_Aranda.line(x, puenteA2021, line_width=2)



pYear2018Puente_Arandaadj = figure(title='Puente Aranda 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Puente_Arandaadj.line(x, puenteA2018adj, line_width=2)
pYear2019Puente_Arandaadj = figure(title='Puente Aranda 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Puente_Arandaadj.line(x, puenteA2019adj, line_width=2)
pYear2021Puente_Arandaadj = figure(title='Puente Aranda 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Puente_Arandaadj.line(x, puenteA2021adj, line_width=2)


pYear2018Tunal = figure(title='Tunal 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Tunal.line(x, tunal2018, line_width=2)
pYear2019Tunal = figure(title='Tunal 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Tunal.line(x, tunal2019, line_width=2)
pYear2021Tunal = figure(title='Tunal 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Tunal.line(x, tunal2021, line_width=2)


pYear2018Tunaladj = figure(title='Tunal 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Tunaladj.line(x, tunal2018adj, line_width=2)
pYear2019Tunaladj = figure(title='Tunal 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Tunaladj.line(x, tunal2019adj, line_width=2)
pYear2021Tunaladj = figure(title='Tunal 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Tunaladj.line(x, tunal2021adj, line_width=2)

pYear2018Usaquen = figure(title='Usaquen 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Usaquen.line(x, usaquen2018, line_width=2)
pYear2019Usaquen = figure(title='Usaquen 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Usaquen.line(x, usaquen2019, line_width=2)
pYear2021Usaquen = figure(title='Usaquen 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Usaquen.line(x, usaquen2021, line_width=2)

pYear2018Usaquenadj = figure(title='Usaquen 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Usaquenadj.line(x, usaquen2018adj, line_width=2,)
pYear2019Usaquenadj = figure(title='Usaquen 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Usaquenadj.line(x, usaquen2019adj, line_width=2)
pYear2021Usaquenadj = figure(title='Usaquen 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Usaquenadj.line(x, usaquen2021adj, line_width=2)



grid = gridplot([
 [pYear2018Carvajal,pYear2019Carvajal, pYear2021Carvajal]
,[pYear2018Carvajaladj,pYear2019Carvajaladj, pYear2021Carvajaladj] 
,[pYear2018Centro,pYear2019Centro, pYear2021Centro]
,[pYear2018Centroadj,pYear2019Centroadj, pYear2021Centroadj]  
,[pYear2018Kennedy,pYear2019Kennedy, pYear2021Kennedy]
,[pYear2018Kennedyadj,pYear2019Kennedyadj, pYear2021Kennedyadj]
,[pYear2018Las_Ferias,pYear2019Las_Ferias, pYear2021Las_Ferias]
,[pYear2018Las_Feriasadj,pYear2019Las_Feriasadj, pYear2021Las_Feriasadj]
,[pYear2018Puente_Aranda, pYear2019Puente_Aranda, pYear2021Puente_Aranda]
,[pYear2018Puente_Arandaadj, pYear2019Puente_Arandaadj, pYear2021Puente_Arandaadj]
,[pYear2018Tunal,pYear2019Tunal,pYear2021Tunal]
,[pYear2018Tunaladj,pYear2019Tunaladj,pYear2021Tunaladj]
,[pYear2018Usaquen,pYear2019Usaquen,pYear2021Usaquen]
,[pYear2018Usaquenadj,pYear2019Usaquenadj,pYear2021Usaquenadj]
], width=266, height=235)

st.bokeh_chart(grid)

pYear2018Carvajalmean = figure(title='carvajal2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Carvajalmean.line(x, carvajal2018mean, line_width=2,color= "indigo")
pYear2019Carvajalmean = figure(title='carvajal2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Carvajalmean.line(x, carvajal2019mean, line_width=2,color= "mediumaquamarine")
pYear2021Carvajalmean = figure(title='carvajal2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Carvajalmean.line(x, carvajal2021mean, line_width=2,color= "coral")

pYear2018Centromean = figure(title='Centro 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Centromean.line(x, centro2018mean, line_width=2,color= "indigo")
pYear2019Centromean = figure(title='Centro 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Centromean.line(x, centro2019mean, line_width=2,color= "mediumaquamarine")
pYear2021Centromean = figure(title='Centro 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Centromean.line(x, centro2021mean, line_width=2,color= "coral")

pYear2018Kennedymean = figure(title='Kennedy 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Kennedymean.line(x, kennedy2018mean, line_width=2,color= "indigo")
pYear2019Kennedymean = figure(title='Kennedy 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Kennedymean.line(x, kennedy2019mean, line_width=2,color= "mediumaquamarine")
pYear2021Kennedymean = figure(title='Kennedy 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Kennedymean.line(x, kennedy2021mean, line_width=2,color= "coral")

pYear2018Las_Feriasmean = figure(title='Las Ferias 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Las_Feriasmean.line(x, lasFerias2018mean, line_width=2,color= "indigo")
pYear2019Las_Feriasmean = figure(title='Las Ferias 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Las_Feriasmean.line(x, lasFerias2019mean, line_width=2,color= "mediumaquamarine")
pYear2021Las_Feriasmean = figure(title='Las Ferias 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Las_Feriasmean.line(x, lasFerias2021mean, line_width=2,color= "coral")

pYear2018Puente_Arandamean = figure(title='Puente Aranda 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Puente_Arandamean.line(x, puenteA2018mean, line_width=2,color= "indigo")
pYear2019Puente_Arandamean = figure(title='Puente Aranda 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Puente_Arandamean.line(x, puenteA2019mean, line_width=2,color= "mediumaquamarine")
pYear2021Puente_Arandamean = figure(title='Puente Aranda 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Puente_Arandamean.line(x, puenteA2021mean, line_width=2,color= "coral")

pYear2018Tunalmean = figure(title='Tunal 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Tunalmean.line(x, tunal2018mean, line_width=2,color= "indigo")
pYear2019Tunalmean = figure(title='Tunal 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Tunalmean.line(x, tunal2019mean, line_width=2,color= "mediumaquamarine")
pYear2021Tunalmean = figure(title='Tunal 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Tunalmean.line(x, tunal2021mean, line_width=2,color= "coral")

pYear2018Usaquenmean = figure(title='Usaquen 2018',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2018Usaquenmean.line(x, usaquen2018mean, line_width=2,color= "indigo")
pYear2019Usaquenmean = figure(title='Usaquen 2019',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2019Usaquenmean.line(x, usaquen2019mean, line_width=2,color= "mediumaquamarine")
pYear2021Usaquenmean = figure(title='Usaquen 2021',x_axis_label='Tiempo',y_axis_label='Cantidad de C')
pYear2021Usaquenmean.line(x, usaquen2021mean, line_width=2,color= "coral")

grid2 = gridplot([
 [pYear2018Carvajalmean,pYear2019Carvajalmean, pYear2021Carvajalmean]
,[pYear2018Centromean,pYear2019Centromean, pYear2021Centromean]
,[pYear2018Kennedymean,pYear2019Kennedymean, pYear2021Kennedymean]
,[pYear2018Las_Feriasmean,pYear2019Las_Feriasmean, pYear2021Las_Feriasmean]
,[pYear2018Puente_Arandamean, pYear2019Puente_Arandamean, pYear2021Puente_Arandamean]
,[pYear2018Tunalmean,pYear2019Tunalmean,pYear2021Tunalmean]
,[pYear2018Usaquenmean,pYear2019Usaquenmean,pYear2021Usaquenmean]
], width=266, height=235)

st.bokeh_chart(grid2)