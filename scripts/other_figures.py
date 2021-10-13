import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.colors as pc
import warnings
from visualize_plan import COLORS_DISCRETE, PLAIN_LAYOUT
from datetime import datetime, timedelta


LABEL_X = 'Time (number of days)'
MARGIN_LEFT = 38
MARGIN_DEFAULT = 80


def get_rgba_color(color, alpha):
    """
    Returns the color in RGBA form rgba(R, G, B, A), where R, G, B are from [0, 255] and A is from
    [0, 1].
    """
    if '#' in color:
        rgb_255 = pc.hex_to_rgb(color)
    elif 'rgb(' in color:
        rgb_255 = pc.unlabel_rgb(color)
    else:
        rgb_255 = color
    return 'rgba({}, {}, {}, {})'.format(rgb_255[0], rgb_255[1], rgb_255[2], alpha)


def plot_lines(df, title='', x_label='', y_label='', line_dash=None, legend_dict=None,
               colors=COLORS_DISCRETE, layout_dict=None):
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
            color_discrete_sequence=colors,
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


def plot_error_distribution(input_folder, output_folder, ending='png'):
    file_name = 'Error'
    file_data = os.path.join(input_folder, f'{file_name}.csv')
    file_plot = os.path.join(output_folder, f'{file_name}.{ending}')
    # Read data
    df = pd.read_csv(file_data, sep=',')
    title = 'Relative error distribution for the fitted SEIRD model'
    # Make the plot
    fig = px.violin(df, x='Error', box=True, color_discrete_sequence=COLORS_DISCRETE, title=title,
                    labels={'Error': 'Relative error'},)
    fig.update_layout(**PLAIN_LAYOUT)
    fig.update_layout(margin=dict(l=MARGIN_LEFT, r=MARGIN_LEFT))
    fig.write_image(file_plot)


def plot_prediction(input_folder, output_folder, country, ending='png'):
    file_name = f'Prediction-{country}'
    file_data = os.path.join(input_folder, f'{file_name}.csv')
    file_plot = os.path.join(output_folder, f'{file_name}.{ending}')
    # Read data
    df = pd.read_csv(file_data, sep=',')
    # Add info about dates
    start_date = datetime.strptime('2020-01-13', '%Y-%m-%d')
    if country == 'Norway':
        start_date = datetime.strptime('2020-08-16', '%Y-%m-%d')
    df.drop(columns=['x'], inplace=True)
    df['x'] = [start_date + timedelta(days=i) for i in range(len(df))]
    df = pd.melt(df, id_vars=['x'], var_name='name', value_name='y')
    title = f'New daily infections<br><sup>{country}</sup>'
    # Make the plot
    colors = COLORS_DISCRETE
    if country == 'Norway':
        # Switch colors to ease differentiation
        colors[2] = COLORS_DISCRETE[3]
        colors[3] = COLORS_DISCRETE[2]
    fig = plot_lines(df, title=title, x_label='', y_label='', colors=colors)
    if country == 'Norway':
        change_date = start_date + timedelta(days=40)
        fig.add_shape(
            type='line',
            x0=change_date, y0=0, x1=change_date, y1=900,
            line=dict(color='gray', width=2))
        fig.add_annotation(
            x=change_date, y=900,
            xshift=5, yshift=-10,
            text='NPI change',
            showarrow=False,
            xanchor='left',
            font=dict(color='gray'))
    if country == 'Italy':
        y_min = -2e3
        y_max = 37e3
        file_name_splits = f'Prediction-Italy-splits'
        file_data_splits = os.path.join(input_folder, f'{file_name_splits}.csv')
        splits = pd.read_csv(file_data_splits, sep=',')['Splits with delay'].values
        splits_dates = [start_date + timedelta(days=int(split)) for split in splits]
        for i, split in enumerate(splits_dates):
            fig.add_traces([
                go.Scatter(
                    x=[split] * 2,
                    y=[y_min, y_max],
                    line=dict(color='gray', dash='dot'),
                    name='Splits',
                    mode='lines',
                    showlegend=(i == 0)
                )
            ])
        fig.update_layout(yaxis_range=[y_min, y_max])
    fig.write_image(file_plot)


def plot_methods(input_folder, output_folder, file_name, title, ending='png'):
    file_data = os.path.join(input_folder, f'{file_name}.csv')
    file_plot = os.path.join(output_folder, f'{file_name}.{ending}')
    # Read data
    df = pd.read_csv(file_data, sep=',')
    df = pd.melt(df, id_vars=['x'], var_name='name', value_name='y')
    title = f'{title}<br><sup>Predicted daily infections normalized by population</sup>'
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
    fig.for_each_trace(lambda t: t.update(name=t.name.split(",")[0]))
    fig.write_image(file_plot, width=900)  # Default width = 700, height = 500


def plot_coefficients(input_folder, output_folder, ending):
    file_name = 'Coefficients'
    file_data = os.path.join(input_folder, f'{file_name}.csv')
    file_plot = os.path.join(output_folder, f'{file_name}.{ending}')
    # Read data
    df = pd.read_csv(file_data, sep=',')
    # Make the plot
    fig = px.bar(df, x='Coefficient', y='NPI', orientation='h',
                 color_discrete_sequence=COLORS_DISCRETE,
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
    fig.update_layout(xaxis=dict(title=''),
                      yaxis=dict(title='', side='right', autorange='reversed'))
    fig.update_layout(**PLAIN_LAYOUT)
    fig.update_layout(margin=dict(r=0, b=0))
    fig.write_image(file_plot)


def remove_repeating_lines(file_name):
    print(f'Removing repeated lines from {file_name}')
    df = pd.read_csv(file_name, sep=',')
    last = df.iloc[-1]
    columns = df.columns.tolist()
    columns.remove('x')
    df.drop_duplicates(subset=columns, keep='first', inplace=True)
    df = df.append(last)
    if 'Granularity' in file_name:
        df = df[['x', '1', '3', '7', '14', '30',
                 '1 stdev', '3 stdev', '7 stdev', '14 stdev', '30 stdev']]
    df.to_csv(file_name, sep=',', index=None)


def plot_convergence(input_folder, output_folder, file_name, ending='png', plot_stdev=False):
    file_data = os.path.join(input_folder, f'{file_name}.csv')
    file_plot = os.path.join(output_folder, f'{file_name}.{ending}')
    # Read data
    df = pd.read_csv(file_data, sep=',')
    data_columns = [col for col in df.columns if ('stdev' not in col) and (col != 'x')]
    df_mean = df[['x'] + data_columns]
    df_mean = pd.melt(df_mean, id_vars=['x'], var_name='name', value_name='y')
    title = f'Hypervolume values for different {file_name.lower()}'
    title += '<br><sup>Areas denote the mean +/- standard deviation</sup>'
    legend_dict = dict(yanchor='bottom', y=0, xanchor='right', x=1, title=file_name)
    # Plot mean values
    colors = COLORS_DISCRETE
    if 'Granularity' in file_name:
        colors = px.colors.sequential.Plasma[::2][::-1]
    fig = plot_lines(df_mean, title=title, x_label='Number of evaluations', y_label='',
                     colors=colors, legend_dict=legend_dict)
    if plot_stdev:
        # Add standard deviation
        used_colors = [data['line']['color'] for data in fig.data]
        for col in data_columns:
            df[f'{col} upper'] = df[col] + df[f'{col} stdev']
            df[f'{col} lower'] = df[col] - df[f'{col} stdev']
        fig_stdev = go.Figure([
            go.Scatter(
                x=df['x'].tolist() + df['x'].tolist()[::-1],  # x, then x reversed
                y=df[f'{col} upper'].tolist() + df[f'{col} lower'].tolist()[::-1],
                # upper, then lower reversed
                fill='toself',
                line=dict(color='rgba(255,255,255,0)'),  # Transparent line
                fillcolor=get_rgba_color(used_colors[i], alpha=0.2),
                showlegend=False
            )
            for i, col in enumerate(data_columns)
        ])
        for i in range(len(data_columns)):
            fig.add_trace(fig_stdev.data[i])
    fig.update_xaxes(type='log')
    fig.write_image(file_plot)


def make_all_plots(input_folder, output_folder, ending='png'):
    plot_convergence(input_folder, output_folder, 'Granularity', ending)
    plot_convergence(input_folder, output_folder, 'Representations', ending)
    plot_error_distribution(input_folder, output_folder, ending)
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
    # remove_repeating_lines(os.path.join(in_folder, 'Granularity.csv'))
    # remove_repeating_lines(os.path.join(in_folder, 'Representations.csv'))
    make_all_plots(in_folder, out_folder, ending='png')
    make_all_plots(in_folder, out_folder, ending='pdf')
