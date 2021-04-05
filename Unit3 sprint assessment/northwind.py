import sqlite3

conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()

expensive_items_q = (
    "SELECT ProductName "
    "FROM Product ORDER BY UnitPrice DESC LIMIT 10"
)
curs.execute(expensive_items_q)
expensive_items = curs.fetchall()

# [('Côte de Blaye',), ('Thüringer Rostbratwurst',),
# ('Mishi Kobe Niku',), ("Sir Rodney's Marmalade",),
# ('Carnarvon Tigers',), ('Raclette Courdavault',),
# ('Manjimup Dried Apples',), ('Tarte au sucre',),
# ('Ipoh Coffee',), ('Rössle Sauerkraut',)]



avg_hire_age_q = "SELECT AVG(HireDate - BirthDate) FROM Employee"
curs.execute(avg_hire_age_q)
avg_hire_age = curs.fetchall()
# [(37.22222222222222,)]

avg_age_by_city_q = "SELECT AVG(HireDate - BirthDate), City " \
                  "FROM Employee GROUP BY City"
curs.execute(avg_age_by_city_q)
avg_age_by_city = curs.fetchall()

# [(29.0, 'Kirkland'), (32.5, 'London'),
# (56.0, 'Redmond'), (40.0, 'Seattle'), (40.0, 'Tacoma')]

ten_most_expensive_q = "SELECT Product.ProductName, Supplier.CompanyName " \
                     "FROM Product" \
                     " LEFT JOIN Supplier " \
                     "ON Product.SupplierId = Supplier.Id " \
                     "ORDER BY Product.UnitPrice DESC LIMIT 10"
curs.execute(ten_most_expensive_q)
ten_most_expensive = curs.fetchall()
# [('Côte de Blaye', 'Aux joyeux ecclésiastiques'),
# ('Thüringer Rostbratwurst', 'Plutzer Lebensmittelgroßmärkte AG'),
# ('Mishi Kobe Niku', 'Tokyo Traders'),
# ("Sir Rodney's Marmalade", 'Specialty Biscuits, Ltd.'),
# ('Carnarvon Tigers', 'Pavlova, Ltd.'),
# ('Raclette Courdavault', 'Gai pâturage'),
# ('Manjimup Dried Apples', "G'day, Mate"),
# ('Tarte au sucre', "Forêts d'érables"),
# ('Ipoh Coffee', 'Leka Trading'),
# ('Rössle Sauerkraut', 'Plutzer Lebensmittelgroßmärkte AG')]

largest_category_q = "SELECT Category.CategoryName " \
                   "FROM Product " \
                   "lEFT JOIN Category on Product.SupplierId = Category.Id " \
                   "GROUP BY Product.CategoryId " \
                   "ORDER BY COUNT(*) DESC LIMIT 1"
curs.execute(largest_category_q)
largest_category = curs.fetchall()
# [('Produce',)]

most_territories_q = "SELECT Employee.LastName, Employee.FirstName  " \
                   "FROM EmployeeTerritory " \
                   "LEFT JOIN Employee " \
                   "ON EmployeeTerritory.EmployeeId = Employee.Id " \
                   "GROUP BY EmployeeID ORDER BY COUNT(*) DESC LIMIT 1"
curs.execute(most_territories_q)
most_territories = curs.fetchall()
# [('King', 'Robert')]

