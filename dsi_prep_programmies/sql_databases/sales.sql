BEGIN;

DELETE FROM purchases;
DELETE FROM products;


INSERT INTO products (id, name, price) VALUES
  (9001, 'Electric Razor', 59.99),
  (9002, 'Turkey Jerky',  3.59),
  (9003,  'Paper Towels',  4.15),
  (9004, 'Straightrazor', 15.12),
  (9005, 'Barcelona Chair', 1579.00);


INSERT INTO purchases (id, custid, prodid, quantity, date) VALUES
  (5501, 1001, 9003, 3, '2017-01-03'),
  (5502, 1003, 9002, 1, '2017-02-05'),
  (5503, 1001, 9001, 3, '2017-03-10'),
  (5004, 1006, 9002, 1, '2017-03-11');

COMMIT;
