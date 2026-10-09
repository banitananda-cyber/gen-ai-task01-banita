#List of products
products= ["mobile", "Guitar", "Bed", "Table", "headphones","piano"]


#tuple of product
sample_products=("mobile",20000,"electronics")

#print
print("2nd product:",products[1],"\nlast_product:",products[-1])

#Append
products.extend(["teddy bear","doll"])

#print
print("Updated products list:", products)

#convert tuple to list
sample_products_list=list(sample_products)
sample_products_list[1]=25000
print("Updated sample products list:",sample_products_list)

#convert list to tuple
sample_products_tuple=tuple(sample_products_list)
print("Updated sample products tuple:",sample_products_tuple)

#categories list and set
categories= ["electronics", "musical instruments", "furniture","toys","home appliances","clothing"]
categories_set=set(categories)
print("Categories set:",categories_set)
categories_set.add("sports")
categories_set.add("clothing")#ignoring duplicate
print("Updated categories set:",categories_set)
Check_categories= "sports" in categories_set
print("Is 'sports' category present in the set?:",Check_categories)
total_categories=len(categories_set)
print("Total number of categories:",total_categories)

#dictionaries
price_dict={"mobile":20000,
            "Guitar":15000.50,
            "Bed":30000,
            "Table":10000,
            "headphones":5000.80,
            "piano":25000}
price_dict["teddy bear"]=1500
price_dict.update({"Table":12000})
removed_price=price_dict.pop("headphones",None)
average_price=sum(price_dict.values())/len(price_dict)
print("average price of products:",average_price)
print("Maximum price of products:",max(price_dict.values()),"\nMinimum price of products:",min(price_dict.values()))

#Combine
combined_list=list(zip(products,price_dict.values(),categories))
combined_tuple=tuple(zip(products,price_dict.values(),categories))
print("Combined tuple of products and categories:",combined_tuple)


