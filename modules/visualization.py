import plotly.express as px

class Visualizations:
    def bar(self, df, x, y, title="Bar Chart"):
        fig = px.bar(df, x=x, y=y, title=title)
        return fig
    
    def scatter(self, df, x, y, color=None, title="Scatter Plot"):
        fig = px.scatter(df, x=x, y=y, color=color, title=title)
        return fig
    
    def line(self, df, x, y, title="Line Chart"):
        fig = px.line(df, x=x, y=y, title=title)
        return fig