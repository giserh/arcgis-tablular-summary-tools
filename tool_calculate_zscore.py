"""
Provide tool binding to calculate zscore functionality in summary utilities.
"""
# import just what we need to speed up tool loading
from summary_utilities import calculate_zscore
from arcpy import GetParameterAsText

# run the function
calculate_zscore(
    table=GetParameterAsText(0),
    data_field=GetParameterAsText(1),
    zscore_field=GetParameterAsText(2)
)
