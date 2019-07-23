### [Example of quantiles](https://www.bounteous.com/insights/2016/06/26/compute-quantiles-or-bucketingbinning/)
  ```
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
