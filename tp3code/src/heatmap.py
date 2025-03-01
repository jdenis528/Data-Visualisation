'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template


def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.
    fig = px.imshow(data,
                    labels=dict(x="Year", y="Neighbordhood"),
                    )
    
    
    
    
    
    
    
    
    
    
    
    
    
       fig = px.imshow(
        data,  # Data to display (assuming it's a 2D matrix or dataframe)
        labels=dict(x="Year", y="Neighborhood"),
        color_continuous_scale="Viridis",  # You can choose another color scale if needed
        title="Heatmap of Trees by Year and Neighborhood"
        
        
            # Set the color bar title
    fig.update_coloraxes(colorbar_title="Trees")

    # Add custom hover template (assuming hover_template is available)
    fig.update_traces(hovertemplate=hover_template.create_hover_template())  # Assuming this is a valid function
    
    # Customize layout
    fig.update_layout(
        dragmode=False,  # Disable drag mode
        xaxis=dict(tickmode='array', tickvals=list(range(len(data.columns))), ticktext=data.columns.tolist()),  # Set year labels as x-ticks
        yaxis=dict(tickmode='array', tickvals=list(range(len(data.index))), ticktext=data.index.tolist())  # Set neighborhood labels as y-ticks
    )

    return fig
    )


