/* SQL
problem: select the Nth highest salary
author: Yanchun Stanley
upload date: 06/16/2019*/

CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        SELECT distinct ISNULL(Salary, null) as NHighestSalary
        FROM (select dense_rank() over (order by Salary desc) as rank, salary from Employee) as ranksal
        WHERE rank =@N
                
    );
END
