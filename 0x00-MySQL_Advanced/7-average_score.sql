-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Change the delimiter to allow for multiple statements in the procedure
DELIMITER $$

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    -- Declare a variable to hold the average score
    DECLARE avg_score FLOAT;

    -- Compute the average score for the specified user
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;

    -- Update the user's average score in the users table
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END$$

-- Reset the delimiter to the default
DELIMITER ;
