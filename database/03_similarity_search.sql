CREATE OR REPLACE FUNCTION match_documents(

    query_embedding vector(384),

    top_k integer
)
RETURNS TABLE (
    chunk text,
    source text,
    similarity float
)
AS $$
BEGIN
    RETURN QUERY
    SELECT
        d.chunk,
        d.source,
        1 - (d.embedding <=> query_embedding) AS similarity
    FROM documents d
    ORDER BY similarity DESC
    LIMIT top_k;
END;
$$ LANGUAGE plpgsql;