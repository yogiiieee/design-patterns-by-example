from src.patterns.creational.builder.query import Query

def main():
    query = (
        Query.Builder("users", "id", "name", "email")
        .where("age > 18")
        .order_by("name")
        .limit(10)
        .offset(0)
        .build()
    )
    print(query)
    print(query.to_sql())

if __name__ == "__main__":
    main()
