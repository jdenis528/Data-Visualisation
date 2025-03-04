'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip

    tooltip_template = '''
        <b>Country:</b> %{customdata[0]}<br>
        <b>Population:</b> %{customdata[1]}<br>
        <b>GDP:</b> %{customdata[2]} USD<br>
        <b>CO2 emissions:</b> %{customdata[3]} tons
    '''
    
    return tooltip_template
   
