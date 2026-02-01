package patterns.creational.builder;

import java.util.*;

class Query {
    // required
    private final List<String> columns;
    private final String table;

    // optional
    private final List<String> whereClauses;
    private final String orderBy;
    private final Integer limit;
    private final Integer offset;
    // can add more fields as needed

    // Private constructor to prevent direct instantiation
    private Query(Builder builder) {
        this.columns = builder.columns;
        this.table = builder.table;
        this.whereClauses = builder.whereClauses;
        this.orderBy = builder.orderBy;
        this.limit = builder.limit;
        this.offset = builder.offset;
    }

    @Override
    public String toString() {
        return "Query{" +
                "columns=" + columns +
                ", table='" + table + '\'' +
                ", whereClauses=" + whereClauses +
                ", orderBy='" + orderBy + '\'' +
                ", limit=" + limit +
                ", offset=" + offset +
                '}';
    }

    public String toSql() {
        StringBuilder sql = new StringBuilder("SELECT ");
        if(columns.size() == 1 && columns.get(0).equals("*")) {
            sql.append("*");
        } else {
            sql.append(String.join(", ", columns));
        }
        sql.append(" FROM ").append(table);
        if(!whereClauses.isEmpty()) {
            sql.append(" WHERE ").append(String.join(" AND ", whereClauses));
        }
        if(orderBy != null) {
            sql.append(" ORDER BY ").append(orderBy);
        }
        if(limit != null) {
            sql.append(" LIMIT ").append(limit);
        }
        if(offset != null) {
            sql.append(" OFFSET ").append(offset);
        }
        return sql.append(";").toString();
    }

    public static class Builder {
        private final List<String> columns = new ArrayList<>();
        private final String table;
        private List<String> whereClauses = new ArrayList<>();
        private String orderBy;
        private Integer limit;
        private Integer offset;

        public Builder(String table, String... columns) {
            this.table = table;
            this.columns.addAll(Arrays.asList(columns));
        }
        
        // For each method, we return the Builder object itself
        public Builder where(String condition) {
            this.whereClauses.add(condition);
            return this;
        }

        public Builder orderBy(String column) {
            this.orderBy = column;
            return this;
        }

        public Builder limit(Integer limit) {
            this.limit = limit;
            return this;
        }

        public Builder offset(Integer offset) {
            this.offset = offset;
            return this;
        }

        public Query build() {
            if(this.table.isEmpty()) {
                throw new IllegalArgumentException("Table is required");
            }
            if(this.columns.isEmpty()) {
                this.columns.add("*");
            }
            return new Query(this);
        }
    }
}