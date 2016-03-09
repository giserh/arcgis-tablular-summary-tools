# Tabular Summary Tools

Frequently when trying to derive information from data sets, it can be handy to have a measure of what the data is doing. Statistics provides the tools for doing this. With the release of ArcGIS 10.4, SciPy is included with the default Python installation. SciPy and the already included NumPy module together make deriving statistical information comparatively straightforward. This small repo takes advantage of this functionality with a toolbox tapping into this module.
 
## Tools
 
### Add and Calculate ZScores

Just like it sounds, this tool adds a new field to the table. Then, it calcuates the ZScore for each row based on a previously existing numeric field.

## Calculate ZScores

This tool calculates and populates a field with ZScores based on a previously existing field in the table.

# References

* [SciPy](http://www.scipy.org)
    * [SciPy Statistical ZScore](http://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.zscore.html)
* [NumPy](http://www.numpy.org)

