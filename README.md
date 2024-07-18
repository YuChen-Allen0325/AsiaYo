### 資料庫測驗

解一:

SELECT
    o.bnb_id,
    b.name as bnb_name,
    SUM(o.amount) as may_amount
FROM
    bnbs as b
JOIN
    orders as o ON b.id = o.bnb_id
WHERE
    o.created_at >= '2024-05-01' AND o.created_at <= '2024-05-31' AND o.currency = 'TWD'
GROUP BY
    o.bnb_id
ORDER BY
    may_amount DESC
LIMIT 10;


解二:

對於常SELECT ,JOIN 及 WHERE使用到的欄位添加INDEX , 添加INDEX可以讓 "R" 的速度加速, 不過會讓 "CUD" 的速度變慢, 每一次的操作都要遵照原先的INDEX, 所以在做 "CUD" 時都是需要在做重新排序的

水平分區, 過舊的資料是可以切去別張table, 並藉由API進行判斷要訪問的對象table, 訂單類跟存log都是大量record存於一張table之中

資料表分區 (尚無此經驗)

