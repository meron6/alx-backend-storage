-- Task 8: Optimize simple search - create an index called idx_name_first
-- on the 'names' table for the first letter of the 'name' column
CREATE INDEX idx_name_first ON names (name(1));
