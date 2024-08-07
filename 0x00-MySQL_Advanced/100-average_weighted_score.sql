-- Task 12: Average Weighted Score - This task involves creating a stored procedure named ComputeAverageWeightedScoreForUser that calculates and stores the average weighted score for a student.
-- user_id, a value from users.id (it's assumed that user_id corresponds to an existing user)
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE w_avg_score FLOAT;
    SET w_avg_score = (SELECT SUM(score * weight) / SUM(weight)
                        FROM users U
                        INNER JOIN corrections C ON U.id = C.user_id
                        INNER JOIN projects P ON C.project_id = P.id
                        WHERE U.id = user_id);
    UPDATE users SET average_score = w_avg_score WHERE id = user_id;
END
$$
DELIMITER ;
