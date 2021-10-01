import os
import glob
import re
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.colors as pc
from plotly.subplots import make_subplots
import warnings
from visualize_plan import COLORS_DISCRETE, PLAIN_LAYOUT


LABEL_X = 'Time (number of days)'


def plot_lines(df, title='', x_label='', y_label='', line_dash=None, legend_dict=None,
               layout_dict=None):
    """Creates a line plot for the given data frame.

    The data frame (df) should have columns 'x', 'y' that contain the data for the lines and 'name',
    which contains the label for the line.
    """
    try:
        fig = px.line(
            df,
            x='x',
            y='y',
            color='name',
            line_dash=line_dash,
            color_discrete_sequence=COLORS_DISCRETE,
            #category_orders='name',
            title=title,
        )
        fig.update_layout(xaxis=dict(title=x_label), yaxis=dict(title=y_label), showlegend=True)
        if legend_dict is not None:
            fig.update_layout(legend=legend_dict)
        else:
            fig.update_layout(legend=dict(yanchor='top', y=1, xanchor='left', x=0, title=None))
        fig.update_layout(**PLAIN_LAYOUT)
        if layout_dict is not None:
            fig.update_layout(**layout_dict)
        return fig
    except Exception as e:
        warnings.warn('Plot not produced due to error: {}'.format(e), RuntimeWarning)
        return []


def plot_prediction(input_folder, output_folder, country, ending='png'):
    file_name = f'Prediction-{country}'
    file_data = os.path.join(input_folder, f'{file_name}.csv')
    file_plot = os.path.join(output_folder, f'{file_name}.{ending}')
    # Read data
    df = pd.read_csv(file_data, sep=',')
    df = pd.melt(df, id_vars=['x'], var_name='name', value_name='y')
    title = f'New daily infections<br><sup>{country}</sup>'
    # Make the plot
    fig = plot_lines(df, title=title, x_label=LABEL_X, y_label='')
    if country == 'Norway':
        fig.add_shape(
            type='line',
            x0=40, y0=0, x1=40, y1=900,
            line=dict(color='gray', width=2))
        fig.add_annotation(
            x=40, y=900,
            xshift=5, yshift=-10,
            text='NPI change',
            showarrow=False,
            xanchor='left',
            font=dict(color='gray'))
    fig.write_image(file_plot)


def plot_methods(input_folder, output_folder, file_name, title, ending='png'):
    file_data = os.path.join(input_folder, f'{file_name}.csv')
    file_plot = os.path.join(output_folder, f'{file_name}.{ending}')
    # Read data
    df = pd.read_csv(file_data, sep=',')
    df = pd.melt(df, id_vars=['x'], var_name='name', value_name='y')
    title = f'{title}<br><sup>Normalized by population</sup>'
    # Make the plot
    fig = plot_lines(df, title=title, x_label=LABEL_X, y_label='')
    fig.write_image(file_plot)


def plot_npi_costs(input_folder, output_folder, ending='png'):
    file_name = 'NPI-costs'
    file_data = os.path.join(input_folder, f'{file_name}.csv')
    file_plot = os.path.join(output_folder, f'{file_name}.{ending}')
    # Read data
    df = pd.read_csv(file_data, sep=',')
    df = pd.melt(df, id_vars=['x'], var_name='name', value_name='y')
    title = 'NPI costs'
    legend_dict = dict(yanchor='top', y=1, xanchor='right', x=1, title=None)
    # Make the plot
    fig = plot_lines(df, title=title, x_label=LABEL_X, y_label='', legend_dict=legend_dict)
    fig.write_image(file_plot)


def plot_npi_intensity(input_folder, output_folder, ending='png'):
    file_name = 'NPI-intensity'
    file_data = os.path.join(input_folder, f'{file_name}.csv')
    file_plot = os.path.join(output_folder, f'{file_name}.{ending}')
    # Read data
    df = pd.read_csv(file_data, sep=',')
    df = pd.melt(df, id_vars=['x'], var_name='name', value_name='y')
    df['line_dash'] = 'solid'
    df.loc[df['name'].str.startswith('H'), 'line_dash'] = 'dash'
    title = 'NPI intensity'
    legend_dict = dict(title='')
    # Make the plot
    fig = plot_lines(df, title=title, x_label=LABEL_X, y_label='', line_dash='line_dash',
                     legend_dict=legend_dict)
    fig.write_image(file_plot, width=900)  # Default width = 700, height = 500


def plot_coefficients(input_folder, output_folder, ending):
    file_name = 'Coefficients'
    file_data = os.path.join(input_folder, f'{file_name}.csv')
    file_plot = os.path.join(output_folder, f'{file_name}.{ending}')
    # Read data
    df = pd.read_csv(file_data, sep=',')
    # Make the plot
    fig = px.bar(df, x='Coefficient', y='NPI', orientation='h',
                 title='NPI coefficients from the linear model')
    # Add annotations
    annotations = []
    for i in range(len(df)):
        annotations.append(dict(xref='paper', yref='y1',
                                y=i, x=-0.2,
                                text='{:.4f}'.format(df.loc[i, 'Coefficient']),
                                showarrow=False))
    fig.update_layout(annotations=annotations)
    # Adjust layout
    fig.update_layout(xaxis=dict(title=''), yaxis=dict(title='', side='right', autorange='reversed'))
    fig.update_layout(**PLAIN_LAYOUT)
    fig.write_image(file_plot)


def make_all_plots(input_folder, output_folder, ending='png'):
    plot_prediction(input_folder, output_folder, 'Italy', ending)
    plot_prediction(input_folder, output_folder, 'Norway', ending)
    plot_methods(input_folder, output_folder, 'Methods-a',
                 'Mean average error of HMLE variants', ending)
    plot_methods(input_folder, output_folder, 'Methods-b',
                 'Mean average error of HMLE classifiers', ending)
    plot_npi_costs(input_folder, output_folder, ending)
    plot_npi_intensity(input_folder, output_folder, ending)
    plot_coefficients(input_folder, output_folder, ending)


if __name__ == '__main__':
    in_folder = os.path.join('figure-data')
    out_folder = os.path.join('figure-data')
    make_all_plots(in_folder, out_folder, ending='png')
    make_all_plots(in_folder, out_folder, ending='pdf')
    # TODO Figure 2 & 3a: Talk to Nina
