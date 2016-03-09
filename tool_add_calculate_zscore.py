"""
Provide tool binding to add and calculate zscore functionality in summary utilities.
"""
# import just what we need to speed up tool loading
from summary_utilities import add_calculate_zscore
from arcpy import GetParameterAsText

# run the function
add_calculate_zscore(
    table=GetParameterAsText(0),
    data_field=GetParameterAsText(1),
    zscore_field_name=GetParameterAsText(2),
    zscore_field_alias=GetParameterAsText(3)
)
