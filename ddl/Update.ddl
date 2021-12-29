UPDATE Author SET AuthorName = "{}" WHERE idAuthor = {};
UPDATE Book SET idCategory = {}, Title = "{}", ISBN = "{}", Year = {}, Price = "{}", Pages = "{}", BookDesc = "{}", BookLink = "{}" WHERE idBook = {};
UPDATE Category SET CategoryDesc = "{}" WHERE idCategory = {};
UPDATE Customer SET Name = "{}", Surname = "{}", City = "{}", State = "{}", ZipCode = "{}" WHERE idCustomer = {};
UPDATE Orders SET idCustomer = {}, OrderDate = "{}", Price = "{}" WHERE idOrder = {};
