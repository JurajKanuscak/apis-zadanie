SELECT * FROM Author;
SELECT Title, ISBN, Year, Price, Pages, BookDesc, BookLink, AuthorName, CategoryDesc FROM Book JOIN Author_Book ON (Book.idBook = Author_Book.idBook) JOIN Author ON (Author_Book.idAuthor = Author.idAuthor) JOIN Category ON (Book.idCategory = Category.idCategory);
SELECT * FROM Category;
SELECT * FROM Customer;
SELECT Orders.idOrder, OrderDate, Orders.Price, Title FROM Orders JOIN Book_Order ON (Orders.idOrder = Book_Order.idOrder) JOIN Book ON (Book_Order.idBook = Book.idBook);
SELECT * FROM Orders WHERE idCustomer={} AND OrderDate="{}" AND Price="{}";
