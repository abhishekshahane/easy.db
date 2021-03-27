from helpers import obj_query

def advanced_query(args, selfdb):
    db_args = args[0]
    query_args = args[1]

    queries = ["STARTS", "ENDS"]
    query = None
    for query_func in queries:
        if query_func in query_args:
            query = query_func
    if query == None:
        raise TypeError("Query cannot be empty")
    query_args = query_args.replace(f"{query}(", "").replace(")", "")
        
    query_types = ["key", "value"]

    db = obj_query(selfdb, db_args)

    if "," in query_args:
        query_type = query_args.split(",")[0].strip()
        query_value = query_args.split(",")[1].strip()
    else:
        query_type = "key"  # Default query type
        query_value = query_args
    query_value = query_value.replace("'", "")

    if query_type not in query_types:
        raise TypeError("Query type must be 'key' or 'value'")

    rows = []
    for key, value in db.items():
        if query_type == "value": wanted = value
        elif query_type == "key": wanted = key
        wanted = str(wanted)

        putInRows = False
        if query == "STARTS":
            putInRows = wanted.startswith(query_value)
        if query == "ENDS":
            putInRows = wanted.endswith(query_value)
        
        if putInRows:
            full_obj = {key: value}
            rows.append(full_obj)

    return rows