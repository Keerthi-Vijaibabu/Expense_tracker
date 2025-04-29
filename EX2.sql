USE KEERTHI;

CREATE TABLE Restaurants (
    RestaurantID INT PRIMARY KEY,
    RestaurantName VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL,
    CuisineType VARCHAR(50) NOT NULL
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    RestaurantID INT,
    CustomerID INT NOT NULL,
    OrderDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID)
);

DESC orders;
DESC restaurants;


-- Inserting into Restaurants
INSERT INTO Restaurants (RestaurantID, RestaurantName, Location, CuisineType) VALUES
(1, "Keerthi's Kitchen", 'NewYork', 'Italian'),
(2, 'Sushi World', 'Tokyo', 'Japanese'),
(3, 'Taco Heaven', 'Los Angeles', 'Mexican'),
(4, 'Curry Corner', 'London', 'Indian'),
(5, 'Pasta Express', 'Chicago', 'Italian');

-- Inserting into Orders
INSERT INTO Orders (OrderID, RestaurantID, CustomerID, OrderDate, Amount) VALUES
(1, 1, 101, '2024-07-15', 45),
(2, 2, 102, '2024-06-20', 55),
(5, 5, 105, '2024-06-30', 25);

INSERT INTO Orders (OrderID, RestaurantID, CustomerID, OrderDate, Amount) VALUES
(6, 109, 105, '2024-06-30', 25);

SELECT * FROM Restaurants;
SELECT * FROM Orders;

DROP TABLE Restaurants;
DROP TABLE Orders;

ALTER TABLE orders 
Drop FOREIGN KEY orders_ibfk_1;

ANALYZE TABLE orders;