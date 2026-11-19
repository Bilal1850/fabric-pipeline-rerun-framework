-- Bronze auto-rerun: identify tables that failed in the current batch for a source system
-- and fetch the metadata needed to re-copy them (used by the rerun Lookup activity).
SELECT  a.ItemName,
        a.Status,
        b.SourceSchema,
        b.SourceTable,
        b.SourceColumnList,
        b.TargetTable
FROM    [DataOpsWarehouse].[CFR].[TableActivityLogs]      AS a
LEFT JOIN [DataOpsWarehouse].[Metadata].[Src_Brn_Tbl_Lst] AS b
       ON a.SourceSystem = b.SourceSystem
WHERE   b.SourceSystem = 'ACH'
  AND   a.Status    = 'Failed'
  AND   BatchID     =  @{pipeline().parameters.BatchID}
  AND   BatchDate   = '@{pipeline().parameters.BatchDate}';
