import os
import glob
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.colors as pc
from plotly.subplots import make_subplots
import warnings

# Column names
INFECTIONS_COL = 'Infections'
INFECTIONS_LABEL = 'New daily infections'
STRINGENCY_COL = 'Stringency'
STRINGENCY_LABEL = 'Daily stringency of interventions'
PRESCRIPTION = 'PrescriptionIndex'

# Set the colors of the background and grid
PLAIN_LAYOUT = dict(
    plot_bgcolor='white',
    font=dict(color='dimgray', family='Balto, Gravitas One, Arial'),
    xaxis=dict(showline=True, linewidth=1, linecolor='dimgray', zerolinecolor='lightgray',
               gridcolor='lightgray'),
    yaxis=dict(showline=True, linewidth=1, linecolor='dimgray', zerolinecolor='lightgray',
               gridcolor='lightgray'),
    # For 3-D plots
    scene=dict(
        xaxis=dict(showline=True, linewidth=1, linecolor='dimgray', zerolinecolor='lightgray',
                   gridcolor='lightgray', backgroundcolor='white'),
        yaxis=dict(showline=True, linewidth=1, linecolor='dimgray', zerolinecolor='lightgray',
                   gridcolor='lightgray', backgroundcolor='white'),
        zaxis=dict(showline=True, linewidth=1, linecolor='dimgray', zerolinecolor='lightgray',
                   gridcolor='lightgray', backgroundcolor='white'),
    )
)

# Set the color of the discrete traces
COLORS_DISCRETE = px.colors.qualitative.Bold[:10]
COLORS_MAP = {'Plan {}'.format(i + 1): c for i, c in enumerate(COLORS_DISCRETE)}
COLORS_MAP.update({
    'All min': '#919191',
    'All mid': '#5e5e5e',
    'All max': '#303030',
    'Current': '#cc6699',
    'Implemented plan': '#303030'
})
# Set continuous colors
COLORS_SEQUENTIAL = px.colors.sequential.Sunsetdark

# List of all the policies
POLICIES = ['C1_School closing', 'C2_Workplace closing', 'C3_Cancel public events',
            'C4_Restrictions on gatherings', 'C5_Close public transport',
            'C6_Stay at home requirements', 'C7_Restrictions on internal movement',
            'C8_International travel controls', 'H1_Public information campaigns',
            'H2_Testing policy', 'H3_Contact tracing', 'H6_Facial Coverings']


def get_rgb_color(color):
    """
    Returns the color in RGB form (r, g, b), where r, g, b are from [0, 1] from color written
    either in RGB form (R, G, B), where R, G, B are from [0, 255] or in hex form.
    """
    if '#' in color:
        return pc.unconvert_from_RGB_255(pc.hex_to_rgb(color))
    else:
        return pc.unconvert_from_RGB_255(pc.unlabel_rgb(color))


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


def get_hex_color(color):
    """
    Returns the color in HEX from from the RGB form (r, g, b), where r, g, b are from [0, 1].
    """
    return '#' + ''.join(['{:02X}'.format(int(round(255 * x))) for x in color])


def get_intermediate_colors(start_color='#ffffff', end_color='#000000', num_colors=5):
    """
    Returns a list of intermediate colors between the input colors. The input colors are given in
    HEX form, while the result is in the RGB form (r, g, b), where r, g, b are from [0, 1].
    """
    start_color = get_rgb_color(start_color)
    end_color = get_rgb_color(end_color)
    values = np.linspace(0, 1, num_colors)
    # find_intermediate_color requires input in form (r, g, b), where r, g, b are from [0, 1]
    return [pc.find_intermediate_color(start_color, end_color, x) for x in values]


def get_discrete_sequential_colors(color=COLORS_DISCRETE[0], num_colors=5):
    """
    Returns a list of sequential colors from white to color that contains num_colors. Colors
    correspond to values in [0, 1].
    """
    intermediate_colors = get_intermediate_colors(end_color=color, num_colors=num_colors)
    sequential_colors = []
    values = np.linspace(0, 1, num_colors + 1)
    for i in range(num_colors):
        sequential_colors.extend([[values[i], intermediate_colors[i]],
                                  [values[i + 1], intermediate_colors[i]]])
    sequential_colors = pc.convert_colorscale_to_rgb(sequential_colors)
    return sequential_colors


def get_discrete_diverging_colors(color_1=COLORS_DISCRETE[0],
                                  color_2=COLORS_DISCRETE[1], num_colors=5):
    """
    Returns a list of diverging colors with white in the middle that contains 2 * num_colors - 1
    colors. Colors correspond to values in [0, 1].
    """
    intermediate_colors_1 = get_intermediate_colors(end_color=color_1, num_colors=num_colors)
    intermediate_colors_2 = get_intermediate_colors(end_color=color_2, num_colors=num_colors)
    all_colors = intermediate_colors_2[::-1][:-1] + intermediate_colors_1
    diverging_colors = []
    values = np.linspace(0, 1, 2 * num_colors)
    for i in range(2 * num_colors - 1):
        diverging_colors.extend([[values[i], all_colors[i]], [values[i + 1], all_colors[i]]])
    diverging_colors = pc.convert_colorscale_to_rgb(diverging_colors)
    return diverging_colors


def get_policies():
    """
    Returns a DataFrame with information about policies.
    """
    policies_max = [3, 3, 2, 4, 2, 3, 2, 4, 2, 3, 2, 4]
    return pd.DataFrame(index=POLICIES, data=policies_max, columns=['Max'])


def add_country(df):
    """
    Returns the DataFrame with an additional 'Country' column (constructed from CountryName and
    RegionName).
    """
    if 'Country' not in df.columns:
        df['Country'] = df.apply(
            lambda x: '{}{}'.format(x['CountryName'],
                                    '' if pd.isnull(x['RegionName']) else
                                    ': {}'.format(x['RegionName'])), axis=1)
    return df


def plot_objectives(df, infections_col='Infections', stringency_col='Stringency',
                    infections_label='Average infections', stringency_label='Average stringency',
                    prescription='PrescriptionIndex', title='Average infections vs. stringency',
                    layout_dict=None):
    """
    Plots the two objectives (infections and stringency index) for each of the plans in the data.
    Assumes the input DataFrame contains only one country.
    """
    try:
        assert len(df['Country'].unique()) == 1
        df_mean = df.groupby([prescription])[[infections_col, stringency_col]].mean()
        df_mean.reset_index(inplace=True)
        df_mean[prescription] = df_mean[prescription].astype(str)
        fig = px.scatter(
            df_mean,
            x=stringency_col,
            y=infections_col,
            labels={infections_col: infections_label,
                    stringency_col: stringency_label},
            color=prescription,
            color_discrete_map=COLORS_MAP,
            text=prescription,
            title=title,
            hover_data={prescription: False}
        )
        fig.for_each_trace(
            lambda t: t.update(textfont_color=t.marker.color, customdata=[t.marker.color],
                               textposition='top center'))
        fig.update_traces(cliponaxis=False)
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))
        fig.update_layout(showlegend=False, hovermode='closest')
        fig.update_layout(**PLAIN_LAYOUT)
        if layout_dict is not None:
            fig.update_layout(**layout_dict)
        return fig
    except Exception as e:
        warnings.warn('Plot not produced due to error: {}'.format(e), RuntimeWarning)
        return []


def plot_objective_together(df, objective_col='Infections', objective_label='Infections',
                            prescription='PrescriptionIndex', hover_decimals=False,
                            title='Infections', layout_dict=None):
    """
    Plot objective over time for the given country on the same plot for all plans.
    Assumes the input DataFrame contains only one country.
    """
    try:
        assert len(df['Country'].unique()) == 1
        fig = px.line(
            df,
            x='Date',
            y=objective_col,
            labels={objective_col: objective_label, prescription: 'Plan'},
            color=prescription,
            color_discrete_map=COLORS_MAP,
            title=title,
            hover_data={'Country': False, 'Date': False}
        )
        fig.update_layout(xaxis=dict(title=''), yaxis=dict(title=''), showlegend=True)
        fig.update_layout(hovermode='x')
        fig.update_layout(**PLAIN_LAYOUT)
        if layout_dict is not None:
            fig.update_layout(**layout_dict)
        # Compact hover labels
        fig.for_each_trace(lambda trace: trace.update(
            customdata=[trace.name] * len(trace.y),
            hovertemplate='%{customdata}: %{y:,.2f}<extra></extra>' if hover_decimals else
            '%{customdata}: %{y:,.0f}<extra></extra>'
        ))
        return fig
    except Exception as e:
        warnings.warn('Plot not produced due to error: {}'.format(e), RuntimeWarning)
        return []


def plot_policy_heatmap(df, policies_df, plan='Plan 1', plan_color=None, title='Plan 1',
                        prescription='PrescriptionIndex', layout_dict=None):
    """
    Plot plan over time as a heatmap for the given country.
    Assumes the input DataFrame contains only one country.
    """
    try:
        assert len(df['Country'].unique()) == 1
        df = df[df[prescription] == plan]
        policies = list(policies_df.index.values)
        # Colors
        colorscale = get_discrete_sequential_colors(
            color=COLORS_MAP[plan] if plan_color is None else plan_color, num_colors=5)
        ticks = np.linspace(0, 4, 5)
        colorbar = dict(thickness=20,
                        tickvals=ticks * 4 / 5 + 2 / 5,
                        ticktext=['{:.0f}'.format(t) for t in ticks],
                        outlinecolor='black',
                        outlinewidth=0.5)
        # Settings for both heatmaps
        settings = dict(
            colorscale=colorscale,
            colorbar=colorbar,
            zmin=0,
            zmax=4
        )
        # Prescription by day heatmap
        data = go.Heatmap(
            z=df[policies],
            x=df['Date'],
            y=policies,
            hovertemplate='%{x}<br>%{y}<br>Level=%{z}<extra></extra>',
            transpose=True,
            **settings
        )
        # Max level heatmap
        data_max = go.Heatmap(
            z=[policies_df['Max'].values],
            x=['Max'],
            y=policies,
            hovertemplate='%{y}<br>Max level=%{z}<extra></extra>',
            transpose=True,
            **settings
        )
        fig = make_subplots(rows=1, cols=2, column_widths=[0.05, 0.95],
                            shared_yaxes=True, horizontal_spacing=0.01)
        fig.add_trace(data_max, row=1, col=1)
        fig.add_trace(data, row=1, col=2)
        fig.update_xaxes(fixedrange=True, row=1, col=1, mirror='allticks', side='top')
        fig.update_yaxes(fixedrange=True, row=1, col=1)
        fig.update_xaxes(fixedrange=True, row=1, col=2)
        fig.update_yaxes(fixedrange=True, row=1, col=2)
        fig.update_layout(yaxis=dict(autorange='reversed'))
        fig.update_layout(plot_bgcolor='white', title=title)
        fig.update_layout(**PLAIN_LAYOUT)
        # Overwrite plain_layout setting that shows axes
        fig.update_layout(xaxis=dict(showline=False), yaxis=dict(showline=False))
        if layout_dict is not None:
            fig.update_layout(**layout_dict)
        return fig
    except Exception as e:
        warnings.warn('Plot not produced due to error: {}'.format(e), RuntimeWarning)
        return []


def get_country_date_string(country, date):
    return '{}, {}-{}-{}'.format(country, date[:4], date[4:6], date[6:8])


def plot_data(path_in, path_out):
    """Creates plots (objective space, infections, stringency, heatmaps for each plan) in the output
    path for all files in the input path.
    Returns a DataFrame containing information about this data.
    """
    info_df = pd.DataFrame(columns=['country', 'category', 'weights', 'start', 'plan'])
    for file_in in glob.glob(os.path.join(path_in, '*.csv')):
        print(f'Working on {file_in}')
        df = pd.read_csv(file_in, sep=',')
        add_country(df)
        info = {
            'country': None,
            'category': None,
            'weights': None,
            'start': None
        }
        for string in os.path.basename(file_in).split('.csv')[0].split('_'):
            key, value = string.split('-')
            info.update({key: value})
        stringency_label = STRINGENCY_LABEL
        # Special case when the stringency is computed from the GDP
        if info['weights'] == 'gdp':
            stringency_label = 'GDP loss [%]'
            df[STRINGENCY_COL] *= 100
        file_name = os.path.join(
            path_out, 'country-{}-{}_category-{}_weights-{}_viz-XXX.png'.format(
                info['country'].lower().replace(' ', ''), info['start'], info['category'],
                info['weights']))
        title_info = '{}, cat. {}, {} weights'.format(
            get_country_date_string(info['country'], info['start']),
            info['category'].replace('m', '-'), info['weights'].replace('gdp', 'GDP')
        )
        # Plot of the objective space
        fig_obj = plot_objectives(
            df, infections_col=INFECTIONS_COL, prescription=PRESCRIPTION,
            stringency_col=STRINGENCY_COL, infections_label=INFECTIONS_LABEL + ' (avg)',
            stringency_label=stringency_label + ' (avg)',
            title='{}<br><sup>{}</sup>'.format('Average infections vs. stringency', title_info)
        )
        fig_obj.write_image(file_name.replace('XXX', 'objectives'))
        # Infections
        fig_inf = plot_objective_together(
            df, objective_col=INFECTIONS_COL, objective_label=INFECTIONS_LABEL,
            prescription=PRESCRIPTION,
            title='{}<br><sup>{}</sup>'.format(INFECTIONS_LABEL, title_info))
        fig_inf.write_image(file_name.replace('XXX', 'infections'))
        # Stringency
        fig_str = plot_objective_together(
            df, objective_col=STRINGENCY_COL, objective_label=stringency_label,
            prescription=PRESCRIPTION,
            title='{}<br><sup>{}</sup>'.format(stringency_label, title_info))
        fig_str.write_image(file_name.replace('XXX', 'stringency'))
        # Separate plans
        policies_df = get_policies()
        plans = df[PRESCRIPTION].unique()
        for plan in plans:
            fig = plot_policy_heatmap(
                df, policies_df, plan=plan, prescription=PRESCRIPTION,
                title='{}<br><sup>{}</sup>'.format(plan, title_info))
            info.update({'plan': plan.lower().replace(' ', '')})
            fig.write_image(file_name.replace('XXX', info['plan']))
            info_df.loc[len(info_df)] = info
    return info_df


def save_data_js(df, file_name):
    """Creates a JavaScript file with information about the data from the input DataFrame. """
    df['country-date'] = df[['country', 'start']].apply(
        lambda x: '{}-{}'.format(str(x[0]).lower().replace(' ', ''), x[1]), axis=1)
    countries = df['country'].unique()
    categories = df['category'].unique()
    plans = df['plan'].unique()
    category_order = ['m2', 'm1', '0', '1', '2']
    with open(file_name, 'w') as f:
        f.write('/******************************/\n')
        f.write('/* Automatically created file */\n')
        f.write('/******************************/\n')
        f.write('\n/* Countries */\n')
        f.write('var namesCou = [\n')
        for country in countries:
            f.write(f'\t"{country}",\n')
        f.write('];\n')
        f.write('var valuesCou = [\n')
        for country in countries:
            f.write('\t"{}",\n'.format(country.lower().replace(' ', '')))
        f.write('];\n')
        f.write('\n/* Categories */\n')
        f.write('var namesCat = [\n')
        # Make sure the categories are sorted correctly
        for category in category_order:
            if category in categories:
                f.write('\t"{}",\n'.format(category.replace('m', '-')))
        f.write('];\n')
        f.write('var valuesCat = [\n')
        # Make sure the categories are sorted correctly
        for category in category_order:
            if category in categories:
                f.write(f'\t"{category}",\n')
        f.write('];\n')
        f.write('\n/* Plans */\n')
        f.write('var plans = [\n')
        for plan in plans:
            f.write(f'\t"{plan}",\n')
        f.write('];\n')
        f.write('\n/* Not all categories are available for all countries */\n')
        f.write('var couCat = {\n')
        for country in countries:
            f.write('\t"{}": [\n'.format(country.lower().replace(' ', '')))
            df_country = df[df['country'] == country]
            for category in category_order:
                if category in df_country['category'].unique():
                    df_category = df_country[df_country['category'] == category]
                    for date in df_category['start'].unique():
                        f.write('\t\t"country-{}-{}_category-{}",\n'.format(
                            country.lower().replace(' ', ''),
                            date,
                            category
                        ))
            f.write('\t],\n')
        f.write('};\n')
        f.write('\n/* Not all countries are available for all categories */\n')
        f.write('var catCou = {\n')
        for category in category_order:
            if category in df['category'].unique():
                f.write('\t"{}": [\n'.format(category))
                df_category = df[df['category'] == category]
                for country in countries:
                    df_country = df_category[df_category['country'] == country]
                    for date in df_country['start'].unique():
                        f.write('\t\t"country-{}-{}_category-{}",\n'.format(
                            country.lower().replace(' ', ''),
                            date,
                            category
                        ))
                f.write('\t],\n')
        f.write('};\n')


if __name__ == '__main__':
    input_folder = os.path.join('..', 'data')
    output_folder = os.path.join('..', 'assets', 'img', 'plots')
    data = plot_data(path_in=input_folder, path_out=output_folder)
    save_data_js(data, os.path.join('..', 'assets', 'js', 'data.js'))
