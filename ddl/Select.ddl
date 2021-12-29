SELECT * FROM Author;
SELECT * FROM Book;
SELECT * FROM Category;
SELECT * FROM Customer;
SELECT * FROM Orders;
SELECT Orders.idOrder, OrderDate, Orders.Price, Title FROM Orders
  JOIN Book_Order ON (Orders.idOrder = Book_Order.idOrder)
  JOIN Book ON (Book_Order.idBook = Book.idBook);
SELECT * FROM Author WHERE AuthorName="{}";
