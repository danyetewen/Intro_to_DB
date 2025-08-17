-- Switch to the alx_book_store database
USE alx_book_store;

-- Print full description of the books table
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'books'
  AND TABLE_SCHEMA = 'alx_book_store';
