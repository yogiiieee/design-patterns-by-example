class Query:
    # required
    _columns: list[str]
    _table: str
    # optional
    _where_clauses: list[str] | None
    _order_by: str | None
    _limit: int | None
    _offset: int | None
    # can add more fields as needed

    def __init__(self, builder: "Builder") -> None:
        self._columns = builder._columns
        self._table = builder._table
        self._where_clauses = builder._where_clauses
        self._order_by = builder._order_by
        self._limit = builder._limit
        self._offset = builder._offset

    def __repr__(self) -> str:
        return f"Query(table={self._table}, columns={self._columns}, where_clauses={self._where_clauses}, order_by={self._order_by}, limit={self._limit}, offset={self._offset})"

    def to_sql(self) -> str:
        if len(self._columns) == 1 and self._columns[0] == "*":
            columns = "*"
        else:
            columns = ", ".join(self._columns)
        sql = f"SELECT {columns} FROM {self._table}"
        if self._where_clauses:
            sql += f" WHERE {' AND '.join(self._where_clauses)}"
        if self._order_by:
            sql += f" ORDER BY {self._order_by}"
        if self._limit:
            sql += f" LIMIT {self._limit}"
        if self._offset:
            sql += f" OFFSET {self._offset}"
        return sql + ";"

    class Builder:
        def __init__(self, table: str, *args) -> None:
            self._table = table
            self._columns = list(args) if args else ["*"]
            self._where_clauses = []
            self._order_by = None
            self._limit = None
            self._offset = None

        # for each method, we return the Builder object itself
        def where(self, condition: str) -> "Query.Builder":
            self._where_clauses.append(condition)
            return self

        def order_by(self, column: str) -> "Query.Builder":
            self._order_by = column
            return self

        def limit(self, limit: int) -> "Query.Builder":
            self._limit = limit
            return self

        def offset(self, offset: int) -> "Query.Builder":
            self._offset = offset
            return self

        def build(self) -> "Query":
            if not self._table:
                raise ValueError("Table is required")
            if not self._columns:
                self._columns = ["*"]
            return Query(self)
