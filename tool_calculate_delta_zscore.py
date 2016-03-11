"""
Provide tool binding to add and calculate zscore functionality in summary utilities.
"""
# import just what we need to speed up tool loading
from summary_utilities import calculate_delta_zscore
from arcpy import GetParameterAsText

# run the function
calculate_delta_zscore(
    table=GetParameterAsText(0),
    data_field_one=GetParameterAsText(1),
    data_field_two=GetParameterAsText(2),
    delta_field=GetParameterAsText(3),
    zscore_field=GetParameterAsText(4)
)
