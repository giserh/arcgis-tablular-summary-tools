"""
Provide tool binding to add and calculate zscore functionality in summary utilities.
"""
# import just what we need to speed up tool loading
from summary_utilities import add_calculate_delta_zscore
from arcpy import GetParameterAsText

# run the function
add_calculate_delta_zscore(
    table=GetParameterAsText(0),
    data_field_one=GetParameterAsText(1),
    data_field_two=GetParameterAsText(2),
    delta_field_name=GetParameterAsText(3),
    delta_field_alias=GetParameterAsText(4),
    zscore_field_name=GetParameterAsText(5),
    zscore_field_alias=GetParameterAsText(6)
)
