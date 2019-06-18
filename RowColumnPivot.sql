   

/* SQL

problem: Change row values to coloumn header using MSSQL Pivot 

author: Yanchun Stanley

upload date: 06/18/2019*/


SELECT StudentId
,Math as 'Math'
,English as 'English'
,Score
FROM
  (SELECT StudendID
    ,Score
    ,Class
   FROM Score) p
 PIVOT
  (SELECT MAX(Score) FOR Class in ('Math','English')) as pvt
 ORDER by pvt.StudendId
