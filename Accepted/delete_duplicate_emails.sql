-- https://leetcode.com/problems/delete-duplicate-emails/


DELETE P1
FROM Person P1, Person P2
WHERE P1.Email = P2.Email
AND P1.Id > P2.Id
;


-- In mysql we can't updating a table while select from the same table.
-- So we have to select from a wrapped table instead.
-- Besides, this is much faster than the above solution.
DELETE FROM Person
WHERE Id NOT IN
(
    SELECT *
    FROM
    (
        SELECT MIN(Id) AS Id
        FROM Person
        GROUP BY Email
    ) TEMP
)