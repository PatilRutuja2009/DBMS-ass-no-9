> use kunal
switched to db kunal
> db.book.insert({"book_isbn":1,"Title":"DSA","Publisher_Name":"Amar","author":{"Name":"Dipak","Address":"Pune","Phone_no":[{"Landline":1234,"Mobile":1234567890}]},"Publisher_City":"Baramati","Price":400,"Copy":200});
> db.book.insert({"book_isbn":2,"Title":"DBMS","Publisher_Name":"Dipak","author":{"Name":"Arbaj","Address":"Baramati","Phone_no":[{"Landline":647673,"Mobile":0987654321}]},"Publisher_City":"Daund","Price":300,"Copy":400});
> db.book.insert({"book_isbn":3,"Title":"CNE","Publisher_Name":"chandu","author":{"Name":"Saurabh","Address":"Pune","Phone_no":[{"Landline":76534,"Mobile":4793973484}]},"Publisher_City":"Nashik","Price":600,"Copy":350});
> db.book.insert({"book_isbn":4,"Title":"DBMS","Publisher_Name":"Pearson","author":{"Name":"Kunal","Address":"Nashik","Phone_no":[{"Landline":45678,"Mobile":3847563920}]},"Publisher_City":"Nashik","Price":700,"Copy":450});
> db.book.insert({"book_isbn":5,"Title":"TOC","Publisher_Name":"kulkarni","author":{"Name":"Ruturaj","Address":"Pune","Phone_no":[{"Landline":45678,"Mobile":64758930384}]},"Publisher_City":"Mumbai","Price":700,"Copy":750});
> db.book.find().pretty();
{
    "_id" : ObjectId("5d883b17f05ad77639472821"),
    "book_isbn" : 1,
    "Title" : "DSA",
    "Publisher_Name" : "Amar",
    "author" : {
        "Name" : "Dipak",
        "Address" : "Pune",
        "Phone_no" : [
            {
                "Landline" : 1234,
                "Mobile" : 1234567890
            }
        ]
    },
    "Publisher_City" : "Baramati",
    "Price" : 400,
    "Copy" : 200
}
{
    "_id" : ObjectId("5d883b7bf05ad77639472822"),
    "book_isbn" : 2,
    "Title" : "DBMS",
    "Publisher_Name" : "Dipak",
    "author" : {
        "Name" : "Arbaj",
        "Address" : "Baramati",
        "Phone_no" : [
            {
                "Landline" : 647673,
                "Mobile" : 987654321
            }
        ]
    },
    "Publisher_City" : "Daund",
    "Price" : 300,
    "Copy" : 400
}
{
    "_id" : ObjectId("5d883bcdf05ad77639472823"),
    "book_isbn" : 3,
    "Title" : "CNE",
    "Publisher_Name" : "chandu",
    "author" : {
        "Name" : "Saurabh",
        "Address" : "Pune",
        "Phone_no" : [
            {
                "Landline" : 76534,
                "Mobile" : 4793973484
            }
        ]
    },
    "Publisher_City" : "Nashik",
    "Price" : 600,
    "Copy" : 350
}
{
    "_id" : ObjectId("5d883c26f05ad77639472824"),
    "book_isbn" : 4,
    "Title" : "DBMS",
    "Publisher_Name" : "Pearson",
    "author" : {
        "Name" : "Kunal",
        "Address" : "Nashik",
        "Phone_no" : [
            {
                "Landline" : 45678,
                "Mobile" : 3847563920
            }
        ]
    },
    "Publisher_City" : "Nashik",
    "Price" : 700,
    "Copy" : 450
}
{
    "_id" : ObjectId("5d883c74f05ad77639472825"),
    "book_isbn" : 5,
    "Title" : "TOC",
    "Publisher_Name" : "kulkarni",
    "author" : {
        "Name" : "Ruturaj",
        "Address" : "Pune",
        "Phone_no" : [
            {
                "Landline" : 45678,
                "Mobile" : 64758930384
            }
        ]
    },
    "Publisher_City" : "Mumbai",
    "Price" : 700,
    "Copy" : 750
}
> db.book.find({"Publisher_City":"Nashik"}).pretty()
{
    "_id" : ObjectId("5d883bcdf05ad77639472823"),
    "book_isbn" : 3,
    "Title" : "CNE",
    "Publisher_Name" : "chandu",
    "author" : {
        "Name" : "Saurabh",
        "Address" : "Pune",
        "Phone_no" : [
            {
                "Landline" : 76534,
                "Mobile" : 4793973484
            }
        ]
    },
    "Publisher_City" : "Nashik",
    "Price" : 600,
    "Copy" : 350
}
{
    "_id" : ObjectId("5d883c26f05ad77639472824"),
    "book_isbn" : 4,
    "Title" : "DBMS",
    "Publisher_Name" : "Pearson",
    "author" : {
        "Name" : "Kunal",
        "Address" : "Nashik",
        "Phone_no" : [
            {
                "Landline" : 45678,
                "Mobile" : 3847563920
            }
        ]
    },
    "Publisher_City" : "Nashik",
    "Price" : 700,
    "Copy" : 450
}
> db.book.find({"Publisher_Name":"Pearson"}).pretty()
{
    "_id" : ObjectId("5d883c26f05ad77639472824"),
    "book_isbn" : 4,
    "Title" : "DBMS",
    "Publisher_Name" : "Pearson",
    "author" : {
        "Name" : "Kunal",
        "Address" : "Nashik",
        "Phone_no" : [
            {
                "Landline" : 45678,
                "Mobile" : 3847563920
            }
        ]
    },
    "Publisher_City" : "Nashik",
    "Price" : 700,
    "Copy" : 450
}
> db.book.update({"Publisher_Name":"Pearson"},{$set:{"Publisher_City":"Pune"}})
> db.book.find().pretty()
{
    "_id" : ObjectId("5d883b17f05ad77639472821"),
    "book_isbn" : 1,
    "Title" : "DSA",
    "Publisher_Name" : "Amar",
    "author" : {
        "Name" : "Dipak",
        "Address" : "Pune",
        "Phone_no" : [
            {
                "Landline" : 1234,
                "Mobile" : 1234567890
            }
        ]
    },
    "Publisher_City" : "Baramati",
    "Price" : 400,
    "Copy" : 200
}
{
    "_id" : ObjectId("5d883b7bf05ad77639472822"),
    "book_isbn" : 2,
    "Title" : "DBMS",
    "Publisher_Name" : "Dipak",
    "author" : {
        "Name" : "Arbaj",
        "Address" : "Baramati",
        "Phone_no" : [
            {
                "Landline" : 647673,
                "Mobile" : 987654321
            }
        ]
    },
    "Publisher_City" : "Daund",
    "Price" : 300,
    "Copy" : 400
}
{
    "_id" : ObjectId("5d883bcdf05ad77639472823"),
    "book_isbn" : 3,
    "Title" : "CNE",
    "Publisher_Name" : "chandu",
    "author" : {
        "Name" : "Saurabh",
        "Address" : "Pune",
        "Phone_no" : [
            {
                "Landline" : 76534,
                "Mobile" : 4793973484
            }
        ]
    },
    "Publisher_City" : "Nashik",
    "Price" : 600,
    "Copy" : 350
}
{
    "Copy" : 450,
    "Price" : 700,
    "Publisher_City" : "Pune",
    "Publisher_Name" : "Pearson",
    "Title" : "DBMS",
    "_id" : ObjectId("5d883c26f05ad77639472824"),
    "author" : {
        "Name" : "Kunal",
        "Address" : "Nashik",
        "Phone_no" : [
            {
                "Landline" : 45678,
                "Mobile" : 3847563920
            }
        ]
    },
    "book_isbn" : 4
}
{
    "_id" : ObjectId("5d883c74f05ad77639472825"),
    "book_isbn" : 5,
    "Title" : "TOC",
    "Publisher_Name" : "kulkarni",
    "author" : {
        "Name" : "Ruturaj",
        "Address" : "Pune",
        "Phone_no" : [
            {
                "Landline" : 45678,
                "Mobile" : 64758930384
            }
        ]
    },
    "Publisher_City" : "Mumbai",
    "Price" : 700,
    "Copy" : 750
}
> db.book.find({},{"Publisher_Name":1,"_id":0})
{ "Publisher_Name" : "Amar" }
{ "Publisher_Name" : "Dipak" }
{ "Publisher_Name" : "chandu" }
{ "Publisher_Name" : "Pearson" }
{ "Publisher_Name" : "kulkarni" }

> db.book.remove({$and:[{"Publisher_Name":{$gte:"c"}},{"Publisher_Name":{$lt:"d"}}]})
> db.book.find().pretty()
{
    "_id" : ObjectId("5d883b17f05ad77639472821"),
    "book_isbn" : 1,
    "Title" : "DSA",
    "Publisher_Name" : "Amar",
    "author" : {
        "Name" : "Dipak",
        "Address" : "Pune",
        "Phone_no" : [
            {
                "Landline" : 1234,
                "Mobile" : 1234567890
            }
        ]
    },
    "Publisher_City" : "Baramati",
    "Price" : 400,
    "Copy" : 200
}
{
    "Copy" : 450,
    "Price" : 700,
    "Publisher_City" : "Pune",
    "Publisher_Name" : "Pearson",
    "Title" : "DBMS",
    "_id" : ObjectId("5d883c26f05ad77639472824"),
    "author" : {
        "Name" : "Kunal",
        "Address" : "Nashik",
        "Phone_no" : [
            {
                "Landline" : 45678,
                "Mobile" : 3847563920
            }
        ]
    },
    "book_isbn" : 4
}
{
    "_id" : ObjectId("5d883c74f05ad77639472825"),
    "book_isbn" : 5,
    "Title" : "TOC",
    "Publisher_Name" : "kulkarni",
    "author" : {
        "Name" : "Ruturaj",
        "Address" : "Pune",
        "Phone_no" : [
            {
                "Landline" : 45678,
                "Mobile" : 64758930384
            }
        ]
    },
    "Publisher_City" : "Mumbai",
    "Price" : 700,
    "Copy" : 750
}
