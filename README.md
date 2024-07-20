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

反正規化 (視情況使用), 正規化可以讓每一張table減少資料的重複和提高數據的完整性, 但其實會讓每一次訪問的速度下降 (目前經驗大都只使用到二階正規化)  

### API 實作測驗  
本測驗使用的是DRF做為基底, 設計模式為REST API, SOLID原則皆符合  
  
以下為unit test結果  

--- 成功 ---  
![image](https://github.com/user-attachments/assets/6ebeb955-5428-43b8-98c9-4ee9e7736f13)  
  
  
--- 失敗  name 包含了英文以外的字 ---  
![image](https://github.com/user-attachments/assets/be22a75b-e2c2-4688-8534-3181f3c47d32)    
  
  
--- 失敗 name 首字沒有大寫 ---  
![image](https://github.com/user-attachments/assets/d5ca2286-772c-4293-bf93-02b253889318)  
  
  
--- 失敗 price 超過2000 ---  
![image](https://github.com/user-attachments/assets/5d88ef82-7cba-4ac1-b1be-f13616a901d2)  
  
  
--- 失敗 currency 格式錯誤 ---  
![image](https://github.com/user-attachments/assets/3f433a1a-2870-4d1a-8f7a-4e24f7e26568)  
  


