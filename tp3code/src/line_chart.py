'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.
    fig = px.scatter()   # Utiliser un scatter comme base pour une figure vide
    
    
    
    # For information text to the figure
    fig.add_annotation(
        text='No data to display. Select a cell in the heatmap for more information.',
        x=0.5, y=0.5,
        xanchor='center', yanchor='middle',
        showarrow=False,
        font=dict(
            family=THEME['font_family'],
            size=14,
            color=THEME['dark_color']
        )
    )
    
    # Pour cacher les axes et les étiquettes des ticks
    fig.update_xaxes(visible=False, showticklabels=False)
    fig.update_yaxes(visible=False, showticklabels=False)
    
    # Définir la mise en page pour désactiver le mode de glissement et appliquer les couleurs
    fig.update_layout(
        dragmode=False, # Désactivation du mode de glissement
        paper_bcolor=THEME['background_color'], # Couleur de fond de la figure (papier)
        plot_bgcolor=THEME['background_color'] # Couleur de fond de la zone de tracé
    )
    
    return fig
    



def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    # TODO : Draw the rectangle
    # Ajout du rectangle à la figure
    fig.add_shape(
        type="rect", #Définition du type de forme comme rectangle
        x0=0, y0=0.25, # Position au niveau du coin inférieur gauche (x=0 pour l'axe X, y=0.25 pour l'axe y)
        x1=1, y1=0.75, # Position du coin supérieur droit (x=1 pour prendre toute la largeur, y=0.75 pour la hauteur)
        xref="paper", yref="paper", # Utiliser les coordonnées relatives par rapport au papier
        fillcolor=THEME['pale_color'], # Pour remplir avec la couleur pale_color du dictionnaire THEME
        opacity=0.5, # Opacité du rectangle où que la transparence est de 0 à 1
        layer="below", # En vue que le rectangle sois sous le texte
        line=dict(width=0) # Aucun bord pour le rectangle    
    )
    
    return fig





def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    # TODO : Construct the required figure. Don't forget to include the hover template
    # Pour vérification si line_data est vide ou bien que la somme des 'Counts' soit également à zéro
    if line_data.empty or line_data['Counts'].sum() == 0:
        return get_empty_figure() # Ici on retourne une figure vide si absence de donnée
    
    # s'il y a présence seulement d'un point de données, on fera
    if len(line_data) == 1:
         fig = px.scatter(
             line_data,
             x='Date_Plantation',
             y='Counts',
             title = f"Trees planted in {arrond} - {year}"
             labels={'y': 'Trees'},
             color_discrete_sequence=['black']
        )
    
    else:
        # En cas de plusieurs points, on trace une ligne avec des marqueurs
        fig = px.line(
           line_data,
           x='Date_Plantation',
           y='Counts',
           title = f"Trees planted in {arrond} - {year}"
           labels={'y': 'Trees'},
           color_discrete_sequence=['black'] 
        )
        fig.update_traces(line_color='black')
    
    # Pour configurer les axes et layout
    fig.update_layout(
        xaxis=dict(
            tickformat="%d %b",
            title='' # Pas de titre à l'axe des x 
        ),
        dragmode=False
    )
         
    
    # Apply custom hover template
    fig.update_traces(
        hovertemplate=hover_template.get_linechart_hover_template()  # Use the specified hover template
    )
    
    return fig
