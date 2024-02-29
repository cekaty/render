#importing all the libraries-----------------------------------
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import dash
from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output, State
import dash_daq as daq

#starting the application------------------------------------------------------
app= dash.Dash(__name__)
server=app.server

#colors theming----------------------------------------------------------------
colors = {
    'background': '#000000',
    'black': '#000000',
    'grey': '#202020',
    'white': "#FFFFFF",
    'gold': "#D4AF37",
    'cyan': "#03DAC6",
    'purple': "#6200EE"
}

#adding images-----------------------------------------------------------------
fig = go.Figure()
fig.add_layout_image(
    dict(
        source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/vox.png",
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)

#declaring the dataset---------------------------------------------------------
df= pd.read_csv("AQMD_data.csv") #"df" is "data frame"
print(df[:5])

#all about charts and graphs----------------------------------------------------
fig1=px.bar(df,x="Humidity",y="PM2.5",template="plotly_dark", title="Humidity vs PM2.5")

fig2=px.bar(df,x="Humidity",y="PM2.5",template="plotly_dark", title="Humidity vs PM10")

fig3=px.bar(df,x="Humidity",y="PM2.5",template="plotly_dark", title="Humidity vs PM1")

fig4=px.bar(df,x="Humidity",y="PM2.5",template="plotly_dark", title="Humidity vs Temperature")

fig1.update_layout(
    plot_bgcolor=colors['grey'],
    paper_bgcolor=colors['black'],
    font_color=colors['white']
)
fig2.update_layout(
    plot_bgcolor=colors['grey'],
    paper_bgcolor=colors['black'],
    font_color=colors['white']
)
fig3.update_layout(
    plot_bgcolor=colors['grey'],
    paper_bgcolor=colors['black'],
    font_color=colors['white']
)
fig4.update_layout(
    plot_bgcolor=colors['grey'],
    paper_bgcolor=colors['black'],
    font_color=colors['white']
)

#application layout------------------------------------------------------------
app.layout = html.Div(style = {'backgroundColor': 'black'}, children=[

    html.Br(),

    html.H1('Cekaty Innovations', style={'text-align': 'center', 'color':'gold', 'font-family':'georgia'}),
    
    html.H1("AQMD Dashboard", style={'text-align': 'center', 'color':'white', 'font-family':'georgia'}),

    html.Div(style={'padding-left':'10px','display': 'inline-block', 'width':'15%', 'color':'black'},
             children=[
             dcc.Dropdown(['Jaipur', 'Dehradun', 'Delhi'],
                 id='location-dropdown',
                 placeholder="Select Location")
             ]),

    html.Div(style={'padding-left':'10px','display': 'inline-block', 'width':'15%', 'color':'black'},
             children=[
             dcc.Dropdown(['Every 5 Minutes', 'Every 30 Minutes', 'Every 1 Hour'],
                 id='frequency-dropdown',
                 placeholder="Set Data Frequency")
             ]),

    html.H2("Analyzed Data", style={'text-align': 'left',
                                    'color': 'black',
                                    'backgroundColor':'gold',
                                    'font-family':'georgia',
                                    'border-style':'solid',
                                    'border-color':'gold',
                                    'border-radius':'15px',
                                    'padding-left':'10px'}),


    html.Div(style={'display': 'inline-block', 'width':'50%', 'color': colors['white']},
             children=[
             dcc.Graph(id='graph5',figure=fig1)
             ]),

    html.Div(style={'display': 'inline-block', 'width':'50%', 'color': colors['white']},
             children=[
             dcc.Graph(id='graph6',figure=fig2)
             ]),
    html.Div(style={'display': 'inline-block', 'width':'50%', 'color': colors['white']},
             children=[
             dcc.Graph(id='graph7',figure=fig3)
             ]),
    html.Div(style={'display': 'inline-block', 'width':'50%', 'color': colors['white']},
             children=[
             dcc.Graph(id='graph8',figure=fig4)
             ]),

    html.H2("Raw Data", style={'text-align': 'left',
                                    'color': 'black',
                                    'backgroundColor':'gold',
                                    'font-family':'georgia',
                                    'border-style':'solid',
                                    'border-color':'gold',
                                    'border-radius':'15px',
                                    'padding-left':'10px'}),

    html.Div(style={'display':'inline-block','color':'white','width':'20%','padding-left':'10px'},children=[html.H3("Set Data Frequency")]),

    dash_table.DataTable(df.to_dict('records'),
                         [{"name": i, "id": i} for i in df.columns],
                         style_cell={'textAlign': 'center'},
                         style_header={
                             'backgroundColor': 'grey',
                             'fontWeight': 'bold'
                             },
                         ),

    html.Div(style={'display':'inline-block','color':'white','width':'25%','padding-left':'10px'},children=[html.H3("Download the updated CSV file from here >>> ")]),
    
    html.Div(style={'display':'inline-block','color':'white','width':'20%'},children=[html.Button("Download CSV", id="btn_csv"), dcc.Download(id="download-dataframe-csv")]),

    html.Br(),

    html.Div(style={'display': 'inline-block', 'width':'50%', 'color': colors['white']},
             children=[
             dcc.Graph(id='graph1',figure=fig1)
             ]),

    html.Div(style={'display': 'inline-block', 'width':'50%', 'color': colors['white']},
             children=[
             dcc.Graph(id='graph2',figure=fig2)
             ]),
    html.Div(style={'display': 'inline-block', 'width':'50%', 'color': colors['white']},
             children=[
             dcc.Graph(id='graph3',figure=fig3)
             ]),
    html.Div(style={'display': 'inline-block', 'width':'50%', 'color': colors['white']},
             children=[
             dcc.Graph(id='graph4',figure=fig4)
             ])

    ])

#application callback--------------------------------------------------
@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)

#download action---------------------------------------------------
def func(n_clicks):
    return dcc.send_data_frame(df.to_csv, "AQMD_updated.csv")

#main code for running the entire application---------------------
if __name__ == '__main__':
    app.run_server(debug=True)
