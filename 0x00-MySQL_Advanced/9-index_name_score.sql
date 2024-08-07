-- Task 9: Optimize search and score - this creates an index named idx_name_first_score on the table 'names'
-- that indexes the first letter of the 'name' field and the 'score' field
CREATE INDEX idx_name_first_score ON names (SUBSTRING(name FROM 1 FOR 1), score);
