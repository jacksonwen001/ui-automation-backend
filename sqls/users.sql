 CREATE TABLE IF NOT EXISTS (
  `id` BIGINT PRIMARY KEY AUTO INCREMENT, 
  `email` VARCHAR(100) NOT NULL,
  `hashed_password` VARCHAR(500), 
  `is_active` INT DEFAULT 0
 )
