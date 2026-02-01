package patterns.creational.builder;

public class QueryClient {
    public static void main(String[] args) {
        Query query = new Query.Builder("users", "id", "name", "email")
            .where("age > 18")
            .orderBy("name")
            .limit(10)
            .offset(0)
            .build();
        System.out.println(query);
        System.out.println(query.toSql());
    }
}