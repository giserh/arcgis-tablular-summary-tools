"""
Provide tool binding to calculate zscore functionality in summary utilities.
"""
# import just what we need to speed up tool loading
from summary_utilities import calculate_percent_delta
from arcpy import GetParameterAsText

# run the function
calculate_percent_delta(
    table=GetParameterAsText(0),
    data_field_one=GetParameterAsText(1),
    data_field_two=GetParameterAsText(2),
    delta_field=GetParameterAsText(3)
)
