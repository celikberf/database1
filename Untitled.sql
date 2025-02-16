ALTER TABLE products  
ADD CONSTRAINT fk_categories_products 
FOREIGN KEY (Categoryid) 
REFERENCES categories(id);
