/*SQL: 
problem: Write a SQL query to find employees who earn the top three salaries in each of the department. 
author: Yanchun Stanley 
upload date: 06/16/2019*/

SELECT Department
,Employee
,Salary
FROM
(SELECT d.Name as 'Department'
,e.Name as 'Employee'
,e.Salary
,dense_rank() over (partition by d.Id order by e.Salary DESC) as 'rank'
FROM Employee e 
INNER JOIN Department d
on e.DepartmentId = d.Id) as tbl
WHERE rank <=3
