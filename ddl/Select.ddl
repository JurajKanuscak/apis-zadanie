SELECT * FROM Author;
SELECT * FROM Book;
SELECT * FROM Category;
SELECT * FROM Customer;
SELECT * FROM Order;
SELECT Order.idOrder, OrderDate, Order.Price, Title FROM Order
  JOIN Book_Order ON (Order.idOrder = Book_Order.idOrder)
  JOIN Book ON (Book_Order.idBook = Book.idBook);
