CREATE TABLE IF NOT EXISTS `projects`(
  `id`          BINARY(36) PRIMARY KEY, 
  `name`        VARCHAR(50) NOT NULL UNIQUE, 
  `created_at`  DATETIME NOT NULL
)