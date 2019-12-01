from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
import requests
import json

def get_data():
    # url = 'https://api.unibit.ai/historicalstockprice/AAPL?range=3m&interval=2&AccessKey=demo'
    res = """{
	"Meta Data" : {
		"datapoints" : 45,
		"creditsCost" : 4500,
		"interval" : "2 day(s)",
		"timeZone" : "US/Eastern",
		"lastRefreshed" : "Tue Apr 23 08:59:20 GMT 2019",
		"ticker" : "AAPL"
	},
	"Stock price" : [ {
		"date" : "2019-04-08",
		"open" : 196.42,
		"high" : 200.22,
		"low" : 196.34,
		"close" : 200.1,
		"adj_close" : 200.1,
		"volume" : 25872966
	}, {
		"date" : "2019-04-04",
		"open" : 196.42,
		"high" : 200.22,
		"low" : 196.34,
		"close" : 200.1,
		"adj_close" : 200.1,
		"volume" : 25872966
	}, {
			"date" : "2019-04-02",
		"open" : 196.42,
		"high" : 200.22,
		"low" : 196.34,
		"close" : 200.1,
		"adj_close" : 200.1,
		"volume" : 25872966
	}, {
		"date" : "2019-04-08",
		"open" : 196.42,
		"high" : 200.22,
		"low" : 196.34,
		"close" : 200.1,
		"adj_close" : 200.1,
		"volume" : 25872966
	} ]
}"""
    res = json.loads(res)['Stock price']
    return res



def get_simple_candlestick():
    data = get_data()
    x,y,z,w,k=[],[],[],[],[]

    for item in data:
        x.append(item['date']),
        y.append(item['open']),
        z.append(item['high']),
        w.append(item['low']),
        k.append(item['close'])

    trace1 = go.Candlestick(
         x=x,
        open = y,
        high = z,
        low = w,
        close = k
    )
    # trace = go.Ohlc(
    #     x=data['date'],
    #     open = data['open'],
    #     high = data['high'],
    #     low = data['low'],
    #     close = data['close']
    # )

    layout = go.Layout(
        # autosize=True,
        # width = 800,
        # height=900,
        xaxis=dict(
            autorange=True
        ),
        yaxis=dict(
            autorange=True
        )
    )
    plot_data = [trace1]
    figure = go.Figure(data=plot_data, layout=layout)
    plot_div = plot(figure, output_type='div', include_plotlyjs=False)
    return plot_div


def get_topographical_3D_surface_plot():
    raw_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

    data = [go.Surface(z=raw_data.as_matrix())]

    layout = go.Layout(

        autosize=False,
        width=800,
        height=700,
        margin=dict(
            l=65,
            r=50,
            b=65,
            t=90
            )
        )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div',filename='elevations-3d-surface')

    return plot_div


def pie_chart():
    fig = {
  "data": [
    {
      "values": [16, 15, 12, 6, 5, 4, 42],
      "labels": [
        "US",
        "China",
        "European Union",
        "Russian Federation",
        "Brazil",
        "India",
        "Rest of World"
      ],
      "domain": {"column": 0},
      "name": "GHG Emissions",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },
    {
      "values": [27, 11, 25, 8, 1, 3, 25],
      "labels": [
        "US",
        "China",
        "European Union",
        "Russian Federation",
        "Brazil",
        "India",
        "Rest of World"
      ],
      "text":["CO2"],
      "textposition":"inside",
      "domain": {"column": 1},
      "name": "CO2 Emissions",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    }],
  "layout": {
        "title":"Global Emissions 1990-2011",
        "grid": {"rows": 1, "columns": 2},
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "GHG",
                "x": 0.20,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "CO2",
                "x": 0.8,
                "y": 0.5
            }
        ]
    }
}

    plot_div = plot(fig, output_type='div',filename='donut')
    return plot_div
