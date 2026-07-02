CREATE TABLE IF NOT EXISTS documents (

    id BIGSERIAL PRIMARY KEY,

    chunk TEXT NOT NULL,

    embedding VECTOR(384)

);