### User defined function
Big query supports running user defined function, with a language as well. The example below show js but it can support C (?)
  ```sql
  CREATE TEMP FUNCTION convertToEqualBin(colV FLOAT64, minV FLOAT64, maxV FLOAT64, nBin FLOAT64)
  RETURNS STRING
  LANGUAGE js AS
    """
      const binWidth = (maxV - minV) / nBin
      var binLowVal = minV
      var binHighVal = minV + binWidth
      var binAsString = `[${binLowVal}, ${binHighVal})`
      while (colV >= binHighVal) {
        binLowVal = binHighVal
        binHighVal = binLowVal + binWidth
        binAsString = `[${binLowVal}, ${binHighVal})`
      }
      return binAsString
    """;
  ```

### Do equal width binning:
The function below before binning of column COL of table TAB:

  ```sql
  CREATE TEMP FUNCTION convertToEqualBin(colV FLOAT64, minV FLOAT64, maxV FLOAT64, nBin FLOAT64)
  RETURNS STRING
  LANGUAGE js AS
    """
    const binWidth = (maxV - minV) / nBin
    var binLowVal = minV
    var binHighVal = minV + binWidth
    var binAsString = `[${binLowVal.toFixed(2)}, ${binHighVal.toFixed(2)})`
    while (colV >= binHighVal) {
      binLowVal = binHighVal
      binHighVal = binLowVal + binWidth
      if (binHighVal == maxV){
        binAsString = `[${binLowVal.toFixed(2)}, ${binHighVal.toFixed(2)}]`
      }
      else {
        binAsString = `[${binLowVal.toFixed(2)}, ${binHighVal.toFixed(2)})`
      }
    }
    return binAsString
    """;
  WITH
      infos AS (
        SELECT
          customerId,
          firstDayOfMonth,
          COL,
          (SELECT MIN(COL) FROM `TAB`) minVal,
          (SELECT MAX(COL) FROM `TAB`) maxVal,
          (SELECT SQRT(COUNT(COL)) FROM `TAB`) nBin
        FROM `TAB`
        GROUP BY customerId, firstDayofMonth, COL
      )
  SELECT
    customerId,
    firstDayOfMonth,
    COL,
    convertToEqualBin(COL, minVal, maxVal, nBin) as binnedCOL
  FROM infos
  ORDER BY customerId asc, firstDayOfMonth desc
  ```


### [Example of quantiles](https://www.bounteous.com/insights/2016/06/26/compute-quantiles-or-bucketingbinning/)
  ```sql
  SELECT
    trafficSource.medium,
    SUM(totals.visits) AS sessions,
    -- 5 will give the min, 25%, 50%, 75%, max with 20% error
    -- the more buckets, the better the approximation (error = 1/number of buckets)
    -- at the cost of more computation
    -- QUANTILES returns all of the buckets, use NTH to extract the bucket you want
    NTH(2, QUANTILES(totals.timeOnSite, 5)) AS firstQuartile,
    NTH(3, QUANTILES(totals.timeOnSite, 5)) AS mean,
    NTH(3, QUANTILES(totals.timeOnSite, 5)) AS thirdQuartile
  FROM (
    SELECT
      trafficSource.medium,
      totals.visits,
      -- Sessions with a single page view will have no time on site reported
      IF(totals.timeOnSite IS NULL, 0, totals.timeOnSite) AS totals.timeOnSite
    FROM
      [google.com:analytics-bigquery:LondonCycleHelmet.ga_sessions_20130910])
  GROUP BY
    trafficSource.medium
  ```
