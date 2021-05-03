import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

tax2gdp = pd.read_csv('data/tax2gdp.csv')

#filter some outliers
tax2gdp2 = tax2gdp[tax2gdp['GDP (In billions)'] < 10000]

fig = go.Figure(go.Bar(
    x=tax2gdp2["Tax Percentage"],
    y=tax2gdp2["GDP (In billions)"],
    name="Tax in the country",
    marker={'color':"blue"}
))
fig.update_layout(title='Tax rate by GDP for countries',
                   showlegend=True)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title="Tax rate by GDP of countries"

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='assignment4',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    ]
)

if __name__ == '__main__':
    app.run_server()
